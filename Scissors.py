import cv2
import os

def split_image(input_image_path, num_parts):
    try:
        # Read the image using OpenCV
        img = cv2.imread(input_image_path)

        # Get the dimensions of the image
        height, width = img.shape[:2]

        # Calculate the width of each part based on the number of parts
        part_width = width // num_parts

        # Create a 'cropped' folder adjacent to the input image location
        output_folder_path = os.path.join(os.path.dirname(input_image_path), 'cropped')
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        # Split the image into parts based on the specified number
        for i in range(num_parts):
            left = i * part_width
            upper = 0
            right = left + part_width
            lower = height

            # Crop the image
            part = img[upper:lower, left:right]

            # Save each part to the 'cropped' folder
            cv2.imwrite(os.path.join(output_folder_path, f"part_{i}.png"), part)

        print(f"Image has been split into {num_parts} parts and saved in the 'cropped' folder.")
        return output_folder_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Get user input for input image path and number of parts
input_image_path = input("Enter the path to the input image: ").strip('\"')
num_parts = int(input("Enter the number of parts to split the image into: "))

# Split the image and get the output folder path
output_folder = split_image(input_image_path, num_parts)

if output_folder:
    print(f"Cropped images are saved in: {output_folder}")
else:
    print("Failed to split the image.")
