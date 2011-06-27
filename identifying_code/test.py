#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""生成简单的内容为文字的图片
"""

import codecs
import random
import Image
import ImageDraw
import ImageFont
# import ImageFilter



# 新建图片
img = Image.new("RGB", (100, 60))
# 绘制图片
draw = ImageDraw.Draw(img)
# 字体
font = ImageFont.truetype('wqy-microhei.ttc', 20)
# 绘入线条
# draw.line([10,50,30,20,15,2,5,13])
for i in xrange(150):
    x = random.choice(range(101))
    y = random.choice(range(61))
    xx = random.choice(range(30))
    yy = random.choice(range(20))
    draw.line([x, y, x + xx, y + yy], fill=(x, y, x + xx, y + yy))
    draw.line([y, x, x + xx, y + yy], fill=(x, y, x + xx, y + yy))
            
# 从文件中读取文字
filename = ur'text.txt'
encoding = 'utf8'
words = []
for line in codecs.open(filename, 'r', encoding):
    for word in line:
        word.strip()
        if word:
            words.append(word)
print len(words)
txt = [random.choice(words) for i in range(5)]
print txt

# 绘入文字
leng = []
# for i in u"test 测试":
for i in txt:
    leng.append(i)
    # print leng
    draw.text((0 + len(leng)*11, random.uniform(1,40)), i , 
            font=font, fill=(23, 234, 333))
# 浮雕滤镜
# img = img.filter(ImageFilter.EMBOSS).filter(ImageFilter.FIND_EDGES)
# 保存到文件
img.save('test.png', 'png')
# 显示图片
# img.show()
