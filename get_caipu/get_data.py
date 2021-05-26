
"""
    运行顺序
    首先运行get_data.py将所有的数据存到数据库当中
    再运行app.py将所有效果展示
"""
from get_caipu.analyze_url import get_data
from get_caipu.get_url import set_data

if __name__ == '__main__':
    # 拿链接
    # set_data()
    # 存数据
    get_data()
