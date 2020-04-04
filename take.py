import cv2
import os
cap = cv2.VideoCapture(0)#创建一个 VideoCapture 对象
ret_flag, Vshow = cap.read()
path = os.getcwd()
savename  = "007.jpg"
savepath = path + "/" + savename
cv2.imwrite(savepath, Vshow)
cap.release() #释放摄像头
