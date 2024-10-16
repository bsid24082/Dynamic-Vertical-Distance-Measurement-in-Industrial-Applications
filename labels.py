import os
import json

# Paths to annotations and images
json_dir = '/Users/bsid24082/Documents/IIQ/Honey3/json_annotations'  # JSON annotations folder
output_dir = '/Users/bsid24082/Documents/IIQ/Honey3/yolo_labels'  # YOLO labels output folder
image_dir = '/Users/bsid24082/Documents/IIQ/Honey3/images'  # Corresponding image folder

# YOLO class labels (Add your labels here in correct order)
class_labels = ['jar', 'full', 'partially_filled']

# Function to convert bounding box coordinates from polygon points to YOLO format
def convert_to_yolo(image_width, image_height, points):
    x_min = min([p[0] for p in points])
    y_min = min([p[1] for p in points])
    x_max = max([p[0] for p in points])
    y_max = max([p[1] for p in points])

    # YOLO expects bbox as (center_x, center_y, width, height)
    bbox_width = (x_max - x_min) / image_width
    bbox_height = (y_max - y_min) / image_height
    center_x = (x_min + x_max) / (2 * image_width)
    center_y = (y_min + y_max) / (2 * image_height)
    
    return center_x, center_y, bbox_width, bbox_height

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each JSON file
for json_file in os.listdir(json_dir):
    if json_file.endswith('.json'):
        json_path = os.path.join(json_dir, json_file)
        
        # Load the JSON file
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Get corresponding image file path
        image_file = os.path.join(image_dir, data['imagePath'])
        # Ensure the image exists
        if not os.path.exists(image_file):
            continue
        
        # Read image dimensions
        image_width = data['imageWidth']
        image_height = data['imageHeight']
        
        # Prepare YOLO label file
        yolo_label_file = os.path.join(output_dir, os.path.splitext(json_file)[0] + '.txt')
        
        with open(yolo_label_file, 'w') as yolo_file:
            for shape in data['shapes']:
                label = shape['label']
                if label in class_labels:
                    class_id = class_labels.index(label)
                    points = shape['points']
                    yolo_bbox = convert_to_yolo(image_width, image_height, points)
                    yolo_file.write(f"{class_id} {' '.join(map(str, yolo_bbox))}\n")