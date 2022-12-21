import cv2
import numpy as np
import face_recognition
import os
import pandas as pd

# Membaca rfid pasien dari file txts
f = open('test.txt')
txt = f.read()
f.close()
rfid_pasien = int(txt)

# mengambil data spreadsheet
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1ja8NXuQgRO7XPEB9WxfFf48ESaRzjgI335N4687kWFA/export?format=csv")

# mengambil data wajah
path = 'ImagesRecognition'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEndcodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEndcodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    succeed, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS  = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex]
            # print(name)
            tabel_data1 = df[(df.Id_rfid == rfid_pasien)]
            tabel_data2 = df[(df.Nama_pasien == name)]

            tabel_data1_str = str(tabel_data1)
            tabel_data2_str = str(tabel_data2)

            file = open("data.txt",'w')

            if (tabel_data1_str != tabel_data2_str):
                file.write("False")
                file.close
            else :
                file.write("True")
                file.close

    cv2.imshow('webcam', img)
    cv2.waitKey(1)