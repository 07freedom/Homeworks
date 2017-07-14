#!/usr/bin/env python
a = []
def snake(N):
	M = []
	for i in range(N):
		M.append([0]*N)
	for i in range(N//2):
		for j in range(N-1):
			M[0][j] = j+1
			M[j][-1] = j+N
			M[-1][-j-1] = j+2*(N-1)+1
			M[-j-1][0] = j+3*(N-1)+1
	return M

N = 5
M = snake(N)
for i in range(N):
	print (M[i])