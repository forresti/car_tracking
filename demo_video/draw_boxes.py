import cv2

def read_bboxes(boxF):
    

#@param box_dict = {xmin, xmax, ymin, ymax}
#  TODO: make sure this updates 'img' in place ... or else, return 'img'
'''
def drawBox(img, box_dict, box_ID):

    cv2.rectangle(img, (xmin,ymin), (xmax,ymax)) #TODO: x first or y first? 
    #TODO: draw box ID too
'''

if __name__ == "__main__":

    #TODO: decide whether to use original video or ffmpeg'd images
    #TODO: if using original video, scale boxes to original video
    #TODO: figure out how to save video output

    boxF = 'boxes_bradley_univ_90min.txt' #from vatic
    fps = 1 #annotation frequency (only used if drawing on original video)
    
    imgDir = '~/installers/vatic/public/frames/bradley_univ_90min' #vatic'd frames


