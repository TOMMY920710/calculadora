# calculadora

⚡ PokéCalculator

Una calculadora gráfica interactiva inspirada en el diseño clásico de la Pokédex, desarrollada en Python. La aplicación cuenta con botones personalizados que combinan números e imágenes (sprites) de Pokémon obtenidos en tiempo real.

📸 Características

Diseño Retro: Interfaz temática basada en el color rojo Pokedex y pantalla verde estilo Game Boy.

Sprites Dinámicos: Asignación de Pokémon icónicos (Bulbasaur, Charmander, Squirtle, Pikachu, etc.) a los botones numéricos del 0 al 9.

Carga por API: Las imágenes de los Pokémon se descargan automáticamente desde la PokéAPI al iniciar o presionar por primera vez.

Operaciones Básicas: Suma, resta, multiplicación, división, paréntesis, punto decimal y borrado.

🛠️ Tecnologías Utilizadas

Python 3.10+ (Lenguaje principal)

Tkinter (Librería estándar para la interfaz gráfica)

Pillow (PIL) (Procesamiento y escalado de imágenes)

Requests (Peticiones HTTP para descargar los sprites)

🚀 Requisitos e Instalación

1. Clonar o descargar el proyecto

Descarga este repositorio o copia los archivos en tu computadora.

2. Instalar dependencias

Asegúrate de tener Python instalado (versión 3.10 o superior recomendada). Abre tu terminal o consola de comandos e instala las librerías necesarias con:

pip install pillow requests


Nota para usuarios de Linux (Ubuntu/Debian): Si ejecutas el programa y obtienes un error con tkinter, instálalo ejecutando:

sudo apt install python3-tk


🎮 Cómo Ejecutar la Aplicación

Abre la terminal en la carpeta donde guardaste el archivo y ejecuta:

python calculadora.py


📌 Captura de Teclado y Pokémon Asignados

Botón

Pokémon Asignado

1

#001 Bulbasaur

2

#002 Ivysaur

3

#003 Venusaur

4

#004 Charmander

5

#005 Charmeleon

6

#006 Charizard

7

#007 Squirtle

8

#008 Wartortle

9

#009 Blastoise

0

#025 Pikachu
