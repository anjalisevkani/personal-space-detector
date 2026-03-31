import cv2
import numpy as np
import math

# Loading the face detection model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# For opening the webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

# Setting the window
cv2.namedWindow("Personal Space Detector", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Personal Space Detector", 640, 480)

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    face_centers = []

    # First drawing the rectangles and then finding centres
    for (x, y, w, h) in faces:
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        face_centers.append((cx, cy))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    # Checking the distance between the faces
    status = "Safe Distance"

    if len(face_centers) >= 2:
        for i in range(len(face_centers)):
            for j in range(i + 1, len(face_centers)):
                distance_value = calculate_distance(face_centers[i], face_centers[j])

                if distance_value < 250:
                    status = "Too Close!"
                    cv2.line(frame, face_centers[i], face_centers[j], (0, 0, 255), 2)
                else:
                    cv2.line(frame, face_centers[i], face_centers[j], (0, 255, 0), 2)
    else:
        status = "Only one person"

    # Displaying the status
    color = (0, 255, 0) if status == "Safe Distance" else (0, 0, 255)

    cv2.putText(frame, status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                3)

    cv2.imshow("Personal Space Detector", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()