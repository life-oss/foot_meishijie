import re

import pymysql
from lxml import etree

from get_url import get_url


def get_data():
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='foot', port=3306, charset='utf8')
    cursor = db.cursor()
    sql = 'select dishes_system,url from foot_url;'
    cursor.execute(sql)
    # 拿全部数据
    urls = cursor.fetchall()
    # print(url)
    i = 1

    for dishes_system_list, url in urls:
        dishes_system = method_name(str(dishes_system_list))
        dish_name, private_int_fcount, craft, taste, time, difficulty, main_ingredient, ingredient = analyze(str(url))
        sql1 = 'insert into menu values(0,\"%s",\"%s",\"%s",\"%s",\"%s",\"%s",\"%s",\"%s",\"%s")' % (
            str(dishes_system), str(dish_name), str(private_int_fcount), str(craft), str(taste), str(time),
            str(difficulty),
            str(main_ingredient), str(ingredient))
        cursor.execute(sql1)
        db.commit()
        print("写入第" + str(i) + "条数据")
        i += 1
    cursor.close()
    db.close()
    print("数据全部拿到，恭喜!!!")


def analyze(url):
    # 做出判断是否为重定向的地址
    # 然后拿到详情页的数据
    html = get_url(url)

    list = etree.HTML(html)
    # 菜名
    dish_name = \
        list.xpath('//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/h1/text()')[0]
    # 收藏数
    private_int_fcount = list.xpath('//*[@id="addfav_btn"]/em/text()')[0]
    # 工艺
    craft = list.xpath(
        '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[1]/strong/text()')[
        0]
    # 口味
    taste = list.xpath(
        '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[2]/strong/text()')[
        0]
    # 时间
    time = list.xpath(
        '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[3]/strong/text()')[
        0]
    # 难度
    difficulty = list.xpath(
        '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="info2"]/div[4]/strong/text()')[
        0]
    # 主料
    main_ingredient_list = list.xpath(
        '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="recipe_ingredientsw"]/div[1]/div[2]/strong/a/text()')
    main_ingredient = ','.join(main_ingredient_list)
    ingredient_list = list.xpath(
        '//*[@id="app"]/div[@class="recipe_header"]/div[1]/div[@class="recipe_header_info"]/div[@class="recipe_ingredientsw"]/div[2]/div[2]/strong/a/text()')
    ingredient = ','.join(ingredient_list)
    return dish_name, private_int_fcount, craft, taste, time, difficulty, main_ingredient, ingredient


# 试验
# print(analyze('https://www.meishij.net/zuofa/chaoyixuetangcupaigu.html'))

def method_name(url):
    html = get_url(url)
    list = etree.HTML(html)
    dishes_system_list = list.xpath('//div[@class="list_s2"]/h1[@class="list_title"]/text()')[0]
    # 正则(.+?)菜
    dishes_system_match = re.match(r'(.+?)菜', str(dishes_system_list))
    dishes_system = dishes_system_match.group()
    return dishes_system


# 试验
# print(method_name('https://www.meishij.net/caixi/chuancai/'))
if __name__ == '__main__':
    get_data()
