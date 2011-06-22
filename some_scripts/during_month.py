#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 输出 2008.8 到 2011.6 的年月
    结果类似：['2010.12', '2011.01', '2011.02', '2011.03']
"""

def main():
    from pprint import pprint
    pprint(['%d.%02d' % (i/12, (i%12)+1) # 因为余数可能为零，而月份没有0月，
                                         # 所以加1
            for i in xrange(2008*12+8-1, 2011*12+6)] # 因为输出时加了个1所以
                                            # 列表减了个1
          )

if __name__ == '__main__':
    main()
