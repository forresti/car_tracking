
#FIXME: currently need to run this in the 'vatic' folder (else get "api key not loaded error) ... why?

#FIXME: 'turkic extract' crashes below 5fps

input_video_dir=~/millennium_nscratch/forresti/vatic_videos/
input_video=$input_video_dir/bradley_univ_Thu_14_May_2015__06_00_01.mp4
input_frame_dir=$input_video_dir/bradley_univ_Thu_14_May_2015__06_00_01_frames_5fps
job_name=bradley_univ

mkdir $input_frame_dir
turkic extract $input_video $input_frame_dir --fps 5

turkic load $input_video Car \
--blow-radius 1 \
--train-with $job_name \
--duration 2700 \ #2700 frames (90min @ 0.5 fps)

#--title "Label the cars in this video (15sec of video). Per-object bonus."
#--description "Draw boxes around the cars, trucks, and vehicles in this video. When the cars move, you move the boxes. See 'show instructions' in the HIT. Feel free to email us with questions."
#--lifetime 604800 
#--keywords "video, tagging, annotation, cars"
#--cost 0.05    
#--per-object-bonus 0.02 
#--completion-bonus 0.1  


#TODO: separate script to...
#- dump bboxes
#- load bboxes into opencv
#- annotate video in opencv (bboxes and timers)

