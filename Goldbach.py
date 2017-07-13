#!/usr/bin/env python
def Goldbach(n):
	primes = [2]
	for num in range(2,n):
	# 遍历寻找所有质数
		if (num % 2) != 0: # 排除所有偶数（加速1）
			primes.append(num)
			for i in range(3, (num//2)+1): # 只验证前半质数（加速2）
				if num % i == 0:
					primes.pop()
					break		
	for prime in primes:
		if n-prime in primes:
			return ([prime, n-prime])
	

print (Goldbach(20000))