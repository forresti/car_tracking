import random
from pprint import pprint
import time
from subprocess import call

#record video stream for 10sec
#url = input stream
#name = output filename (without path or extension)
#sample usage: ./record_10sec.sh http://192.73.220.158/now.jpg?snap=spush capistrano_parking_programmaticTest2 

def recordOneVideo(url, name):
    now = time.strftime("%a_%d_%b_%Y__%H_%M_%S")

    #cmd='DISPLAY=:0.0 cvlc -I dummy \"' + url + '\" --sout="#transcode{vcodec=wmv2,vb=2048}:standard{mux=asf,dst=/media/imagenet_disk/parkingLot_videos/' + name +'_' + now +'.asf,access=file}" --run-time=10.0 --play-and-exit'.decode('utf-8') #11/20/14

    #cmd='DISPLAY=:0.0 cvlc -I dummy \"' + url + '\" --sout="#transcode{vcodec=mp4v,vb=2048}:standard{mux=mp4,dst=/media/imagenet_disk/parkingLot_videos/' + name +'_' + now +'.mp4,access=file}" --run-time=10.0 --play-and-exit'.decode('utf-8') #11/11/14 (originally vb=1024)

    cmd='DISPLAY=:0.0 cvlc -I dummy \"' + url + '\" --sout="#transcode{vcodec=mp4v,vb=4096}:standard{mux=mp4,dst=/media/forrest/imagenet_disk/parkingLot_videos/' + name +'_' + now +'.mp4,access=file}" --run-time=30.0 --play-and-exit'.decode('utf-8') #11/24/14 (vb=4096)

    print cmd
    call(cmd, shell=True)

def read_camera_list():
    cameraList = []
    fname = '/media/forrest/imagenet_disk/car_tracking/cameras.tsv'
    f = open(fname)
    line = f.readline()
    while(line):
        [url, name] = line.split() #split on whitespace
        #TODO: use dict instead here?
        cameraList.append([url, name])
        line = f.readline() 

    return cameraList

if __name__ == "__main__":
    cameraList = read_camera_list()
    #pprint(cameraList)
    #recordOneVideo('http://192.73.220.158/now.jpg?snap=spush', 'capistrano_parking')
    #print random.choice(cameraList)
    randomCamera = random.choice(cameraList)
    recordOneVideo(randomCamera[0], randomCamera[1])
