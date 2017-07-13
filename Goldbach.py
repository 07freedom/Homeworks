#!/usr/bin/env python
import datetime

starttime = datetime.datetime.now()
def Goldbach(n):
	primes = []
	for num in range(3,n,2):
	# 遍历寻找所有质数 排除所有偶数（加速1）
		primes.append(num)
		for i in range(3, (num//3)+1): # 只验证前1/3质数（加速2）
			if num % i == 0:
				primes.pop()
				break		
	for prime in primes:
		if n-prime in primes:
			return ([prime, n-prime])
	
print (Goldbach(100000))
endtime = datetime.datetime.now()
print (endtime - starttime)