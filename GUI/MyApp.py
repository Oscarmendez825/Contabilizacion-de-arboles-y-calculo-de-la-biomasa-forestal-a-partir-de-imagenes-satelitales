import os
import json
import tkinter as tk
from PIL import Image, ImageTk
from DeepForest import model as df
from tkinter import filedialog, messagebox
from BiomassEstimation import Biomass as bm


class MyApp:
    def __init__(self, root):
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
        self.img_label = tk.Label(root, text="Imagen seleccionada: ####", font=("Helvetica", 15, "bold"), bg=bg_color, fg=label_color)
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
        if self.loaded_image_path:
            gen_tif_path = "./tempImage.tif"
            df.pre_process_image(image_path=self.loaded_image_path, tif_path=gen_tif_path, image_filter=None)
            predicted_value = df.predict_image(path=gen_tif_path, model=self.model, patch_size=525)
            biomass_estimation = bm.estimate_total_biomass(number_of_trees=predicted_value, dap=1.15, delta=0.8)
            os.remove(gen_tif_path)
            os.remove("./tempImage.png")
            self.tree_count_label.config(text=str(predicted_value))
            self.biomass_label.config(text=str(biomass_estimation) + "kg")

            # Guardar los resultados
            self.save_results(predicted_value, biomass_estimation)
        else:
            messagebox.showinfo("Error", "Por favor, carga una imagen antes de obtener resultados.")

    def save_results(self, tree_count, biomass):
        result = {"Cantidad de arboles": tree_count, "Biomasa": biomass}
        try:
            with open("Resultados.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(result)

        with open("Resultados.json", "w") as file:
            json.dump(data, file, indent=4)