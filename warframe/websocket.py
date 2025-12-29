import asyncio
import json
import logging
import uuid
from typing import Optional, Any, Callable, Dict
import aiohttp
from .exceptions import WarframeAPIError

logger = logging.getLogger(__name__)

class WarframeMarketSocket:
    """
    WebSocket client for Warframe Market.
    """
    WS_URL = "wss://ws.warframe.market/socket"
    SUB_PROTOCOL = "wfm"
    
    def __init__(self, language: str = "en", platform: str = "pc", token: Optional[str] = None, timeout: int = 10):
        self._ws: Optional[aiohttp.ClientWebSocketResponse] = None
        self._session: Optional[aiohttp.ClientSession] = None
        self._handlers: Dict[str, Callable] = {}
        self._pending_requests: Dict[str, asyncio.Future] = {}
        self._listen_task: Optional[asyncio.Task] = None
        self.language = language
        self.platform = platform
        self.token = token
        self.timeout = timeout
        
    async def connect(self):
        if self._session is None:
            self._session = aiohttp.ClientSession(
                headers={
                    "Language": self.language,
                    "Platform": self.platform,
                    "accept": "application/json",
                }
            )
            
        try:
            self._ws = await self._session.ws_connect(
                self.WS_URL, 
                protocols=[self.SUB_PROTOCOL],
                headers={
                    "Language": self.language,
                    "Platform": self.platform,
                    "accept": "application/json",
                },
                timeout=self.timeout
            )
            self._listen_task = asyncio.create_task(self._listen())
            logger.info("Connected to Warframe Market WebSocket")
            if self.token:
                await self.sign_in(self.token)
        except Exception as e:
            logger.error(f"Failed to connect to WebSocket: {e}")
            raise WarframeAPIError(f"WebSocket connection failed: {e}")

    async def disconnect(self):
        if self._listen_task:
            self._listen_task.cancel()
            try:
                await self._listen_task
            except asyncio.CancelledError:
                pass
            
        if self._ws:
            await self._ws.close()
            self._ws = None
            
        if self._session:
            await self._session.close()
            self._session = None
            
    async def _listen(self):
        try:
            async for msg in self._ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    try:
                        data = json.loads(msg.data)
                        await self._handle_message(data)
                    except json.JSONDecodeError:
                        logger.error(f"Failed to decode message: {msg.data}")
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    logger.error(f"WebSocket error: {msg.data}")
                    break
        except Exception as e:
            logger.error(f"Error in listener: {e}")

    async def _handle_message(self, message: Dict[str, Any]):
        route = message.get("route")
        ref_id = message.get("refId")
        payload = message.get("payload")
        
        # If it's a response to a request
        if ref_id and ref_id in self._pending_requests:
            future = self._pending_requests.pop(ref_id)
            if not future.done():
                future.set_result(payload)
            return

        # If it's an event we have a handler for
        if route and route in self._handlers:
            try:
                await self._handlers[route](payload)
            except Exception as e:
                logger.error(f"Error in handler for {route}: {e}")

    async def send(self, route: str, payload: Any) -> Any:
        """
        Send a message and wait for response.
        """
        if not self._ws:
            raise WarframeAPIError("WebSocket is not connected")
            
        msg_id = str(uuid.uuid4())
        message = {
            "route": route,
            "payload": payload,
            "id": msg_id
        }
        
        future = asyncio.get_event_loop().create_future()
        self._pending_requests[msg_id] = future
        
        await self._ws.send_json(message)
        
        try:
            # Wait for response with timeout
            return await asyncio.wait_for(future, timeout=self.timeout)
        except asyncio.TimeoutError:
            self._pending_requests.pop(msg_id, None)
            raise WarframeAPIError(f"Timeout waiting for response to {route}")

    def on(self, route: str, handler: Callable):
        """Register a handler for a specific route."""
        self._handlers[route] = handler

    async def sign_in(self, token: str) -> Any:
        return await self.send("@wfm|cmd/auth/signIn", {"token": token})

    async def sign_out(self) -> Any:
        return await self.send("@wfm|cmd/auth/signOut", {})

    def on_online_report(self, handler: Callable):
        self.on("@wfm|event/reports/online", handler)
