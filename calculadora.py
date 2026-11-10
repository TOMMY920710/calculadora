import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

# Mapeo de botones a IDs de Pokémon de la Pokedex Nacional
# 1: Bulbasaur, 2: Ivysaur, 3: Venusaur, 4: Charmander, 5: Charmeleon, 6: Charizard, 7: Squirtle, 8: Wartortle, 9: Blastoise, 0: Pikachu
POKEMON_MAP = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 25,
}

# Cache para almacenar las imágenes de Pillow/Tkinter
images_cache = {}


def fetch_pokemon_image(poke_id):
    """Descarga el sprite del Pokémon desde la PokéAPI y lo adapta para Tkinter."""
    if poke_id in images_cache:
        return images_cache[poke_id]

    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            img_data = response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((45, 45), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            images_cache[poke_id] = tk_img
            return tk_img
    except Exception as e:
        print(
            f"No se pudo cargar el Pokémon #{poke_id}. Usando fallback. Error: {e}"
        )

    return None


class PokemonCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("PokéCalculator ⚡")
        self.root.geometry("380x560")
        self.root.configure(bg="#CC0000")  # Rojo Pokedex
        self.root.resizable(False, False)

        self.expression = ""

        # Contenedor del Pantalla / Display
        display_frame = tk.Frame(self.root, bg="#CC0000", pady=15)
        display_frame.pack(fill="x", padx=20)

        # Pantalla estilo retro Game Boy / Pokedex
        self.display = tk.Entry(
            display_frame,
            font=("Consolas", 24, "bold"),
            bg="#8B956D",  # Verde pantallita GameBoy
            fg="#0F380F",
            justify="right",
            bd=5,
            relief="sunken",
        )
        self.display.pack(fill="x", ipady=10)

        # Frame de Botones
        buttons_frame = tk.Frame(self.root, bg="#222222", bd=5, relief="raised")
        buttons_frame.pack(padx=15, pady=10, fill="both", expand=True)

        # Configurar grilla
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)

        # Diseño del teclado
        # (Texto del botón, fila, columna, tipo de botón)
        buttons_layout = [
            ("C", 0, 0, "action"),
            ("(", 0, 1, "action"),
            (")", 0, 2, "action"),
            ("/", 0, 3, "op"),
            ("7", 1, 0, "num"),
            ("8", 1, 1, "num"),
            ("9", 1, 2, "num"),
            ("*", 1, 3, "op"),
            ("4", 2, 0, "num"),
            ("5", 2, 1, "num"),
            ("6", 2, 2, "num"),
            ("-", 2, 3, "op"),
            ("1", 3, 0, "num"),
            ("2", 3, 1, "num"),
            ("3", 3, 2, "num"),
            ("+", 3, 3, "op"),
            ("0", 4, 0, "num"),
            (".", 4, 1, "action"),
            ("⌫", 4, 2, "action"),
            ("=", 4, 3, "equals"),
        ]

        self.create_buttons(buttons_frame, buttons_layout)

    def create_buttons(self, frame, layout):
        for text, row, col, btype in layout:
            if btype == "num":
                poke_id = POKEMON_MAP.get(text)
                poke_img = fetch_pokemon_image(poke_id)

                btn = tk.Button(
                    frame,
                    text=f" {text}",
                    image=poke_img,
                    compound="left",  # Imagen a la izquierda, número a la derecha
                    font=("Arial", 14, "bold"),
                    bg="#F0F0F0",
                    fg="#111",
                    activebackground="#FFDE00",
                    bd=3,
                    command=lambda t=text: self.on_button_click(t),
                )
            elif btype == "op":
                btn = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 16, "bold"),
                    bg="#3B4CCA",  # Azul Pokémon
                    fg="white",
                    activebackground="#2A3A99",
                    bd=3,
                    command=lambda t=text: self.on_button_click(t),
                )
            elif btype == "equals":
                btn = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 16, "bold"),
                    bg="#FFDE00",  # Amarillo Pikachu
                    fg="#3B4CCA",
                    activebackground="#E6C200",
                    bd=3,
                    command=lambda: self.evaluate_expression(),
                )
            else:  # Acciones: C, (, ), ., ⌫
                btn = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 12, "bold"),
                    bg="#FF5350",
                    fg="white",
                    bd=3,
                    command=lambda t=text: self.on_button_click(t),
                )

            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        else:
            self.expression += str(char)

        self.update_display(self.expression)

    def update_display(self, val):
        self.display.delete(0, tk.END)
        self.display.insert(0, val)

    def evaluate_expression(self):
        try:
            # Evaluar la expresión matemática
            result = str(eval(self.expression))
            self.update_display(result)
            self.expression = result
        except Exception:
            messagebox.showerror("Error", "Expresión matemática inválida")
            self.expression = ""
            self.update_display("")


if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonCalculator(root)
    root.mainloop()