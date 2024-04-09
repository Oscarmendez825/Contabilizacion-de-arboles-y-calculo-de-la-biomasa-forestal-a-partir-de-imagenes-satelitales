import os
import cv2
from .. import Filters as filters
from .. import rgba2rgb 


def test_filters(input_image_path, output_directory):
    """
    This function tests various image filters on an input image and saves the filtered images.

    Parameters:
    input_image_path (str): The path to the input image file.
    output_directory (str): The directory to save the filtered images.

    """

    # List of filter types to test
    filter_types = ["morphological", "color_segmentation", "background_removal", 
                    "enhance_contrast", "median_filter", 
                    "histogram_equalization", "gaussian_filter", "bilateral_filter"]

    # Convert the image from RGBA to RGB
    output_image_path = os.path.join(output_directory, 'output_image_rgb.png')
    rgba2rgb.convert_rgba_to_rgb(input_image_path, output_image_path)

    # Iterate over all filter types
    for filter_type in filter_types:
        # Apply the desired filter to the RGB image
        filtered_image = filters.select_and_execute(output_image_path, filter_type)
        
        # Save the filtered image with a unique name
        filtered_image_path = os.path.join(output_directory, f'filtered_image_{filter_type}.png')
        cv2.imwrite(filtered_image_path, filtered_image)

# Example of usage
input_image_path = './ImageProcessing/Tests/Images/testImage.png'
output_directory = './ImageProcessing/Tests/Output_Filtered_Images/'
test_filters(input_image_path, output_directory)

