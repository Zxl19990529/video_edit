#####################################
# 2019.7.8
# by Xinliang Zhang
# example:  python vis_xml_bbox.py --ann_dir box/ --img_dir image/
#####################################
from PIL import Image,ImageDraw
import os
import numpy as  np 
import xml.etree.ElementTree as ET 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ann_dir',type=str,default='Annotations',help="Direction to annotation files.")
parser.add_argument('--img_dir',type=str,default='JPEGImages',help='Direction to JPEGImage files.')
parser.add_argument('--save_dir',type=str,default='visualized',help='Direction to save the visualized images.')

args = parser.parse_args()
save_dir = args.save_dir
ann_dir = args.ann_dir
img_dir = args.img_dir
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
def get_bbox(tree):
    root = tree.getroot()
    result = []
    for child in root:
        if child.tag == 'object':
            name = ''
            pt = []
            for subchild in child:
                if subchild.tag == 'name':
                    name = subchild.text
                    # print(name)# holothurian
                if subchild.tag == 'bndbox':
                    for subsub_child in subchild:
                        pt.append(int(subsub_child.text))
            # print(pt)# [642, 412, 757, 524]  [x_min,y_min,x_max,y_max]
            result.append([name,pt])
        else:
            continue
    return result

count = 0
for filename in os.listdir(ann_dir):
    amount = len(os.listdir(ann_dir))
    base_name = filename.split('.')[0]
    xml_file = os.path.join(ann_dir,filename)
    tree = ET.parse(xml_file)
    result = get_bbox(tree)
    # print(result)
    img = os.path.join(img_dir,base_name+'.jpg')
    img = Image.open(img)
    # img.show()
    # break
    draw = ImageDraw.Draw(img)
    for target in result:
        text = target[0]
        pt = target[1]
        x1,y1,x2,y2 = pt[0],pt[1],pt[2],pt[3]
        # draw.rectangle((x1,y1,x2,y2))
        # 增宽线条宽度
        draw.rectangle((x1,y1,x2,y2), width=2)   # width=3时 比较粗
        draw.text((x1,y1),text)
    img.save(os.path.join(save_dir,base_name+'.jpg'))
    count+=1
    print(os.path.join(save_dir,base_name+'.jpg'),"\t %d/%d"%(count,amount))

# python vis_xml_bbox.py --ann_dir ann_horizontal --img_dir img_horizontal --save_dir h
# python vis_xml_bbox.py --ann_dir ann_vertical/ --img_dir img_vertical/ --save_dir v
    
# python vis_xml_bbox.py --ann_dir data/dataset_5543/train_5543/box/  --img_dir data/dataset_5543/train_5543/image/ --save_dir data/dataset_5543/visual_train_5543/
#  python code_self/vis_xml_bbox.py --ann_dir data/dataset_5543/test_bbox_5543/  --img_dir data/dataset_5543/test_5543/ --save_dir visual_test_xml_data/
