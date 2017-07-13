#!/usr/bin/env python


def sum_line(y):
    y_list = list(map(sum, zip(y[1:], y[:-1])))
    y_list.insert(0, 1)
    y_list.append(1)
    return y_list


def next_line(m, n, line):
    if m == n:
        return line
    else:
        return next_line(m+1, n, sum_line(line))


def yanghui(m, n):
    if n > m or n < 0:
        print("invalid query")
    elif m == 0:
        print(1)
    elif m == 1:
        y = 1, 1
        print(y[n-1])
    else:
        y = 1, 1
        print(next_line(1, m, y)[n])


def generate_y(m):
    if m >= 0:
        print(1)
    else:
        print('invalid query')
    if m >= 1:
        print(1, 1)
    if m >= 2:
        for i in range(m)[2:]:
            y = 1, 1
            y = next_line(1, i, y)
            for j in range(len(y)):
                print(y[j], end=' ')
            print(' ')



