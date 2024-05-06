import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class MyApp:
    def __init__(self, root):
        """
        This function initializes the application.

        Parameters:
        root (Tk): The root window of the application.
        """

        self.root = root
        self.root.title("Contabilización de árboles y cálculo de la biomasa a partir de imágenes satelitales")

        # Color configuration
        bg_color = "#d6eadf"  # Background color
        button_color = "#eac4d5"  # Button color
        label_color = "#809bce"  # Label color
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
        label2 = tk.Label(labels_frame, text="####", font=font, bg=bg_color, fg=label_color)
        label2.pack(anchor='w', padx=10, pady=5)
        label3 = tk.Label(labels_frame, text="Biomasa calculada:", font=font, bg=bg_color, fg=label_color)
        label3.pack(anchor='w', padx=10, pady=5)
        label4 = tk.Label(labels_frame, text="####", font=font, bg=bg_color, fg=label_color)
        label4.pack(anchor='w', padx=10, pady=5)

    def load_image(self):
        """
        This function loads an image and displays it in the application.
        """

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((350, 350))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def use_model(self):
        """
        This function uses a model to calculate the number of trees and the biomass from the loaded image.
        """
        print("use model")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
