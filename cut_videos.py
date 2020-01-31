import cv2 
import os
from multiprocessing import Pool
from tqdm import tqdm
videos_to_cut = 'videos_to_cut'
videonames = sorted(os.listdir(videos_to_cut))

def cut_video(videoname,task_id):
    video_path = os.path.join(videos_to_cut,videoname)
    save_folder = video_path.split('.mp4')[0]
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    pbar = tqdm(range(frame_count),position=task_id)
    count = 0
    while True:
        ret,frame = video.read()
        pbar.update(1)
        count += 1
        if not ret:
            break
        save_name = str(count)+'.jpg'
        save_path = os.path.join(save_folder,save_name)
        cv2.imwrite(save_path,frame)

if __name__ == "__main__":
    num_workers = 8
    pol = Pool(num_workers)
    for i,videoname in enumerate(videonames):
        # print(videoname)
        pol.apply_async(cut_video,(videoname,i))
    pol.close()
    pol.join()
    print('END !')

