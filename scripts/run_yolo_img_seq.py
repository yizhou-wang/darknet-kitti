import os
import glob

img_list = glob.glob("/mnt/disk1/kitti-dataset/raw_data/2011_09_26/2011_09_26_drive_0001_sync/image_02/data/*.png")
img_list = sorted(img_list)

commands = ['./darknet detector test cfg/coco.data cfg/yolov2.cfg yolov2.weights ']
commands.extend(img_list)  
print commands

os.system('\n'.join(commands))
