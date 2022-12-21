import cv2
import numpy as np
import face_recognition

# import image and convert to rgb
imgRobert = face_recognition.load_image_file('ImagesBasic/Robert Downey Jr.jpg')
imgRobert = cv2.cvtColor(imgRobert, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Chris Hemsworth.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Detect faces in the image
faceLoc = face_recognition.face_locations(imgRobert)[0]
encodeRobert = face_recognition.face_encodings(imgRobert)[0]
cv2.rectangle(imgRobert, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255),2)

# Find all the faces and face encodings in the image
results = face_recognition.compare_faces([encodeRobert], encodeTest)
faceDis = face_recognition.face_distance([encodeRobert], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)})', (50,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# Find
cv2.imshow('Robert Downey Jr', imgRobert)
cv2.imshow('Robert Test', imgTest)
cv2.waitKey(0)
