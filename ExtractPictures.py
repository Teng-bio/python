#pip install opencv
import cv2
timeF = 1  # 视频帧计数间隔频率
vc = cv2.VideoCapture('./DC_E-cadGFP_1min_01.avi')  # 读入视频文件，命名cv
n = 1  # 计数
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
     
i = 0
while rval:  # 循环读取视频帧  
    if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imwrite('./Images/image{}.png'.format(i), frame) # 存储为图像
    n = n + 1
    #cv2.waitKey(1)
    rval, frame = vc.read()

vc.release()
