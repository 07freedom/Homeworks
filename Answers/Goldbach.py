#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import math
import datetime


# 法1：不删除偶数  
# # 结果：3 923453   时间：0:01:42.145881
# starttime_1 = datetime.datetime.now()
# def Goldbach_1(num):
    # prime_num = list(filter(lambda x:not [x % j for j in range(2,int(math.sqrt(x))+1) if x % j == 0],range(2,num+1)))
    # for i in prime_num:
        # if num - i in prime_num:
            # print(i,num-i)
            # break
# Goldbach_1(923456)
# endtime_1 = datetime.datetime.now()
# print(endtime_1 - starttime_1)


# 法2：删除偶数
# 结果：3 923453 时间：0:00:30
starttime_2 = datetime.datetime.now()
def Goldbach_2(num):
    num_range = list(range(3,num+1,2))
    num_range.insert(0,2)
    prime_num = list(filter(lambda x:not [x % j for j in range(2,int(math.sqrt(x))+1) if x % j == 0],num_range))
    for i in prime_num:
        if num - i in prime_num:
            print(i,num-i)
            break
Goldbach_2(923456)
endtime_2 = datetime.datetime.now()
print(endtime_2 - starttime_2)


