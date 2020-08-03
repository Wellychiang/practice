import requests
from lxml import etree
from pprint import pprint
import json
import re
from selenium import webdriver
from time import sleep


def crawl(urls):
    for res in (requests.get(url) for url in urls):  # 產生器形式
        yield len(res.content), res.status_code, res.url


def req_nba():
    url = 'https://nlnbamdnyc-a.akamaihd.net/fs/nba/feeds_s2019/schedule/2020/7_27.js'
    headers = {
        'Referer': 'https://watch.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    data = {'t': '1596362940000'}
    qw = requests.get(url, headers=headers, params=data)
    a = re.findall('g_schedule=(.*)', qw.text)

    count = -1
    for i in range(6):
        count += 1
        one = {k: v for k, v in json.loads(a[0])['games'][6][count].items()}
        print(one['h'] + ' vs ' + one['v'], one['hr'], count)


#  Chromedriver在下載資料夾, 還沒加入環境變數
def selenium_nba():
    b = webdriver.Chrome('/Users/g45p2k7a8/Downloads/chromedriver')
    b.implicitly_wait(3)
    b.get('https://watch.nba.com/')
    accept = b.find_element_by_xpath("//*[contains(text(),'I Accept') and @id='onetrust-accept-btn-handler']")
    accept.click()
    # b.get('https://watch.nba.com/')
    # sleep(5)
    # game = b.find_element_by_xpath("//*[contains(span,'比賽')]")
    # game.click()
    page = b.page_source
    with open('source.txt', 'a') as file:
        print(page, file=file)


selenium_nba()


