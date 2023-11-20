import numpy as np
import cv2
import os
import random

def augment_image_and_label(image, label):
    # Flip the image and label horizontally with a 50% chance
    if random.choice([True, False]):
        image = cv2.flip(image, 1)  # Horizontal flip
        label = cv2.flip(label, 1)  # Horizontal flip for label

    # Flip the image and label vertically with a 50% chance
    if random.choice([True, False]):
        image = cv2.flip(image, 0)  # Vertical flip
        label = cv2.flip(label, 0)  # Vertical flip for label

    # Rotate the image and label slightly (up to +/- 15 degrees)
    angle = random.uniform(-15, 15)
    rows, cols, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    label = cv2.warpAffine(label, rotation_matrix, (cols, rows), flags=cv2.INTER_NEAREST)

    return image, label

def process_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith('.npy'):
            file_path = os.path.join(folder_path, filename)
            # Load the npy file
            data = np.load(file_path)
            image, label = data[:, :, :3], data[:, :, 3]

            # Augment both the image and label
            augmented_image, augmented_label = augment_image_and_label(image, label)

            # Combine the augmented image and label
            augmented_data = np.zeros_like(data)
            augmented_data[:, :, :3] = augmented_image
            augmented_data[:, :, 3] = augmented_label

            # Save the augmented data
            output_file_path = os.path.join(output_folder, "aug_" + filename)
            np.save(output_file_path, augmented_data)
# Define your source and destination directories

# Define your source and destination directories
source_directory = '/content/drive/My Drive/Skoli/6H/Deep Learning/Final Project/carseg_data_2/arrays_reduced'
destination_directory = '/content/drive/My Drive/Skoli/6H/Deep Learning/Final Project/carseg_data_2/arrays_reduced_augmented'

# Process the folder
process_folder(source_directory, destination_directory)
