import  json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
# 处理数据
f_us = open("E:/黑马程序员资料\资料\可视化案例数据\折线图数据/美国.txt","r",encoding="UTF-8")
us_data = f_us.read()
print(us_data)
f_jp = open("E:/黑马程序员资料\资料\可视化案例数据\折线图数据/日本.txt","r",encoding="UTF-8")
jp_data = f_jp.read()

f_India = open("E:/黑马程序员资料\资料\可视化案例数据\折线图数据/印度.txt","r",encoding="UTF-8")
India_data = f_India.read()

#去掉不喝JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
India_data = India_data.replace("jsonp_1629350745930_63180(","")

#去掉不合JSon的规范的结果
us_data = us_data[:-2]
jp_data = jp_data[:-2]
India_data = India_data[:-2]

# jason转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
India_dict = json.loads(India_data)
# print(type(us_dict))
print(us_dict)

# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
India_trend_data = India_dict["data"][0]["trend"]

# 获取日期数据，用于x轴，取2020年(导31结束）
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
India_x_data = India_trend_data["updateDate"][:314]
# print(us_x_data)

# 获取确诊数据
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
India_y_data = India_trend_data["list"][0]["data"][:314]


# 生成图表
Line = Line()

# 添加x轴
Line.add_xaxis(us_x_data)   #x轴可以共用

# 添加y轴
Line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
Line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
Line.add_yaxis("印度确诊人数",India_y_data,label_opts=LabelOpts(is_show=False))

# 全局选项
Line.set_global_opts(
    #标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%"),


)

#调用render方法生成
Line.render()
#关闭问价对象
f_jp.close()
f_India.close()
f_us.close()
