from pyecharts.charts import Bar
from pyecharts.options import *

# 使用Bar构建基础柱状图
bar = Bar()

# 添加x轴的数据
bar.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))



# 反转x y轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")

