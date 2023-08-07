#!/usr/bin/env python3

from PIL import Image
import os 

# Source and destination directories
source_directory = 'images'
destination_directory = './opt/icons/'

# Ensure the destination directory exists
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# List of valid image file extensions
image_extensions = ['.png', '.tiff', '.tif', '.jpg', '.jpeg', '.bmp', '.gif']

# Iterate through all files in the source directory
for filename in os.listdir(source_directory):
    print(filename)
    
    # Skip non-image files
    if os.path.splitext(filename)[1].lower() not in image_extensions:
        continue
    
    # Open an image file
    with Image.open(os.path.join(source_directory, filename)) as img:
        # Rotate and resize
        img = img.rotate(-90, expand=True)  # Negative value for clockwise rotation
        img = img.resize((128, 128))

        # Convert to RGB if the mode is not RGB
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save the image in JPEG format to the destination directory
        base_name, _ = os.path.splitext(filename)
        img.save(os.path.join(destination_directory, base_name + '.jpeg'), 'JPEG')

print("Processing complete!")
