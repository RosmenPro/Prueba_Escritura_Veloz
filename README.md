# Prueba de Escritura Veloz

Esta aplicación de escritorio permite al usuario realizar pruebas de escritura veloz con una serie de frases predefinidas. Mide el tiempo que tarda el usuario en escribir la frase mostrada y evalúa la precisión comparando la frase escrita con la original.

## Funcionalidades

- Selección aleatoria de frases de prueba.
- Medición del tiempo que tarda el usuario en escribir una frase.
- Evaluación de la precisión de la escritura, comparando la frase escrita por el usuario con la original.
- Interfaz gráfica de usuario sencilla utilizando `Tkinter`.

## Requisitos

Para ejecutar este proyecto necesitas tener instalado:

- Python 3.x
- Tkinter (generalmente incluido en las instalaciones estándar de Python)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener `Tkinter` instalado. Si no lo tienes, puedes instalarlo ejecutando:

   ```bash
   sudo apt-get install python3-tk  # En sistemas basados en Debian/Ubuntu
   ```

## Uso

1. Ejecuta el script:
   ```bash
   python3 prueba_escritura.py
   ```

2. Aparecerá una ventana con las siguientes opciones:
   - Iniciar: Muestra una frase aleatoria para que el usuario la escriba y comienza a contar el tiempo.
   - Detener: Finaliza la prueba cuando el usuario haya terminado de escribir y muestra el tiempo transcurrido junto con la precisión de la escritura.
3. El usuario debe escribir la frase en el campo de entrada y luego detener la prueba para ver los resultados.

## Estructura del código

- `PruebaEscritura`: Es la clase principal que maneja la lógica de la aplicación.
- `iniciar_prueba`: Selecciona una frase aleatoria y registra el tiempo de inicio.
- `detener_prueba`: Calcula el tiempo total que tomó escribir la frase y la precisión de la escritura.
- `evaluar_precision`: Compara la frase escrita por el usuario con la original y calcula cuántas palabras coinciden.

## Contribuir

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, siéntete libre de crear un pull request.

## Actualizaciones pendientes

- Resultados en la GUI en lugar de en la terminal

---

# Typing Speed Test

This desktop application allows users to take typing speed tests with a series of predefined phrases. It measures the time it takes for the user to type the displayed phrase and evaluates accuracy by comparing the typed phrase to the original.

## Features

- Random selection of test phrases.
- Measurement of the time it takes for the user to type a phrase.
- Evaluation of typing accuracy by comparing the user's typed phrase to the original.
- Simple graphical user interface using `Tkinter`.

## Requirements

To run this project, you need to have installed:

- Python 3.x
- Tkinter (usually included in standard Python installations)

## Installation

1. Clone this repository or download the files.
2. Make sure to have `Tkinter` installed. If you don’t have it, you can install it by running:

   ```bash
   sudo apt-get install python3-tk  # On Debian/Ubuntu-based systems
   ```

## Usage

1. Run the script:
   ```bash
   python3 typing_speed_test.py
   ```

2. A window will appear with the following options:
   - Start: Displays a random phrase for the user to type and starts the timer.
   - Stop: Ends the test when the user has finished typing and shows the elapsed time along with the typing accuracy.
3. The user should type the phrase in the input field and then stop the test to see the results.

## Code Structure

- `TypingTest`: The main class that handles the application logic.
- `start_test`: Selects a random phrase and records the start time.
- `stop_test`: Calculates the total time taken to type the phrase and the typing accuracy.
- `evaluate_accuracy`: Compares the user's typed phrase with the original and calculates how many words match.

## Contributing

Contributions are welcome. If you have any suggestions or improvements, feel free to create a pull request.

## Pending Updates

- Results in the GUI instead of the terminal

