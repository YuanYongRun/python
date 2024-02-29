from typing import Union
# 使用Union[类型，类型,.....]在里面写上类型


my_list: list[Union[int,str]] =[1,2,"itheima","itcast"]


def func(data: Union[int,str]) -> Union[int,str]:
    pass

func()
