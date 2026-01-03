# Warframe Market API for Python

[中文文档](README_zh.md)

A robust, asynchronous Python wrapper for the Warframe Market API (v2). This package allows developers to easily interact with Warframe Market data, including items, orders, statistics, missions, and more.

## 🚀 Features

- **Asynchronous**: Built on `aiohttp` for high-performance, non-blocking API calls.
- **Multi-language Support**: Full support for all 12 languages supported by Warframe Market (en, zh-hans, ko, ru, etc.).
- **Type Hinting**: Uses Python dataclasses for clear data structures and IDE autocompletion.
- **Comprehensive Coverage**: Access items, orders, statistics, missions, NPCs, and user profiles.
- **Advanced Matching**: Built-in fuzzy matching and alias support for item names.
- **WebSocket Support**: Real-time data streaming capabilities.
- **Robust Error Handling**: Comprehensive error handling with specific exception types.

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install warframe
```

### From Source

```bash
git clone https://github.com/NathanYYDS/warframe-api-for-python.git
cd warframe-api-for-python
pip install -e .
```

## 🔧 Quick Start

Here's a simple example to get you started:

```python
import asyncio
from warframe import WarframeMarketClient

async def main():
    # Initialize the client (defaults to English, PC platform)
    async with WarframeMarketClient() as client:
        # Get all tradable items
        items = await client.get_items()
        print(f"Found {len(items)} items.")
        
        if items:
            first_item = items[0]
            print(f"First item: {first_item.item_name}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 📖 Detailed Usage

### Client Initialization

```python
# Initialize with default settings (English, PC)
client = WarframeMarketClient()

# Initialize with custom settings
client = WarframeMarketClient(
    language='zh-hans',    # Language support: en, zh-hans, ko, ru, de, fr, pt, zh-hant, es, it, pl, uk
    platform='pc',         # Platform: pc, ps4, xb1, switch
    timeout=10,            # Request timeout in seconds
    rate_limit=3,          # Requests per second (default: 3)
    token=None             # Authentication token (if required)
)
```

### Basic Operations

#### Get Items

```python
async with WarframeMarketClient() as client:
    # Get all tradable items
    items = await client.get_items()
    print(f"Found {len(items)} items")
    
    # Get specific item details
    item_details = await client.get_item("wisp_prime_set")
    print(item_details)
```

#### Get Orders

```python
async with WarframeMarketClient(language='en') as client:
    # Get all orders for an item
    orders = await client.get_item_orders("wisp_prime_set")
    
    # Get online players only
    online_orders = await client.get_item_orders("wisp_prime_set", players="online")
    
    # Get orders with specific rank
    ranked_orders = await client.get_item_orders("wisp_prime_set", rank=5)
```

#### Get Top Orders

```python
async with WarframeMarketClient(language='en') as client:
    # Get top buy/sell orders for an item
    top_orders = await client.get_top_orders_for_item("wisp_prime_set")
    
    print("Top Sell Orders (Cheapest):")
    for order in top_orders['sell']:
        print(f"{order.user.ingame_name}: {order.platinum} plat (Qty: {order.quantity})")

    print("\nTop Buy Orders (Highest Bid):")
    for order in top_orders['buy']:
        print(f"{order.user.ingame_name}: {order.platinum} plat (Qty: {order.quantity})")
```

#### Get Statistics

```python
async with WarframeMarketClient() as client:
    # Get price history and volume statistics
    stats = await client.get_statistics("wisp_prime_set")
    print(stats)
```

#### Get World State

```python
async with WarframeMarketClient() as client:
    # Get current mission data
    missions = await client.get_missions()
    for mission in missions:
        print(f"{mission.node} - {mission.mission_type} ({mission.faction})")
    
    # Get NPC data
    npcs = await client.get_npcs()
    for npc in npcs:
        print(f"NPC: {npc.name}")
```

### Advanced Features

#### Item Matching with Aliases

```python
from warframe import WarframeMarketClient, ItemMatcher

async def advanced_matching_example():
    async with WarframeMarketClient() as client:
        # Get all items for matcher
        items = await client.get_items()
        
        # Create matcher
        matcher = ItemMatcher(items)
        
        # Match items with fuzzy logic
        item, display_name = matcher.match("wisp prime set")
        if item:
            print(f"Matched: {display_name} ({item.url_name})")
        
        # Match with aliases
        item, display_name = matcher.match("花p")
        if item:
            print(f"Matched with alias: {display_name}")
```

#### WebSocket Integration

```python
import asyncio
from warframe import WarframeMarketSocket

async def websocket_example():
    socket = WarframeMarketSocket()
    
    try:
        await socket.connect()
        
        # Register handlers
        def handle_online_report(payload):
            print("Online report:", payload)
        
        socket.on_online_report(handle_online_report)
        
        # Keep connection alive
        await asyncio.sleep(30)
        
    finally:
        await socket.disconnect()
```

## 📚 API Reference

### WarframeMarketClient

| Method | Parameters | Description |
|--------|------------|-------------|
| `get_items()` | None | Get list of all tradable items |
| `get_item(item_url_name)` | `item_url_name` (str) | Get full info about one item |
| `get_item_orders(item_url_name, rank=None, rank_lt=None, players="all")` | `item_url_name` (str), `rank` (int), `rank_lt` (int), `players` (str) | Get all orders for an item |
| `get_top_orders_for_item(item_url_name, rank=None, rank_lt=None, ...)` | Multiple optional parameters | Get top buy/sell orders |
| `get_statistics(item_url_name)` | `item_url_name` (str) | Get price history and statistics |
| `get_missions()` | None | Get list of active missions |
| `get_npcs()` | None | Get list of NPCs |
| `get_most_recent_orders()` | None | Get recent orders stream |
| `get_riven_weapons()` | None | Get list of all tradable riven items |
| `get_riven_weapon(slug)` | `slug` (str) | Get full info about one riven item |
| `get_riven_attributes()` | None | Get list of all attributes for riven weapons |
| `get_asset_url(path)` | `path` (str) | Get asset URL for images |

### Models

#### ItemShort
- `id` (str): Unique identifier
- `url_name` (str): URL-friendly name
- `item_name` (str): Display name
- `thumb` (str): Thumbnail URL
- `vaulted` (bool): Vaulted status
- `all_names` (dict): All localized names

#### Order
- `id` (str): Order ID
- `creation_date` (str): Creation timestamp
- `visible` (bool): Visibility status
- `quantity` (int): Quantity
- `user` (User): User information
- `last_update` (str): Last update timestamp
- `platinum` (int): Platinum amount
- `order_type` (str): Order type (buy/sell)
- `region` (str): Region
- `platform` (str): Platform
- `mod_rank` (int): Mod rank (if applicable)

#### User
- `id` (str): User ID
- `ingame_name` (str): In-game name
- `status` (str): Online status
- `region` (str): Region
- `reputation` (int): Reputation score
- `platform` (str): Platform
- `avatar` (str): Avatar URL
- `last_seen` (str): Last seen timestamp

#### Mission
- `id` (str): Mission ID
- `node` (str): Node name
- `faction` (str): Faction
- `min_enemy_level` (int): Min enemy level
- `max_enemy_level` (int): Max enemy level
- `mission_type` (str): Mission type
- `nightmare` (bool): Nightmare mode
- `archwing` (bool): Archwing mission
- `tower` (bool): Tower mission

#### NPC
- `id` (str): NPC ID
- `name` (str): NPC name
- `thumb` (str): Thumbnail URL

### ItemMatcher

| Method | Parameters | Description |
|--------|------------|-------------|
| `match(query)` | `query` (str) | Match query to item with fuzzy logic and aliases |

## 🛡️ Error Handling

The package provides specific exceptions:

- `WarframeAPIError`: Base exception
- `APIRequestError`: API request errors with status code and message
- `TimeoutError`: Request timeout
- `InvalidParameterError`: Invalid parameters

```python
from warframe import APIRequestError

try:
    async with WarframeMarketClient() as client:
        items = await client.get_items()
except APIRequestError as e:
    print(f"API Error {e.status_code}: {e.message}")
```

## ⚙️ Rate Limiting

The client automatically handles rate limiting with configurable requests per second:

```python
client = WarframeMarketClient(rate_limit=3)  # Default is 3 requests per second
```

## 📝 Version

0.3.0

### Update Log (0.3.0)

- Added `ItemMatcher` class for fuzzy matching and alias support
- Implemented user-defined alias system (supports chained aliases and substring replacement)
- Enhanced normalization logic for item names (handles Chinese interpunct "·")
- Refactored matching logic to be reusable and robust
- Added WebSocket support for real-time data streaming
- Improved documentation and examples

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to Warframe Market for providing the API
- Inspired by the excellent work of the community
