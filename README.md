臉部辨識系統
===========
 用python 的 face_recognition模組 去辨識兩張照片是否為同一個人
_____
環境
====
python3.6
步驟
======
python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf  
(這裡面包含dlib模組 還有 安裝dlib 需要的whl檔案)  

pip install face_recognition  

pip install opencv-python (會用到裡面的cv2套件)  


![image]()

參考資料
======
https://hjwang520.pixnet.net/blog/post/404096783-%E5%9C%A8anaconda%E6%88%90%E5%8A%9F%E5%AE%89%E8%A3%9Dopencv%E3%80%81dlib%E5%92%8Cface_recognition  
https://ithelp.ithome.com.tw/articles/10212669  
https://yanwei-liu.medium.com/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%B8%80-%E4%BD%BF%E7%94%A8open-cv%E8%BE%A8%E8%AD%98%E5%9C%96%E7%89%87%E5%8F%8A%E5%BD%B1%E7%89%87%E4%B8%AD%E7%9A%84%E4%BA%BA%E8%87%89-527ef48f3a86
