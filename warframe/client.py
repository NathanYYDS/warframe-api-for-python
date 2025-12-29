import asyncio
import logging
from typing import List, Optional, Dict, Any, Union
import aiohttp
import json
from urllib.parse import quote
from .models import ItemShort, Order, User, Mission, NPC
from .exceptions import APIRequestError, TimeoutError, InvalidParameterError

logger = logging.getLogger(__name__)

class WarframeMarketClient:
    """
    Async client for Warframe Market API v2.
    """
    BASE_URL = "https://api.warframe.market/v2"
    ASSETS_BASE_URL = "https://warframe.market/static/assets"
    
    def __init__(
        self, 
        language: str = 'en',  # WFM have support for 12 languages: ko, ru, de, fr, pt, zh-hans, zh-hant, es, it, pl, uk, en
        platform: str = 'pc', 
        timeout: int = 10,
        rate_limit: int = 3,
        token: Optional[str] = None
    ):
        self.language = language
        self.platform = platform
        self.timeout = timeout
        self.rate_limit = rate_limit  # Requests per second
        self._session: Optional[aiohttp.ClientSession] = None
        self._rate_lock = asyncio.Lock()
        self._next_available_time: float = 0.0
        self._token: Optional[str] = token
        
    async def __aenter__(self):
        await self.open()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        
    async def open(self):
        if self._session is None:
            self._session = aiohttp.ClientSession(
                headers={
                    "Language": self.language,
                    "Platform": self.platform,
                    "accept": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                }
            )
        return self
            
    async def close(self):
        if self._session:
            await self._session.close()
            self._session = None
    
    def set_token(self, token: str):
        self._token = token
    
    def clear_token(self):
        self._token = None

    async def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        if not self._session:
            await self.open()
        
        url = f"{self.BASE_URL}{endpoint}"
        async with self._rate_lock:
            now = asyncio.get_event_loop().time()
            wait = max(0.0, self._next_available_time - now)
            if wait > 0:
                await asyncio.sleep(wait)
            self._next_available_time = asyncio.get_event_loop().time() + (1.0 / max(1, self.rate_limit))
        try:
            headers = kwargs.pop("headers", {})
            if self._token:
                headers = {**headers, "Authorization": f"Bearer {self._token}"}
            async with self._session.request(method, url, timeout=self.timeout, headers=headers, **kwargs) as response:
                if response.status >= 400:
                    try:
                        error_data = await response.json()
                        error_content = error_data.get('error')
                        if isinstance(error_content, dict):
                            message = json.dumps(error_content, ensure_ascii=False)
                        else:
                            message = str(error_content) if error_content else str(response.reason)
                    except Exception:
                        message = str(response.reason)
                    raise APIRequestError(response.status, message)
                data = await response.json()
                return data.get("data", {}) or data.get("payload", {})
        except asyncio.TimeoutError:
            raise TimeoutError(f"Request to {url} timed out")
        except aiohttp.ClientError as e:
            raise APIRequestError(0, str(e))

    async def get_items(self) -> List[ItemShort]:
        """Get list of all tradable items"""
        data = await self._request("GET", "/items")
        items_data = data if isinstance(data, list) else data.get("items", [])
        return [ItemShort.from_dict(item, preferred_lang=self.language) for item in items_data]

    async def get_item(self, item_url_name: str) -> Dict[str, Any]:
        """Get full info about one, particular item"""
        safe_name = quote(item_url_name, safe="")
        data = await self._request("GET", f"/items/{safe_name}")
        return data.get("item", data)

    async def get_item_orders(self, item_url_name: str, rank: Optional[int] = None, rank_lt: Optional[int] = None, players: str = "all") -> List[Order]:
        safe_name = quote(item_url_name, safe="")
        endpoint = f"/orders/item/{safe_name}"
        params: Dict[str, Any] = {}
        if rank is not None:
            params["rank"] = int(rank)
        if rank_lt is not None:
            params["rankLt"] = int(rank_lt)
        data = await self._request("GET", endpoint, params=params)
        orders_data = data.get("orders", []) if isinstance(data, dict) else data
        orders = [Order.from_dict(o) for o in orders_data]
        pf = players.lower()
        if pf == "online":
            orders = [o for o in orders if o.user and o.user.status in ("online", "ingame")]
        elif pf == "ingame":
            orders = [o for o in orders if o.user and o.user.status == "ingame"]
        return orders

    async def get_missions(self) -> List[Mission]:
        """Get list of all Missions"""
        data = await self._request("GET", "/missions")
        return [Mission.from_dict(m) for m in data]
    
    async def get_npcs(self) -> List[NPC]:
        """Get list of all NPCs"""
        data = await self._request("GET", "/npcs")
        return [NPC.from_dict(n) for n in data]

    async def get_statistics(self, item_url_name: str) -> Dict[str, Any]:
        """Get statistics for an item"""
        safe_name = quote(item_url_name, safe="")
        data = await self._request("GET", f"/items/{safe_name}/statistics")
        return data.get("statistics_closed", {})
    
    async def get_most_recent_orders(self) -> List[Order]:
        data = await self._request("GET", "/orders/recent")
        orders_data = data.get("orders", []) if isinstance(data, dict) else data
        return [Order.from_dict(o) for o in orders_data]

    async def get_top_orders_for_item(
        self,
        item_url_name: str,
        rank: Optional[int] = None,
        rank_lt: Optional[int] = None,
        charges: Optional[int] = None,
        charges_lt: Optional[int] = None,
        amber_stars: Optional[int] = None,
        amber_stars_lt: Optional[int] = None,
        cyan_stars: Optional[int] = None,
        cyan_stars_lt: Optional[int] = None,
        subtype: Optional[str] = None,
    ) -> Dict[str, List[Order]]:
        params: Dict[str, Any] = {}
        if rank is not None:
            params["rank"] = int(rank)
        if rank_lt is not None:
            params["rankLt"] = int(rank_lt)
        if charges is not None:
            params["charges"] = int(charges)
        if charges_lt is not None:
            params["chargesLt"] = int(charges_lt)
        if amber_stars is not None:
            params["amberStars"] = int(amber_stars)
        if amber_stars_lt is not None:
            params["amberStarsLt"] = int(amber_stars_lt)
        if cyan_stars is not None:
            params["cyanStars"] = int(cyan_stars)
        if cyan_stars_lt is not None:
            params["cyanStarsLt"] = int(cyan_stars_lt)
        if subtype is not None:
            params["subtype"] = subtype
        try:
            safe_name = quote(item_url_name, safe="")
            data = await self._request("GET", f"/orders/item/{safe_name}/top", params=params)
            buy_data = data.get("buy", [])
            sell_data = data.get("sell", [])
            return {
                "buy": [Order.from_dict(o) for o in buy_data],
                "sell": [Order.from_dict(o) for o in sell_data],
            }
        except APIRequestError as e:
            orders = await self.get_item_orders(item_url_name, rank=rank, rank_lt=rank_lt, players="online")
            buy = [o for o in orders if o.order_type == "buy"]
            sell = [o for o in orders if o.order_type == "sell"]
            buy_sorted = sorted(buy, key=lambda o: o.platinum, reverse=True)[:5]
            sell_sorted = sorted(sell, key=lambda o: o.platinum)[:5]
            return {"buy": buy_sorted, "sell": sell_sorted}
    # Helper to resolve image urls
    def get_asset_url(self, path: str) -> str:
        return f"{self.ASSETS_BASE_URL}/{path}"
