import requests as rq
from bs4 import BeautifulSoup as bs
from myRegex import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}


def get_response(url):
    try:
        response = rq.request(method='get', url=url, headers=headers)
        response.encoding = response.apparent_encoding
        if response is not None:
            return bs(response.content, 'lxml')
        return
        response
    except:
        print(f'this {url} is dead')
        return None


def get_info(page):
    content = str(page)

    org = get_org(content)
    tel_list = get_tel(content)
    tel_list = [tel.replace(u'\xa0', u'') for tel in tel_list]
    return org, tel_list


def get_url(page, url):
    regex = r'(?<=://)[a-zA-z\.0-9]+(?=\/)'
    baseurl = re.findall(regex, url, re.U)
    if baseurl is None:
        return []
    try:
        tags = page.select("a")
        res = set()
        for tag in tags:
            if tag.get('href') is not None:
                context = str(tag['href'])
                if context.__contains__('xmu.edu.cn'):
                    res.add(tag['href'])
        return res
    except:
        print(f'get_url: {url} failed')
        return None
