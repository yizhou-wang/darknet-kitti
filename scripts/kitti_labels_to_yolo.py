from uwimg import *
from os import listdir
import time
import ast


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

#print(obj2index_table)
assert len(obj2index_table) == 9 and len(label2obj_table) == 32

print(obj2index_table)

label_path = "../bao_kitti_labels/"

files = [f for f in listdir(label_path)]
output_path = "../labels/"
output_file = None

output = None

for f in files:
    print(f) 
    label_file = label_path + f
    
    c = 0
    for line in open(label_file, "r").readlines()[1:]:
        
        attrs = line.strip("\r\n").strip(" ").replace('""','\'').split(",")
        
        #print(attrs, len(attrs))
        image_file_name = attrs[0][:-3] + 'txt'
        
        if output_file == None:
            output_file = image_file_name
            output = open(output_path + output_file, "a")
            #output.write("\n")
        elif output_file != image_file_name:
            output.close()
            output_file = image_file_name
            output = open(output_path + output_file, "a")
            #output.write("\n")
        
        if len(attrs) < 13:
            continue
        
        
        tmp = ",".join(attrs[7:]).replace('{', '').replace('}', '').replace('"', '')
        tmp = "{" + tmp + "}"
        
        dic = ast.literal_eval(tmp)
        assert len(dic) == 6
        
        top_left_x = float(dic['x'])        
        top_left_y = float(dic['y'])
        width = float(dic['width'])
        height = float(dic['height'])
        
        center_x = top_left_x + width / 2.0
        center_y = top_left_y + height / 2.0
        
        
        
        im = load_image("../JPEGImages/" + image_file_name[:-3] + "jpg")
        
        dw = 1.0 / im.w
        dh = 1.0 / im.h
        
        x = center_x * dw
        y = center_y * dh
        
        w = width * dw
        h = height * dh
        
        
        obj_typ = dic['object type'].strip("\n").strip(" ")
        if obj_typ not in label2obj_table:
            continue
        obj_ind = obj2index_table[label2obj_table[obj_typ]]
        
        output.write(str(obj_ind))
        
        output.write(" " + str(x))
        output.write(" " + str(y))
        output.write(" " + str(w))
        output.write(" " + str(h))
        output.write("\n")
        
        c += 1
        
        
        
        
