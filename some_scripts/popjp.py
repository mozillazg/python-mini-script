#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 15个日本鬼子和15个美国鬼子站成一圈，数到9就从圈里面踢出一个来，
要求写个程序把日本鬼子都给踢出来，美国鬼子都不被踢出来，
输出美国鬼子应该站在哪些位置。
"""

def popjp(people, jp, number):
    index = 0
    for i in range(jp):
        index = (number + index - 1) % len(people)
        people.pop(index)
    return people

def main():
    people = range(1, 31)
    us_list = popjp(people, 15, 9)
    print us_list

if __name__ == '__main__':
    main()

