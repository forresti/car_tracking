from bs4 import BeautifulSoup
from IPython import embed
import subprocess
import os
import errno
#import pysrt
import time
import urllib2
import urlparse
import os

def mkdir_path(path):
    if not os.access(path, os.F_OK):
        os.mkdir(path)

#TODO: take frame rate as input argument
# @param vidLocation -- e.g. outdata/qS4DJgFmNFM/qS4DJgFmNFM.m4v
# @param outDir -- e.g. outdata/qS4DJgFmNFM 
# @return imgDir, where images have been saved
#         in imgDir, we'll get "00001.png, 00002.png, etc"
def slice_video_to_frames(vidLocation, outDir):
    imgDir = outDir

    if not os.path.isdir(imgDir):
        os.mkdir(imgDir)

    #example: "ffmpeg  -i qS4DJgFmNFM.mp4  -r 0.2 outdata/qS4DJgFmNFM/images/%5d.png"
    ffmpeg_cmd = "ffmpeg  -i %s  -r .5 %s/" %(vidLocation, imgDir)  # -r 2 = 2fps  
    ffmpeg_cmd = ffmpeg_cmd + "%5d.png" 
    print ffmpeg_cmd
    subprocess.call(ffmpeg_cmd, shell=True)
    print "grabbed video frames"

    #else:
    #    print "found cached video frames"
    return imgDir

if __name__ == "__main__":
    #video_id = 'WJ_-uXQeGSo' #7sec Mirriad coke zero video

    #inVideo = '/media/imagenet_disk/capistrano.mp4'
    inVideo = './capistrano_short.mp4'
    outDir = './capistrano_short'

    #outDir = 'outdata/%s' %video_id
    #TODO: inVideo -> outDir (remove the <video_id>.mp4 from end of filename)
    imgDir = slice_video_to_frames(inVideo, outDir)


