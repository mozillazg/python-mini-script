#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2


"""获取用于在中国天气网查询天气的城市 ID
"""

def get_id(keyword, debug=False):
    query = urllib.urlencode({
            'callback': 'jsonp1308665312716',
            '_': '1308665332660',
            'language': 'zh',
            'keyword': str(keyword)
            })
    url = 'http://toy.weather.com.cn/SearchBox/searchBox?%s' % query
    data = urllib2.urlopen(url).read()
    data = eval(data.split('(')[1].split(')')[0])
    name = None
    id = None
    try:
        print data['i']
        name = [n['d'] + '-' + n['n'] for n in data['i']]
        id = [n['i'] for n in data['i']]
    except:
        print 'sorry, no data'
    if debug:
        print url
        print data
        if name:
            print '\n'.join([
                    name[n] + ':' + id[n] for n in range(len(name))
                ]).decode('utf8').encode('gbk')
    return (name, id)

def main():
    keyword = raw_input('input(输入城市名、全拼、简拼、电话区号、邮编查询):').strip()
    name, id = get_id(keyword, debug=True)
    if name:
        print '\n'.join([
                name[n] + ':' + id[n] for n in range(len(name))
            ]).decode('utf8').encode('gbk')

if __name__ == '__main__':
    main()
