#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第2章-6 求交错序列前N项和 (15分)'

__author__ = 'Killer'


n = int(input())

sum = 0
k=1
for i in range(1,n+1):
    sum +=i/(2*i-1)*k
    k=-k
print(f'{sum:.3f}')
