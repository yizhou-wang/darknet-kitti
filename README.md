![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet for KITTI

This repository is forked from [pjreddie/darknet](https://github.com/pjreddie/darknet). 

## What's new for this repository? 

This version of darknet is modified to fit KITTI 2D object dataset. 

## Train YOLOv2 for KITTI ##

The detail of the revision is written at http://yizhouwang.net/blog/2018/07/29/train-yolov2-kitti/.

## Train YOLOv3 for KITTI ##

The detail of the revision is written at http://yizhouwang.net/blog/2018/08/05/train-yolov3-kitti/.

## Test image sequence using YOLO ##

New function `testseq` in darknet is written for testing image sequence. The file names of the image sequence should be listed in a `txt` file `<namelist.txt>`. To use `testseq`, run the following code in the terminal:
```
./darknet detector testseq cfg/kitti.data cfg/kitti.cfg <weights_file> <namelist.txt>
```
