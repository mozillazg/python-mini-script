#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json


"""获取用于在中国天气网查询天气的城市 ID
"""

def get_id(keyword, debug=False):
    """keyword 必须为 UTF-8 编码
    result = ((u'广东'，u'深圳', u'11111'),)
    """
    query = urllib.urlencode({
            'callback': 'jsonp1308665312716',
            '_': '1308665332660',
            'language': 'zh',
            'keyword': keyword
            })
    url = 'http://toy.weather.com.cn/SearchBox/searchBox?%s' % query
    data = urllib2.urlopen(url).read()

    # data = '''jsonp1308665312716({"i":[{"n":"桑植","m":"SZ","d":"湖南","i":"101251102","t":"i"},{"n":"尚志","m":"SZ","d":"黑龙江","i":"101050111","t":"i"},{"n":"商州","m":"SZ","d":"陕西","i":"101110604","u":"","t":"i"},{"n":"嵊州","m":"SZ","d":"浙江","i":"101210505","t":"i"},{"n":"深泽","m":"SZ","d":"河北","i":"101090108","t":"i"},{"n":"申扎","m":"SZ","d":"西藏","i":"101140703","t":"i"},{"n":"深圳","m":"SZ","d":"广东","i":"101280601","t":"i"},{"n":"深州","m":"SZ","d":"河北","i":"101090811","t":"i"},{"n":"石柱","m":"SZ","d":"重庆","i":"101042500","t":"i"},{"n":"师宗","m":"SZ","d":"云南","i":"101290406","t":"i"}]});'''
   
    # data = eval(data.split('(')[1].split(')')[0])
    data = json.loads(data.split('(')[1].split(')')[0])
    try:
        result = tuple([(n['d'], n['n'], n['i']) for n in data['i']])
    except:
        return ((u'None', u'None', u'None'), )
    if debug:
        print url
        print data
        print result
        # print [str(a) for a in list(result)]
        # print [repr(a) for a in list(result)]
    # result = ((u'广东'，u'深圳', u'11111'),)  
    return result

def main():
    keyword = raw_input('输入城市名、全拼、简拼、电话区号、邮编查询:').strip()
    keyword = keyword.decode('gbk').encode('utf8')
    print repr(keyword)
    result = list(get_id(keyword, debug=True))
    for a, b, c in result:
        print a, b, c

if __name__ == '__main__':
    main()
