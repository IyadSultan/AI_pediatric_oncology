Image Processing Tool
This tool is designed to process images by rotating and resizing them.

Dependencies
pillow (previously PIL) - You can install it via pip with the following command:
Copy code
pip install pillow

How it works
The tool scans the images folder for image files.
For each image found:
The image is rotated 90 degrees clockwise.
It's resized based on predefined dimensions.
The processed image is saved back to the images folder, overwriting the original.