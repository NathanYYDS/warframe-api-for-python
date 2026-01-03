from typing import Dict, List, Optional, Tuple
from .models import ItemShort

class ItemMatcher:
    def __init__(self, items: Optional[List[ItemShort]] = None):
        # Map normalized/aliased name -> (ItemShort, display_name)
        self.item_map: Dict[str, Tuple[ItemShort, str]] = {}
        # User defined aliases: Alias -> Target
        self.user_aliases: Dict[str, str] = {}
        if items:
            self.load_items(items)

    def load_aliases(self, alias_content: str):
        """
        Load aliases from string content.
        Format: target<-alias1<-alias2
        Example: wispp<-花甲p<-花p
        This means: 花p -> wispp, 花甲p -> wispp
        """
        self.user_aliases.clear()
        lines = alias_content.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            parts = [p.strip() for p in line.split('<-')]
            if len(parts) < 2:
                continue
                
            target = parts[0]
            
            # Map all subsequent aliases to the first one (target)
            for alias in parts[1:]:
                # Normalize source for consistent lookup
                norm_source = self._normalize(alias)
                
                # Store normalized source -> raw target
                # We will re-normalize target during resolution if needed
                self.user_aliases[norm_source] = target

    def _normalize(self, name: str) -> str:
        """Standard normalization for lookup keys"""
        normalized = name.lower().replace(" ", "")
        normalized = normalized.replace("总图", "蓝图")
        # Remove interpunct (middle dot) common in CN names like "赋能·专注" -> "赋能专注"
        normalized = normalized.replace("·", "")
        return normalized

    def load_items(self, items: List[ItemShort]):
        """
        Load items and build the alias map.
        """
        self.item_map.clear()
        
        for item in items:
            # We want to index all languages
            # item.all_names is a dict like {'en': 'Wisp Prime Set', 'zh-hans': 'Wisp Prime 套装', ...}
            
            names_to_process = []
            if item.all_names:
                names_to_process.extend(item.all_names.values())
            
            # Fallback if no all_names or to ensure item_name is covered
            if item.item_name and item.item_name not in names_to_process:
                names_to_process.append(item.item_name)
                
            for name in names_to_process:
                self._add_entry(name, item)

    def _add_entry(self, name: str, item: ItemShort):
        """Helper to add entries for a specific name variant"""
        # Store normalized name (lowercase + no space)
        normalized_name = self._normalize(name)
        self.item_map[normalized_name] = (item, name)
        
        # 1. Add alias for "Prime" -> "P"
        if "prime" in name.lower():
            alias_name = name.lower().replace("prime", "p")
            self.item_map[self._normalize(alias_name)] = (item, name)
        
        # 2. Add alias for "头部神经光元" -> "头"
        if "头部神经光元" in name:
            alias_name = name.lower().replace("头部神经光元", "头")
            self.item_map[self._normalize(alias_name)] = (item, name)
        
        # Parts list for blueprint logic
        parts = ["机体", "系统", "头部", "神经", "光元", "枪管", "枪托", "枪机", "刀刃", "握柄", "连接器", "弓臂", "弓弦", 
                 "chassis", "systems", "neuroptics", "barrel", "stock", "receiver", "blade", "handle", "link", "limb", "string"]

        # 3. Add alias for removing "蓝图" / "Blueprint"
        # Only if it is a part (component), not the main blueprint
        if "蓝图" in name:
            has_part = any(p in name for p in parts)
            if has_part:
                alias_name = name.lower().replace("蓝图", "")
                self.item_map[self._normalize(alias_name)] = (item, name)

        if "blueprint" in name.lower():
            has_part = any(p in name.lower() for p in parts)
            if has_part:
                alias_name = name.lower().replace("blueprint", "")
                self.item_map[self._normalize(alias_name)] = (item, name)

        # 4. Add alias for "蓝图" -> "总图"
        # This is implicitly handled by _normalize which converts "总图" -> "蓝图" in the query.
        # But we keep it if we want to support reverse lookup or exact matches if normalization changes.
        # Actually, since _normalize maps input "总图" -> "蓝图", 
        # and "蓝图" is in the map (from original name), we don't strictly need to add "总图" to the map.
        # BUT, to match legacy behavior or ensure robustness:
        if "蓝图" in name:
            alias_name = name.lower().replace("蓝图", "总图")
            # Note: _normalize("...总图") -> "...蓝图", so this key effectively becomes the same as the original key
            # unless we skip normalization for storage? No, consistency is better.
            # If we store "总图" normalized, it becomes "蓝图". So it overwrites the original entry (same content).
            # So this block effectively does nothing if _normalize converts 总图->蓝图.
            pass

        # 5. COMBINED ALIASES
        current_name = name.lower()
        original_lower = current_name
        
        if "prime" in current_name:
            current_name = current_name.replace("prime", "p")
        if "头部神经光元" in current_name:
            current_name = current_name.replace("头部神经光元", "头")
            
        if "蓝图" in current_name:
            has_part = any(p in name for p in parts)
            if has_part:
                current_name = current_name.replace("蓝图", "")
        
        if "blueprint" in current_name:
            has_part = any(p in name.lower() for p in parts)
            if has_part:
                current_name = current_name.replace("blueprint", "")

        if current_name != original_lower:
            self.item_map[self._normalize(current_name)] = (item, name)

    def match(self, query: str) -> Tuple[Optional[ItemShort], Optional[str]]:
        """
        Match a query string to an item.
        Returns (ItemShort, display_name) or (None, None).
        """
        if not query:
            return None, None
            
        # Normalize input
        lookup_name = self._normalize(query)
        
        # Apply user aliases (substring replacement)
        # We prioritize longest aliases first to avoid partial matches of shorter aliases taking precedence
        # Cache sorted keys could be an optimization but fine for now
        sorted_aliases = sorted(self.user_aliases.keys(), key=len, reverse=True)
        
        max_depth = 10
        for _ in range(max_depth):
            replaced = False
            for alias in sorted_aliases:
                if alias in lookup_name:
                    target = self.user_aliases[alias]
                    # Only replace if it actually changes something (avoid A->A loops if any)
                    new_name = lookup_name.replace(alias, target)
                    if new_name != lookup_name:
                        lookup_name = self._normalize(new_name) # Re-normalize after replacement
                        replaced = True
                        break 
            
            if not replaced:
                break
        
        if lookup_name in self.item_map:
            return self.item_map[lookup_name]
            
        # Fallback strategies
        
        # 1. Try appending "一套" (for Chinese users)
        fallback_cn_set = lookup_name + "一套"
        if fallback_cn_set in self.item_map:
            return self.item_map[fallback_cn_set]
            
        # 2. Try appending "set"
        fallback_set = lookup_name + "set"
        if fallback_set in self.item_map:
            return self.item_map[fallback_set]
            
        # 3. Try appending "蓝图"
        fallback_bp = lookup_name + "蓝图"
        if fallback_bp in self.item_map:
            return self.item_map[fallback_bp]
            
        # 4. Try appending "blueprint"
        fallback_bp_en = lookup_name + "blueprint"
        if fallback_bp_en in self.item_map:
            return self.item_map[fallback_bp_en]

        return None, None
