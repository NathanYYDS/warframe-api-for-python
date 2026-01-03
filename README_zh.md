# warframe-api-for-python

Warframe Market API (v2) 的健壮、异步 Python 封装库。本软件包允许开发者轻松地与 Warframe Market 数据进行交互，包括物品、订单、统计数据、任务等。

## 🚀 特性

- **异步**：基于 `aiohttp` 构建，实现高性能、非阻塞的 API 调用。
- **多语言支持**：完全支持 Warframe Market 支持的所有 12 种语言（en, zh-hans, ko, ru, 等）。
- **类型提示**：使用 Python dataclasses 提供清晰的数据结构和 IDE 自动补全支持。
- **全面覆盖**：访问物品、订单、统计数据、任务、NPC 和用户资料。
- **高级匹配**：内置模糊匹配和别名支持。
- **WebSocket 支持**：实时数据流能力。
- **健壮的错误处理**：提供具体的异常处理机制。

## 📦 安装

### 从 PyPI (推荐)

```bash
pip install warframe
```

### 从源码安装

```bash
git clone https://github.com/NathanYYDS/warframe-api-for-python.git
cd warframe-api-for-python
pip install -e .
```

## 🔧 快速开始

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

## 📖 详细使用方法

### 客户端初始化

```python
# 使用默认设置（英文，PC 平台）
client = WarframeMarketClient()

# 使用自定义设置
client = WarframeMarketClient(
    language='zh-hans',    # 语言支持: en, zh-hans, ko, ru, de, fr, pt, zh-hant, es, it, pl, uk
    platform='pc',         # 平台: pc, ps4, xb1, switch
    timeout=10,            # 请求超时（秒）
    rate_limit=3,          # 每秒请求数（默认: 3）
    token=None             # 认证令牌（如果需要）
)
```

### 基本操作

#### 获取物品列表

```python
async with WarframeMarketClient() as client:
    # 获取所有可交易物品
    items = await client.get_items()
    print(f"找到 {len(items)} 个物品")
    
    # 获取特定物品详情
    item_details = await client.get_item("wisp_prime_set")
    print(item_details)
```

#### 获取订单

```python
async with WarframeMarketClient(language='en') as client:
    # 获取物品的所有订单
    orders = await client.get_item_orders("wisp_prime_set")
    
    # 仅获取在线玩家订单
    online_orders = await client.get_item_orders("wisp_prime_set", players="online")
    
    # 获取特定等级的订单
    ranked_orders = await client.get_item_orders("wisp_prime_set", rank=5)
```

#### 获取顶级订单

```python
async with WarframeMarketClient(language='en') as client:
    # 获取物品的最佳买卖订单
    top_orders = await client.get_top_orders_for_item("wisp_prime_set")
    
    print("顶级卖单（最低价）:")
    for order in top_orders['sell']:
        print(f"{order.user.ingame_name}: {order.platinum} 白金 (数量: {order.quantity})")

    print("\n顶级买单（最高出价）:")
    for order in top_orders['buy']:
        print(f"{order.user.ingame_name}: {order.platinum} 白金 (数量: {order.quantity})")
```

#### 获取统计数据

```python
async with WarframeMarketClient() as client:
    # 获取物品的价格历史和交易量统计
    stats = await client.get_statistics("wisp_prime_set")
    print(stats)
```

#### 获取世界状态

```python
async with WarframeMarketClient() as client:
    # 获取当前任务数据
    missions = await client.get_missions()
    for mission in missions:
        print(f"{mission.node} - {mission.mission_type} ({mission.faction})")
    
    # 获取 NPC 数据
    npcs = await client.get_npcs()
    for npc in npcs:
        print(f"NPC: {npc.name}")
```

### 高级功能

#### 使用别名进行物品匹配

```python
from warframe import WarframeMarketClient, ItemMatcher

async def advanced_matching_example():
    async with WarframeMarketClient() as client:
        # 获取所有物品用于匹配器
        items = await client.get_items()
        
        # 创建匹配器
        matcher = ItemMatcher(items)
        
        # 使用模糊逻辑匹配物品
        item, display_name = matcher.match("wisp prime set")
        if item:
            print(f"匹配成功: {display_name} ({item.url_name})")
        
        # 使用别名匹配
        item, display_name = matcher.match("花p")
        if item:
            print(f"使用别名匹配: {display_name}")
```

#### WebSocket 集成

