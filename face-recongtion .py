import face_recognition

#將對照的圖片放入數組(如果是電腦上的路徑要用絕對路徑，而且斜線用雙斜線,不然會錯誤)
chen_image = face_recognition.load_image_file("D:\\Desktop\\picture\\me.jpg")
#選擇辨認的圖片
unknown_image = face_recognition.load_image_file("D:\\Desktop\\picture\\me-now.jpg")

#獲取每張臉部圖片中的臉部编碼
#由於每个圖像中可能有多個面，所以只返回一個编碼列表。
#因為每張圖片只有一張臉，所以只索取每個圖像中的第一個编碼，所以我取索引0。
chen_face_encoding = face_recognition.face_encodings(chen_image)[0]
print("chen_face_encoding:{}".format(chen_face_encoding))
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
print("unknown_face_encoding :{}".format(unknown_face_encoding))

known_faces = [
    chen_face_encoding
]
#經過每張臉的比對，顯示true 或false
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("result :{}".format(results))
