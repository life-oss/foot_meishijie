import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

db = pymysql.connect(host='localhost', user='root', passwd='123456', db='foot', port=3306, charset='utf8')
cursor = db.cursor()
sql = 'select dish_name,private_int_fcount from foot_menu ORDER BY private_int_fcount desc LIMIT 0,10;'
cursor.execute(sql)
# 拿全部数据
urls = cursor.fetchall()
# print(url)
i = 1
dish_name = []
private_int_fcount = []
for dish_name_list, private_int_fcount_list in urls:
    dish_name.append(dish_name_list)
    private_int_fcount.append(private_int_fcount_list)
cursor.close()
db.close()
'''
此程序用于柱形图可视化的创建
'''
c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(dish_name)
        .add_yaxis('菜名', private_int_fcount)
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts={"text": "中华菜系Top10", "subtext": "数据来源于美食杰"})
        .render("../templates/echarts/bar.html")
)
