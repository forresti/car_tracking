import time
from subprocess import call

#record video stream for 10sec
#url = input stream
#name = output filename (without path or extension)
#sample usage: ./record_10sec.sh http://192.73.220.158/now.jpg?snap=spush capistrano_parking_programmaticTest2 

def recordOneVideo(url, name):
    now = time.strftime("%a_%d_%b_%Y__%H_%M_%S")

    cmd='cvlc -I rc ' + url + ' --sout="#transcode{vcodec=mp4v,vb=1024}:standard{mux=mp4,dst=/media/imagenet_disk/parkingLot_videos/' + name +'_' + now +'.mp4,access=file}" --run-time=10.0 --play-and-exit'.decode('utf-8')

    print cmd
    call(cmd, shell=True)


if __name__ == "__main__":
   recordOneVideo('http://192.73.220.158/now.jpg?snap=spush', 'capistrano_parking')
 
