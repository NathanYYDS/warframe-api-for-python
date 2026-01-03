# Warframe Market API for Python - API Documentation

## Overview

This document provides comprehensive documentation for the Warframe Market API wrapper for Python. The library provides asynchronous access to Warframe Market data including items, orders, statistics, missions, and more.

## Table of Contents

1. [Core Classes](#core-classes)
2. [WarframeMarketClient](#warframemarketclient)
3. [Models](#models)
4. [ItemMatcher](#itemmatcher)
5. [WarframeMarketSocket](#warframemarketsocket)
6. [Exceptions](#exceptions)
7. [Usage Examples](#usage-examples)

## Core Classes

### WarframeMarketClient

The main class for interacting with the Warframe Market API.

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `language` | str | `'en'` | Language code (en, zh-hans, ko, ru, de, fr, pt, zh-hant, es, it, pl, uk) |
| `platform` | str | `'pc'` | Platform (pc, ps4, xb1, switch) |
| `timeout` | int | `10` | Request timeout in seconds |
| `rate_limit` | int | `3` | Maximum requests per second |
| `token` | Optional[str] | `None` | Authentication token |

#### Methods

##### `__aenter__()`
Enter the async context manager.

##### `__aexit__(exc_type, exc_val, exc_tb)`
Exit the async context manager.

##### `open()`
Open the HTTP session.

##### `close()`
Close the HTTP session.

##### `set_token(token: str)`
Set authentication token.

##### `clear_token()`
Clear authentication token.

##### `get_items() -> List[ItemShort]`
Get list of all tradable items.

##### `get_item(item_url_name: str) -> Dict[str, Any]`
Get full information about a specific item.

##### `get_item_orders(item_url_name: str, rank: Optional[int] = None, rank_lt: Optional[int] = None, players: str = "all") -> List[Order]`
Get all orders for an item.

##### `get_missions() -> List[Mission]`
Get list of all missions.

##### `get_npcs() -> List[NPC]`
Get list of all NPCs.

##### `get_statistics(item_url_name: str) -> Dict[str, Any]`
Get statistics for an item.

##### `get_most_recent_orders() -> List[Order]`
Get most recent orders.

##### `get_top_orders_for_item(item_url_name: str, rank: Optional[int] = None, rank_lt: Optional[int] = None, charges: Optional[int] = None, charges_lt: Optional[int] = None, amber_stars: Optional[int] = None, amber_stars_lt: Optional[int] = None, cyan_stars: Optional[int] = None, cyan_stars_lt: Optional[int] = None, subtype: Optional[str] = None) -> Dict[str, List[Order]]`
Get top buy/sell orders for an item.

##### `get_asset_url(path: str) -> str`
Get asset URL for images.

### ItemMatcher

Class for fuzzy matching and alias support for item names.

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | Optional[List[ItemShort]] | `None` | List of items to initialize the matcher with |

#### Methods

##### `load_aliases(alias_content: str)`
Load user-defined aliases from string content.

##### `load_items(items: List[ItemShort])`
Load items and build the alias map.

##### `match(query: str) -> Tuple[Optional[ItemShort], Optional[str]]`
Match a query string to an item.

### WarframeMarketSocket

WebSocket client for real-time data streaming.

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `language` | str | `'en'` | Language code |
| `platform` | str | `'pc'` | Platform |
| `token` | Optional[str] | `None` | Authentication token |
| `timeout` | int | `10` | Connection timeout |

#### Methods

##### `connect()`
Connect to WebSocket.

##### `disconnect()`
Disconnect from WebSocket.

##### `sign_in(token: str) -> Any`
Sign in with authentication token.

##### `sign_out() -> Any`
Sign out.

##### `on(route: str, handler: Callable)`
Register a handler for a specific route.

##### `on_online_report(handler: Callable)`
Register handler for online reports.

## Models

### ItemShort

Represents a basic item with minimal information.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | str | Unique identifier |
| `url_name` | str | URL-friendly name |
| `item_name` | str | Display name |
| `thumb` | str | Thumbnail URL |
| `vaulted` | Optional[bool] | Vaulted status |
| `all_names` | Dict[str, str] | All localized names |

#### Class Methods

##### `from_dict(data: Dict[str, Any], preferred_lang: Optional[str] = None) -> ItemShort`
Create ItemShort instance from dictionary data.

### Order

Represents an order on Warframe Market.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | str | Order ID |
| `creation_date` | str | Creation timestamp |
| `visible` | bool | Visibility status |
| `quantity` | int | Quantity |
| `user` | User | User information |
| `last_update` | str | Last update timestamp |
| `platinum` | int | Platinum amount |
| `order_type` | str | Order type (buy/sell) |
| `region` | str | Region |
| `platform` | str | Platform |
| `mod_rank` | Optional[int] | Mod rank (if applicable) |

#### Class Methods

##### `from_dict(data: Dict[str, Any]) -> Order`
Create Order instance from dictionary data.

### User

Represents a user on Warframe Market.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | str | User ID |
| `ingame_name` | str | In-game name |
| `status` | str | Online status |
| `region` | str | Region |
| `reputation` | int | Reputation score |
| `platform` | Optional[str] | Platform |
| `avatar` | Optional[str] | Avatar URL |
| `last_seen` | Optional[str] | Last seen timestamp |

#### Class Methods

##### `from_dict(data: Dict[str, Any]) -> User`
Create User instance from dictionary data.

### Mission

Represents a mission in Warframe.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | str | Mission ID |
| `node` | str | Node name |
| `faction` | str | Faction |
| `min_enemy_level` | int | Minimum enemy level |
| `max_enemy_level` | int | Maximum enemy level |
| `mission_type` | str | Mission type |
| `nightmare` | bool | Nightmare mode |
| `archwing` | bool | Archwing mission |
| `tower` | bool | Tower mission |

#### Class Methods

##### `from_dict(data: Dict[str, Any]) -> Mission`
Create Mission instance from dictionary data.

### NPC

Represents an NPC in Warframe.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | str | NPC ID |
| `name` | str | NPC name |
| `thumb` | Optional[str] | Thumbnail URL |

#### Class Methods

##### `from_dict(data: Dict[str, Any]) -> NPC`
Create NPC instance from dictionary data.

## Exceptions

### WarframeAPIError

Base exception class for all Warframe API errors.

### APIRequestError

Exception raised for API request errors.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `status_code` | int | HTTP status code |
| `message` | str | Error message |

### TimeoutError

Exception raised for request timeouts.

### InvalidParameterError

Exception raised for invalid parameters.

## Usage Examples

### Basic Client Usage

```python
import asyncio
from warframe import WarframeMarketClient

async def basic_usage():
    async with WarframeMarketClient() as client:
        # Get all items
        items = await client.get_items()
        print(f"Found {len(items)} items")
        
        # Get specific item
        item = await client.get_item("wisp_prime_set")
        print(item)
        
        # Get orders
        orders = await client.get_item_orders("wisp_prime_set")
        print(f"Found {len(orders)} orders")
```

### Advanced Matching

```python
from warframe import WarframeMarketClient, ItemMatcher

async def advanced_matching():
    async with WarframeMarketClient() as client:
        # Get all items
        items = await client.get_items()
        
        # Create matcher
        matcher = ItemMatcher(items)
        
        # Match with fuzzy logic
        item, display_name = matcher.match("wisp prime set")
        if item:
            print(f"Matched: {display_name} ({item.url_name})")
        
        # Match with aliases
        item, display_name = matcher.match("花p")
        if item:
            print(f"Matched with alias: {display_name}")
```

### WebSocket Usage

```python
import asyncio
from warframe import WarframeMarketSocket

async def websocket_usage():
    socket = WarframeMarketSocket()
    
    try:
        await socket.connect()
        
        # Register handler for online reports
        def handle_online_report(payload):
            print("Online report:", payload)
        
        socket.on_online_report(handle_online_report)
        
        # Keep connection alive
        await asyncio.sleep(30)
        
    finally:
        await socket.disconnect()
```

### Error Handling

```python
from warframe import WarframeMarketClient, APIRequestError

async def error_handling():
    try:
        async with WarframeMarketClient() as client:
            items = await client.get_items()
    except APIRequestError as e:
        print(f"API Error {e.status_code}: {e.message}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

## Rate Limiting

The client automatically handles rate limiting with configurable requests per second:

```python
# Default is 3 requests per second
client = WarframeMarketClient(rate_limit=3)

# Custom rate limit
client = WarframeMarketClient(rate_limit=5)
```

## Language Support

The library supports all 12 languages supported by Warframe Market:

- English (`en`)
- Simplified Chinese (`zh-hans`)  
- Korean (`ko`)
- Russian (`ru`)
- German (`de`)
- French (`fr`)
- Portuguese (`pt`)
- Traditional Chinese (`zh-hant`)
- Spanish (`es`)
- Italian (`it`)
- Polish (`pl`)
- Ukrainian (`uk`)

## Platform Support

Supported platforms:
- PC (`pc`)
- PlayStation 4 (`ps4`)
- Xbox One (`xb1`)
- Nintendo Switch (`switch`)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
