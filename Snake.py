#!/usr/bin/env python
def snake(N):
	M = []
	for i in range(N):
		M.append([0]*N)
	base = 0
	for i in range(N//2):
		for j in range(N-1-2*i):
			M[i][j+i] = j+1+base
			M[j+i][-1-i] = j+(N-1-2*i)+1+base
			M[-1-i][-j-1-i] = j+2*(N-1-2*i)+1+base
			M[-j-1-i][i] = j+3*(N-1-2*i)+1+base
		base = base + 4*(N-1)
	if N % 2 == 1:
		M[N//2][N//2] = N*N
	return M

N = 7
M = snake(N)
for i in range(N):
	print (M[i])