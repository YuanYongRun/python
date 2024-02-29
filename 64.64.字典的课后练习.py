# 组织字典记录数据
info_dcit = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友":{
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华":{
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"升职加薪之前的情况:{info_dcit}")
# 遍历字典
for name in info_dcit:
    # if条件判断级别
    if info_dcit[name]["级别"] == 1:
    #升职加薪操作
        employee_info_dict = info_dcit[name]
    #修改员工的信息
        employee_info_dict["级别"] = 2  # 级别加1
        employee_info_dict["工资"] += 1000
    # 将员工的信息更新回info_dict
        info_dcit[name] = employee_info_dict

print(f"升职加薪后的情况:{info_dcit}")