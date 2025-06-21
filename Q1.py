import cv2
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Reduce the number of intensity levels in an image

def reduce_intensity_levels(image_path, x):

    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    # Validate 
    if not (x > 0 and (x & (x - 1) == 0)):
        print(f"Error: Desired number of intensity levels ({x}) must be a positive integer power of 2.")
        return

    # Calculate the factor to quantize the intensity levels
    levels_factor = 256 // x
    
    # Apply the reduction:
    reduced_image = (image // levels_factor) * levels_factor

    # Display original and reduced images 
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image (256 Levels)')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(reduced_image, cmap='gray')
    plt.title(f'Reduced to {x} Levels')
    plt.axis('off')

    plt.show()

    # Save the processed image
    output_filename = f"output_intensity_reduced_to_{x}_levels.jpg"
    cv2.imwrite(output_filename, reduced_image)
    print(f"Processed image saved as {output_filename}")


if __name__ == "__main__":
    
    image_path_input = 'input_image.jpg' 

    print("---- Question 1: Reduce Number of Intensity Levels ----")
    try:
        num_levels_input = int(input("Enter the desired number of intensity levels (integer power of 2): "))
        reduce_intensity_levels(image_path_input, num_levels_input)
    except ValueError:
        print("Invalid input. Please enter an integer.") 