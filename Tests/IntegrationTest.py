import pytest
import os
import tkinter as tk
from GUI.MyApp import MyApp


@pytest.fixture
def app():
    root = tk.Tk()
    yield MyApp(root)
    root.destroy()


def test_use_model(app):
    # Mocking the loaded image path
    app.loaded_image_path = "C:/Users/oscar/OneDrive/Documentos/GitHub/Contabilizacion-de-arboles-y-calculo-de-la-biomasa-forestal-a-partir-de-imagenes-satelitales/Data/Images/t29.png"

    # Running the use_model function
    app.use_model()

    # Asserting the expected values
    assert app.tree_count_label.cget("text") == "85"
    assert app.biomass_label.cget("text") == "31.881722537813232kg"
