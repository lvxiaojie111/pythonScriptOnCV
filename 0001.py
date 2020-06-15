#
#
#author:lvjunjie
#time:2020-4-12-15:22
#function:从voc2012数据集中挑选出类别为人的数据集集标注文件
#
#
import os
import re
import shutil
#原始图片存放路径
src_jpg_path=""
#原始标注文件存放路径
src_xml_path=""

#目标图片存放路径
dst_jpg_path=""
#目标标注文件存放路径
dst_xml_path=""
#txt文件路径
txt_file_dir=r"D:\VOCdevkit\VOC2012\ImageSets\Main\person_trainval.txt"
f=open(txt_file_dir,'r',encoding='utf-8')
data=f.readlines()
data_list=[]
for i in data:
    print(i,type(i))
    i=i.strip()#去掉收尾空格、换行
    # \W匹配任何非单词字符
    #https://blog.csdn.net/qq_31672701/article/details/100711585
    #i=re.split('\W+',i)#转化为列表数据
    #i=i.strip().replace("  ",',').split(",")
    i=re.sub(" +",' ',i)#将连续多个空格替换为一个空格功能
    i=i.strip().split(" ")#以单个空格为基准，把每一行记录转化为列表
    print(i,type(i))
    # i=list(map(int,i))
    data_list.append(i)
print("读取的数据长度为{}".format(len(data_list)))
print("读取的数据为：",data_list)

#将每一行字符串记录转化整形记录
# data_strTo_int_list=[]
# for s in data_list:
#     i=list(map(int,s))
#     print(i)
#     data_strTo_int_list.append(i)
# print("读取的数据长度为{}".format(len(data_strTo_int_list)))
# print("读取的数据为：",data_strTo_int_list)

#获取标注为1的正样本数据集
pos_data_list=[]
for i in range(len(data_list)):
    if data_list[i][1]=='1':
        pos_data_list.append(data_list[i])
print("正样本人体的数据长度为{0}".format(len(pos_data_list)))
print("正样本的数据为： ",pos_data_list)

#把含有正样本数据的图片拷贝到新的文件夹
#把含有正样本数据的标记xml文件拷贝到新的文件夹
src_data_dir=r'D:\VOCdevkit\VOC2012\JPEGImages'
dst_data_dir=r"D:\VOCdevkit\VOC2012\ljjjpeg"
src_xml_dir=r'D:\VOCdevkit\VOC2012\Annotations'
dst_xml_dir=r"D:\VOCdevkit\VOC2012\ljjAnnotations"
if os.path.exists(dst_data_dir):
    #os.remove(dst_data_dir)
    shutil.rmtree(dst_data_dir)
    os.makedirs(dst_data_dir)
    print("目标jpg文件已经移除,并且创建了新的文件")
else:
    os.makedirs(dst_data_dir)
    print("目标jpg文件已成功创建")
if os.path.exists(dst_xml_dir):
    #os.remove(dst_data_dir)
    shutil.rmtree(dst_xml_dir)
    os.makedirs(dst_xml_dir)
    print("目标xml文件已经移除,并且创建了新的文件")
else:
    os.makedirs(dst_xml_dir)
    print("目标xml文件已成功创建")
#拷贝dst文件
remainder=len(pos_data_list)
for i in pos_data_list:
    jpg_name=str(i[0])+".jpg"
    src_jpg_dir=os.path.join(src_data_dir,jpg_name)
    #print(src_jpg_dir)
    #dst_jpg_dir=os.path.join(dst_data_dir,jpg_name)
    shutil.copy2(src_jpg_dir,dst_data_dir)
    remainder-=1
    print("还有{}个jpg文件待拷贝".format(remainder))
#拷贝xml文件
remainder=len(pos_data_list)
for i in pos_data_list:
    xml_name=str(i[0])+".xml"
    src_jpg_dir=os.path.join(src_xml_dir,xml_name)
    #print(src_jpg_dir)
    #dst_jpg_dir=os.path.join(dst_data_dir,jpg_name)
    shutil.copy2(src_jpg_dir,dst_xml_dir)
    remainder-=1
    print("还有{}个xml文件待拷贝".format(remainder))

