import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# ==============================
# LOAD DATASET
# ==============================

path = 'dataset'
images = []
classNames = []

# Only load image files
myList = [f for f in os.listdir(path) if f.endswith(('.jpg','.jpeg','.png'))]
print("Images Found:", myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    else:
        print(f"Error loading image {cl}")

# ==============================
# ENCODING FUNCTION
# ==============================

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if len(encodes) > 0:
            encodeList.append(encodes[0])
        else:
            print("Warning: Face not detected in one image")
    return encodeList

# ==============================
# ATTENDANCE FUNCTION
# ==============================

def markAttendance(name):
    with open('attendance.csv', 'a+') as f:
        f.seek(0)
        dataList = f.readlines()
        nameList = []

        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%d-%m-%Y %H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            print(f"{name} Attendance Marked at {dtString}")

# ==============================
# START ENCODING
# ==============================

print("Encoding Faces...")
encodeListKnown = findEncodings(images)
print("Encoding Complete")

# ==============================
# START CAMERA
# ==============================

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Camera Error")
        break

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):

        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

        # Threshold control
        if matches[matchIndex] and faceDis[matchIndex] < 0.50:

            name = classNames[matchIndex].upper()
            confidence = round((1 - faceDis[matchIndex]) * 100, 2)

            # Green Box
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)

            cv2.putText(img,f'{name}  {confidence}%',
                        (x1+6,y2-6),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,(255,255,255),2)

            markAttendance(name)

        else:
            # Red Box for Unknown
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),3)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)

            cv2.putText(img,"UNKNOWN",
                        (x1+6,y2-6),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,(255,255,255),2)

    cv2.imshow('AI Smart Attendance System', img)

    # Press ENTER to exit
    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()
