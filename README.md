臉部辨識系統
===========

 用python 的 face_recognition模組 去辨識兩張照片是否為同一個人  
 
環境
====

python 3.6

步驟
======
python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf  
(這裡面包含dlib模組 還有 安裝dlib 需要的whl檔案)  

pip install face_recognition  

pip install opencv-python (會用到裡面的cv2套件)  

程式碼
======

先偵測預設照片(face_detection.py)

![image](https://github.com/timmy10289/face_recognition/blob/main/detect.jpg)  
最後把要對照得照片做臉部圖像的編碼比對(face_recognition.py)   

![image](https://github.com/timmy10289/face_recognition/blob/main/recognition.jpg)  
參考資料
======
https://hjwang520.pixnet.net/blog/post/404096783-%E5%9C%A8anaconda%E6%88%90%E5%8A%9F%E5%AE%89%E8%A3%9Dopencv%E3%80%81dlib%E5%92%8Cface_recognition  
https://www.itread01.com/content/1543785318.html
