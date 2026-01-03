# warframe-api-for-python

Warframe Market API (v2) 的健壮、异步 Python 封装库。本软件包允许开发者轻松地与 Warframe Market 数据进行交互，包括物品、订单、统计数据、任务等。

## 安装

```bash
git clone https://github.com/NathanYYDS/warframe-api-for-python.git
cd warframe-api-for-python
pip install -e .
```

## 特性

- **异步**：基于 `aiohttp` 构建，实现高性能、非阻塞的 API 调用。
- **多语言支持**：完全支持 Warframe Market 支持的所有 12 种语言（en, zh-hans, ko, ru 等）。
- **类型提示**：使用 Python dataclasses 提供清晰的数据结构和 IDE 自动补全支持。
- **全面覆盖**：访问物品、订单、统计数据、任务、NPC 和用户资料。

## 使用方法

### 快速开始

以下是一个简单的入门示例：

```python
import asyncio
from warframe import WarframeMarketClient

async def main():
    # 初始化客户端（默认为英文，PC 平台）
    async with WarframeMarketClient() as client:
        # 获取所有可交易物品
        items = await client.get_items()
        print(f"找到 {len(items)} 个物品。")
        
        if items:
            first_item = items[0]
            print(f"第一个物品: {first_item.item_name}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 进阶用法

#### 指定语言和平台

初始化客户端时可以指定语言和平台：

```python
# 使用简体中文和 PC 平台进行初始化
client = WarframeMarketClient(language='zh-hans', platform='pc')
```

#### 获取顶级订单

获取特定物品的最佳买单和卖单：

```python
async with WarframeMarketClient(language='en') as client:
    # 获取 "Wisp Prime Set" 的顶级订单
    # 注意：你需要物品的 'url_name'（例如 "wisp_prime_set"）
    top_orders = await client.get_top_orders_for_item("wisp_prime_set")
    
    print("顶级卖单（最低价）:")
    for order in top_orders['sell']:
        print(f"{order.user.ingame_name}: {order.platinum} 白金 (数量: {order.quantity})")

    print("\n顶级买单（最高出价）:")
    for order in top_orders['buy']:
        print(f"{order.user.ingame_name}: {order.platinum} 白金 (数量: {order.quantity})")
```

#### 获取物品统计数据

检索物品的历史价格统计数据：

```python
async with WarframeMarketClient() as client:
    stats = await client.get_statistics("wisp_prime_set")
    # stats 包含历史数据，如交易量、最低/最高价格等
    print(stats)
```

#### 获取世界状态（任务）

访问当前任务数据：

```python
async with WarframeMarketClient() as client:
    missions = await client.get_missions()
    for mission in missions:
        print(f"{mission.node} - {mission.mission_type} ({mission.faction})")
```

## 支持的函数

客户端支持以下主要操作：

- `get_items()`: 获取所有物品列表。
- `get_item(item_url_name)`: 获取特定物品的详细信息。
- `get_item_orders(item_url_name, ...)`: 获取物品的所有订单（支持可选过滤）。
- `get_top_orders_for_item(item_url_name)`: 获取物品的最佳买/卖订单。
- `get_statistics(item_url_name)`: 获取价格历史和交易量统计数据。
- `get_most_recent_orders()`: 获取最近发布的订单流。
- `get_missions()`: 获取活跃任务列表。
- `get_npcs()`: 获取 NPC 列表。

## 版本

0.3.0

### 更新日志 (0.3.0)
- 新增 `ItemMatcher` 类，支持模糊匹配和别名系统。
- 实现了用户自定义别名系统（支持链式别名和子串替换）。
- 增强了物品名称的标准化逻辑（处理中文间隔号 "·"）。
- 重构了匹配逻辑，使其可重用且更健壮。

## 许可证

MIT
