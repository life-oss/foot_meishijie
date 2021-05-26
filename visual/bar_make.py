import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


def bar_make():
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='foot', port=3306, charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT
        dishes_system,dish_name,
        browse_the_numbert
    FROM
        new_menu 
    ORDER BY
        browse_the_numbert DESC 
        LIMIT 0,
        10;'''
    cursor.execute(sql)
    # 拿全部数据
    urls = cursor.fetchall()
    # print(url)
    i = 1
    dish_name = []
    browse_the_numbert = []
    for dishes_system,dish_name_list, browse_the_numbert_list in urls:
        dish_name.append(dish_name_list)
        browse_the_numbert.append(browse_the_numbert_list)
    cursor.close()
    db.close()
    '''
    此程序用于柱形图可视化的创建
    '''
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(dish_name)
            .add_yaxis('菜名', browse_the_numbert)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts={"text": "中华菜系Top10", "subtext": "数据来源于美食杰"})
            .render("../templates/echarts/bar.html")
    )
