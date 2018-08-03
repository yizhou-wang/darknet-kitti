from uwimg import *
from os import listdir
import time
import ast
import sys

obj2index_table = dict()
label2obj_table = dict()


for line in open("names.txt").readlines():
    tmp = line.strip("\n").split(":")
    if len(tmp) < 2:
        continue
    
    obj = tmp[0].strip(" ")
    label = tmp[1].strip(" ")
    
    if obj not in obj2index_table:
        size = len(obj2index_table)
        obj2index_table[obj] = size
    
    label2obj_table[label] = obj

print(obj2index_table)
time.sleep(5)

assert len(obj2index_table) == 9 and len(label2obj_table) == 32

kitti_origi_label_path = "../label_2/"

files = [f for f in listdir(kitti_origi_label_path)]

for f in files:
    label_file = kitti_origi_label_path + f
    
    output = open("../labels/" + f, 'w')
    
    im = load_image("../JPEGImages/" + f[:-3] + "jpg")
        
    dw = 1.0 / im.w
    dh = 1.0 / im.h
    
    for line in open(label_file, "r").readlines():
        tmp = line.strip("\n").strip(" ").split(" ")
        if tmp[0] == "Misc" or tmp[0] == "DontCare":
            continue
        
        obj_ind = obj2index_table[label2obj_table[tmp[0]]]
        
        top_left_x = float(tmp[4])       
        top_left_y = float(tmp[5])
        bottom_right_x = float(tmp[6])
        bottom_right_y = float(tmp[7])
        
        assert top_left_x < bottom_right_x and top_left_y < bottom_right_y
        
        width = bottom_right_x - top_left_x
        height = bottom_right_y - top_left_y
        
        center_x = top_left_x + (width / 2)
        center_y = top_left_y + (height / 2)
        
        x = center_x * dw
        y = center_y * dh
        
        w = width * dw
        h = height * dh
        
        output.write(str(obj_ind))
        
        output.write(" " + str(x))
        output.write(" " + str(y))
        output.write(" " + str(w))
        output.write(" " + str(h))
        output.write("\n")
        
    output.close()
        
        
