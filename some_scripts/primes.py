#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log
from itertools import takewhile
from itertools import count
from time import time

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def logs(n):
    xlogs = (log(x) for x in xrange(1, n+1) if isPrime(x))
    # 当 n 特别大导致 xrange 异常时
    # xlogs = (log(x)
            # for x in takewhile(lambda x: x<n+1, (1+i*1 for i in count()))
            # if isPrime(x))
    return xlogs

def main():
    n = long(eval(raw_input("n:").strip()))
    start = time()
    print start
    xlogs = logs(n)
    xsum = sum(xlogs)
    ratio = xsum/n
    print "n: %s\nsum: %s\nratio: %s" %(n, xsum, ratio)
    print (time() - start)

if __name__ == '__main__':
    while True:
        main()
