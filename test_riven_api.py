#!/usr/bin/env python3
"""
测试Riven API方法的简单脚本
"""
import asyncio
from warframe import WarframeMarketClient

async def test_riven_api():
    """测试新增的Riven API方法"""
    async with WarframeMarketClient() as client:
        print("测试 Riven API 方法...")
        
        # 测试获取所有Riven武器列表
        print("\n1. 测试 get_riven_weapons()")
        try:
            riven_weapons = await client.get_riven_weapons()
            print(f"成功获取 {len(riven_weapons)} 个Riven武器")
            if riven_weapons:
                weapon = riven_weapons[0]
                print(f"  示例武器: {weapon.item_name} (slug: {weapon.slug})")
        except Exception as e:
            print(f"获取Riven武器列表失败: {e}")
        
        # 测试获取特定Riven武器详情
        print("\n2. 测试 get_riven_weapon()")
        try:
            # 使用一个示例slug，实际使用时应替换为真实存在的slug
            sample_slug = "kulstar"  # 这是示例slug，可能需要根据实际情况调整
            riven_weapon = await client.get_riven_weapon(sample_slug)
            print(f"成功获取Riven武器详情: {riven_weapon.item_name}")
            print(f"  类型: {riven_weapon.riven_type}")
            print(f"  裂隙倾向性: {riven_weapon.disposition}")
        except Exception as e:
            print(f"获取特定Riven武器详情失败: {e}")
        
        # 测试获取所有Riven属性列表
        print("\n3. 测试 get_riven_attributes()")
        try:
            riven_attributes = await client.get_riven_attributes()
            print(f"成功获取 {len(riven_attributes)} 个Riven属性")
            if riven_attributes:
                attr = riven_attributes[0]
                print(f"  示例属性: {attr.item_name} (slug: {attr.slug})")
        except Exception as e:
            print(f"获取Riven属性列表失败: {e}")
        
        print("\n测试完成!")

if __name__ == "__main__":
    asyncio.run(test_riven_api())
