import cv2
import os

input_path = 'videos_to_make/2019-05-11_06.31.53_track'
imgs = sorted(os.listdir(input_path))

fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 24
size = (1920,1080)
writer = cv2.VideoWriter('output.mp4',fourcc,fps,size)

for i,img in enumerate(imgs):
    img_path = os.path.join(input_path,str(i)+'_track.jpg')
    img_file = cv2.imread(img_path)
    writer.write(img_file)
    print(img_path)