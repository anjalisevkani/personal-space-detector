import cv2
import math

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

# Distance threshold
DISTANCE_THRESHOLD = 120

print("Press ESC to exit...")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Resize
    frame = cv2.resize(frame, (800, 600))

    # Detect People
    boxes, _ = hog.detectMultiScale(frame, winStride=(8, 8))

    centers = []

    # Draw bounding boxes and get centers
    for (x, y, w, h) in boxes:
        cx = x + w // 2
        cy = y + h // 2
        centers.append((cx, cy))

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw center point
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

    # Check Distance Between People
    intrusion_detected = False

    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):

            x1, y1 = centers[i]
            x2, y2 = centers[j]

            # Euclidean distance
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Draw line between people
            if distance < DISTANCE_THRESHOLD:
                intrusion_detected = True
                color = (0, 0, 255)  
                label = "Too Close!"
            else:
                color = (0, 255, 0)

            cv2.line(frame, (x1, y1), (x2, y2), color, 2)

            # Display distance
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2

            cv2.putText(frame, f"{int(distance)}", (mid_x, mid_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)


    # Warning
    if intrusion_detected:
        cv2.putText(frame, "PERSONAL SPACE VIOLATION!",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3)

    else:
        cv2.putText(frame, "Safe Distance",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2)


    # Show Output
    cv2.imshow("Personal Space Detector", frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()