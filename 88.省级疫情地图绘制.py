import json
from pyecharts .charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts


# 读取文件
f = open("E:/黑马程序员资料\资料\可视化案例数据\地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()

# 获取河南数据
# json数据转换为python字典
data_dict = json.loads(data)

# 获取河南省的数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]
data_list = []
# 准备数据为元组放入list
for city_data in cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm))

# 手动添加济源市
data_list.append(("济源市",55))


# 构建地图
map = Map()

# 添加数据
map.add("河南省疫情分布",data_list,"河南")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        # is_show=True,
        is_piecewise=True,    #是否分段
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#CCFFF"},
            {"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999","color":"#CC3333"},
            {"min":100000,"label":"10000+","color":"#990033"},
        ]
    )
)

# 绘图
map.render("河南省疫情地图.html")

