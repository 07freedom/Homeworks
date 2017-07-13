#!/usr/bin/env python

def yanghui(n):
    lst = []
    for row in range(n):
        if row < 2:
            n_row = [1 for i in range(row+1)]
        else:
            last_row = lst[-1]
            n_row = [last_row[i]+last_row[i+1] for i in range(len(last_row)-1)]
            n_row = [1] + n_row + [1]
        lst.append(n_row)
    return lst


def yanghui_2(n,k):
    lst = yanghui(n)[-1]
    return lst[k]


# print(yanghui_2(5,3))
yh = yanghui(5)
# for i in yh:
    # print('{:^15}'.format(str(i)[1:-1]))
print (yh)