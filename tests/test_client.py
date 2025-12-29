import asyncio
import unittest
from warframe import WarframeMarketClient, Order, Mission, NPC, ItemShort

class TestClientPublicEndpoints(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = WarframeMarketClient(language="zh-hans", platform="pc", timeout=10, rate_limit=3)
        await self.client.open()

    async def asyncTearDown(self):
        await self.client.close()

    async def test_get_items(self):
        items = await self.client.get_items()
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)
        self.assertIsInstance(items[0], ItemShort)
        self.assertIsInstance(items[0].item_name, str)

    async def test_get_item(self):
        items = await self.client.get_items()
        data = await self.client.get_item(items[0].url_name)
        self.assertIsInstance(data, dict)
        self.assertTrue(len(data) >= 1)

    async def test_get_item_orders(self):
        items = await self.client.get_items()
        orders = await self.client.get_item_orders(items[0].url_name, players="online")
        self.assertIsInstance(orders, list)
        if orders:
            self.assertIsInstance(orders[0], Order)

    async def test_get_statistics(self):
        items = await self.client.get_items()
        try:
            stats = await self.client.get_statistics(items[0].url_name)
            self.assertIsInstance(stats, dict)
        except Exception as e:
            if hasattr(e, "status_code") and e.status_code == 404:
                return
            raise

    async def test_get_missions(self):
        missions = await self.client.get_missions()
        self.assertIsInstance(missions, list)
        if missions:
            self.assertIsInstance(missions[0], Mission)

    async def test_get_npcs(self):
        npcs = await self.client.get_npcs()
        self.assertIsInstance(npcs, list)
        if npcs:
            self.assertIsInstance(npcs[0], NPC)

    async def test_get_top_orders_for_item(self):
        items = await self.client.get_items()
        top = await self.client.get_top_orders_for_item(items[0].url_name)
        self.assertIsInstance(top, dict)
        self.assertIn("buy", top)
        self.assertIn("sell", top)
        self.assertIsInstance(top["buy"], list)
        self.assertIsInstance(top["sell"], list)
        if top["buy"]:
            self.assertIsInstance(top["buy"][0], Order)
        if top["sell"]:
            self.assertIsInstance(top["sell"][0], Order)

    def test_get_asset_url(self):
        url = self.client.get_asset_url("items/images/en/dual_rounds.png")
        self.assertTrue(url.startswith("https://warframe.market/static/assets/"))
