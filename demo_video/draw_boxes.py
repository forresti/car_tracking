import cv2
from pprint import pprint
from IPython import embed

def read_bboxes(boxF):
    boxes = []
    f = open(boxF, 'r')
    line = f.readline()
    while line:
        #'lost' = outside of view screen (don't draw)
        [objID, x1, y1, x2, y2, frameID, lost, 
                occluded, generated, category] = line.split(' ')

        box_dict = {'objID':int(objID), 
                    'xmin':int(x1), 'xmax':int(x2), 
                    'ymin':int(y1), 'ymax':int(y2), 
                    'frameID':int(frameID), 'lost':int(lost), 'occluded':int(occluded), 
                    'generated':int(generated), 'category':category.strip()}
        boxes.append(box_dict) 
        line = f.readline()
    f.close()
    return boxes

#@param boxes = dict of bboxes from read_bboxes()
def get_frame_ID_list(boxes):
    frameID = [b['frameID'] for b in boxes]
    return list(set(frameID)) #unique frame IDs

#@param box_dict = {xmin, xmax, ymin, ymax}
#TODO: make sure this updates 'img' in place ... or else, return 'img'

#put bbox on image
def draw_box(img, box_dict):
    if box_dict['lost'] == True: #'lost' means 'object is out of frame.'
        return

    xmin = box_dict['xmin']
    xmax = box_dict['xmax']
    ymin = box_dict['ymin']
    ymax = box_dict['ymax']
    color = (0,255,0)
    cv2.rectangle(img, (xmin,ymin), (xmax,ymax), color) #TODO: x first or y first? 

#using FFMPEG'd images (typically downsampled from orig video)
if __name__ == "__main__":

    boxF = 'boxes_bradley_univ_90min.txt' #from vatic
    fps = 1 #annotation frequency (only used if drawing on original video)
    imgDir = '~/installers/vatic/public/frames/bradley_univ_90min' #vatic'd frames

    boxes = read_bboxes(boxF)
    frame_list = get_frame_ID_list(boxes)

    #0, 1, 2, ... 5400
    for frameID in frame_list[0:1]:
        imgF = '/Users/forrest/computerVision/0.jpg' 
        #imgF = imgDir + '/0/%d/%d.jpg' % ( mod(frameID, 100), frameID ) #vatic's wierd directory hierarchy
        img = cv2.imread(imgF)
        my_boxes = [b for b in boxes if b['frameID'] == frameID]

        for b in my_boxes:
            draw_box(img, b) #TODO: need to return img or not?
            #TODO: annotate timer on each box

    cv2.namedWindow("preview")
    cv2.imshow("preview", img)
    cv2.waitKey(0) #you have to have the window in focus for it to listen (any key -> exit)

