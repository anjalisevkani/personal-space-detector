import cv2
import math

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    boxes, _ = hog.detectMultiScale(frame)
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    
    centers = []

    for (x, y, w, h) in boxes:
        cx = x + w//2
        cy = y + h//2
        centers.append((cx, cy))
    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            dist = math.sqrt(
                (centers[i][0] - centers[j][0])**2 +
                (centers[i][1] - centers[j][1])**2
            )

            if dist < 100:  # your threshold
                cv2.putText(frame, "Too Close!", (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


cap.release()
cv2.destroyAllWindows()



