import os
import re
import shutil
import random

# Define your source and destination directories
source_directory = '/content/drive/My Drive/Skoli/6H/Deep Learning/Final Project/carseg_data_2/arrays'
destination_directory = '/content/drive/My Drive/Skoli/6H/Deep Learning/Final Project/carseg_data_2/arrays_reduced'

# Create the destination directory if it does not exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Define patterns for the file names
photo_pattern = re.compile(r'photo_\d{4}\.npy')
orange_pattern = re.compile(r'orange_3_doors_\d{4}\.npy')
black_pattern = re.compile(r'black_5_doors_\d{4}\.npy')

# List to store the file names
orange_files = []
black_files = []

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    if photo_pattern.match(filename):
        shutil.copy(os.path.join(source_directory, filename), destination_directory)
    elif orange_pattern.match(filename):
        orange_files.append(filename)
    elif black_pattern.match(filename):
        black_files.append(filename)

# Randomly select 150 files from orange and black categories
selected_orange_files = random.sample(orange_files, min(150, len(orange_files)))
selected_black_files = random.sample(black_files, min(150, len(black_files)))

# Copy the selected files to the destination directory
for filename in selected_orange_files + selected_black_files:
    shutil.copy(os.path.join(source_directory, filename), destination_directory)

print("Files successfully copied to", destination_directory)
