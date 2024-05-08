from PIL import Image


def convert_rgba_to_rgb(image_path, output_path):
    """
    This function converts an RGBA image to RGB.

    Parameters:
    image_path (str): The path to the input image file.
    output_path (str): The path to save the output image file.

    """

    # Load the image
    img = Image.open(image_path)

    # Ensure the image has an alpha channel
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):

        # Convert the image to RGB
        alpha = img.convert('RGB')

        # Save the new image
        alpha.save(output_path)


def convert_png_to_tiff(png_path, tiff_path):
    """
    Converts a PNG image to a TIFF image.

    Parameters:
    png_path (str): The path to the source PNG image.
    tiff_path (str): The path where the converted TIFF image will be saved.

    Returns:
    None
    """
    # Open the PNG image
    img = Image.open(png_path)

    # Save the image as a TIFF image
    img.save(tiff_path, "TIFF")