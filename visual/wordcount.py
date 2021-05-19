import collections
import jieba
import pymysql
import pyecharts.options as opts
from pyecharts.charts import WordCloud


def get_text(sql):
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='foot', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    # 拿全部数据
    urls = cursor.fetchall()
    text = ""
    for text_list in urls:
        text += text_list[0] + ""
    # print(text)
    return text


def split_word(text):
    word_list = list(jieba.cut(text, cut_all=False, HMM=True))
    with open("stop_word.txt", 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    object_list = []
    for word in word_list:
        if word not in stopwords:
            object_list.append(word)
    # collections.Counter 计数器，统计单词个数
    word_counts = collections.Counter(object_list)
    word_count = word_counts.most_common(2000)
    # 筛选词语
    return word_count


def word_cloud(data, i, str):
    c = (
        WordCloud()
            .add(
            "",
            data,
            # 添加数据
            word_gap=5,
            word_size_range=[15, 80])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=str, title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render(f"../templates/wordcount/ingredient{i}.html")
    )


if __name__ == '__main__':
    # 主料词云分析
    sql = 'select main_ingredient from foot_menu;'
    data = split_word(get_text(sql))
    word_cloud(data, 1, "主料分析")
    # 配料词云分析
    sql2 = 'select ingredient from foot_menu;'
    data = split_word(get_text(sql2))
    word_cloud(data, 2, "辅料分析")
