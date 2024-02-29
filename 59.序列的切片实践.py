my_str = "万过薪月，员序程马黑来，nohtyP学"

# 倒序字符，切片取出
result1 = my_str[::-1][9:14]
print(f"方式1结果:{result1}")

result2 = my_str[5:10][::-1]
print(f"方式2结果:{result2}")

# split分割
result3 = my_str.split("，")[1].replace("来","")[::-1]
print(f"方式3结果:{result3}")

