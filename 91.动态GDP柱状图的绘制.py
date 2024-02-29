# # 准备列表
# my_list = [["a",33],["b",55],["c",11]]
#
# # 排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]
#
#
# my_list.sort(key = choose_sort_key,reverse=True)
#
# print(my_list)
#
# # 基于lamda函数
# my_list.sort(key = lambda element:element[1],reverse=True)
# print(my_list)

from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("E:/黑马程序员资料\资料\可视化案例数据\动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()
f.close()

# 删除第一条数据
data_lines.pop(0)

# 将数据转换为字典存储格式
# {年份:[国家:gdp],[国家,gdp],.........],[国家:gdp],[国家,gdp],.........],...}
# 定义一个字典
data_dict = {}
for line in data_lines:
    years = int(line.split(",")[0])   #年份
    country = line.split(",")[1]      #国家
    gdp = float(line.split(",")[2])   #GDP数据
    # 如何判断字典里面有没有指定的key
    try:
        data_dict[years].append([country,gdp])
    except KeyError:
        data_dict[years]=[]
        data_dict[years].append([country, gdp])


#创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})
# 排序年份
sorted_years_list = sorted(data_dict.keys())
for year in sorted_years_list:
    data_dict[year].sort(key = lambda element:element[1],reverse=True)
    #取出本年份前八的国家
    year_data =data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])   #x轴添加国家
        y_data.append(country_gdp[1])   # Y轴添加GDP数据

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP:(亿)",y_data,label_opts=LabelOpts(position="right"))

    # 反转x和y轴
    bar.reversal_axis()
    #设置每一年的图标的标题
    bar.set_global_opts(
        title_opts= TitleOpts(title=f"{year}年全球前八GDP的数据")
    )
    timeline.add(bar,str(year))

# 设置时间线
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False,
)

# 绘图
timeline.render("1960-2019全球GDP前八的国家.html")