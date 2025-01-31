from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="/home/hardik/project/automatic-number-plate-recognition-python-yolov8/config.yaml", epochs=1)  # train the model