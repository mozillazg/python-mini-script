#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cnnb.com.cn/gb/node2/newspaper/pdf/dnsb/2006/06/index.html
# http://www.cnnb.com.cn/gb/node2/newspaper/pdf/dnsb/2006/08/index.html
import urllib2
import re
from pprint import pprint
import urllib

def get_link():
    reg = re.compile(ur"""<a.*?
                    href=["']?([^\.]*?\.pdf)["']?.*?>
                    第[^<]*?版\s*医疗指南</a>""", re.X)
    pages = [
    'http://www.cnnb.com.cn/gb/node2/newspaper/pdf/dnsb/2006/%02d/index.html'
        %(6+n) for n in xrange(3)
    ]
    pprint(pages)
    links = []
    for page in pages:
        # page = u'file:///D:/download/宽带报纸_中国宁波网.htm'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) \
                                    Gecko/20100101 Firefox/4.0.1'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(url=page, headers=headers)

        
        html = urllib2.urlopen(request).read()
        html = unicode(html, 'gb2312')
        # pprint(html)
        # html = re.sub(r'\n|\r', '', html)
        link = reg.findall(html, re.S | re.I)
        links += link
        pprint(link)
    pprint(links)
    return links

if __name__ == '__main__':
    links = get_link()
    host = 'http://www.cnnb.com.cn'
    save = ''
    print '\n'.join([host + '/' + link for link in links])



