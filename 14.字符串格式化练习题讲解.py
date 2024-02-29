""""
讲解字符串格式化的课后练习题
"""

# 定义需要的变量
name = "传智播客"
stock_price = 19.99
stcok_code = "00302"
#
stcok_price_daily_growth_factor = 1.2
growth_days = 7

finally_stcok_price = stock_price * stcok_price_daily_growth_factor ** growth_days

print(f"公司:{name}，股票代码:{stcok_code},当前股价:{stock_price}")
print(f"每日增长系数:%f,经过%d天的增长后，股价达到了:%.2f"%(stcok_price_daily_growth_factor,growth_days,finally_stcok_price))