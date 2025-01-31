import os
from ultralytics import YOLO
import cv2

# Define the directories and paths for WSL
VIDEOS_DIR = '/mnt/c/Users/hardi/Downloads/project/' 
video_path = os.path.join(VIDEOS_DIR, 'test (cars vedio).mp4')
video_path_out = '{}_out.mp4'.format(video_path)
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Path to your best.pt or last.pt model (adjust depending on which model you want to use)
model_path = '/mnt/c/Users/hardi/Downloads/project/models/license_plate_detector/best.pt'


# Load a custom YOLO model
model = YOLO(model_path)

threshold = 0.5

while ret:
    # Run the YOLO model on the frame
    results = model(frame)[0]

    # Iterate over detected objects and draw bounding boxes
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            # Draw the bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            # Put the class name above the bounding box
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Write the processed frame to the output video
    out.write(frame)

    # Read the next frame
    ret, frame = cap.read()

# Release resources
cap.release()
out.release()

print(f"Video saved to {video_path_out}")
