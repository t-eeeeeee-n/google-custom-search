#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json

from time import sleep
from googleapiclient.discovery import build

# TODO
GOOGLE_API_KEY = ""
CUSTOM_SEARCH_ENGINE_ID = ""

DATA_DIR = 'data'


def makeDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def getSearchResponse(keyword):
    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    makeDir(DATA_DIR)

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    page_limit = 3
    start_index = 1
    response = []
    for n_page in range(0, page_limit):
        try:
            sleep(1)
            response.append(service.cse().list(
                q=keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                lr='lang_ja',
                num=10,
                start=start_index
            ).execute())
            start_index = response[n_page].get("queries").get("nextPage")[0].get("startIndex")
        except Exception as e:
            print(e)
            break

    data_list = list()
    for item in response[0]["items"]:
        data_list.append({
            'title': item["title"],
            'link': item["link"],
            'displayLink': item["displayLink"],
            'snippet': item["snippet"]
        })
    print(data_list)


if __name__ == '__main__':
    target_keyword = 'ダイエット'

    getSearchResponse(target_keyword)
