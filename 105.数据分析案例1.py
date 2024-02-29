# 读取数据，设计FileReader类
from date_define import Record
from file_define import File_reader,TextFileReader,JsonFileReader
from pyecharts.charts import Bar,ThemeRiver
from pyecharts.options import *
from pyecharts.globals import  ThemeType

text_file_reader = TextFileReader("E:/黑马程序员资料/2011年1月销售数据.txt")
json_file_reader =JsonFileReader("E:/黑马程序员资料/2011年2月销售数据JSON.txt")

jan_data:list[Record] = text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为1个list存储
all_data:list[Record] = jan_data+feb_data

#开始进行数值计算
# {"2011-01-01":1234}
data_dict ={}
for record in all_data:
    if record.data in data_dict.keys():
        # 当前日期已经有记录了，和老记录做累加
        data_dict[record.data] +=record.money
    else:
        data_dict[record.data] =record.money

print(data_dict)


# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))    #添加x轴数据
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts= TitleOpts(title="每日销售额")

)
bar.render("每日销售额图表开发.html")
