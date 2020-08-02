import requests
from lxml import etree
from pprint import pprint
import json
import re


def crawl(urls):
    for res in (requests.get(url) for url in urls):  # 產生器形式
        yield len(res.content), res.status_code, res.url


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
