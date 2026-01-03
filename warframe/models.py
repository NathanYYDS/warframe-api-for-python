from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict

@dataclass
class ItemShort:
    id: str
    url_name: str
    item_name: str
    thumb: str
    vaulted: Optional[bool] = None
    # Add a new field to store all localized names
    all_names: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any], preferred_lang: Optional[str] = None) -> 'ItemShort':
        # Handle V2 structure
        # data = {'id': '...', 'slug': '...', 'i18n': {'en': {'name': '...', 'thumb': '...'}}}
        
        url_name = data.get('slug') or data.get('url_name') or data.get('urlName')
        
        # Extract info from i18n if available, defaulting to 'en' or first available
        i18n = data.get('i18n', {})
        all_names = {}
        if i18n:
            lang_data = None
            if preferred_lang and preferred_lang in i18n:
                lang_data = i18n.get(preferred_lang)
            if not lang_data:
                lang_data = i18n.get('en') or next(iter(i18n.values()), {})
            item_name = lang_data.get('name')
            thumb = lang_data.get('thumb')
            
            # Populate all_names
            for lang, details in i18n.items():
                if name := details.get('name'):
                    all_names[lang] = name
        else:
            item_name = data.get('item_name') or data.get('itemName')
            thumb = data.get('thumb')

        return cls(
            id=data.get('id'),
            url_name=url_name,
            item_name=item_name,
            thumb=thumb,
            vaulted=data.get('vaulted'),
            all_names=all_names
        )

@dataclass
class User:
    id: str
    ingame_name: str
    status: str
    region: str
    reputation: int
    platform: Optional[str] = None
    avatar: Optional[str] = None
    last_seen: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        return cls(
            id=data.get('id'),
            ingame_name=data.get('ingame_name') or data.get('ingameName'),
            status=data.get('status'),
            region=data.get('region') or data.get('locale'),
            reputation=data.get('reputation'),
            platform=data.get('platform'),
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
        
        # Try to get platform/region from order data, fallback to user data
        platform = data.get('platform')
        if not platform and user:
            platform = user.platform
            
        region = data.get('region')
        if not region and user:
            region = user.region

        return cls(
            id=data.get('id'),
            creation_date=data.get('creation_date') or data.get('creationDate') or data.get('createdAt'),
            visible=data.get('visible'),
            quantity=data.get('quantity'),
            user=user,
            last_update=data.get('last_update') or data.get('lastUpdate') or data.get('updatedAt'),
            platinum=data.get('platinum'),
            order_type=data.get('order_type') or data.get('orderType') or data.get('type'),
            region=region,
            platform=platform,
            mod_rank=data.get('mod_rank') or data.get('modRank') or data.get('rank')
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

@dataclass
class Riven:
    """Riven weapon model"""
    id: str
    slug: str
    game_ref: str
    group: str
    riven_type: str
    disposition: float
    req_mastery_rank: int
    item_name: str
    wiki_link: Optional[str] = None
    icon: Optional[str] = None
    thumb: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Riven':
        # Extract name from i18n
        i18n = data.get('i18n', {})
        item_name = ""
        if i18n:
            lang_data = i18n.get('en') or next(iter(i18n.values()), {})
            item_name = lang_data.get('name', '')
        
        return cls(
            id=data.get('id'),
            slug=data.get('slug'),
            game_ref=data.get('gameRef'),
            group=data.get('group'),
            riven_type=data.get('rivenType'),
            disposition=data.get('disposition'),
            req_mastery_rank=data.get('reqMasteryRank'),
            item_name=item_name,
            wiki_link=data.get('i18n', {}).get('en', {}).get('wikiLink'),
            icon=data.get('i18n', {}).get('en', {}).get('icon'),
            thumb=data.get('i18n', {}).get('en', {}).get('thumb')
        )

@dataclass
class RivenAttribute:
    """Riven attribute model"""
    id: str
    slug: str
    game_ref: str
    group: str
    prefix: str
    suffix: str
    exclusive_to: List[str]
    positive_is_negative: bool
    positive_only: bool
    negative_only: bool
    unit: str
    item_name: str
    icon: Optional[str] = None
    thumb: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RivenAttribute':
        # Extract name from i18n
        i18n = data.get('i18n', {})
        item_name = ""
        if i18n:
            lang_data = i18n.get('en') or next(iter(i18n.values()), {})
            item_name = lang_data.get('name', '')
        
        return cls(
            id=data.get('id'),
            slug=data.get('slug'),
            game_ref=data.get('gameRef'),
            group=data.get('group'),
            prefix=data.get('prefix'),
            suffix=data.get('suffix'),
            exclusive_to=data.get('exclusiveTo', []),
            positive_is_negative=data.get('positiveIsNegative'),
            positive_only=data.get('positiveOnly'),
            negative_only=data.get('negativeOnly'),
            unit=data.get('unit'),
            item_name=item_name,
            icon=data.get('i18n', {}).get('en', {}).get('icon'),
            thumb=data.get('i18n', {}).get('en', {}).get('thumb')
        )
