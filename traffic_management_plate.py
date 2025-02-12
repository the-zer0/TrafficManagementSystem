from ultralytics import YOLO
import cv2
import easyocr
import matplotlib.pyplot as plt

def control_traffic(vehicle_count):
    """Determine traffic signal color based on vehicle count."""
    if vehicle_count > 10:
        return "Green"  # go
    elif vehicle_count > 5:
        return "Yellow"  #wait
    else:
        return "Red"  # stop

# YOLO model
model = YOLO("yolov8n.pt")

# EasyOCR number plate eader
reader = easyocr.Reader(['en'])

video_path = "traffic_video.mp4"  
cap = cv2.VideoCapture(video_path)

# cap = cv2.VideoCapture(0)  # Open laptop webcam

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


frame_count = 0  # counter

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break 

    results = model(frame)

    vehicle_count = sum(len(result.boxes) for result in results)
    signal = control_traffic(vehicle_count)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            vehicle_roi = frame[y1:y2, x1:x2]

            gray_vehicle = cv2.cvtColor(vehicle_roi, cv2.COLOR_BGR2GRAY)

            number_plate_text = reader.readtext(gray_vehicle, detail=0)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box

            # Display detected number plate text in GREEN
            if number_plate_text:
                plate_text = number_plate_text[0]
                cv2.putText(frame, f'Plate: {plate_text}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2) 

    # Display count & signal
    cv2.putText(frame, f'Vehicles: {vehicle_count}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f'Signal: {signal}', (50, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis("off")  
    plt.show(block=False) 
    plt.pause(0.01)  
    plt.clf()  

    cv2.imwrite(f"output_frame_{frame_count}.jpg", frame)
    frame_count += 1

cap.release()
plt.close() 