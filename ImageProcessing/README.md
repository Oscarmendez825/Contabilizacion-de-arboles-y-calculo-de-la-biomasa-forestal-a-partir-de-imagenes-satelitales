# Tree Crown Counting Image Processing Filters

This folder contains Python scripts implementing various image processing filters and techniques for preprocessing images intended to be used by a machine learning model for counting tree crowns.

## Overview

The scripts provided here are aimed at enhancing the quality of input images and highlighting relevant features to improve the performance of the tree crown counting model.

## Included Filters

1. **Contrast Enhancement**: Enhance the contrast of images to highlight tree crowns.
2. **Median Filtering**: Apply median filtering for noise reduction and smoothing.
3. **Morphological Filtering**: Utilize morphological operations for noise removal and shape enhancement.
4. **Color Segmentation**: Segment colors to highlight tree regions based on distinctive color features.
5. **Background Removal**: Remove complex and distracting backgrounds to isolate tree crowns.

## Usage

Each filter is implemented in a separate Python function. To use these filters:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the `installer.bat`.
3. Execute the desired function(s) on your images.
4. Preprocessed images can then be used as input for the tree crown counting model.

## Usage: Running ImageProcessing.py

To apply all filters present in Filters.py and preprocess images, you can use the `ImageProcessingTest.py` script. This script serves as an example of using all the filters provided in Filters.py.

### Requirements

- Python 3.11 or higher
- OpenCV
- scikit-image

### Usage Instructions

1. Make sure you have Python 3.11 installed on your system.
2. Install the necessary dependencies by running `installer.bat`.
3. Place the input image(s) in the directory `Test/Images`.
4. Execute the following command from the root directory of the project:
   ```
   python -m ImageProcessing.Tests.ImageProcessingTest
   ```
5. The output images with applied filters will be saved in the directory `Test/Output_Filtered_Images`.
