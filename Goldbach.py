#!/usr/bin/env python
import math
import datetime

# Input：923456
# 结果：3 923453 时间：0:00:6.31
starttime = datetime.datetime.now()
def Goldbach(n):
	primes = []
	for num in range(3,n,2):
	# 遍历寻找所有质数 排除所有偶数（加速1）
		primes.append(num)
		for i in range(3, int(math.sqrt(num))+1): # 只验证小于开方的质数（加速2）
			if num % i == 0:
				primes.pop()
				break		# 好像提前break又加速不少（加速3）
	for prime in primes:
		if n-prime in primes:
			return ([prime, n-prime])
	
print (Goldbach(923456))
endtime = datetime.datetime.now()
print (endtime - starttime)