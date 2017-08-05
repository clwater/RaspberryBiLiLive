#!/bin/bash
while true
do
ffmpeg -re -i "/media/pi/smp/xz/file/我的丈夫工作无能第一集.mp4" -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://txy.live-send.acg.tv/live-txy/?streamname=live_23096370_8183481&key=f81e2011b51ef0a36aaa591ad353fec3"
done