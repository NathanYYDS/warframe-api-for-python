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
    def getItemsList(self, language: str = 'zh-hans') -> List[Item]:
        """
        Fetches the list of items from the Warframe Market API.

        Example:
            wf_api = WarframeMarketApi()
            items = wf_api.getItemsList(language='zh-hans')

        Parameters:
            language (str): The language to use for the request, defaults to 'zh-hans' (Simplified Chinese).
            Available language options:
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

        Returns:
            List[Item]: A list of Item objects. Returns an empty list if the request fails.

        Raises:
            ValueError: If the provided language is not in the supported languages list.
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

        response = requests.get(url=api_url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            items_data = response.json()["payload"]["items"]
            items = [Item(**item) for item in items_data]
            
            # Print each Item object's information
            for item in items:
                print(item)
                
            print(f"Total items fetched: {len(items)}")
            return items
        else:
            print(f"Failed to fetch items list, status code: {response.status_code}")
            return []