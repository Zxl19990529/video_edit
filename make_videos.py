import cv2
import os
from multiprocessing import Process,Pool
from tqdm import tqdm
import time

def make_video(imgs_folder, fps, size, task_id):
    folder_name = imgs_folder.split('/')[-1]
    imgs = sorted(os.listdir(imgs_folder))
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = fps
    size = size
    save_dir = os.path.join(imgs_folder+'.mp4')
    writer = cv2.VideoWriter(save_dir, fourcc, fps, size)
    log = 'processing '+imgs_folder+' task id : %d' % task_id
    f = open('log.txt', 'a')
    f.writelines(log+'\n')
    f.close()
    pbar = tqdm(imgs, position=task_id)
    for i, img in enumerate(imgs):
        pbar.update(1)
        img_path = os.path.join(imgs_folder, str(i)+'.jpg')
        img_file = cv2.imread(img_path)
        writer.write(img_file)
        # print(img_path)
    f = open('log.txt', 'a')
    f.writelines(imgs_folder+'task id : %d ' % task_id + ' completed !\n')
    f.close()
    pbar.close()
    folders.remove(folder_name)

num_workers = 6# 定义了用几个核
videos_imgs_dir = 'videos_to_make'
folders = sorted(os.listdir(videos_imgs_dir))

if __name__ == "__main__":
    pol = Pool(num_workers)
    for i,folder in enumerate(folders):
        current_video = os.path.join(videos_imgs_dir,folder)
        pol.apply_async(make_video,(current_video,20,(1920,1080),i))# pol.apply_async(函数名，（参数1，参数2，……）)
    pol.close()
    pol.join()
