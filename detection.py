import cv2
import numpy as np
from ultralytics import YOLO

def run_yolo():
    cap = cv2.VideoCapture(0)  # Open webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    model = YOLO("best.pt")  # Load your trained YOLO model

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        results = model(frame, conf=0.6, classes=0)  # Detect objects (modify classes if needed)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0].to('cpu').detach().numpy().copy()  # Get bounding box
                c = box.cls

                # Draw bounding box & label
                cv2.rectangle(frame, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0, 0, 255), 2)
                cv2.putText(frame, model.names[int(c)], (int(b[0]), int(b[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Ball Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_yolo()