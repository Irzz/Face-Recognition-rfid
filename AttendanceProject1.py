<<<<<<< HEAD
import cv2
import numpy as np
import face_recognition
import os
import pandas as pd

# meminta rfid pasien
# rfid_pasien = int(input("Tempelkan kartu rfid anda : "))

# mengambil data spreadsheet
# df = pd.read_csv("https://docs.google.com/spreadsheets/d/1ja8NXuQgRO7XPEB9WxfFf48ESaRzjgI335N4687kWFA/export?format=csv")
# tabel_data = df[(df.Id_rfid == rfid_pasien)]
# tabel_data_str = str(tabel_data)

# rfid_pasien_str = str(rfid_pasien)

# mengambil data wajah
path = 'ImagesAttendance'
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
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
            
            # matching = rfid_pasien_str + name == tabel_data_str
            # matching_str = str(matching)
            # print(type(matching_str))

            file = open("data.txt",'w')

            file.write(name)
            file.close

    cv2.imshow('webcam', img)
    cv2.waitKey(1)




=======
import cv2
import numpy as np
import face_recognition
import os
import pandas as pd

# meminta rfid pasien
# rfid_pasien = int(input("Tempelkan kartu rfid anda : "))

# mengambil data spreadsheet
# df = pd.read_csv("https://docs.google.com/spreadsheets/d/1ja8NXuQgRO7XPEB9WxfFf48ESaRzjgI335N4687kWFA/export?format=csv")
# tabel_data = df[(df.Id_rfid == rfid_pasien)]
# tabel_data_str = str(tabel_data)

# rfid_pasien_str = str(rfid_pasien)

# mengambil data wajah
path = 'ImagesAttendance'
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
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
            
            # matching = rfid_pasien_str + name == tabel_data_str
            # matching_str = str(matching)
            # print(type(matching_str))

            file = open("data.txt",'w')

            file.write(name)
            file.close

    cv2.imshow('webcam', img)
    cv2.waitKey(1)




>>>>>>> a6274af809e02f83c8076c2a721021cc83108b41
