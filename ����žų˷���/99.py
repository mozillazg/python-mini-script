#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输出 9x9 乘法表

for x in range(1, 10):
    a = []
    for y in range(1, x+1):
        a.append('%s x %s = %-2s  ' %(y, x, x*y))
    print ''.join(a)
    