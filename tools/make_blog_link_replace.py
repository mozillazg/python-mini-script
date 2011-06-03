#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

# 返回博客固定连接，类似于：hello-world

while True:
    text = raw_input("请输入要作为博客固定链接的英文文本：").strip()
    if text:
        break

link1 = re.sub('[^a-zA-Z0-9]', '-', text) # 匹配特殊符号
link2 = re.sub(r'\-+', '-', link1) # 匹配连续多个 '-'
link = re.sub(r'\-$|^\-', '', link2) # 匹配开头与结尾的 '-'
print link
