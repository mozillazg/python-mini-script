#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser


# 设置默认配置
def default_config( configs, configfile):
    configs.add_section('General')
    configs.set('General', 'URL', 'http://www.baidu.com/favicon.ico')
    with open(configfile, 'wb') as config_file:
        configs.write(config_file)
        config_file.close()
    

CONFIGFILE = 'config.ini'  # 配置文件名称
config = ConfigParser.RawConfigParser()

while True:
    try:
        config.read(CONFIGFILE)
        url = config.get('General', 'URL').decode('utf-8')
    except:
        default_config(config, CONFIGFILE)
    else:
        break
