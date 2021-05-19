import re

import requests
from selenium import webdriver

# for i in range(0, 10):
#     # print(i)
#     i += 1
# url = 'https://www.meishij.net/caixi/shanxicai/?order=-fav_num'
# browser = webdriver.Chrome()
# browser.get(url)
#
# a = browser.find_element_by_link_text('下一页')
# b = a.get_attribute('href')
# browser.close()
# print(b)
#
# c = '山上?水'
# d = re.sub('\?水', '', c)
# print(d)
#
# e = [1, 2, 3]
# f = [1, 2, 3, 4]
# for i in e:
#     g = i
#     for j in f:
#         h = j
#         print(g, h)
#
# # 获得地址
#
# r = requests.get('https://www.meishij.net/zuofa/xiangjuzhushou.html')
# reditList = r.history  # 可以看出获取的是一个地址序列
# print(f'获取重定向的历史记录：{reditList}')
# print(f'获取第一次重定向的headers头部信息：{reditList[0].headers}')
# print(f'获取重定向最终的url：{reditList[len(reditList) - 1].headers["location"]}')
#
# from analyze_url import analyze
#
#
# def analyze(url):
#     # 做出判断是否为重定向的地址
#     # 然后拿到详情页的数据
#     html = get_url(url)
#
#     list = etree.HTML(html)
#     # 菜名
#     dish_name = \
#         list.xpath('//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/h1/text()')[0]
#     # 收藏数
#     private_int_fcount = list.xpath('//*[@id="addfav_btn"]/em/text()')[0]
#     # 工艺
#     craft = list.xpath(
#         '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[1]/strong/text()')[
#         0]
#     # 口味
#     taste = list.xpath(
#         '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[2]/strong/text()')[
#         0]
#     # 时间
#     time = list.xpath(
#         '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[3]/strong/text()')[
#         0]
#     # 难度
#     difficulty = list.xpath(
#         '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[4]/strong/text()')[
#         0]
#     # 主料
#     main_ingredient_list = list.xpath(
#         '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="recipe_ingredientsw"]/div[1]/div[2]/strong/a/text()')
#     main_ingredient = ','.join(main_ingredient_list)
#     ingredient_list = list.xpath(
#         '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="recipe_ingredientsw"]/div[2]/div[2]/strong/a/text()')
#     ingredient = ','.join(ingredient_list)
#     return dish_name, private_int_fcount, craft, taste, time, difficulty, main_ingredient, ingredient
#
#
# while True:
#     analyze('https://www.meishij.net/zuofa/xiangjuzhushou.html')


# 重定向网页：
url = "https://www.meishij.net/zuofa/xiangjuzhushou.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4455.2 Safari/537.36 "
}
cookie = {
    'Cookie': 'MSCookieKey=c2c74a02aa8c4d493a717aab3c849a40.; UM_distinctid=17922cf98f0a12-0edd0fab18db9-6e52772c-144000-17922cf98f1f8c; CNZZDATA1259001544=240567737-1619786531-https%253A%252F%252Fso.meishi.cc%252F%7C1619786531; Hm_lvt_01dd6a7c493607e115255b7e72de5f40=1620391059,1620431749,1620446522,1620446626; Hm_lpvt_01dd6a7c493607e115255b7e72de5f40=1620446633'}
# 2.请求,返回页面数据
try:
    response = requests.get(url, headers=headers, cookies=cookie)
    if response.url == url:
        html = response.text
        print("爬取成功")
    else:
        print("重定向快乐")
except requests.exceptions.ConnectionError:
    requests.status_code = "Connection refused"
