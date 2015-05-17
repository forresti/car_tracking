
#FIXME: currently need to run this in the 'vatic' folder (else get "api key not loaded error) ... why?

#FIXME: 'turkic extract' crashes below 5fps

input_video_dir=~/millennium_nscratch/forresti/vatic_videos/
input_video=$input_video_dir/bradley_univ_Thu_14_May_2015__06_00_01.mp4
input_frame_dir=$input_video_dir/bradley_univ_Thu_14_May_2015__06_00_01_frames_1fps
job_name=bradley_univ_90min


#STEP 1: prepare video and create vatic task
mkdir $input_frame_dir
turkic extract $input_video $input_frame_dir --fps 1

turkic load $job_name $input_frame_dir Car \
--blow-radius 1 \
--length 5400 \ #5400 frames (90min @ 1 fps)

#possibly needed:
turkic publish --offline
turkic find --id $job_name #e.g. https://distill.cs.berkeley.edu?id=136&hitId=offline

#STEP 2: NOW YOU DO THE ANNOTATION

#STEP 3: save bounding boxes that you annotated
turkic dump $job_name -o boxes_${job_name}.txt  #you may need to cp this from vatic dir to demo dir


#TODO: separate script to...
#- load bboxes into opencv
#- annotate video in opencv (bboxes and timers)

