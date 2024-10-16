import os
import shutil

# Define paths
image_train_dir = '/Users/bsid24082/Documents/IIQ/Honey3/images/train'
image_val_dir = '/Users/bsid24082/Documents/IIQ/Honey3/images/val'
yolo_labels_dir = '/Users/bsid24082/Documents/IIQ/Honey3/yolo_labels'

# Create train and val label directories if they don't exist
yolo_labels_train_dir = os.path.join(yolo_labels_dir, 'train')
yolo_labels_val_dir = os.path.join(yolo_labels_dir, 'val')

os.makedirs(yolo_labels_train_dir, exist_ok=True)
os.makedirs(yolo_labels_val_dir, exist_ok=True)

# Get list of images in train and val directories
train_images = [f[:-4] for f in os.listdir(image_train_dir) if f.endswith('.jpg') or f.endswith('.png')]
val_images = [f[:-4] for f in os.listdir(image_val_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Split YOLO labels based on image lists
for label_file in os.listdir(yolo_labels_dir):
    if label_file.endswith('.txt'):
        base_name = label_file[:-4]  # Remove the .txt extension

        # Check if the label belongs to the train set
        if base_name in train_images:
            shutil.copy(os.path.join(yolo_labels_dir, label_file), yolo_labels_train_dir)
        # Check if the label belongs to the val set
        elif base_name in val_images:
            shutil.copy(os.path.join(yolo_labels_dir, label_file), yolo_labels_val_dir)

print("YOLO labels have been split into train and val directories.")