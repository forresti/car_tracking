#!/bin/bash

#record video stream for 10sec
#arg1: input stream
#arg2: output filename (without path or extension)
#sample usage: ./record_10sec.sh http://192.73.220.158/now.jpg?snap=spush capistrano_parking_programmaticTest2 

now=`date +%Y_%m_%d__%H_%M_%S`

#debug? the echo'd command works, but it isnt working from within this script.

cmd="cvlc -I rc $1 --sout=\"#transcode{vcodec=mp4v,vb=1024}:standard{mux=mp4,dst=/media/imagenet_disk/parkingLot_videos/$2_$now.mp4,access=file}\" --run-time=10.0 --play-and-exit"
echo $cmd
#$cmd

#without the 'build cmd, then run' thing ... this works!
cvlc -I rc $1 --sout="#transcode{vcodec=mp4v,vb=1024}:standard{mux=mp4,dst=/media/imagenet_disk/parkingLot_videos/$2_$now.mp4,access=file}" --run-time=10.0 --play-and-exit

