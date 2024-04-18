from deepforest import main

def load_model():
    """
    This function loads the pretrained DeepForest model.

    Returns:
    model (DeepForest): The pretrained DeepForest model.
    """

    # Load the pretrained model
    model = main.deepforest()
    model.use_release()
    return model


def count_tree(model, image):
    """
    This function counts the number of trees in an image using a DeepForest model.

    Parameters:
    model (DeepForest): The DeepForest model to use for prediction.
    image (ndarray): The image to predict on.

    Returns:
    tree_number (int): The number of trees detected in the image.
    """

    # Make predictions on the image
    predictions = model.predict_image(image)

    # Initialize the tree counter
    tree_number = 0

    # Iterate over the predictions and count the trees
    for pred in predictions:
        if pred["label"] == "tree":
            tree_number += 1

    return tree_number

def main():
    """
    This function demonstrates how to use the above functions to count the number of trees in an image.
    """

    # Path to the image
    image_path = "C:/Users/oscar/OneDrive/Documentos/GitHub/Contabilizacion-de-arboles-y-calculo-de-la-biomasa-forestal-a-partir-de-imagenes-satelitales/Data/Images/t5.png"

    # Load the model
    model = load_model()

    # Count trees
    tree_number = count_tree(model, image_path)

    print("Número de árboles detectados:", tree_number)

if __name__ == "__main__":
    main()