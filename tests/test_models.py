import unittest
from warframe import ItemShort, Order, User, Mission, NPC

class TestModels(unittest.TestCase):
    def test_itemshort_i18n(self):
        data = {
            "id": "1",
            "slug": "dual_rounds",
            "i18n": {
                "en": {"name": "Dual Rounds", "thumb": "items/images/en/dual_rounds.png"},
                "zh-hans": {"name": "保障·锡斯特双枪", "thumb": "items/images/zh-hans/dual_rounds.png"}
            }
        }
        item = ItemShort.from_dict(data, preferred_lang="zh-hans")
        self.assertEqual(item.url_name, "dual_rounds")
        self.assertEqual(item.item_name, "保障·锡斯特双枪")
        self.assertTrue(item.thumb.endswith("dual_rounds.png"))

    def test_user_from_dict(self):
        data = {
            "id": "u1",
            "ingameName": "TestUser",
            "status": "online",
            "region": "en",
            "reputation": 10,
            "avatar": "user/avatar/a.png",
            "lastSeen": "2024-01-01T00:00:00Z"
        }
        user = User.from_dict(data)
        self.assertEqual(user.ingame_name, "TestUser")
        self.assertEqual(user.status, "online")

    def test_order_from_dict(self):
        data = {
            "id": "o1",
            "creationDate": "2024-01-01T00:00:00Z",
            "visible": True,
            "quantity": 1,
            "user": {"id": "u1", "ingameName": "TestUser", "status": "online", "region": "en", "reputation": 10},
            "lastUpdate": "2024-01-01T00:00:00Z",
            "platinum": 20,
            "orderType": "sell",
            "region": "en",
            "platform": "pc",
            "modRank": 0
        }
        order = Order.from_dict(data)
        self.assertEqual(order.order_type, "sell")
        self.assertEqual(order.platinum, 20)
        self.assertEqual(order.user.ingame_name, "TestUser")

    def test_mission_from_dict(self):
        data = {
            "id": "m1",
            "node": "Earth",
            "faction": "Grineer",
            "minEnemyLevel": 1,
            "maxEnemyLevel": 5,
            "type": "Exterminate",
            "nightmare": False,
            "archwing": False,
            "tower": False
        }
        mission = Mission.from_dict(data)
        self.assertEqual(mission.mission_type, "Exterminate")

    def test_npc_from_dict(self):
        data = {"id": "n1", "name": "Darvo", "thumb": "npcs/darvo.png"}
        npc = NPC.from_dict(data)
        self.assertEqual(npc.name, "Darvo")

