import requests
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Item:
    thumb: str
    item_name: str
    id: str
    url_name: str
    vaulted: Optional[bool] = None

class WarframeMarketApi:
    def getItemsList(self, language: str = 'zh-hans',timeout:int = 5) -> List[Item]:
        """
        Fetches the list of items from the Warframe Market API.

        Example:
            wf_api = WarframeMarketApi()
            items = wf_api.getItemsList(language='zh-hans')

        Parameters:
            language (str): The language to use for the request, defaults to 'zh-hans' (Simplified Chinese).
                - 'en' (English)
                - 'ru' (Russian)
                - 'ko' (Korean)
                - 'de' (German)
                - 'fr' (French)
                - 'pt' (Portuguese)
                - 'zh-hans' (Simplified Chinese)
                - 'zh-hant' (Traditional Chinese)
                - 'es' (Spanish)
                - 'it' (Italian)
                - 'pl' (Polish)
            timeout (int): The timeout in seconds for the request, defaults to 5 seconds.

        Returns:
            List[Item]: A list of Item objects. Returns an empty list if the request fails.

        Raises:
            ValueError: If the provided language option is not valid.
        """
        api_url = "https://api.warframe.market/v1/items"
        
        # Validate if the provided language is valid
        available_languages = ['en', 'ru', 'ko', 'de', 'fr', 'pt', 'zh-hans', 'zh-hant', 'es', 'it', 'pl']
        if language not in available_languages:
            raise ValueError(f"Unsupported language option '{language}'. Available options are: {', '.join(available_languages)}")
        
        headers = {
            'accept': 'application/json',
            'Language': language
        }

        try:
            response = requests.get(url=api_url, headers=headers, timeout=timeout)
        except requests.Timeout:
            print(f"<getItemList> requests timed out after {timeout} seconds.")
            return []
        except requests.RequestException as e:
            print(f"<getItemList> has an error occurred: {e}")
            return []
        items_data = response.json()["payload"]["items"]
        items = [Item(**item) for item in items_data]
        
        # Print each Item object's information
        for item in items:
            print(item)
            
        print(f"Total items fetched: {len(items)}")
        return items