import commands


def pushFile(url):
    a,b = commands.getstatusoutput('cd /media/pi/smp/xz/file')
    # print a

    import Info
    streamname = Info.streamname
    key = Info.key

    print b
    url = 'ffmpeg -re -i "' + url + '" -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://txy.live-send.acg.tv/live-txy/?streamname=' + streamname+ '&key=' + key


    print url
    # a,b = commands.getstatusoutput(url)
    # print b
