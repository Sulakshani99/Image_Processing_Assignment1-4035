import cv2
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Reduce the number of intensity levels in an image
# Step 1: Load the image in grayscale mode
image_path = 'input_image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print('Error: Image not found.')
    exit()

# Step 2: Get the desired number of intensity levels from the user
levels = int(input('Enter the number of intensity levels (power of 2, e.g., 2, 4, 8, 16, ...): '))
if levels not in [2, 4, 8, 16, 32, 64, 128, 256]:
    print('Error: Number of levels must be a power of 2 between 2 and 256.')
    exit()

# Step 3: Calculate the interval and reduce the image
interval = 256 // levels
reduced_image = (image // interval) * interval

# Step 4: Save and display the reduced image
output_path = f'output_intensity_reduced_to_{levels}_levels.jpg'
cv2.imwrite(output_path, reduced_image)
print(f'Processed image saved as {output_path}')

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title(f'Original Image (256 levels)')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(reduced_image, cmap='gray')
plt.title(f'Reduced to {levels} levels')
plt.axis('off')

plt.show() 