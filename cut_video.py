import cv2 
import os
from multiprocessing import process

video_path = '2019-05-15_17.45.28.mp4'
basename = video_path.split('.mp4')[0]
save_folder = basename
# save_folder = 'dataset/input/img'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

video = cv2.VideoCapture(video_path)
count = 0
while True:
    ret,frame = video.read()
    if not ret:
        print('END')
        break
    img_name = os.path.join(save_folder,str(count)+'.jpg')
    cv2.imwrite(img_name,frame)
    print(img_name)
    count +=1