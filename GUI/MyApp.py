import os
import json
import tkinter as tk
from PIL import Image, ImageTk
from DeepForest import model as df
from tkinter import filedialog, messagebox
from BiomassEstimation import Biomass as bm


class MyApp:
    """
    This class represents a GUI application for counting trees and calculating biomass from satellite images.
    """
    def __init__(self, root):
        """
        Initialize the application.

        Parameters:
        root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Contabilización de árboles y cálculo de la biomasa a partir de imágenes satelitales")

        # Color configuration
        bg_color = "#d6eadf"
        button_color = "#eac4d5"
        label_color = "#809bce"
        title = "Contabilización de árboles y cálculo de la biomasa a partir de imágenes satelitales"

        # Font configuration
        font = ("Helvetica", 12)

        # Window size configuration
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width-100}x{screen_height-100}")

        # Window layout configuration
        self.root.configure(bg=bg_color)

        # Application title
        title_label = tk.Label(root, text=title, font=("Helvetica", 20, "bold"), bg=bg_color, fg=label_color)
        title_label.pack(pady=20)

        # Selected image path label
        self.img_label = tk.Label(root, text="Imagen seleccionada: ####", font=("Helvetica", 9, "bold"), bg=bg_color, fg=label_color)
        self.img_label.pack(pady=20)

        # Button to load image
        load_button = tk.Button(root, text="Subir imagen", font=font, bg=button_color, command=self.load_image,
                                relief="flat", activebackground="#B0C4DE")
        load_button.pack(pady=10)

        # Button to get values
        load_button = tk.Button(root, text="Obtener resultados", font=font, bg=button_color, command=self.use_model,
                                relief="flat", activebackground="#B0C4DE")
        load_button.pack(pady=10)

        # Space to display the image
        self.image_label = tk.Label(root, bg=bg_color)
        self.image_label.pack()

        # Labels at the bottom
        labels_frame = tk.Frame(root, bg=bg_color)
        labels_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        label1 = tk.Label(labels_frame, text="Cantidad de árboles:", font=font, bg=bg_color, fg=label_color)
        label1.pack(anchor='w', padx=10, pady=5)
        self.tree_count_label = tk.Label(labels_frame, text="####", font=font, bg=bg_color, fg=label_color)
        self.tree_count_label.pack(anchor='w', padx=10, pady=5)
        label3 = tk.Label(labels_frame, text="Biomasa calculada:", font=font, bg=bg_color, fg=label_color)
        label3.pack(anchor='w', padx=10, pady=5)
        self.biomass_label = tk.Label(labels_frame, text="####", font=font, bg=bg_color, fg=label_color)
        self.biomass_label.pack(anchor='w', padx=10, pady=5)
        self.model = df.load_model()

        # Attribute to store the path of the loaded image
        self.loaded_image_path = None

    def load_image(self):
        """
        Load an image from the file system and display it in the application.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((350, 350))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.loaded_image_path = file_path
            self.img_label.config(text=str("Imagen seleccionada: " + self.loaded_image_path))

    def use_model(self):
        """
        Use the DeepForest model to predict the number of trees in the loaded image and calculate the total biomass.
        """
        if self.loaded_image_path:
            gen_tif_path = "./tempImage.tif"
            df.pre_process_image(image_path=self.loaded_image_path, tif_path=gen_tif_path, image_filter=None)
            predicted_value = df.predict_image(path=gen_tif_path, model=self.model, patch_size=525)
            biomass_estimation = bm.estimate_total_biomass(number_of_trees=predicted_value, dap=1.15, delta=0.6)
            os.remove(gen_tif_path)
            os.remove("./tempImage.png")
            self.tree_count_label.config(text=str(predicted_value))
            self.biomass_label.config(text=str(biomass_estimation) + "kg")

            # Guardar los resultados
            self.save_results(predicted_value, biomass_estimation)
        else:
            messagebox.showinfo("Error", "Por favor, carga una imagen antes de obtener resultados.")

    def save_results(self, tree_count, biomass):
        """
        Save the results of the tree count and biomass calculation to a JSON file.

        Parameters:
        tree_count (int): The number of trees.
        biomass (float): The calculated biomass.
        """
        result = {"Cantidad de arboles": tree_count, "Biomasa": biomass}
        try:
            with open("Resultados.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(result)

        with open("Resultados.json", "w") as file:
            json.dump(data, file, indent=4)