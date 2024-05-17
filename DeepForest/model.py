from sklearn.metrics import mean_absolute_error, mean_squared_error
from ImageProcessing import Filters, Preprocessing
from deepforest import main as mn
import pandas as pd
import cv2
import os


def pre_process_image(image_path, tif_path, image_filter=None):
    """
    Converts an RGBA image to RGB and then to TIFF format.

    Parameters:
    image_path (str): The path to the source RGBA image.
    tif_path (str): The path where the converted TIFF image will be saved.

    Returns:
    None
    """
    png_path = "./tempImage.png"
    if image_filter is not None:
        image = Filters.select_and_execute(image_path, image_filter)
        cv2.imwrite(png_path, image)
        Preprocessing.convert_rgba_to_rgb(png_path, png_path)
        Preprocessing.convert_png_to_tiff(png_path, tif_path)
    else:
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


def predict_image(path, model, patch_size=400):
    """
    Predicts the number of trees in an image using the DeepForest model and prints the result.

    Parameters:
    path (str): The path to the image.

    Returns:
    tree_value (int): number of trees
    """
    predictions = model.predict_tile(raster_path=path, return_plot=False, patch_size=patch_size)
    tree_value = count_tree(predictions)
    return tree_value


def evaluate_predictions(test_data, model, image_filter=None, patch_size=400):
    """
    Evaluates the predictions made by the model on test data.

    Parameters:
    test_data (DataFrame): DataFrame containing test data with columns 'Title' (image name)
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
        pre_process_image(image_path, gen_tif_path, image_filter)
        predicted_value = predict_image(gen_tif_path, model, patch_size)
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


def test_deep_forest(model, image_filter=None, patch_size=400):
    # Read test data from CSV file
    test_data = pd.read_csv("../Data/TestData.csv", sep=";")
    # Call the evaluate_predictions function to get MAE and MSE
    mae, mse = evaluate_predictions(test_data, model, image_filter, patch_size)
    print("Mean Absolute Error:", mae)
    print("Mean Squared Error:", mse)
    return mae, mse


def grid_search(model, patch_size):
    image_filters = [None, "histogram_equalization", "median_filter", "gaussian_filter", "bilateral_filter", "background_removal"]

    best_mae = float('inf')
    best_mse = float('inf')
    best_image_filter = None

    for image_filter in image_filters:
        print("patch_size:", patch_size)
        print("filter:", image_filter)
        mae, mse = test_deep_forest(model, image_filter=image_filter, patch_size=patch_size)

        if mae < best_mae:
            best_mae = mae
            best_mse = mse
            best_image_filter = image_filter

    print("Best Mean Absolute Error:", best_mae)
    print("Best Mean Squared Error:", best_mse)
    print("Best Image Filter:", best_image_filter)

    with open("results.txt", "a") as file:
        file.write("Patch Size: {}\n".format(patch_size))
        file.write("Best Mean Absolute Error: {}\n".format(best_mae))
        file.write("Best Mean Squared Error: {}\n".format(best_mse))
        file.write("Best Image Filter: {}\n\n".format(best_image_filter))


def load_model():
    model = mn.deepforest()
    model.use_release(check_release=False)
    return model

def main():
    """
    Main function to preprocess the image, load the DeepForest model, and predict the number of trees.

    Returns:
    None
    """
    model = mn.deepforest()
    model.use_release(check_release=False)
    grid_search(model, patch_size=515)


if __name__ == '__main__':
    main()
