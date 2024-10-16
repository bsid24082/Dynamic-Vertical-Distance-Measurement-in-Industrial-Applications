import cv2
import os

# Paths to the images and label directories
image_dir = '/Users/bsid24082/Documents/IIQ/Honey3/images/train'  # or val
label_dir = '/Users/bsid24082/Documents/IIQ/Honey3/yolo_labels/train'  # or val

# Class names
class_names = ['Jar', 'partially_filled', 'full']

# Function to draw bounding boxes on images
def visualize_labels(image_path, label_path):
    # Read the image
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    
    # Read the corresponding label file
    with open(label_path, 'r') as f:
        for line in f.readlines():
            # YOLO format: class_id, x_center, y_center, width, height (all normalized)
            class_id, x_center, y_center, box_width, box_height = map(float, line.strip().split())

            # Convert back to pixel values
            x_center *= width
            y_center *= height
            box_width *= width
            box_height *= height

            # Convert to top-left corner coordinates
            x1 = int(x_center - (box_width / 2))
            y1 = int(y_center - (box_height / 2))
            x2 = int(x_center + (box_width / 2))
            y2 = int(y_center + (box_height / 2))

            # Draw the bounding box
            color = (0, 255, 0)  # Green color for boxes
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

            # Put the label on the box
            label = class_names[int(class_id)]
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Display the image
    cv2.imshow('Labeled Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Loop over the images and labels
for image_file in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_file)
    label_file = image_file.replace('.jpg', '.txt')  # Assuming YOLO label format
    label_path = os.path.join(label_dir, label_file)

    if os.path.exists(label_path):
        visualize_labels(image_path, label_path)