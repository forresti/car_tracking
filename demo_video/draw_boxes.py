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

#@param curr_minute = amount of time this car has been parked.
#@param box_dict contains, at a mininum: xmin, xmax, ymin, ymax
def draw_timer(img, box_dict, curr_minute):
    if box_dict['lost'] == True: #'lost' means 'object is out of frame.'
        return

    if curr_minute < 60:
        color = (255,255,255)
    else: #YOU PARKED TOO LONG!
        color = (0,0,255) #RED

    font = cv2.FONT_HERSHEY_SIMPLEX
    string = '%d min' %curr_minute
    fontScale = 0.3
    thickness = 1
    textSz = cv2.getTextSize(string, font, fontScale, thickness)
    textW = textSz[0][0]
    textH = textSz[0][1]

    originX = box_dict['xmax'] - (box_dict['xmax'] - box_dict['xmin'])/2 - textW/2 #left side of text box (horizontally centered in img)
    originY = box_dict['ymin'] + textH #top of text box = top of bbox
    origin = (originX, originY)    

    #origin = (box_dict['xmin'], box_dict['ymax']) #bottom-left of text box (TODO: improve positioning)
    cv2.putText(img, string, origin, font, fontScale, color, thickness)

#@param objID = ID of box according to vatic
def get_first_frame(objID, boxes):
    #assume 'boxes' is sorted by frame ID

    #ignore 'lost=1', where object is outside of frame
    boxes_this_ID = [b for b in boxes if b['objID'] == objID and b['lost'] == 0] 
    first_frame = boxes_this_ID[0]['frameID']
    return first_frame

def get_unique_boxes(boxes):
    box_IDs = [b['objID'] for b in boxes]
    box_IDs = list(set(box_IDs)) #unique IDs
    return box_IDs

#@param unique_box_IDs = list of bbox IDs (deduplicated)
def get_first_frames(boxes):
    unique_box_IDs = get_unique_boxes(boxes)    
    max_box_ID = max(unique_box_IDs)
    first_frames = [0]*(max_box_ID+1) #one entry per unique box ID (ok if some IDs are missing)

    for box_ID in unique_box_IDs:
        first_frames[box_ID] = get_first_frame(box_ID, boxes)

    return first_frames 

#using FFMPEG'd images (typically downsampled from orig video)
if __name__ == "__main__":

    boxF = 'boxes_bradley_univ_90min.txt' #from vatic
    fps = 1 #annotation frequency (only used if drawing on original video)
    imgDir = '/home/forrest/installers/vatic/public/frames/bradley_univ_90min' #vatic'd frames

    boxes = read_bboxes(boxF)
    frame_list = get_frame_ID_list(boxes)
    first_frames = get_first_frames(boxes) 
    print "got first frames per box"

    #0, 1, 2, ... 5400
    for frameID in frame_list[4000:5100:10]:

        subdir = frameID / 100 #int division
        #imgF = '/Users/forrest/computerVision/0.jpg' 
        imgF = imgDir + '/0/%d/%d.jpg' % ( subdir, frameID ) #vatic's wierd directory hierarchy

        #print imgF
        img = cv2.imread(imgF)
        my_boxes = [b for b in boxes if b['frameID'] == frameID]

        for b in my_boxes:
            first_frame = first_frames[ b['objID'] ]
            #first_frame = get_first_frame(b['objID'], boxes) #TODO: precompute?
            #print 'first frame: ', first_frame

            curr_second = float(frameID - first_frame) / fps
            curr_minute = int( curr_second / 60 )
            draw_timer(img, b, curr_minute)
            
            #draw_box(img, b) #TODO: need to return img or not?
            #TODO: annotate timer on each box

        cv2.namedWindow("preview")
        cv2.imshow("preview", img)
        cv2.waitKey(0) #you have to have the window in focus for it to listen (any key -> exit)



