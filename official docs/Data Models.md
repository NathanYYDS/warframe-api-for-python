
![](/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F1be91aea-8129-4c98-a207-838c3fdf495b%2F867763f4-b414-4259-86ad-ecbaf7f09657%2Ffriego.webp?table=block&id=65e9ab01-868c-4dcc-a6ba-499e68a04ac9&spaceId=1be91aea-8129-4c98-a207-838c3fdf495b&width=2000&userId=&cache=v2) ![💽 页面图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) ![💽 页面图标](https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f4bd.svg)

# Data Models

**Owner**

![KycKyc](https://lh3.googleusercontent.com/a/ACg8ocL9GeRrMKjNPtAPDEfL5hxH_HMZtHbx6kXV5ts6M7tJP1s=s100)

KycKyc

**Verification**

已验证

**Tags**

documentation

api

**Last edited time**

2025年11月13日 17:18

## Description

All structs are Golang structs with JSON tags (see [How to Use Struct Tags in Go](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)). If you are familiar with them and their quirks, you will likely be able to deduce the data types and identify which fields could be optional. However, just to be sure and to facilitate easier reading, I’ll highlight these fields with a color.

Field is optional

Also, here is our advanced marking system for these models:

![🔜](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - In development 
![🚧](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==) - Unstable or unfinished models

## Models

### ItemShort

Represent trimmed Item model, only used to build initial local copy of tradable items list on a client.

**Golang Struct**

**JSON Example**

```json
{ id:"54aae292e7798909064f1575",slug:"secura-dual-cestra",gameRef:"/Lotus/Weapons/Syndicates/PerrinSequence/Pistols/PSDualCestra",tags:["syndicate","weapon","secondary"],i18n:{ en:{ name:"Secura Dual Cestra",icon:"items/images/en/secura_dual_cestra.3d47a4ec6675ff774bb0da9b16c53e0e.png",thumb:"items/images/en/thumbs/secura_dual_cestra.3d47a4ec6675ff774bb0da9b16c53e0e.128x128.png",subIcon:"sub_icons/weapon/generic_receiver_128x128.png" },maxRank:8,maxCharges:3,vaulted:false,ducats:45,amberStars:8 cyanStars:2,baseEndo:100,endoMultipler:2.0,subtypes:["blueprint","crafted"] }
```

This is an example where all fields may have arbitrary values.

ALT

### Item

Full item model with all possible fields

**Golang Struct**

**JSON Example**

```json
{ id:"54e644ffe779897594fa68d2", tags:["mod","rare","warframe","trinity"], slug:"abating_link", gameRef:"/Lotus/Powersuits/Trinity/LinkAugmentCard", tradable:true,setRoot:false,setParts:["54a73e65e779893a797fff72","54a73e65e779893a797fff73","54a73e65e779893a797fff71","56783f24cbfa8f0432dd89a6","54a73e65e779893a797fff76"],quantityInSet:1, i18n:{ en:{ name:"Abating Link",description:"Link Augment: Reduces Armor Rating by 60% on enemies targeted by Link.",wikiLink:"https://warframe.fandom.com/wiki/Abating_Link", icon:"items/images/en/abating_link.c547fa09315093a5ba6c609a9b195580.png",thumb:"items/images/en/thumbs/abating_link.c547fa09315093a5ba6c609a9b195580.128x128.png",subIcon:"sub_icons/blueprint_128x128.png" } },rarity:"rare",maxRank:9,maxCharges:3,bulkTradable:true,subtypes:["blueprint","crafted"],maxAmberStars:5,maxCyanStars:10,baseEndo:400,endoMultiplier:3,ducats:75,reqMasteryRank:10,vaulted:true,tradingTax:8000,}
```

This is an example where all fields may have arbitrary values.

ALT

### Riven item

Full riven weapon model with all possible fields

**Golang Struct**

`rivenType` could be `kitgun` | `melee` | `pistol` | `rifle` | `shotgun` | `zaw`, but a new one may be added at any time.

`group` used to break riven by groups on the frontend, used for rendering only

**JSON Example**

```json
{ id:"5c5ca81696e8d2003834fdcc",slug:"kulstar",gameRef:"/Lotus/Weapons/Grineer/Pistols/GrnTorpedoPistol/GrnTorpedoPistol",group:"secondary",rivenType:"pistol",disposition:1.3,reqMasteryRank:5,i18n:{ en:{ name:"Kulstar",wikiLink:"https://warframe.fandom.com/wiki/Kulstar",icon:"items/images/en/kulstar.92736ca911a3b84f99bc9e50f24369f0.png",thumb:"items/images/en/thumbs/kulstar.92736ca911a3b84f99bc9e50f24369f0.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Riven attribute

Full riven attribute model with all possible fields

**Golang Struct**

**JSON Example**

```json
{ id:"5c5ca81a96e8d2003834fe7f",slug:"recoil",gameRef:"WeaponRecoilReductionMod",group:"default",prefix:"Zeti",suffix:"Mag",exclusiveTo:["shotgun","rifle","pistol","kitgun"],positiveIsNegative:true,positiveOnly:true,negativeOnly:false,unit:"percent",i18n:{ en:{ name:"Weapon Recoil",icon:"riven_attribute/unknown.png",thumb:"riven_attribute/unknown.thumb.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Lich weapon

**Golang Struct**

**JSON Example**

```json
{ id:"5e9855993d9f64005cd702e6",slug:"kuva_drakgoon",gameRef:"/Lotus/Weapons/Grineer/KuvaLich/LongGuns/Drakgoon/KuvaDrakgoon",reqMasteryRank:13,i18n:{ en:{ name:"Kuva Drakgoon",wikiLink:"https://warframe.fandom.com/wiki/Kuva_Drakgoon",icon:"lich_weapons/images/kuva_drakgoon.1c7452cc19e0d37f8403777906f06f7a.png",thumb:"lich_weapons/images/thumbs/kuva_drakgoon.1c7452cc19e0d37f8403777906f06f7a.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Lich ephemera

**Golang Struct**

**JSON Example**

```json
{ id:"5e98548a3d9f64004f9136bb",slug:"vengeful_charge",gameRef:"/Lotus/Upgrades/Skins/Effects/Kuva/KuvaLightningEphemera",animation:"lich_ephemeras/animations/vengeful_charge.9682a7978dd10f8c63fa160d5ba1660e.webp",element:"electricity",i18n:{ en:{ name:"Vengeful Charge Ephemera",icon:"lich_ephemeras/images/vengeful_charge.68e07295ec11cdb303755a9f26e87f0e.png",thumb:"lich_ephemeras/images/thumbs/vengeful_charge.68e07295ec11cdb303755a9f26e87f0e.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Lich quirk

**Golang Struct**

**JSON Example**

```json
{ id:"5e9855a43d9f6400697e895c",slug:"poor_sense_of_balance",group:"default",i18n:{ en:{ name:"Poor Sense of Balance",description:"The lich will retreat after kneeling down and without stabbing",} } }
```

This is an example where all fields may have arbitrary values.

ALT

### Sister weapon

**Golang Struct**

**JSON Example**

```json
{ id:"60f3feb1b64404003f0bf602",slug:"tenet_tetra",gameRef:"/Lotus/Weapons/Corpus/BoardExec/Primary/CrpBETetra/CrpBETetra",reqMasteryRank:16,i18n:{ en:{ name:"Tenet Tetra",wikiLink:"https://warframe.fandom.com/wiki/Tenet_Tetra",icon:"sister_weapons/images/tenet_tetra.574603420c8673450692e0316abbb8cc.png",thumb:"sister_weapons/images/thumbs/tenet_tetra.574603420c8673450692e0316abbb8cc.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Sister ephemera

**Golang Struct**

**JSON Example**

```json
{ id:"60f3feb5b64404003f0bf61d",slug:"gloriana_ephemera",gameRef:"/Lotus/Upgrades/Skins/Effects/CorpusLichEphemeraC",animation:"sister_ephemeras/animations/gloriana_ephemera.61f00273d398b5ecacf93004bdacf5a8.webp",element:"cold",i18n:{ en:{ name:"Gloriana Ephemera",icon:"sister_ephemeras/images/gloriana_ephemera.0ed0559f0a1f4bd07ccef755fb71152d.png",thumb:"sister_ephemeras/images/thumbs/gloriana_ephemera.0ed0559f0a1f4bd07ccef755fb71152d.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Sister quirk

**Golang Struct**

**JSON Example**

```json
{ id:"60f3feb2b64404003f0bf60a",slug:"coward",group:"default",i18n:{ en:{ name:"Coward",description:"Can leave the mission at low health" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Npc

**Golang Struct**

**JSON Example**

```json
{ id:"62d2eff3751567007abb167e",slug:"infested_grineer",gameRef:"",i18n:{ en:{ name:"Infested Grineer",icon:"npc/images/infested_grineer.52931b27d55248a226c0f793e0863be0.png",thumb:"npc/images/thumbs/infested_grineer.52931b27d55248a226c0f793e0863be0.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Location

**Golang Struct**

**JSON Example**

```json
{ id:"62d2eb5075156700663c83b4",slug:"amarna",gameRef:"ClanNode14",faction:"infested",minLevel:35,maxLevel:45,i18n:{ en:{ nodeName:"Amarna",systemName:"Sedna",icon:"locations/images/sedna.8c77b332a2c4e0d07a03c66cc2b1290e.png",thumb:"locations/images/thumbs/sedna.8c77b332a2c4e0d07a03c66cc2b1290e.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Mission

**Golang Struct**

**JSON Example**

```json
{ id:"62d2f049751567007abb1956",slug:"level_50_70_orb_vallis_bounty",gameRef:"",i18n:{ en:{ name:"Level 50 - 70 Orb Vallis Bounty",icon:"missions/images/level_50_70_orb_vallis_bounty.3401f96abd2236fdb1a6f745b12d597d.png",thumb:"missions/images/thumbs/level_50_70_orb_vallis_bounty.3401f96abd2236fdb1a6f745b12d597d.128x128.png" } } }
```

This is an example where all fields may have arbitrary values.

ALT

### Order

Just an order, that’s it. Without specifying the owner, used in cases where you already know who the owner of the order is, such as in a user profile or your own profile.

**Golang Struct**

**JSON Example**

```json
{ id:"5845a519d3ffb6213325ce33",type:"sell",platinum:109,quantity:1,perTrade:5,rank:10,charges:3,subtype:"crafted",amberStars:5,cyanStars:10,visible:true,createdAt:"2016-12-05T17:34:17Z",updatedAt:"2021-05-21T14:59:02Z",itemId:"56783f24cbfa8f0432dd89a6",group:"all",}
```

This is an example where all fields may have arbitrary values.

ALT

`group` string - default group is always named `all`, all orders without custom group will be put into `all`.

### OrderWithUser

This is a typical order model found in most requests, including a record about an owner.

**Golang Struct**

**JSON Example**

```json
{ id:"5845a519d3ffb6213325ce33",type:"sell",platinum:109,quantity:1,perTrade:5,rank:10,charges:1,subtype:"crafted",amberStars:5,cyanStars:10,vosfor:400,visible:true,createdAt:"2016-12-05T17:34:17Z",updatedAt:"2021-05-21T14:59:02Z",itemId:"56783f24cbfa8f0432dd89a6",user:{ id:"57426ce3d3ffb6355730cd09",ingameName:"KycKyc",avatar:"user/avatar/57c51a3ed3ffb672f34ae3e7.png?22448db7f423a89945968e0ab2563e3c",reputation:0,locale:"en",platform:"pc",crossplay:true,status:"in_game",activity:{ type:"on_mission",details:"The Circuit 55-75",startedAt:"2024-01-17T22:18:19Z" },lastSeen:"2024-01-17T22:18:19Z" } }
```

This is an example where all fields may have arbitrary values.

ALT

### Transaction

Represents an order that has been fully or partially closed.

**Golang Struct**

**JSON Example**

```json
{ id:"6849ae6370683e67b9103703", type:"sell",originId:"6848be91a3948400153846ed", platinum:33, quantity:6, createdAt:"2025-06-11T14:12:17Z", updatedAt:"2025-06-11T16:27:15Z",item:{ id:"653833d6123a401b2563081d",rank:5,charges:6,subtype:"crafter",cyanStars:5,amberStars:7,},user:{ id:"57426ce3d3ffb6355730cd09",ingameName:"KycKyc",avatar:"user/avatar/57c51a3ed3ffb672f34ae3e7.png?22448db7f423a89945968e0ab2563e3c",reputation:0,locale:"en",platform:"pc",crossplay:true,status:"in_game",activity:{ type:"on_mission",details:"The Circuit 55-75",startedAt:"2024-01-17T22:18:19Z" },lastSeen:"2024-01-17T22:18:19Z" } }
```

Depends on endpoint, may have or not have `User` struct inside.

### UserShort

This is a shortened model of a user, which can be found in chats, messages, orders, bids, auctions, etc.

**Golang Struct**

**JSON Example**

```json
{ id:"57426ce3d3ffb6355730cd09",ingameName:"KycKyc",avatar:"user/avatar/57c51a3ed3ffb672f34ae3e7.png?22448db7f423a89945968e0ab2563e3c",reputation:0,locale:"en",platform:"pc",crossplay:true,status:"in_game",activity:{ type:"on_mission",details:"The Circuit 55-75",startedAt:"2024-01-17T22:18:19Z" },lastSeen:"2024-01-17T22:18:19Z" }
```

This is an example where all fields may have arbitrary values.

ALT

### User

Public user profile

**Golang Struct**

**JSON Example**

```json
{ id:"57426ce3d3ffb6355730cd09",ingameName:"KycKyc",slug:"kyckyc",avatar:"user/avatar/57c51a3ed3ffb672f34ae3e7.png?22448db7f423a89945968e0ab2563e3c",background:"user/background/54e0cdf8e77989024a1e34b2.png?14d961de874a4d8f10137e80403244be",about:"<p><code>warframe.market</code> developer</p>",reputation:0,masteryLevel:20,platform:"pc",crossplay:true,locale:"en",achievementShowcase:[{ id:"57426ce3d3ffb6355730cd09",icon:"user/badges/04.png",thumb:"user/badges/04.thumb.png",type:"patreon",i18n:{ en:{ name:"Platinum Patron",description:"Thanks to this contributor, we can keep warframe.market alive!" } } },{ id:"97426ce2d3ffb6335730cd09",icon:"user/badges/best_waifu.png",thumb:"user/badges/best_waifu.thumb.png",type:"custom",i18n:{ en:{ name:"Best waifu",description:"Hats off to you, Ultimate Waifu! You've officially stepped into the legendary league of the iconic hat aficionado. With loyalty that outshines even the most heroic of sidekicks and bravery that would make any adventurer jealous, you're the server's newfound star. Donning this epic headgear, you're not just a player, you're a walking, talking legend with a flair for dramatic narration. Congratulations on becoming the most charismatic, hat-toting hero in the game!" } } }],status:"in_game",activity:{ type:"on_mission",details:"The Circuit 55-75",startedAt:"2024-01-17T22:18:19Z" },lastSeen:"2024-01-17T22:18:19Z",banned:true,banUntil:"2074-01-17T00:00:00Z",warned:true,warnMessage:"You're a bad person",banMessage:"Breaking TOS" }
```

This is an example where all fields may have arbitrary values.

ALT

### UserPrivate

User profile, only available to the user itself.

**Golang Struct**

**JSON Example**

SOON

This is an example where all fields may have arbitrary values.

ALT

### Activity

**Golang Struct**

**JSON Example**

```json
{ type:"on_mission",details:"The Circuit 55-75",startedAt:"2024-01-17T22:18:19Z" }
```

This is an example where all fields may have arbitrary values.

ALT

Where:

`ActivityType` string could be “on_mission" | "dojo" | “unknown” | "" (for now)

### Achievement

**Golang Struct**

**JSON Example**

```json
{ id:"6324ae79cfca4d00514e0cf7",slug:"github_contribution",type:"github",goal:5,i18n:{ en:{ name:"Contributor",description:"This badge approves the contribution towards warframe.market development.",icon:"user/badges/github_contribution.616d111a24024d0b4af37df0c26c387b.webp",thumb:"user/badges/thumbs/github_contribution.616d111a24024d0b4af37df0c26c387b.128x128.webp" } },state:{ featured:true,progress:5,completedAt:"2025-06-22T20:00:01Z" } }
```

This is an example where all fields may have arbitrary values.

ALT

### DashboardShowcase

Mobile app main screen dashboard with featured items.

**Golang Struct**

**JSON Example**

```json
{ i18n:{ en:{ title:"Xaku Prime Access",description:"Xaku Prime, Quassus Prime and Trumna Prime are here!" } },items:[{ item:"673516a9db3ac2cfade14a70",background:"showcase/xakuPrime.webp",bigCard:true },{ item:"673516dddb3ac2cfade14a7c",background:"showcase/xakuPrimeSecondary.webp",bigCard:false },{ item:"673516c5db3ac2cfade14a76",background:"showcase/xakuPrimeSecondary.webp",bigCard:false }] }
```

This is an example where all fields may have arbitrary values.

ALT

### Status

Online status of user.

`invisible`, `offline`, `online`, `ingame`

### Activity type

`UNKNOWN`, `IDLE`, `ON_MISSION`, `IN_DOJO`, `IN_ORBITER`, `IN_RELAY`

### Role

Role on the site

`user`, `moderator`, `admin`

### Tier

Subscription tier, form Patreon \ Afdian \ Nitropay

`none`, `bronze`, `silver`, `gold`, `diamond`

### Language

One of the languages supported by the backend. Like, Frontend can have more languages, but they are only used to translate the user interface.

`ko`, `ru`, `de`, `fr`, `pt`, `zh-hans`, `zh-hant`, `es`, `it`, `pl`, `uk`, `en`

### Platform

Supported platforms

`pc`, `ps4`, `xbox`, `switch`, `mobile`

### Scope

Access scopes

`me`, `profile`, `settings`, `contracts`, `ledger`, `reviews`
