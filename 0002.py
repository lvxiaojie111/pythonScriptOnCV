#coding:utf-8
#
#author:lvjunjie
#time:2020-4-13-14:09
#function:从vox2012人体图片中crop出人体，
#
#
import xml.etree.ElementTree as ET
import os
import cv2 as  cv
#import tensorflow as tf
#从 xml文件中获取人体框坐标，
label_path='D:\\VOCdevkit\\VOC2012\\ljjAnnotations'
data_list=[]
src_pic_path=r"D:\VOCdevkit\VOC2012\JPEGImages"
dst_pic_path=r"D:\VOCdevkit\VOC2012\cropPeople"
for list1 in os.listdir(label_path):
    print(list1)
#     data_list.append(list)
# for xml_name in data_list:
    xml_path=os.path.join(label_path,list1)
    root = ET.parse(xml_path).getroot()

    # # 打印根节点的标签及属性字典
    # print(root.tag)
    # print(root.attrib)
    # # 获取子节点movie的标签及属性字典
    # for i in root:
    #     print(i.tag)
    #     print("********", i.attrib)
    objects = root.findall('object')
    for obj in objects:
        # difficult = obj.find('difficult').text.strip()
        # if (not use_difficult_bbox) and (int(difficult) == 1):
        #     continue
        # print(obj.)
        # obj.find("name")
        print(obj[0].tag)
        print(obj[0].text)
        if(obj[0].text=='person'):
            # print(obj[1].tag)
            # print(obj[1][0].text)
            bbox = obj.find('bndbox')
            print(bbox)
            # bbox=obj[1].text
            # print(bbox)
            #bbox = obj.find('bndbox')
            # class_ind = classes.index(obj.find('name').text.lower().strip())
            xmin = bbox.find('xmin').text.strip()
            xmax = bbox.find('xmax').text.strip()
            ymin = bbox.find('ymin').text.strip()
            ymax = bbox.find('ymax').text.strip()
            # annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, str(class_ind)])
            bnbox=list(map(int,[xmin,xmax,ymin,ymax]))
            print(xml_path)
            print(bnbox)
            picName=list1.split(".")[0]
            print(picName)
            src_pic_path1=os.path.join(src_pic_path,picName+".jpg")
            print(src_pic_path1)
            pic=cv.imread(src_pic_path1)
            # cv.imshow('src_img',pic)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            pic_crop=pic[int(ymin):int(ymax),int(xmin):int(xmax)]
            # cv.imshow("crop_img",pic_crop)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            dst_pic_path1=os.path.join(dst_pic_path,picName+'.jpg')
            print(dst_pic_path1)
            cv.imwrite(dst_pic_path1,pic_crop)
            print('从图片',dst_pic_path1,'中提取路径已经保存成功')
#