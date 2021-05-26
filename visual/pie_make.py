import pyecharts.options as opts
import pymysql
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType


def get_data():
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='foot', port=3306, charset='utf8')
    cursor = db.cursor()
    sql = """SELECT DISTINCT
dishes_system,
	COUNT( dishes_system ) AS count 
FROM
	new_menu 
GROUP BY
	dishes_system 
ORDER BY
	count DESC;"""

    cursor.execute(sql)
    # 拿全部数据
    urls = cursor.fetchall()
    # print(url)
    dish_system = []
    count = []
    for dish_system_list, count_list in urls:
        dish_system.append(dish_system_list)
        count.append(count_list)
    cursor.close()
    db.close()
    return dish_system, count


def histogram():
    dish_name, count = get_data()
    x_data = dish_name
    y_data = count
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])
    (
        Pie(init_opts=opts.InitOpts(bg_color='#717f8f', theme=ThemeType.LIGHT))
            .add(
            series_name="占比",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="各菜系占比情况",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
            .render("../templates/echarts/pie.html")
    )


# if __name__ == '__main__':
#     histogram()
