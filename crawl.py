import requests


def crawl(urls):
    for res in (requests.get(url) for url in urls):
        yield len(res.content), res.status_code, res.urlgit


urlss = ['https://ithelp.ithome.com.tw/articles/10213503', 'https://ithelp.ithome.com.tw/articles/10213503',
         'https://ithelp.ithome.com.tw/tags/articles/11th%E9%90%B5%E4%BA%BA%E8%B3%BD']

with open('text.txt', 'a') as file:
    for content, status, url in crawl(urlss):
        print(content, '->', status, '->', url, file=file)
