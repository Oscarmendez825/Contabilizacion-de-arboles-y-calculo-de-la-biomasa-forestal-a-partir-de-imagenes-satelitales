from sklearn.metrics import mean_absolute_error, mean_squared_error
from ImageProcessing import Filters, Preprocessing
from deepforest import main as mn
import pandas as pd
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
    predictions = model.predict_tile(raster_path=path, return_plot=False, patch_size=550)
    tree_value = count_tree(predictions)
    return tree_value


def evaluate_predictions(test_data, model):
    """
    Evaluates the predictions made by the model on test data.

    Parameters:
    test_data (DataFrame): DataFrame containing test data with columns 'Title' (image path)
                           and 'TreeCrowns' (actual number of tree crowns).

    Returns:
    mae (float): Mean Absolute Error.
    mse (float): Mean Squared Error.
    """
    actual_values = []
    predicted_values = []

    for index, row in test_data.iterrows():
        image_path = "../Data/Images/"+row['Title']+".png"
        actual_value = row['TreeCrowns']
        gen_tif_path = "./tempImage.tif"
        pre_process_image(image_path, gen_tif_path)
        predicted_value = predict_image(gen_tif_path, model)
        actual_values.append(actual_value)
        predicted_values.append(predicted_value)
        os.remove(gen_tif_path)
        os.remove("./tempImage.png")

    # Calculate MAE and MSE using Scikit-learn functions
    mae = mean_absolute_error(actual_values, predicted_values)
    mse = mean_squared_error(actual_values, predicted_values)

    print("Real:     ", actual_values)
    print("Predicted:", predicted_values)

    return mae, mse


def test_deep_forest(model):
    # Read test data from CSV file
    test_data = pd.read_csv("../Data/TestData.csv", sep=";")
    # Call the evaluate_predictions function to get MAE and MSE
    mae, mse = evaluate_predictions(test_data, model)

    print("Mean Absolute Error:", mae)
    print("Mean Squared Error:", mse)


def main():
    """
    Main function to preprocess the image, load the DeepForest model, and predict the number of trees.

    Returns:
    None
    """
    model = mn.deepforest()
    model.use_release(check_release=False)

    test_deep_forest(model)


if __name__ == '__main__':
    main()
