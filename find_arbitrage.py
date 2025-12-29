import asyncio
import random
import sys
import time
from typing import List, Dict, Any
from warframe import WarframeMarketClient
from tqdm.asyncio import tqdm

async def process_item(client, item, semaphore, min_spread):
    async with semaphore:
        try:
            # 获取该物品的在线/游戏内玩家订单
            orders = await client.get_item_orders(item.url_name, players="online")
            
            # 按 Rank 分组订单 (None 为非 Mod 物品或未指定 Rank)
            orders_by_rank = {}
            for o in orders:
                r = o.mod_rank
                if r not in orders_by_rank:
                    orders_by_rank[r] = []
                orders_by_rank[r].append(o)
            
            # 对每个 Rank 分组分别计算差价
            for rank, group_orders in orders_by_rank.items():
                # 分离买单和卖单
                buy_orders = [o for o in group_orders if o.order_type == "buy"]
                sell_orders = [o for o in group_orders if o.order_type == "sell"]

                if not buy_orders or not sell_orders:
                    continue

                # 寻找最高买价和最低卖价
                max_buy_order = max(buy_orders, key=lambda o: o.platinum)
                min_sell_order = min(sell_orders, key=lambda o: o.platinum)

                spread = max_buy_order.platinum - min_sell_order.platinum
                
                # 只输出差价大于等于 min_spread 的
                if spread >= min_spread:
                    rank_str = str(rank) if rank is not None else "-"
                    min_sell_str = f"{min_sell_order.platinum} ({min_sell_order.user.ingame_name})"
                    max_buy_str = f"{max_buy_order.platinum} ({max_buy_order.user.ingame_name})"
                    tqdm.write(f"{item.item_name:<30} | {rank_str:<5} | {spread:<8} | {min_sell_str:<25} | {max_buy_str:<25}")

        except Exception as e:
            # 仅在调试时打印错误，避免刷屏
            # print(f"\n处理 {item.item_name} 时出错: {e}")
            pass

async def main():
    # 从命令行参数读取最小差价，默认为10
    min_spread = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    print("Connecting to Warframe Market API...")
    # 增加并发度，虽然有 rate_limit 限制请求发送频率，但并发可以利用等待时间
    async with WarframeMarketClient(rate_limit=3) as client:
        # 1. 获取所有物品列表
        print("Fetching item list...")
        all_items = await client.get_items()
        print(f"Retrieved {len(all_items)} items")

        # 扫描全部物品
        target_items = all_items

        print(f"About to concurrently check orders for {len(target_items)} items...")
        print(f"Note: Due to API rate limit (3 req/s), this may take a while. Minimum spread threshold: {min_spread}")

        # 限制并发任务数，防止创建过多任务占用资源
        semaphore = asyncio.Semaphore(10)
        
        start_time = time.time()
        
        # 打印表头
        print("\n" + "="*110)
        print(f"{'Item Name':<30} | {'Rank':<5} | {'Spread':<8} | {'Lowest Sell (Player)':<25} | {'Highest Buy (Player)':<25}")
        print("-" * 110)
        
        tasks = [process_item(client, item, semaphore, min_spread) for item in target_items]
        
        # 使用 tqdm.gather 自动处理进度条
        await tqdm.gather(*tasks, desc="Querying orders")
        
        duration = time.time() - start_time
        print(f"\nScan complete! Elapsed time: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
