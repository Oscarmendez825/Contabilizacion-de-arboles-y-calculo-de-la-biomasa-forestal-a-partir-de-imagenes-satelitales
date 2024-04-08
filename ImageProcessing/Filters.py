import cv2
import numpy as np
from skimage.filters import median
from skimage.io import imread


def morphological_filter(image_path):
    """
    This function applies a morphological filter to an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    opened (ndarray): The filtered image.
    """
    input_image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Create a 5x5 kernel of ones (this is used for the morphological operation)
    kernel = np.ones((5,5),np.uint8)

    # Apply a morphological open operation to the grayscale image using the kernel
    # It can be used to remove noise.
    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    # Return the filtered image
    return opened

def color_segmentation(image_path):
    """
    This function applies color segmentation to an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    segmented_image (ndarray): The image with color segmentation applied.
    """

    # Load the input image
    input_image = cv2.imread(image_path)
    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    # Define the color range for trees (in this case, shades of green)
    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])

    # Apply the mask to segment the colors within the defined range
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply the mask to the original image
    segmented_image = cv2.bitwise_and(input_image, input_image, mask=mask)

    # Return the segmented image
    return segmented_image

def background_removal(image_path):
    """
    This function removes the background from an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    result (ndarray): The image with the background removed.
    """

    # Read the image from the provided path
    input_image = cv2.imread(image_path)

    # Create a background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Apply the background subtraction algorithm to the image
    mask = bg_subtractor.apply(input_image)

    # Apply the mask to remove the background
    result = cv2.bitwise_and(input_image, input_image, mask=mask)

    # Return the image with the background removed
    return result

def enhance_contrast(image_path):
    """
    This function enhances the contrast of an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    equalized (ndarray): The image with enhanced contrast.
    """

    # Read the image from the provided path
    input_image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to enhance the contrast
    equalized = cv2.equalizeHist(gray)

    # Return the image with enhanced contrast
    return equalized

def median_filter(image_path, kernel_size=3):
    """
    This function applies a median filter to an image.

    Parameters:
    image_path (str): The path to the image file.
    kernel_size (int): The size of the kernel to be used in the median filter. Default is 3.

    Returns:
    filtered (ndarray): The image with the median filter applied.
    """

    # Read the image from the provided path
    input_image = cv2.imread(image_path)

    # Apply the median filter
    filtered = cv2.medianBlur(input_image, kernel_size)

    # Return the filtered image
    return filtered

def median_filter_skimage(image_path, kernel_size=3):
    """
    This function applies a median filter to an image using the skimage library.

    Parameters:
    image_path (str): The path to the image file.
    kernel_size (int): The size of the kernel to be used in the median filter. Default is 3.

    Returns:
    filtered (ndarray): The image with the median filter applied.
    """

    # Read the image from the provided path
    input_image = imread(image_path)

    # Apply the median filter
    filtered = median(input_image, selem=np.ones((kernel_size, kernel_size)))

    # Return the filtered image
    return filtered

def histogram_equalization(image_path):
    """
    This function applies histogram equalization to an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    img_histeq (ndarray): The image with histogram equalization applied.
    """

    # Read the image from the provided path
    img = cv2.imread(image_path)

    # Convert the image from BGR to YUV color space
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # Apply histogram equalization to the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # Convert the image back to BGR color space
    img_histeq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    # Return the image with histogram equalization applied
    return img_histeq

def gaussian_filter(image_path):
    """
    This function applies a Gaussian filter to an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    img_smooth (ndarray): The image with the Gaussian filter applied.
    """

    # Read the image from the provided path
    img = cv2.imread(image_path)

    # Apply a Gaussian filter to the image
    img_smooth = cv2.GaussianBlur(img, (5, 5), 0)

    # Return the image with the Gaussian filter applied
    return img_smooth

def bilateral_filter(image_path):
    """
    This function applies a bilateral filter to an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    img_filtered (ndarray): The image with the bilateral filter applied.
    """
    # Read the image from the provided path
    img = cv2.imread(image_path)

    # Apply a bilateral filter to the image
    img_filtered = cv2.bilateralFilter(img, 9, 75, 75)

    # Return the image with the bilateral filter applied
    return img_filtered

def select_and_execute(image_path, filter_type):
    """
    This function selects and executes a specific image filter function.

    Parameters:
    image_path (str): The path to the image file.
    filter_type (str): The type of filter to be applied.

    Returns:
    filtered_image (ndarray): The image with the selected filter applied.
    """

    if filter_type == "morphological":
        filtered_image = morphological_filter(image_path)
    elif filter_type == "color_segmentation":
        filtered_image = color_segmentation(image_path)
    elif filter_type == "background_removal":
        filtered_image = background_removal(image_path)
    elif filter_type == "enhance_contrast":
        filtered_image = enhance_contrast(image_path)
    elif filter_type == "median_filter":
        filtered_image = median_filter(image_path)
    elif filter_type == "median_filter_skimage":
        filtered_image = median_filter_skimage(image_path)
    elif filter_type == "histogram_equalization":
        filtered_image = histogram_equalization(image_path)
    elif filter_type == "gaussian_filter":
        filtered_image = gaussian_filter(image_path)
    elif filter_type == "bilateral_filter":
        filtered_image = bilateral_filter(image_path)
    else:
        raise ValueError("Invalid filter type")

    return filtered_image