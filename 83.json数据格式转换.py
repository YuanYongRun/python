# 导入json模块
import json
# 准备列表，列表每个内容都是字典，将其转换为JSON
data = [{"name":"张大三","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典，将字典转化为Json
d = {"name":"周杰伦","addr":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)


# 将Json字符串转换为python的数据类型
s = '[{"name": "张大三", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)

# 将Json字符串转换为python的数据类型
s = '{"name": "周杰伦", "addr": "台北"}'
d = json.loads(s)
print(type(d))
print(d)