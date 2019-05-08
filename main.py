# -*- coding:utf-8 -*-

import json
import time
import requests
import pymongo
from multiprocessing import Queue
from config import *
from common import aproxy
from concurrent.futures import ThreadPoolExecutor

# Create a queue
queue_list = Queue()

# Initialize the database connection
client = pymongo.MongoClient(host=HOST, port=PORT)
db = client['douguoms']
collection = db['cookbook']

def processing_requests(url, data):
    """handle all interface requests"""
    headers = HEADERS
    proxies = aproxy()
    # response = requests.post(url=url, headers=headers, data=data, proxies=proxies)
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code == 200:
        return response


def get_recipes():
    """get all recipe categories"""
    url = recipe_api
    data_recipe.update({"v": int(time.time())})
    response = processing_requests(url=url, data=data_recipe)
    recipes_sort = json.loads(response.text)
    for recipe in recipes_sort['result']['cs']:             # sort recipes
        for middle_ingredient in recipe['cs']:              # food ingredients
            for ingredient in middle_ingredient['cs']:
                data_one_recipe.update({"keyword": ingredient['name']})
                queue_list.put(data_one_recipe)             # production recipes for all subdivisions


def get_specific_recipes(data):
    """get specific recipes for each category"""
    print("当前处理的食材：", data['keyword'])
    for offset in range(0, MAX_PAGES + 1):
        url = specific_recipe_api.format(offset=offset*20)
        specific_recipes_response = processing_requests(url=url, data=data)
        items = json.loads(specific_recipes_response.text)
        for item in items['result']['list']:
            recipe_info = dict()
            recipe_info['recipe'] = data['keyword']
            if item['type'] == 13:
                recipe_info['recipe_name'] = item['r']['n']
                recipe_info['producer'] = item['r']['an']
                recipe_info['recipe_id'] = item['r']['id']
                recipe_info['describe'] = item['r']['cookstory'].strip()
                recipe_info['difficulty_level'] = item['r']['cook_difficulty']
                recipe_info['cook_time'] = item['r']['cook_time']
                recipe_info['recommendation'] = item['r']['recommendation_tag']
                recipe_info['score'] = item['r']['rate']
                recipe_info['major_seasoning'] = item['r']['major']

                detail_url = detail_api.format(id=str(item['r']['id']))
                data_detail_recipe.update({"_ext": '{"query":{"kw":'+ data['keyword'] +',"src":"2801","idx":"1","type":"13","id":'+ str(item['r']['id']) +'}}'})
                detail_response = json.loads(processing_requests(detail_url, data_detail_recipe).text)

                recipe_info['tips'] = detail_response['result']['recipe']['tips']
                recipe_info['cookstep'] = detail_response['result']['recipe']['cookstep']
                # print(json.dumps(recipe_info))
                print("当前入库的菜谱是： %s" % item['r']['n'])
                collection.insert(recipe_info)
            else:
                continue
        if offset % 5 == 0:
            break
        # break
    print('-' * 50)


if __name__ == '__main__':
    get_recipes()
    # Create a thread pool of size 5
    # pool = ThreadPoolExecutor(max_workers=5)
    # while queue_list.qsize() > 0:
    #     pool.submit(get_specific_recipes, queue_list.get())
    get_specific_recipes(queue_list.get())