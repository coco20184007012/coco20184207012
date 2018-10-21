# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:23:06 2018

@author: Administrator
"""

def fibs(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

lst = fibs(10)
print(lst)