```python
import asyncio
from warframe import WarframeMarketSocket

async def websocket_example():
    socket = WarframeMarketSocket()
    
    try:
        await socket.connect()
        
        # 注册处理器
        def handle_online_report(payload):
            print("在线报告:", payload)
        
        socket.on_online_report(handle_online_report)
        
        # 保持连接
        await asyncio.sleep(30)
        
    finally:
        await socket.disconnect()
```

## 📚 API 参考

### WarframeMarketClient

| 方法 | 参数 | 描述 |
|------|------|------|
| `get_items()` | 无 | 获取所有可交易物品列表 |
| `get_item(item_url_name)` | `item_url_name` (str) | 获取特定物品的详细信息 |
| `get_item_orders(item_url_name, rank=None, rank_lt=None, players="all")` | `item_url_name` (str), `rank` (int), `rank_lt` (int), `players` (str) | 获取物品的所有订单 |
| `get_top_orders_for_item(item_url_name, rank=None, rank_lt=None, ...)` | 多个可选参数 | 获取物品的最佳买卖订单 |
| `get_statistics(item_url_name)` | `item_url_name` (str) | 获取物品的价格历史和统计信息 |
| `get_missions()` | 无 | 获取所有活跃任务列表 |
| `get_npcs()` | 无 | 获取所有 NPC 列表 |
| `get_most_recent_orders()` | 无 | 获取最近发布的订单流 |
| `get_asset_url(path)` | `path` (str) | 获取资产 URL |

### 模型

#### ItemShort
- `id` (str): 唯一标识符
- `url_name` (str): URL 友好名称
- `item_name` (str): 显示名称
- `thumb` (str): 缩略图 URL
- `vaulted` (bool): 是否被封存
- `all_names` (dict): 所有本地化名称

#### Order
- `id` (str): 订单 ID
- `creation_date` (str): 创建时间戳
- `visible` (bool): 可见状态
- `quantity` (int): 数量
- `user` (User): 用户信息
- `last_update` (str): 最后更新时间戳
- `platinum` (int): 白金数量
- `order_type` (str): 订单类型 (buy/sell)
- `region` (str): 地区
- `platform` (str): 平台
- `mod_rank` (int): 模组等级 (如果适用)

#### User
- `id` (str): 用户 ID
- `ingame_name` (str): 游戏内名称
- `status` (str): 在线状态
- `region` (str): 地区
- `reputation` (int): 声望分数
- `platform` (str): 平台
- `avatar` (str): 头像 URL
- `last_seen` (str): 最后上线时间

#### Mission
- `id` (str): 任务 ID
- `node` (str): 节点名称
- `faction` (str): 阵营
- `min_enemy_level` (int): 最低敌人等级
- `max_enemy_level` (int): 最高敌人等级
- `mission_type` (str): 任务类型
- `nightmare` (bool): 梦魇模式
- `archwing` (bool): 空战任务
- `tower` (bool): 塔任务

#### NPC
- `id` (str): NPC ID
- `name` (str): NPC 名称
- `thumb` (str): 缩略图 URL

### ItemMatcher

| 方法 | 参数 | 描述 |
|------|------|------|
| `match(query)` | `query` (str) | 使用模糊逻辑和别名匹配查询到的物品 |

## 🛡️ 错误处理

该库提供了特定的异常：

- `WarframeAPIError`: 基础异常
- `APIRequestError`: API 请求错误，包含状态码和消息
- `TimeoutError`: 请求超时
- `InvalidParameterError`: 无效参数

```python
from warframe import APIRequestError

try:
    async with WarframeMarketClient() as client:
        items = await client.get_items()
except APIRequestError as e:
    print(f"API 错误 {e.status_code}: {e.message}")
```

## ⚙️ 速率限制

客户端自动处理速率限制，支持配置每秒请求数：

```python
client = WarframeMarketClient(rate_limit=3)  # 默认为每秒 3 个请求
```

## 📝 版本

0.3.0

### 更新日志 (0.3.0)

- 添加 `ItemMatcher` 类用于模糊匹配和别名支持
- 实现用户自定义别名系统（支持链式别名和子串替换）
- 增强物品名称标准化逻辑（处理中文间隔号 "·"）
- 重构匹配逻辑使其可重用且更健壮
- 添加 WebSocket 支持用于实时数据流
- 改进文档和示例

## 🤝 贡献

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目根据 GNU Affero General Public License v3.0 许可证发布 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 感谢 Warframe Market 提供 API
- 受社区优秀工作的启发
