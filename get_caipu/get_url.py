import re

import pymysql
import requests
from lxml import etree

"""此程序用于拿取需要爬取的所有url，存于MySQL数据库当中"""

'''
第一步：
爬取网页需要用到的，需要执行多次
'''


def get_url(url):
    # 步骤：
    # 1.模拟浏览器头部信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4455.2 Safari/537.36 "
    }
    cookie = {
        'Cookie': 'MSCookieKey=c2c74a02aa8c4d493a717aab3c849a40.; UM_distinctid=17922cf98f0a12-0edd0fab18db9-6e52772c-144000-17922cf98f1f8c; CNZZDATA1259001544=240567737-1619786531-https%253A%252F%252Fso.meishi.cc%252F%7C1619786531; Hm_lvt_01dd6a7c493607e115255b7e72de5f40=1620391059,1620431749,1620446522,1620446626; Hm_lpvt_01dd6a7c493607e115255b7e72de5f40=1620446633'}
    # 2.请求,返回页面数据
    try:
        response = requests.get(url, headers=headers, cookies=cookie)
        # 针对于重定向网址
        if response.url == url:
            html = response.text
            return html
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"


'''
第二步：
获取中华类别的所有菜系链接
category:是每一大类别的超链接，也是首页
'''


def get_category():
    # 步骤
    # 1.运行get_url方法，拿到最初网址https://www.meishij.net/caipufenlei/
    html = get_url("https://www.meishij.net/caipufenlei/")
    # 2.使用xpath定位元素
    list = etree.HTML(html)
    category_url = list.xpath('/html/body/div[2]/div[1]/div[5]/ul/li/a/@href')
    # 3.循环
    for i in range(len(category_url)):
        url = 'https://www.meishij.net' + str(category_url[i]) + '?order=-fav_num'
        # 4.将列表中不完整的链接加入
        category_url[i] = url
        i += 1
        # 5.输出查看（已经注释）
        # print(url)
    # print(category_url)
    # 6.返回菜谱分类列表
    return category_url


'''
第三步：详情页
'''

# 用于存放其中一系列所有的详情页地址
all_url = []


def detail_page(html):
    list = etree.HTML(html)
    # 详情页的地址
    detail = list.xpath('//div[@class="list_s2_item"]/div/a[1]/@href')
    for i in range(len(detail)):
        all_url.append(detail[i])
        i += 1


'''
第四步：翻页
获取最后的详情页
'''


def next_page(url):
    next_url = [url]
    # 解析这个网页
    # html=get_url(url)
    for i in range(2, 10):
        urls = re.sub('\?order=-fav_num', '', url)
        url = urls + f'p{i}/?order=-fav_num'
        next_url.append(url)
    # 清空
    # all_url = []
    for j in next_url:
        html = get_url(j)
        detail_page(html)
    return all_url


'''
保存数据
'''


def set_data():
    # 获取菜谱系别
    dishes_system_list = get_category()
    # print(dishes_system_list)
    # 获取菜谱详情
    # url_list = next_page()
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='foot', port=3306, charset='utf8')
    cursor = db.cursor()
    # 创建数据表的过程
    # sql = '''
    #        create table foot_url(
    #        id integer primary key autoincrement,
    #        dishes_system varchar,
    #        url varchar)
    #    '''
    for i in dishes_system_list:
        # 首先知道每一大菜系，以每一大菜系做循环
        dishes_system = i
        # print(dishes_system)
        # 列表
        # url_list=next_page(dishes_system)
        # 以每一系列作为
        all_url.clear()
        url_list = next_page(dishes_system)
        # print(url_list)
        for j in range(len(url_list)):
            url = url_list[j]
            # print(url + "第" + str(j) + "条")
            sql = 'insert into url values(0,\"%s\",\"%s\")' % (str(dishes_system), str(url))
            cursor.execute(sql)
            db.commit()
    print('爬取完成，恭喜恭喜！')
    cursor.close()
    db.close()


# if __name__ == '__main__':
    # 测试详情链接的数据
    # print(next_page('https://www.meishij.net/fenlei/jiangxicai/?order=-fav_num'))
    # print(all_page())
    # 测试菜系的数据
    # print(get_category())
    # 运行保存数据
    # set_data()
    # url = get_category()
    # for i in url:
    #     a, b = next_page(i)
    #     print(a)
    #     print(b)
