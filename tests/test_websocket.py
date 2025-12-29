import asyncio
import unittest
from warframe import WarframeMarketSocket

class TestWebSocketUnit(unittest.IsolatedAsyncioTestCase):
    async def test_pending_request_resolution(self):
        ws = WarframeMarketSocket()
        fut = asyncio.get_event_loop().create_future()
        ws._pending_requests["req1"] = fut
        message = {"route": "@wfm|cmd/test:ok", "payload": {"ok": True}, "refId": "req1"}
        await ws._handle_message(message)
        self.assertTrue(fut.done())
        self.assertEqual(fut.result(), {"ok": True})

    async def test_route_handler_dispatch(self):
        ws = WarframeMarketSocket()
        result = {}
        async def handler(payload):
            result["payload"] = payload
        ws.on("@wfm|event/reports/online", handler)
        message = {"route": "@wfm|event/reports/online", "payload": {"connections": 1, "authorizedUsers": 0}}
        await ws._handle_message(message)
        self.assertIn("payload", result)
        self.assertEqual(result["payload"]["connections"], 1)

class TestWebSocketIntegration(unittest.IsolatedAsyncioTestCase):
    async def test_connect_and_disconnect(self):
        ws = WarframeMarketSocket(timeout=5)
        await ws.connect()
        await ws.disconnect()
        self.assertIsNone(ws._ws)

