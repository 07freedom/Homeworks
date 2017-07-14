#!/usr/bin/env python
def snake(N):
	M = []
	for i in range(N):
		M.append([0]*N)
	base = 0
	for i in range(N//2):
		for j in range(N-2*i-1):
			M[i][i+j] = j+base+1
			M[i+j][-i-1] = (N-1-2*i)+j+base+1
			M[-i-1][-i-j-1] = 2*(N-2*i-1)+j+base+1
			M[-i-j-1][i] = 3*(N-1-2*i)+j+1+base
		base = base + 4*(N-1)
	if N % 2 == 1:
		M[N//2][N//2] = N*N
	return M

N = 5
M = snake(N)
for i in range(N):
	print (list(M[i]))