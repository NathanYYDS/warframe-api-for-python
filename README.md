# warframe-api-for-python

[中文文档](README_zh.md)

A robust, asynchronous Python wrapper for the Warframe Market API (v2). This package allows developers to easily interact with Warframe Market data, including items, orders, statistics, missions, and more.

## Installation

```bash
git clone https://github.com/NathanYYDS/warframe-api-for-python.git
cd warframe-api-for-python
pip install -e .
```

## Features

- **Asynchronous**: Built on `aiohttp` for high-performance, non-blocking API calls.
- **Multi-language Support**: Full support for all 12 languages supported by Warframe Market (en, zh-hans, ko, ru, etc.).
- **Type Hinting**: Uses Python dataclasses for clear data structures and IDE autocompletion.
- **Comprehensive Coverage**: Access items, orders, statistics, missions, NPCs, and user profiles.

## Usage

### Quick Start

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

### Advanced Usage

#### specifying Language and Platform

You can specify the language and platform when initializing the client:

```python
# Initialize with Simplified Chinese and PC platform
client = WarframeMarketClient(language='zh-hans', platform='pc')
```

#### Fetching Top Orders

Get the best buy and sell orders for a specific item:

```python
async with WarframeMarketClient(language='en') as client:
    # Get top orders for "Wisp Prime Set"
    # Note: You need the 'url_name' of the item (e.g., "wisp_prime_set")
    top_orders = await client.get_top_orders_for_item("wisp_prime_set")
    
    print("Top Sell Orders (Cheapest):")
    for order in top_orders['sell']:
        print(f"{order.user.ingame_name}: {order.platinum} plat (Qty: {order.quantity})")

    print("\nTop Buy Orders (Highest Bid):")
    for order in top_orders['buy']:
        print(f"{order.user.ingame_name}: {order.platinum} plat (Qty: {order.quantity})")
```

#### Getting Item Statistics

Retrieve historical price statistics for an item:

```python
async with WarframeMarketClient() as client:
    stats = await client.get_statistics("wisp_prime_set")
    # stats contains historical data like volume, min/max price, etc.
    print(stats)
```

#### Getting World State (Missions)

Access current mission data:

```python
async with WarframeMarketClient() as client:
    missions = await client.get_missions()
    for mission in missions:
        print(f"{mission.node} - {mission.mission_type} ({mission.faction})")
```

## Supported Functions

The client supports the following main operations:

- `get_items()`: Retrieve a list of all items.
- `get_item(item_url_name)`: Get detailed information about a specific item.
- `get_item_orders(item_url_name, ...)`: Get all orders for an item with optional filtering.
- `get_top_orders_for_item(item_url_name)`: Get the best buy/sell orders for an item.
- `get_statistics(item_url_name)`: Get price history and volume statistics.
- `get_most_recent_orders()`: Get the stream of most recently posted orders.
- `get_missions()`: Get list of active missions.
- `get_npcs()`: Get list of NPCs.

## Version

0.3.0

### Update Log (0.3.0)
- Added `ItemMatcher` class for fuzzy matching and alias support.
- Implemented user-defined alias system (supports chained aliases and substring replacement).
- Enhanced normalization logic for item names (handles Chinese interpunct "·").
- Refactored matching logic to be reusable and robust.

## License

MIT
