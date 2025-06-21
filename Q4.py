import cv2
import numpy as np
import matplotlib.pyplot as plt

# Task 4: Block-wise averaging to simulate lower spatial resolution

def reduce_spatial_resolution(image_path, block_sizes):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    plt.figure(figsize=(15, 7))
    plt.subplot(1, len(block_sizes) + 1, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    h, w = image.shape # Get image height and width

    for i, block_size in enumerate(block_sizes):
        # Create a copy of the image to modify, and convert to float for accurate averaging
        image_reduced_res = np.copy(image).astype(np.float32) 
        
        for y in range(0, h, block_size):
            for x in range(0, w, block_size):
                current_block = image_reduced_res[y : min(y + block_size, h), 
                                                x : min(x + block_size, w)]
                
                # Calculate the average of pixels in the current block
                average_value = np.mean(current_block)
                
                # Replace all pixels in the block with the calculated average value
                image_reduced_res[y : min(y + block_size, h), 
                                 x : min(x + block_size, w)] = average_value
        
        image_reduced_res = image_reduced_res.astype(np.uint8)

        plt.subplot(1, len(block_sizes) + 1, i + 2)
        plt.imshow(image_reduced_res, cmap='gray')
        plt.title(f'Resolution Reduced with {block_size}x{block_size} Blocks')
        plt.axis('off')
        
        # Save the processed image
        output_filename = f"output_res_reduced_{block_size}x{block_size}.jpg"
        cv2.imwrite(output_filename, image_reduced_res)
        print(f"Processed image saved as {output_filename}")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    image_path_input = 'input_image.jpg' 

    print("\n---- Question 4: Reduce Image Spatial Resolution ----")
    block_sizes_to_apply = [3, 5, 7] 
    reduce_spatial_resolution(image_path_input, block_sizes_to_apply) 