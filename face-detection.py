# 用pil 模組 (python的影像處理套件)
from PIL import Image
import face_recognition
import cv2
#使用time 套件 控制照片出現的時間
import time

t=time.time()
#把你要的照片放進去數組(如果是電腦上的路徑要用絕對路徑，而且斜線用雙斜線,不然會錯誤)
image = face_recognition.load_image_file("D:\\Desktop\\picture\\me.jpg")
frame=cv2.imread("D:\\Desktop\\picture\\me.jpg")

face_locations = face_recognition.face_locations(image)



# print出總共偵測了幾張人臉
print("I found {} face(s) in this photograph.".format(len(face_locations)))

# 用循環print出每個人臉位置
for face_location in face_locations:

        # 每张脸的位置信息
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# 指定人脸的位置信息，然后顯示人臉圖片
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
cv2.imshow('tuxiang',frame) #用opencv 展示圖片框架
cv2.waitKey(1)  #刷新界面 不然會呈现灰色
print('运行时间{}'.format(time.time()-t))
time.sleep(5)  #暂停五秒  展示圖片