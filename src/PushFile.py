#!/usr/bin/python
# -*- coding: UTF-8 -*-

import commands


import sys
reload(sys)
sys.setdefaultencoding('utf8')

def pushFile(url):
    # a,b = commands.getstatusoutput('cd /media/pi/smp/xz/file')
    # print a

    # a, b = commands.getstatusoutput('kill %1')
    # print b

    print 'url: ' + url


    streamname = ''
    key = ''
    with open('streamname', 'r') as f:
        streamname  = f.read()

    with open('key', 'r') as f:
        key = f.read()

    # print b
    url = 'ffmpeg -re -i "/media/pi/smp/xz/file/' + url + '" -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://txy.live-send.acg.tv/live-txy/?streamname=' + \
          streamname+ '&key=' + key + '" &'

    url = url.decode('utf-8')

    # url = str(url)


    print "url2 : " + url
    a,b = commands.getstatusoutput(url)
    print b
