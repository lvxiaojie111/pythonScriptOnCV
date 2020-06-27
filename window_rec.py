"""
python 屏幕录制改进版，无opencv黑框显示！
录制的视频没有声音
@ljj 2020/6/22_pynput
"""
from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from pynput import keyboard#可以全局监听键盘、鼠标事件
import threading
from threading import Timer
from datetime import datetime
flag=False  #停止标志位
list=["D:/VOCdevkit/VOC2012/",'C:/Users/Administrator/Desktop/']
rec_path=list[0]

def task():
    video_record()
def video_record():
    """
    屏幕录制！
    :return:
    """
    name = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #当前的时间
    p = ImageGrab.grab()  # 获得当前屏幕
    a, b = p.size  # 获得当前屏幕的大小
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
    video = cv2.VideoWriter(rec_path+'%s.avi'%name, fourcc, 10, (a, b))  # 输出文件命名为test.mp4,帧率为16，可以自己设置
    atime = datetime.now()
    while True:
        im = ImageGrab.grab()
        imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
        video.write(imm)
        btime = datetime.now()
        timeabs=(btime-atime).seconds
        if(timeabs>1800):#每隔30min重新保存一个文件夹
            name = datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # 当前的时间
            video = cv2.VideoWriter(rec_path + '%s.avi' % name, fourcc, 20, (a, b))  # 输出文件命名为test.mp4,帧率为16，可以自己设置
            atime = datetime.now()
        if flag:
            print("录制结束！")
            break
    video.release()
def on_press(key):
    """
    键盘监听事件！！！
    :param key:
    :return:
    """
    #print(key)
    global flag
    if key == keyboard.Key.esc:
        flag=True
        print("stop monitor！")
        return False  #返回False，键盘监听结束！
def timedTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(1, task, ()).start()

if __name__=='__main__':
    th=threading.Thread(target=video_record)
    th.start()
    # timedTask()
    # th=threading.Thread(target=timedTask)
    # th.start()
    # timedTask()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()