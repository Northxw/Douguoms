# -*- coding:utf-8 -*-

recipe_api = "http://api.douguo.net/recipe/flatcatalogs"
specific_recipe_api = "http://api.douguo.net/recipe/v2/search/{offset}/20"
detail_api = 'http://api.douguo.net/recipe/detail/{id}'

# MONGO SETTINGS
# HOST = '192.168.209.128'
HOST = 'localhost'
PORT = 27017

# HEADERS
HEADERS = {
    "client": "4",
    "version": "6939.2",
    "device": "MI 6",               # device name
    "sdk": "22,5.1.1",
    "imei": "863254011428397",      # 15 international mobile device identification code
    "channel": "baidu",
    "resolution": "1280*720",
    "dpi": "1.5",
    "brand": "Xiaomi",              # device brand
    "scale": "1.5",
    "timezone": "28800",
    "language": "zh",
    "cns": "3",
    "carrier": "CHINA+MOBILE",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",
    "act-code": "781df26f03d497921beb4d314dff6dc3",
    "reach": "10000",
    "newbie": "0",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Keep-Alive",
    "Host": "api.douguo.net",
}

# Recipe classification interface parameters
data_recipe = {
        "client": "4",
        # "_session": "1557216373865355757011001597",
        "v": "",        # timestamp
        "_vs": "2305"
}

# All the recipes under one recipe
data_one_recipe = {
        "client": "4",
        # "_session": "1557233643772355757011001597",
        "keyword": "",
        "order": "3",
        "_vs": "400"
}

data_detail_recipe = {
    "client": "4",
    # "_session": "1557245894286355757011001597",
    "author_id": "0",
    "_vs": "2801",
    "_ext": '{"query":{"kw":"豆腐","src":"2801","idx":"1","type":"13","id":"1064542"}}'
}

MAX_PAGES = 10