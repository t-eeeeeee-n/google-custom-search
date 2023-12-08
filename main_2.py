import requests
from bs4 import BeautifulSoup
import datetime


def googleRankSearch(keywords):
    d_today = datetime.date.today()
    t_now = datetime.datetime.now().time()
    now_time = str(t_now).split('.')

    # 40位までcheck
    url = f"https://www.google.com/search?q={keywords}"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"User-Agent": user_agent,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    # Google検索を実施
    source = requests.get(url, headers=headers).text

    # Google検索の結果からタイトルとURLを抽出
    soup = BeautifulSoup(source, 'html.parser')
    # search_div = soup.find_all(class_='rc')
    search_div = soup.find_all(class_='yuRUbf')
    # search_div = soup.find_all(class_='fl')

    i = 1
    # 抽出したタイトルとURLを表示
    for result in search_div:  # loop result list
        title = result.h3.string
        page_url = result.a.get('href')
        if 'xxx.yyy.zzz' in page_url:
            return [d_today, now_time[0], keywords, i, title, page_url]
        else:
            i = i + 1
    return [d_today, now_time[0], keywords, 0, 'na', 'na']


if __name__ == '__main__':
    target_keyword = '製造+求人'

    response = googleRankSearch(target_keyword)

    print(response)
