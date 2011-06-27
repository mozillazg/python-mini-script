#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""生成简单的包含文字的图片
"""

import codecs
import random
import Image
import ImageDraw
import ImageFont

# 新建图片
img = Image.new("RGB", (100, 60))
# 绘制图片
draw = ImageDraw.Draw(img)
# 字体
font = ImageFont.truetype('wqy-microhei.ttc', 20)
# 绘入文字
draw.text((10, 20), u"test 测试", font=font)
# 保存到文件
img.save('test1.png', 'png')
# 显示图片
img.show()
