#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import deque

def maxInWindows(num, size):
    '''
    双端队列头为主选位坐标，后面按数组大小值降序排列次选位的坐标。必须存坐标，不然没法判断是否在窗口内
    :param num:
    :param size:
    :return:
    '''
    if (size > len(num) or size <= 0):
        return []
    q = deque([])
    output = []
    q.append(0)
    for i in range(len(num)):
        if num[i] >= num[q[0]]:  # 比当前主选位都大，清空队列并加入主选位
            q.clear()
            q.append(i)
        else:
            while (len(q) > 1 and num[q[-1]] <= num[i]): # 作为次选位，并把那些不比自己大，坐标还靠前的没戏的家伙淘汰掉
                q.pop()
            q.append(i)
        if (i >= size - 1):
            if (i - q[0] < size): # 主选位在窗口内，用主选位
                output.append(num[q[0]])
            else:  # 主选位过期，弹出，用后序次选位，次选位的构造决定了deque中存的坐标对应数组值必定是递减的，下一个一定是最优备选位，且滑动窗口一次一格，次选位和主选位不可能同时过期
                q.popleft()
                output.append(num[q[0]])
    return output

print(maxInWindows([2,3,4,2,6,2,5,1],3))