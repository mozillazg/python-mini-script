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

    city_info = re.findall(r'<string>(.*?)</string>', text)[0]
    weathers = re.findall(rex, text)[7:]

    return (city_info, weathers)

if __name__ == '__main__':
    cityname = raw_input('input:').strip().decode('gbk').encode('utf8')
    city_info, weathers = weather(cityname)
    print cityname.decode('utf8')
    if len(weathers) > 1:
        for a in xrange(0, len(weathers)):
            weathers[a] = ' ' + weathers[a]
            if (a+1)%3 == 0:
                weathers[a] = weathers[a] + '\n'
    print ''.join(city_info)
    print ''.join(weathers)
