# EC7212 – Computer Vision and Image Processing

## Take Home Assignment 1

This repository contains Python programs to perform basic image processing operations as part of the EC7212 course assignment.

## Prerequisites
- Python 3.x
- Required libraries:
  - opencv-python
  - numpy
  - matplotlib

Install dependencies using:
```
pip install opencv-python numpy matplotlib
```

## Image Preparation
- Place your input image in the same directory as the scripts.
- The default filename expected by all scripts is `input_image.jpg` (you can change this in the scripts if needed).
- The image should be in grayscale for Q1, Q2, and Q4. Q3 works with color images as well.

## Scripts Overview

### Q1.py — Reduce Number of Intensity Levels
- Reduces the number of intensity levels in a grayscale image to a user-specified power of 2 (e.g., 2, 4, 8, ...).
- **Usage:**
  ```
  python Q1.py
  ```
  - Enter the desired number of intensity levels when prompted.
  - Output: Side-by-side display and a saved image file (e.g., `output_intensity_reduced_to_4_levels.jpg`).

### Q2.py — Spatial Average Filtering
- Applies spatial averaging (mean filtering) to the image with 3x3, 10x10, and 20x20 neighborhoods.
- **Usage:**
  ```
  python Q2.py
  ```
  - Output: Side-by-side display and saved blurred images (e.g., `output_blurred_3x3.jpg`).

### Q3.py — Image Rotation
- Rotates the image by 45 and 90 degrees.
- **Usage:**
  ```
  python Q3.py
  ```
  - Output: Side-by-side display and saved rotated images (e.g., `output_rotated_45_degrees.jpg`).

### Q4.py — Reduce Image Spatial Resolution
- Reduces the spatial resolution by replacing non-overlapping blocks (3x3, 5x5, 7x7) with their average value.
- **Usage:**
  ```
  python Q4.py
  ```
  - Output: Side-by-side display and saved images (e.g., `output_res_reduced_3x3.jpg`).

## Notes
- If you want to use a different image filename, update the `image_path` variable in each script.