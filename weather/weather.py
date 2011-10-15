#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 获取天气信息
powed by http://www.webxml.com.cn/
"""

import re
import urllib2
# from get_id import get_id

#TODO 根据 get_id.py 取得的城市id，
# 直接获取中国天气网(http://weather.com.cn/)的天气数据

def weather(cityname):
    """cityname 必须为 utf8 编码
    """
    headers = {'Host': 'webservice.webxml.com.cn'}
    # text = open('getWeather.xml').read().decode('utf8')
    url = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather?theCityCode=%s&theUserID=' %(urllib2.quote(cityname))
    # print url
    request = urllib2.Request(url=url, headers=headers)
    text = urllib2.urlopen(request).read().decode('utf8')
    # print text

    rex = r'<string>([^<.]*?)</string>'

    weathers = re.findall(rex, text)[7:]

    return weathers

if __name__ == '__main__':
    cityname = raw_input('input:').strip().decode('gbk').encode('utf8')
    weathers = weather(cityname)
    print cityname.decode('utf8')
    if not weathers:
        print u'查询结果为空'
    else:
        print '\n'.join(weathers)
