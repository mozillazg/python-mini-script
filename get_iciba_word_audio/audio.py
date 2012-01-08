#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""从爱词霸下载单词读音音频文件
"""

import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

import urllib2
import re
import os
from BeautifulSoup import BeautifulSoup, SoupStrainer

def get(word, headers=None, lang='US'):
    """获取音频文件链接
    >>> get('receipt')
    http://res.iciba.com/resource/amp3/1/0/1e/11/1e11b989ba2f5e161cdad604bf3de90b.mp3
    """
    # 设置 header
    user_agent = ('Mozilla/5.0 (Windows NT 6.1; rv:9.0) '
                  + 'Gecko/20100101 Firefox/9.0')
    if headers is None:
        headers = {'User-Agent' : user_agent}
    url ='http://www.iciba.com/%s/' % urllib2.quote(word)
    # 读取网页内容
    request = urllib2.Request(url=url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except:
        print u'网络故障！'
        return None
    else:
        # 获取发音所在链接标签
        links = SoupStrainer('a', title=re.compile(ur'真人发音|电脑合成语音'))
        if links:
            audios = [str(tag) for tag in BeautifulSoup(html, parseOnlyThese=links)]
            soup = BeautifulSoup(''.join(audios))
            audios = soup.findAll('a')
            # print audios
            if 'US' in lang.upper() and len(audios) > 1: # 'US'
                audio = audios[1]['onclick'].split("'")[1]
            else: # 'UK'
                audio = audios[0]['onclick'].split("'")[1]
            return audio
        else:
            return None

def path(word, savedir='audio', ext='.mp3'):
    """文件路径
    """
    starts = 'abcdefghijklmnopqrstuvwxyz'
    # 将文件保存到单词开头字母的文件夹中
    for i in starts:
        if word.startswith(i):
            savedir = savedir + os.sep + i
            break
    else:
        savedir = savedir + os.sep + '0-9'
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    # 文件路径
    file_path = savedir + os.sep + word + ext
    return file_path

def save(url, file_path, headers=None):
    """保存音频文件
    """
    if url is None:
        print u'无音频文件可下载！'
    else:
        # 设置 header
        user_agent = ('Mozilla/5.0 (Windows NT 6.1; rv:9.0) '
                      + 'Gecko/20100101 Firefox/9.0')
        if headers is None:
            headers = {'User-Agent' : user_agent}
        headers['Referer'] = 'http://www.iciba.com/%s/' % urllib2.quote(word)
        # 读取网页内容
        request = urllib2.Request(url=url, headers=headers)
        try:
            file_data = urllib2.urlopen(request).read()
        except:
            print u'网络故障！'
            return None
        else:
            with open(file_path,'wb') as output:
                # 写入数据，即保存文件
                output.write(file_data)
            return file_path

def main():
    # import doctest
    # import audio
    # doctest.testmod(audio) # 基于文档字符串的测试
    while True:
        word = raw_input("> ").strip()
        if not word: break
        file_path = path(word)
        # 如果文件已存在
        if os.path.exists(file_path):
            answer = raw_input(u'文件已存在！是否覆盖(y/n):')
            if answer.strip().lower().startswith('y'):
                if save(get(word), file_path):
                    print u'文件已成功下载！'
                    print os.path.realpath(file_path)
            else:
                print u'文件未覆盖！'
                print os.path.realpath(file_path)
        else:
            if save(get(word), file_path):
                print u'文件已成功下载！'
                print os.path.realpath(file_path)

if __name__ == '__main__':
    main()

