
![](/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F1be91aea-8129-4c98-a207-838c3fdf495b%2Fbc61453f-1243-467c-bf2e-ea0844f76a22%2Faaed29f9711eb6abbfb92f20ff8b671d211eb068.jpg?table=block&id=5d987e4a-a2f7-4b55-a80d-b1a09932459d&spaceId=1be91aea-8129-4c98-a207-838c3fdf495b&width=2000&userId=&cache=v2) 

![页面图标](/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F1be91aea-8129-4c98-a207-838c3fdf495b%2Fac47c448-f2ec-432c-a192-0d0084dfc41b%2Fgowfm3-icon2.png?id=5d987e4a-a2f7-4b55-a80d-b1a09932459d&table=block&spaceId=1be91aea-8129-4c98-a207-838c3fdf495b&width=250&userId=&cache=v2)

Owner
![KycKyc](https://lh3.googleusercontent.com/a/ACg8ocL9GeRrMKjNPtAPDEfL5hxH_HMZtHbx6kXV5ts6M7tJP1s=s100)
KycKyc

Tags
documentation, api

Last edited time
2025年9月14日 23:05

其他 1 个属性

## General

[](/Data-Models-65e9ab01868c4dcca6ba499e68a04ac9?pvs=25)

[![💽](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) Data Models](/Data-Models-65e9ab01868c4dcca6ba499e68a04ac9?pvs=25)

[](/Websockets-1d8515beb0be806a87e9e0fc71aad9aa?pvs=25)

[![📡](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) Websockets](/Websockets-1d8515beb0be806a87e9e0fc71aad9aa?pvs=25)

[](/OAuth-2-0-04e1e72398db4cf8ae1b7b1bae4abcc1?pvs=25)

[![🫴](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) OAuth 2.0](/OAuth-2-0-04e1e72398db4cf8ae1b7b1bae4abcc1?pvs=25)

### Version

Documentation describes:
v0.21.2

### Base URLs

Api base path:
https://api.warframe.market/v2/

Some fields could be a path to item icon, or user avatar, or profile background, like:
`items/images/en/dual_rounds.304395bed5a40d76ddb9a62c76736d94.png`

base path for all kind of these things is:
https://warframe.market/static/assets/

### Rate limits

3 requests per second, for now, probably i’ll rise it later.

### Global Parameters

For each query, you can or must add these parameters to get the results you are looking for.

#### Language Header

WFM have support for 12 languages:
ko, ru, de, fr, pt, zh-hans, zh-hant, es, it, pl, uk, en

![➡️ 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) Default value is `en`

Example: Send request with `Language: ko`
Get response like: `{ i18n:{ en:{...},ko:{...} } }`

#### Platform Header

WFM is designed to cater to users across various gaming platforms. It currently supports five platforms:
pc, ps4, xbox, switch, mobile

![➡️ 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) Default value is `pc`

#### Crossplay Header

In addition to platforms, we also have cross-play option. Players across different platforms can trade if they have cross-play enabled in their game settings.

`Platform: pc` `Crossplay: true`

On the other hand, if you only want to get orders from PC and exclude cross-play orders from other platforms, use:

`Platform: pc` `Crossplay: false`

![ℹ️](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) You will still receive orders or contracts from players who have PC and cross-play enabled.

ALT

![➡️ 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) Default value is `true`

### Response Structure

Response body:
`{ apiVersion:"x.x.x",data: payload | null,error: payload | null }`

Where:
`apiVersion` string - is semVer compatible version of our API server.
`data` object | null - if request was successful there you can locate your response data
`error` object | null - if there were any errors, you'll find them here

### Errors

#### Hitting rate limits or other protection from CF

WFM implements rate limits to ensure fair usage and protect against excessive requests per second (RPS). Exceeding these limits results in a `429` error code, often accompanied by a CloudFlare challenge page. In some cases, excessive RPS may lead to outright blocking by CloudFlare.Additionally, if there are too many concurrent connections from a single IP address, a `509` error code is returned. This is a measure to prevent overloading the server with multiple connections from the same source.

#### Handled errors

`{ apiVersion:"x.x.x",data:null,error:{ request:[...],inputs:{ fieldOne:"",fieldTwo:"",...},},}`

Where:
`request` []string - general level request error, like `app.errors.unauthorized`, `app.errors.forbidden`, `app.order.error.exceededOrderLimit`, etc
`inputs` map[string]string - input level errors, like form errors, query param errors, multipart/form-data errors. Example, you are trying to create an order, and put platinum as -1, you will get: `inputs: {platinum: “app.field.tooSmall”}`

#### Unhandled errors

Request killed goroutine for some reason, critical error. You will get `5xx` error without any content.

## Endpoints

Here is our advanced endpoint marking system:

![🔜](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - In development
![🚧](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Unstable or unfinished endpoints, use at your own risk
![♿](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Rate limited endpoints, mind you calls lads
![🔒](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Require authorization
![💔](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Available only for 1st party apps
![🇬🇧](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Can request additional [translations](/5d987e4aa2f74b55a80db1a09932459d?pvs=25#a3aad4b7061f4dc7a7d7b33482a9782a)
![🚫](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Deprecated

### Manifests

Sounds familiar …

#### GET /v2/versions

This endpoint retrieves the current version number of the server's resources, formatted either as a semVer string or as an arbitrary version identifier. Whenever the server database is updated or new versions of mobile apps are released, the version number for relevant resources is also updated. Client applications can check this endpoint periodically to fetch the current server version. A discrepancy between the server's version number and the client's indicates that an update has occurred. In such cases, clients should refresh their local data, like re-downloading item lists, to stay synchronized with the server's latest updates.

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:{ apps:{ ios:"x.x.x",android:"x.x.x",minIos:"x.x.x",minAndroid:"x.x.x",},collections:{ items:"base64",rivens:"base64",liches:"base64",sisters:"base64",missions:"base64",npcs:"base64",locations:"base64",},updatedAt:"2021-05-21T14:59:02Z",},error:null }`

#### GET /v2/items

Get list of all tradable items

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[ItemShort,ItemShort,...],error:null }`

Data model inside: [ItemShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#dfd0751842e34832815c6de6abcc510b)

ALT

#### GET /v2/item/{slug}

Get full info about one, particular item

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field form [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc) and [ItemShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#dfd0751842e34832815c6de6abcc510b) models

Response:
`{ apiVersion:"x.x.x",data:Item,error:null }`

Data model inside: [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc)

ALT

#### GET /v2/item/{slug}/set

If the queried item is not part of any set, the response will contain an array with just that one item.
If the item is part of a set or is a set itself, the response will include an array of all items within that set.

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field from [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc) and [ItemShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#dfd0751842e34832815c6de6abcc510b) models

Response:
`{ apiVersion:"x.x.x",data:{ id:"54a73e65e779893a797fff72",items:[Item,Item,...] } error:null }`

Data model inside: [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc)

ALT

Response Fields
`id` string - id of an item you requested.
`items` []Item - array of items

#### GET /v2/riven/weapons

Get list of all tradable riven items

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[Riven,Riven,...],error:null }`

Data model inside is clickable: [Riven](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#124515beb0be80fb9447f8a01f3129d9)

ALT

#### GET /v2/riven/weapon/{slug}

Get full info about one, particular riven item

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field form [Riven](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#124515beb0be80ea8ed9dab2327a68d0) model

Response:
`{ apiVersion:"x.x.x",data:Riven,error:null }`

Data model inside: [Riven](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#124515beb0be80ea8ed9dab2327a68d0)

ALT

#### GET /v2/riven/attributes

Get list of all attributes for riven weapons

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[RivenAttribute,RivenAttribute,...],error:null }`

Data model inside: [RivenAttribute](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#124515beb0be80579471f998730d3438)

ALT

#### GET /v2/lich/weapons

Get list of all tradable lich weapons

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[LichWeapon,LichWeapon,...],error:null }`

Data model inside: [LichWeapon](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#3ea197e3e83b48979de6804833ce5929)

ALT

#### GET /v2/lich/weapon/{slug}

Get full info about one, particular lich weapon

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field form LichWeapon model

Response:
`{ apiVersion:"x.x.x",data:LichWeapon,error:null }`

Data model inside: [LichWeapon](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#3ea197e3e83b48979de6804833ce5929)

ALT

#### GET /v2/lich/ephemeras

Get list of all tradable lich ephemeras

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[LichEphemera,LichEphemera,...],error:null }`

Data model inside: [LichEphemera](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#144515beb0be8004aa9ede5e9703b7fe)

ALT

#### GET /v2/lich/quirks

Get list of all tradable lich quirks

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[LichQuirk,LichQuirk,...],error:null }`

Data model inside: [LichQuirk](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#144515beb0be801bae53c61fb1c79ddc)

ALT

#### GET /v2/sister/weapons

Get list of all tradable sister weapons

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[SisterWeapon,SisterWeapon,...],error:null }`

Data model inside: [SisterWeapon](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#148515beb0be8099ab53dd2901e9ee63)

ALT

#### GET /v2/sister/weapon/{slug}

Get full info about one, particular sister weapon

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field form SisterWeapon model

Response:
`{ apiVersion:"x.x.x",data:SisterWeapon,error:null }`

Data model inside: [SisterWeapon](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#148515beb0be8099ab53dd2901e9ee63)

ALT

#### GET /v2/sister/ephemeras

Get list of all tradable sister ephemera’s

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[SisterEphemera,SisterEphemera,...],error:null }`

Data model inside: [SisterEphemera](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#148515beb0be80e2a4fec75d78aa8994)

ALT

#### GET /v2/sister/quirks

Get list of all tradable sister quirks

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[SisterQuirk,SisterQuirk,...],error:null }`

Data model inside: [SisterQuirk](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#148515beb0be80558b56c8609474172d)

ALT

#### GET /v2/locations

Get list of all locations (that are known to WFM)

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[Location,Location,...],error:null }`

Data model inside: [Location](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#144515beb0be800b8d4fe582342b8080)

ALT

#### GET /v2/npcs

Get list of all NPC’s (that are known to WFM)

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[Npc,Npc,...],error:null }`

Data model inside: [Npc](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#144515beb0be8069b9aae256456f22e1)

ALT

#### GET /v2/missions

Get list of all Missions (that are known to WFM)

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[Mission,Mission,...],error:null }`

Data model inside: [Mission](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#144515beb0be8011b183d3f0a46545b3)

ALT

### Orders

#### GET /v2/orders/recent

Get the most recent orders. 500 max, for the last 4 hours, sorted by `createdAt`
Cached, with 1min refresh interval.

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[OrderWithUser,OrderWithUser,OrderWithUser,...] error:null }`

Data model inside: [OrderWithUser](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#1955a46ed3914f859cbe405f6d6c0c32)

ALT

#### GET /v2/orders/item/{slug}

Get a list of all orders for an item from users who was online within the last 7 days.

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field form [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc) and [ItemShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#dfd0751842e34832815c6de6abcc510b) models

Response:
`{ apiVersion:"x.x.x",data:[OrderWithUser,OrderWithUser,OrderWithUser,...] error:null }`

Data model inside: [OrderWithUser](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#1955a46ed3914f859cbe405f6d6c0c32)

ALT

#### GET /v2/orders/item/{slug}/top

This endpoint is designed to fetch the top 5 buy and top 5 sell orders for a specific item, exclusively from online users. Orders are sorted by price.

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - field from [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc) and [ItemShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#dfd0751842e34832815c6de6abcc510b) models

Query parameters

▸ `rank` int - Filters orders by the exact rank specified. To retrieve all orders for “Arcane Energize” with a rank of 4, include `rank=4` in the query. This parameter is ignored if the `rankLt` parameter is provided.Accepts value between 0 and Max possible rank of an [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `rankLt` int - Filters orders with a rank less than the specified value.
To retrieve all orders for “Arcane Energize” with a rank less than the maximum possible value of 5, include `rankLt=5` in the query. If both `rank` and `rankLt` are provided, `rankLt` takes precedence.Accepts value between 1 and Max possible rank of an [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `charges` int - Filters orders by the exact number of charges left.
To retrieve all orders for “Lohk” with exactly 2 charges left, include `charges=2` in the query. This parameter is ignored if the `chargesLt` parameter is provided.Accepts value between 0 and maximum possible charges for the [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `chargesLt` int - Filters orders where the number of charges left is less than the specified value. To retrieve all orders for “Lohk” with a charges less than the maximum possible value of 3, include `chargesLt=3` in the query. If both `charges` and `chargesLt` are provided, `chargesLt` takes precedence. Accepts value between 1 and maximum possible charges for the [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `amberStars` int - Filters orders by the exact number of amber stars.
To retrieve all orders for “Ayatan Anasa Sculpture” with exactly 1 amber star, include `amberStars=1` in the query. This parameter is ignored if the `amberStarsLt` parameter is provided.Accepts value between 0 and maximum possible amount of amber stars for the [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `amberStarsLt` int - Filters orders where the number of amber stars is less than the specified value. To retrieve all orders for “Ayatan Anasa Sculpture” with an amber stars less than the maximum possible value of 2, include `amberStarsLt=2` in the query. If both `amberStars` and `amberStarsLt` are provided, `amberStarsLt` takes precedence. Accepts value between 1 and maximum possible amount of amber stars for the [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `cyanStars` int - Filters orders by the exact number of cyan stars.
To retrieve all orders for “Ayatan Anasa Sculpture” with exactly 1 cyan star, include `cyanStars=1` in the query. This parameter is ignored if the `cyanStarsLt` parameter is provided.Accepts value between 0 and maximum possible amount of cyan stars for the [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `cyanStarsLt` int - Filters orders where the number of cyan stars is less than the specified value. To retrieve all orders for “Ayatan Anasa Sculpture” with an cyan stars less than the maximum possible value of 2, include `cyanStarsLt=2` in the query. If both `cyanStars` and `cyanStarsLt` are provided, `cyanStarsLt` takes precedence. Accepts value between 1 and maximum possible amount of cyan stars for the [Item](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#209845f8a3f24b6cad8597b667dca3dc).

▸ `subtype` string - controls the filtering of orders based on item `subtype` field.
To retrieve all orders for crafted “Ambassador Receiver”, include `subtype=crafted` in the query. Accepts any valid subtype form an [Item](https://www.notion.so/Data-Models-65e9ab01868c4dcca6ba499e68a04ac9?pvs=21).

Response:
`{ apiVersion:"x.x.x",data:{ buy:[OrderWithUser,OrderWithUser,...],sell:[OrderWithUser,OrderWithUser,...] },error:null }`

Data model inside: [OrderWithUser](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#1955a46ed3914f859cbe405f6d6c0c32)

ALT

#### GET /v2/orders/user/{slug}

GET `/v2/orders/userId/{userId}`

Getting public orders from specified user.

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `userId` - `id` field form [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#817aa69c97944ad1be60a07d7d169a4e) or [UserShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#c61f4bb38c2e4b7abfcf4cfd3e7bdc35) models
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - `slug` field form [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#817aa69c97944ad1be60a07d7d169a4e) or [UserShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#c61f4bb38c2e4b7abfcf4cfd3e7bdc35) models

Response:
`{ apiVersion:"x.x.x",data:[Order,Order,Order,...],error:null }`

Data model inside: [Order](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#960ee990dfc64d9981a3b5cad3995bf0)

ALT

#### GET /v2/orders/my

This endpoint retrieves all orders associated with the currently authenticated user.

URL parameters:
None

Response:
`{ apiVersion:"x.x.x",data:[Order,Order,Order,...],error:null }`

Data model inside: [Order](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#960ee990dfc64d9981a3b5cad3995bf0)

ALT

#### GET /v2/order/{id}

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `id` - id of an Order

Response:
`{ apiVersion:"x.x.x",data:OrderWithUser,error:null }`

Data model inside: [OrderWithUser](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#1955a46ed3914f859cbe405f6d6c0c32)

ALT

#### POST /v2/order

Create a new order

Request body
`{ "itemId":"54aae292e7798909064f1575","type":"sell","platinum":38,"quantity":12,"visible":true," perTrade ":6," rank ":5," charges ":3," subtype ":"blueprint"," amberStars ":3," cyanStars ":3,}`

Request Fields
`itemId` string - The ID of an item. You can obtain it from [here](/5d987e4aa2f74b55a80db1a09932459d?pvs=25#06f1dcc49ffe4b1bbb50e39ad7ea30cf)
`type` ” sell ” | “ buy ” - The type of order
`platinum` int - The price of the item
`quantity` int - Your stock, representing how many you have and can sell or buy
`visible` bool - Determines if the order should be visible or hidden
`perTrade` int - The minimum number of items required per transaction or trade
`rank` int - The rank of the item, such as a mod rank
`charges` int - The number of charges remaining (e.g., for parazon mods)
`subtype` string - The item's subtype. Refer to the Item model for the possible subtypes an item may have (if applicable)
`amberStars` int - The number of installed amber stars
`cyanStars` int - The number of installed cyan stars

Response:
`{ apiVersion:"x.x.x",data:Order,error:null }`

Data model inside: [Order](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#960ee990dfc64d9981a3b5cad3995bf0)

ALT

#### PATCH /v2/order/{id}

Patch already existing order.

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `Id` - id field form Order model

Request body
`{ " platinum ":10," quantity ":12," perTrade ":3," rank ":1," charges ":2," amberStars ":2," cyanStars ":2," subtype ":"blueprint"," visible ":false }`

Request Fields
`platinum` int - The price of the item
`quantity` int - Your stock, representing how many you have and can sell or buy
`visible` bool - Determines if the order should be visible or hidden
`perTrade` int - The minimum number of items required per transaction or trade
`rank` int - The rank of the item, such as a mod rank
`charges` int - The number of charges remaining (e.g., for parazon mods)
`subtype` string - The item's subtype. Refer to the Item model for the possible subtypes an item may have (if applicable)
`amberStars` int - The number of installed amber stars
`cyanStars` int - The number of installed cyan stars

Response
`{ apiVersion:"x.x.x",data: Order,error:null }`

Data model inside: [Order](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#960ee990dfc64d9981a3b5cad3995bf0)

ALT

#### DELETE /v2/order/{id}

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `Id` - id field form Order model

Response
`{ apiVersion:"x.x.x",data:Order,error:null }`

Data model inside: [Order](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#960ee990dfc64d9981a3b5cad3995bf0)

ALT

#### POST /v2/order/{id}/close

Close a portion or all of an existing order.
Allows you to close part of an open order by specifying a quantity to reduce.
For example, if your order was initially created with a quantity of 20, and you send a request to close 8 units, the remaining quantity will be 12.
If you close the entire remaining quantity, the order will be considered fully closed and removed.

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `Id` - id field form Order model

Request body
`{ "quantity":12,}`

Request Fields
`quantity` int - The number of units to close (subtract from the order's current quantity).

Response:
`{ apiVersion:"x.x.x",data:Transaction,error:null }`

Data model inside is: [Transaction](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#20d515beb0be8067af61faea492bc411), will not include User model in this case.

ALT

#### PATCH /v2/orders/group/{id}

Update group of orders

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `Id` - Group Id, for now only `all` and `ungrouped` are available

Request body
`{ "visible":false,"type":"sell",}`

Request Fields
`visible` bool - visibility state of all orders withing a group
`type` ”sell” | “buy” - target only specific type of orders within a group

Response:
`{ apiVersion:"x.x.x",data:{ updated:13,} error:null }`

Response Fields
`updated` int - How many orders were updated

### Groups

Endpoints to manage order and contract groups.

Currently, only two virtual groups are available for use with any endpoint that requires a `groupId`:
`all` - includes all orders \ contracts, whether grouped or ungrouped.
`ungrouped` - includes only orders \ contracts that are not assigned to any group.

Groups management endpoints will be published later (create, update, delete, etc)

### Users

#### GET /v2/me

Getting information about current authenticated user.

Response
`{ apiVersion:"x.x.x",data:UserPrivate,error:null }`

Data model inside is clickable: [UserPrivate](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#0011943f127c4888a9da7f7ef9f9ddfc)

ALT

#### PATCH /v2/me

Updating your own user record

Request body
`{ "about":"something","platform":"mobile","crossplay":true,"locale":"pt","theme":"light","syncLocale":true,"syncTheme":true,}`

Request Fields
`about` string - profile description
`platform` one of [platforms](/5d987e4aa2f74b55a80db1a09932459d?pvs=25#702bd4e83c4c42e89c4e9ce740c2f248) - main platform you are playing on
`crossplay` bool - is crossplay enabled for your warframe account
`locale` one of [languages](/5d987e4aa2f74b55a80db1a09932459d?pvs=25#a3aad4b7061f4dc7a7d7b33482a9782a) - UI locale and preferable communication language
`theme` ”light” | “dark” | “system” - UI theme
`syncLocale` bool - should we sync locale across devices
`syncTheme` bool - should we sync theme across devices

Response
`{ apiVersion:"x.x.x",data:UserPrivate,error:null }`

Data model inside is clickable: [UserPrivate](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#0011943f127c4888a9da7f7ef9f9ddfc)

ALT

#### POST /v2/me/avatar

Update your avatar. The uploaded image will be resized to 256×256 pixels, focusing on the center of the image.

Request
Content-Type: `multipart/form-data`
`form - data; name = "avatar"; filename = "whatever.png"`

Request Fields
`avatar` file - Image file to upload as the new avatar.

Constraints
Accepts image formats: `.png,.jpg,.jpeg,.webp,.gif,.bmp,.avif`
Maximum upload size is 5mb

Response
`{ apiVersion:"x.x.x",data:UserPrivate,error:null }`

Data model inside is clickable: [UserPrivate](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#0011943f127c4888a9da7f7ef9f9ddfc)

ALT

#### POST /v2/me/background

![ℹ️ 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) Requires user to have at least a silver subscription tier

Update your profile background. The uploaded image will be resized to 1920×820 pixels, focusing on the center of the image.

Request
Content-Type: `multipart/form-data`
`form - data; name = "background"; filename = "whatever.png"`

Request Fields
`background` file - Image file to upload as the new background.

Constraints
Accepts image formats: `.png,.jpg,.jpeg,.webp,.gif,.bmp,.avif`
Maximum upload size is 8mb

Response
`{ apiVersion:"x.x.x",data:UserPrivate,error:null }`

Data model inside is clickable: [UserPrivate](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#0011943f127c4888a9da7f7ef9f9ddfc)

ALT

#### GET /v2/user/{slug}

GET `/v2/userId/{userId}`

Getting information about particular user

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `userId` - `id` field form [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#817aa69c97944ad1be60a07d7d169a4e) or [UserShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#c61f4bb38c2e4b7abfcf4cfd3e7bdc35) models
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - `slug` field form [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#817aa69c97944ad1be60a07d7d169a4e) or [UserShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#c61f4bb38c2e4b7abfcf4cfd3e7bdc35) models

Response
`{ apiVersion:"x.x.x",data:User,error:null }`

Data model inside: [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#b192f26b800043818ad6a00a3bfcb832)

ALT

### Achievements

#### GET /v2/achievements

Get list of all available achievements, except secret ones.

Response
`{ apiVersion:"x.x.x",data:[Achievement,Achievement,...],error:null }`

Data model inside: [Achievement](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#1fb030d3e4e44d7f97c467195de4a943), without `state`

ALT

#### GET /v2/achievements/user/{slug}

GET `/v2/achievements/userId/{userId}`

Get a list of all user achievements

URL parameters:
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `userId` - `id` field form [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#817aa69c97944ad1be60a07d7d169a4e) or [UserShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#c61f4bb38c2e4b7abfcf4cfd3e7bdc35) models
![🔹](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `slug` - `slug` field form [User](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#817aa69c97944ad1be60a07d7d169a4e) or [UserShort](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#c61f4bb38c2e4b7abfcf4cfd3e7bdc35) models

Query parameters
▸ `featured` bool - Return only `featured: true` achievements.

Response
`{ apiVersion:"x.x.x",data:[Achievement,Achievement,...],error:null }`

Data model inside: [Achievement](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#1fb030d3e4e44d7f97c467195de4a943), will include `state`

ALT

### Authentication

#### POST /auth/signin

Wfm Frontend
Ios app
Android app

Request body
`{ "email":"whatever@gmail.com","password":"12345","clientId":"wfm-0000","deviceId":"random uniq id","deviceName":"My cool Nokia 3310" }`

Request Fields
`email` string - user email
`password` string - user password
`deviceId` string - Id of device, used to identify this specific device and tie all sessions to it.
`deviceName` string - Name of the device, human readable.

Headers
This should be set:
![🟠](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `X-Firebase-AppCheck` string - AppCheck verification token

Response
`{ "apiVersion":"x.x.x","data":{ "accessToken":"...","refreshToken":"...","tokenType":"Bearer","expiresIn":12345 },"error":null }`

![⚠️ 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) User registration, first party applications only

WFM Frontend
Ios app
Android app

Request body
`{ "email":"whatever@gmail.com","password":"12345","clientId":"wfm-0000","deviceId":"random uniq id","deviceName":"My Nokia 3310" "platform":"pc","locale":"ko" }`

Request Fields
`email` string - user email
`password` string - user password
`deviceId` string - Id of device, could be random generated string, used to identify this specific device and tie all sessions to it.
`deviceName` string - Name of the device, human readable.
`platform` string - platform user are playing on, one of: [Platform](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#51ff3a5923744b419248901539bca5b9)

Headers
This should be set:
![🟠](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `X-Firebase-AppCheck` string - AppCheck verification token

Response
`{ "apiVersion":"x.x.x","data":{ "accessToken":"...","refreshToken":"...","tokenType":"Bearer","expiresIn":12345 },"error":null }`

#### POST /auth/refresh

Refresh all session tokens

Request body
`{ "grantType":"refresh_token","clientId":"wfm-0000","deviceId":"BASD001-KSADFDG" "refreshToken":"JwtRefreshToken" }`

Request Fields
`grantType` string - should be `refresh_token`
`deviceId` string - Id of device, used to identify this specific device and tie all sessions to it.
`refreshToken` string - usually almost expired refresh token

Headers
![🟠](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `X-Firebase-AppCheck` string - AppCheck verification token

Response
`{ "apiVersion":"x.x.x","data":{ "accessToken":"...","refreshToken":"...","tokenType":"Bearer","expiresIn":12345 },"error":null }`

#### POST /auth/signout

Terminate current session. Refresh and access tokens will become unusable.

Request body
`{ }`

Headers
![🟠](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) `Authorization` string - JWT access token in format: `Bearer YourJWTAccessToken`

Example
Response
empty (no body), status code: `200`

### Dashboard

#### GET /v2/dashboard/showcase

Mobile app main screen dashboard with featured items.

Response:
`{ apiVersion:"x.x.x",data:{ DashboardShowcase },error:null }`

Data model inside is clickable: [DashboardShowcase](/65e9ab01868c4dcca6ba499e68a04ac9?pvs=25#14c515beb0be809e9843d098dc53d476)

ALT

### OAuth

`/oauth/authorize` - authorize request by 3rd party account
`/oauth/token` - exchange code for access token, with PKCE
`/oauth/revoke` - revoke access token

x1.00 > < >> << O
