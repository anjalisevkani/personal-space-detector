import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

boxes, _ = hog.detectMultiScale(frame)
for (x, y, w, h) in boxes:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)