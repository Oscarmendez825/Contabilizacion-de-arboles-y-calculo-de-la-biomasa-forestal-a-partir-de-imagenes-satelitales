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