from myBloom import *
from Reptile import *
import pandas as pd

query_url = []#视作一个队列，存储搜索到的网站
init_url = 'https://xmu.edu.cn/'#一切罪恶的开始
query_url.append(init_url)
url_filter = init_bloom(size=2e8)#初始化布隆过滤器
tel_dict = {}#存储已经找到了的信息，防止重复存储

if __name__ == '__main__':
    try:
        cnt = 0     #计数
        print("link start!")
        while len(query_url):
            url = query_url.pop(0)
            page = get_response(url)    #返回一个soup
            if page is not None:
                url_list = get_url(page, url)
                org, tel_list = get_info(page)
            else:
                url_list = []
                org, tel_list = None, []

            if len(tel_list) > 0 and org is not None:
                if org in tel_dict.keys():
                    tel_dict[org] = tel_dict[org] | set(tel_list)
                else:
                    tel_dict[org] = set(tel_list)
                print(org, tel_list)

            for url in url_list:
                if url not in url_filter:
                    cnt = cnt + 1
                    url_filter.add(url)
                    query_url.append(url)

            if cnt > 500:   #当访问了500个网站时，直接退出，可以修改成更大的数
                print("overflow!")
                break

    except IndexError as e:
        print(e)
    finally:
        tel_dict.update((key, str(val)) for key, val in tel_dict.items())
        df = pd.DataFrame(list(tel_dict.items()))
        df.to_csv('dataset.csv', encoding='utf8')
        print(df)





