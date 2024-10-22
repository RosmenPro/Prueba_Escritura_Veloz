Prueba de Escritura Veloz
Esta aplicación de escritorio permite al usuario realizar pruebas de escritura veloz con una serie de frases predefinidas. Mide el tiempo que tarda el usuario en escribir la frase mostrada y evalúa la precisión comparando la frase escrita con la original.

Funcionalidades
Selección aleatoria de frases de prueba.
Medición del tiempo que tarda el usuario en escribir una frase.
Evaluación de la precisión de la escritura, comparando la frase escrita por el usuario con la original.
Interfaz gráfica de usuario sencilla utilizando Tkinter.
Requisitos
Para ejecutar este proyecto necesitas tener instalado:

Python 3.x
Tkinter (generalmente incluido en las instalaciones estándar de Python)
Instalación
Clona este repositorio o descarga los archivos.
Asegúrate de tener Tkinter instalado. Si no lo tienes, puedes instalarlo ejecutando:
bash
Copiar código
sudo apt-get install python3-tk  # En sistemas basados en Debian/Ubuntu
Uso
Ejecuta el script:
bash
Copiar código
python3 prueba_escritura.py
Aparecerá una ventana con las siguientes opciones:
Iniciar: Muestra una frase aleatoria para que el usuario la escriba y comienza a contar el tiempo.
Detener: Finaliza la prueba cuando el usuario haya terminado de escribir y muestra el tiempo transcurrido junto con la precisión de la escritura.
El usuario debe escribir la frase en el campo de entrada y luego detener la prueba para ver los resultados.
Estructura del código
PruebaEscritura: Es la clase principal que maneja la lógica de la aplicación.
iniciar_prueba: Selecciona una frase aleatoria y registra el tiempo de inicio.
detener_prueba: Calcula el tiempo total que tomó escribir la frase y la precisión de la escritura.
evaluar_precision: Compara la frase escrita por el usuario con la original y calcula cuántas palabras coinciden.
Contribuir
Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, siéntete libre de crear un pull request.
