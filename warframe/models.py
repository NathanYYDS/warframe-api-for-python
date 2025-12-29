from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict

@dataclass
class ItemShort:
    id: str
    url_name: str
    item_name: str
    thumb: str
    vaulted: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any], preferred_lang: Optional[str] = None) -> 'ItemShort':
        # Handle V2 structure
        # data = {'id': '...', 'slug': '...', 'i18n': {'en': {'name': '...', 'thumb': '...'}}}
        
        url_name = data.get('slug') or data.get('url_name') or data.get('urlName')
        
        # Extract info from i18n if available, defaulting to 'en' or first available
        i18n = data.get('i18n', {})
        if i18n:
            lang_data = None
            if preferred_lang and preferred_lang in i18n:
                lang_data = i18n.get(preferred_lang)
            if not lang_data:
                lang_data = i18n.get('en') or next(iter(i18n.values()), {})
            item_name = lang_data.get('name')
            thumb = lang_data.get('thumb')
        else:
            item_name = data.get('item_name') or data.get('itemName')
            thumb = data.get('thumb')

        return cls(
            id=data.get('id'),
            url_name=url_name,
            item_name=item_name,
            thumb=thumb,
            vaulted=data.get('vaulted')
        )

@dataclass
class User:
    id: str
    ingame_name: str
    status: str
    region: str
    reputation: int
    avatar: Optional[str] = None
    last_seen: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        return cls(
            id=data.get('id'),
            ingame_name=data.get('ingame_name') or data.get('ingameName'),
            status=data.get('status'),
            region=data.get('region'),
            reputation=data.get('reputation'),
            avatar=data.get('avatar'),
            last_seen=data.get('last_seen') or data.get('lastSeen')
        )

@dataclass
class Order:
    id: str
    creation_date: str
    visible: bool
    quantity: int
    user: User
    last_update: str
    platinum: int
    order_type: str
    region: str
    platform: str
    mod_rank: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Order':
        user_data = data.get('user')
        user = User.from_dict(user_data) if user_data else None
        
        return cls(
            id=data.get('id'),
            creation_date=data.get('creation_date') or data.get('creationDate'),
            visible=data.get('visible'),
            quantity=data.get('quantity'),
            user=user,
            last_update=data.get('last_update') or data.get('lastUpdate'),
            platinum=data.get('platinum'),
            order_type=data.get('order_type') or data.get('orderType') or data.get('type'),
            region=data.get('region'),
            platform=data.get('platform'),
            mod_rank=data.get('mod_rank') or data.get('modRank')
        )

@dataclass
class Mission:
    id: str
    node: str
    faction: str
    min_enemy_level: int
    max_enemy_level: int
    mission_type: str
    nightmare: bool
    archwing: bool
    tower: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Mission':
        return cls(
            id=data.get('id'),
            node=data.get('node'),
            faction=data.get('faction'),
            min_enemy_level=data.get('min_enemy_level') or data.get('minEnemyLevel'),
            max_enemy_level=data.get('max_enemy_level') or data.get('maxEnemyLevel'),
            mission_type=data.get('mission_type') or data.get('type'),
            nightmare=data.get('nightmare'),
            archwing=data.get('archwing'),
            tower=data.get('tower')
        )
    
@dataclass
class NPC:
    id: str
    name: str
    thumb: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NPC':
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            thumb=data.get('thumb')
        )
