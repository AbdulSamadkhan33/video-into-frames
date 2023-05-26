import os
import sys
import time
import cv2

def get_video_names():
   temp_files = os.listdir("folder that contian video")
   files = []
   for file in temp_files:
     if not os.path.isfile(file):
      
      files.append(file)

   return files

def extract_frames(video):
   current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
   folder_name = os.path.join(current_dir, video.split(".")[0])
   os.makedirs(folder_name, exist_ok= True)

   cam =cv2.VideoCapture(os.path.join("folder that contain video", video))
   
   while(True):
      
       ret, frame = cam.read()
       if ret:
          name = str(int(time.time())) + "jpj"
          video_dir = os.path.join(folder_name, name)
          print("creating folder" + video_dir)
          cv2.imwrite(video_dir, frame)
       else:
          break
       cam.release()
       cv2.destroyAllWindows()
    

for video in get_video_names():
   extract_frames(video)

for path in get_video_names():
   folder_name = os.path.join(".", path.split(".")[0])
      
