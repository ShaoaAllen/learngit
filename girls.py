import requests
from bs4 import BeautifulSoup
import os

def getItems(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select('.postlist li span a')
    itemList = []
    for i in items:
        itemList.append(i.get("href"))
    # print(itemList)
    return itemList


def getPic(url):
    # url = 'https://www.mzitu.com/176302'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    num = int(soup.select(".pagenavi a span")[-2].text)
    os.mkdir(f'G:\\chao\\{url[-6:]}')
    for i in range(num):
        url_i = f'{url}/{i+1}'
        # print(url_i)
        res_i = requests.get(url_i)
        soup_i = BeautifulSoup(res_i.text, 'html.parser')
        url_i = soup_i.select('.main-image a img')[0].get('src')
        # print(url_i)
        headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                'Referer': 'http://www.mzitu.com'}
        response = requests.get(url_i, headers=headers)
        f = open(f'G:\\chao\\{url[-6:]}\\{i}.jpg', 'wb')
        f.write(response.content)
        f.close()
    print(f"{url} download finished")


def getPages(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    num = int(soup.select('.nav-links a')[-2].text)
    pagelist = []
    for n in range(int(num/10)):
        if n == 0:
            pagelist.append(url)
        else:
            pagelist.append(f'{url}/page/{n+1}')
    return pagelist


def run(url):
    pages = getPages(url)
    for page in pages:
        items = getItems(page)
        for i in items:
            getPic(i)
    print('Done!')


if __name__ == "__main__":
    url = 'https://www.mzitu.com/'
    run(url)