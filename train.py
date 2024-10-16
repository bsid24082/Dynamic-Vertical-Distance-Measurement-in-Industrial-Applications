from ultralytics import YOLO

# Load the YOLO model (nano version for faster training, replace with 'yolov8n-seg.pt' if you're working with segmentation)
model = YOLO('yolov8n.pt')  # You can use yolov8l.pt or yolov8x.pt for higher accuracy but slower training

# Train the model on your dataset
model.train(
    data='/Users/bsid24082/Documents/IIQ/Honey3/ honey_dataset.yaml',  # Path to the data YAML file (defining train and val)
    imgsz=640,  # Image size (YOLO default is 640x640)
    epochs=50,  # Number of epochs for training
    batch=16,   # Batch size
    # name='honey_jar_detection'  # Name of the experiment
)