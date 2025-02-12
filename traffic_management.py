from ultralytics import YOLO
import cv2
import easyocr
import matplotlib.pyplot as plt

def control_traffic(vehicle_count):
    """Determine traffic signal color based on vehicle count."""
    if vehicle_count > 50:
        return "Green"  # go
    elif vehicle_count > 25:
        return "Yellow"  # wait
    else:
        return "Red"  # stop


model = YOLO("yolov8n.pt")



video_path = "traffic_video.mp4"
cap = cv2.VideoCapture(video_path)



frame_count = 0  # Counter

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

            # extract vehicle region
            vehicle_roi = frame[y1:y2, x1:x2]

            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # green box

    # display count & signal
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
