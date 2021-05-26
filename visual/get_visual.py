from visual.bar_make import bar_make
from visual.pie_make import histogram
from visual.wordcount import split_word, word_cloud, get_text

if __name__ == '__main__':
    # 柱形图运行
    bar_make()
    # 饼图运行
    histogram()
    # 词云运行
    # 主料词云分析
    sql = 'select main_ingredient from new_menu;'
    data = split_word(get_text(sql))
    word_cloud(data, 1, "主料分析")
    # 配料词云分析
    sql2 = 'select ingredient from new_menu;'
    data = split_word(get_text(sql2))
    word_cloud(data, 2, "辅料分析")