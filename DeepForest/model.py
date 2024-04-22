from ImageProcessing import Filters, Preprocessing
from deepforest import main as mn
import os

def pre_process_image(image_path, tif_path):
    """
    Converts an RGBA image to RGB and then to TIFF format.

    Parameters:
    image_path (str): The path to the source RGBA image.
    tif_path (str): The path where the converted TIFF image will be saved.

    Returns:
    None
    """
    png_path = "./tempImage.png"
    Preprocessing.convert_rgba_to_rgb(image_path, png_path)
    Preprocessing.convert_png_to_tiff(png_path, tif_path)


def count_tree(predictions):
    """
    Counts the number of trees in an image using a DeepForest model.

    Parameters:
    predictions (DataFrame): The DataFrame containing the predictions from the DeepForest model.

    Returns:
    tree_number (int): The number of trees detected in the image.
    """
    tree_number = predictions[predictions['label'] == 'Tree'].shape[0]
    return tree_number


def predict_image(path, model):
    """
    Predicts the number of trees in an image using the DeepForest model and prints the result.

    Parameters:
    path (str): The path to the image.

    Returns:
    None
    """
    predictions = model.predict_tile(raster_path=path, return_plot=False, patch_size=400)
    filtered_predictions = predictions[predictions['score'] > 0.15]
    tree_value = count_tree(filtered_predictions)
    print(tree_value)


def main():
    """
    Main function to preprocess the image, load the DeepForest model, and predict the number of trees.

    Returns:
    None
    """
    model = mn.deepforest()
    model.use_release(check_release=False)
    gen_tif_path = "./tempImage.tif"
    gen_image_path = "../Data/Images/t8.png"
    pre_process_image(gen_image_path, gen_tif_path)
    predict_image("./tempImage.tif", model)
    os.remove(gen_tif_path)
    os.remove("./tempImage.png")


if __name__ == '__main__':
    main()
