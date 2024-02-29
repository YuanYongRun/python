
# 读取数据文件
import json
from pyecharts.charts import Map
from pyecharts.options import  *

f = open("E:/黑马程序员资料\资料\可视化案例数据\地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()

# 关闭文件
f.close()

#取到各省的数据
# 将字符串转到json转换为python的字典
data_dict = json.loads(data)

# 从字典中取出各省份的数据
replace_dict = {
    "北京": "北京市",
    "上海": "上海市",
    "天津": "天津市",
    "重庆": "重庆市",
    "新疆": "新疆维吾尔自治区",
    "内蒙古": "内蒙古自治区",
    "宁夏": "宁夏回族自治区",
    "西藏": "西藏自治区",
    "广西": "广西壮族自治区",
    "香港": "香港特别行政区",
    "澳门": "澳门特别行政区",
}
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并将每个省封装到列表中
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]

    if province_name in replace_dict:
        province_name = replace_dict[province_name]
    else:
        province_name += "省"

    province_data["name"] = province_name
    province_confirm = province_data["total"]["confirm"]  #确诊人数
    data_list.append((province_name,province_confirm))

print(data_list)


# 创建地图对象
map = Map()

# 添加数据
map.add("各省确诊人数",data_list,"china")

# 设置全局配置，定制分段视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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
map.render()