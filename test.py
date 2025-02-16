from warframe import WarframeMarketApi

api = WarframeMarketApi()
items = api.getItemsList()

for item in items:
    print(item)
