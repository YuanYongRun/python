def check(num):
    # 判断体温
    print("欢迎来到黑马程序员!请出示你的健康码以及72小时核酸证明")
    if num <=37.5:
        print(f"你的体温是{num}度，正常，请进")
    else:
        print(f"你的体温是{num}度，不正常，请隔离")

check(37.8)