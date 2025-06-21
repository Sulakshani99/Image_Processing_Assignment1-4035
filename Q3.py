import cv2
import numpy as np
import matplotlib.pyplot as plt

# Task 3: Rotate an image by 45 and 90 degrees

def rotate_image(image_path, angles):

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 7))
    plt.subplot(1, len(angles) + 1, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    h, w = image.shape[:2] # Get image height and width

    for i, angle in enumerate(angles):
        image_rotated = None

        if angle == 90:
            # For 90 degrees, cv2.
            image_rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            print(f"Rotated by {angle} degrees using cv2.rotate.")
        elif angle == 45:
            
            center = (w / 2, h / 2) # Rotation center
            
            # Get the 2x3 rotation matrix. 1.0 is the scale factor.
            M = cv2.getRotationMatrix2D(center, angle, 1.0)

            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            nW = int((h * sin) + (w * cos)) # New width
            nH = int((h * cos) + (w * sin)) # New height

            # Adjust the rotation matrix to translate the image so it fits in the new dimensions
            M[0, 2] += (nW / 2) - center[0]
            M[1, 2] += (nH / 2) - center[1]

            image_rotated = cv2.warpAffine(image, M, (nW, nH))
            print(f"Rotated by {angle} degrees using warpAffine.")
        else:
            print(f"Rotation for {angle} degrees not specifically implemented in this example. Skipping.")
            continue # Skip to the next angle

        if image_rotated is not None:
            # Convert to RGB for matplotlib display
            image_rotated_rgb = cv2.cvtColor(image_rotated, cv2.COLOR_BGR2RGB)
            
            plt.subplot(1, len(angles) + 1, i + 2)
            plt.imshow(image_rotated_rgb)
            plt.title(f'Rotated by {angle} Degrees')
            plt.axis('off')
            
            # Save the processed image
            output_filename = f"output_rotated_{angle}_degrees.jpg"
            cv2.imwrite(output_filename, image_rotated)
            print(f"Processed image saved as {output_filename}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    image_path_input = 'input_image.jpg' 

    print("\n---- Question 3: Image Rotation ----")
    rotate_image(image_path_input, [45, 90]) 