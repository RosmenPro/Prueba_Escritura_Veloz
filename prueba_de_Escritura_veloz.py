"""3. Prueba de Escritura Veloz
La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una
oración de manera precisa.
Este programa puede requerir crear una interfaz gráfica de usuario (GUI) mediante el módulo
tkinter. Si eres nuevo en las GUI, este ejemplo es una buena introducción, ya que tan solo
necesitas crear una serie de etiquetas simples, botones y campos de entrada para crear una
ventana. Puedes usar el módulo timeit de Python para manejar el aspecto de temporización
de nuestra prueba de escritura, y el módulo random para seleccionar aleatoriamente una frase
de prueba."""

import tkinter as tk  # Importamos el módulo tkinter para crear la interfaz gráfica
import timeit  # Importamos el módulo timeit para medir el tiempo
import random  # Importamos el módulo random para seleccionar aleatoriamente frases de prueba

class PruebaEscritura:
    def __init__(self, master):
        self.master = master
        master.title("Prueba de Escritura Veloz")  # Creamos una ventana con un título

        # Lista de frases de prueba
        self.frases = ["La vida es como una bicicleta. Para mantener el equilibrio, debes seguir adelante.",
                       "El secreto de la felicidad no es hacer siempre lo que se quiere, sino querer siempre lo que se hace.",
                       "La verdadera medida de la amistad es como te trata alguien cuando no estamos de humor.",
                       "No hay camino para la paz, la paz es el camino.",
                       "El éxito es la capacidad de ir de fracaso en fracaso sin perder el entusiasmo."]

        # Etiqueta para mostrar la frase de prueba
        self.label_frase = tk.Label(master, text="")
        self.label_frase.pack()

        # Campo de entrada para que el usuario escriba la frase
        self.entry_escritura = tk.Entry(master)
        self.entry_escritura.pack()

        # Botón para iniciar la prueba
        self.boton_iniciar = tk.Button(master, text="Iniciar", command=self.iniciar_prueba)
        self.boton_iniciar.pack()

        # Botón para detener la prueba
        self.boton_detener = tk.Button(master, text="Detener", command=self.detener_prueba)
        self.boton_detener.pack()
        self.boton_detener.config(state=tk.DISABLED)  # El botón de detener se deshabilita al principio

        self.tiempo_inicio = None  # Variable para almacenar el tiempo de inicio de la prueba

    def iniciar_prueba(self):
        # Seleccionamos aleatoriamente una frase de prueba y la mostramos en la etiqueta
        frase = random.choice(self.frases)
        self.label_frase.config(text=frase)
        self.tiempo_inicio = timeit.default_timer()  # Registramos el tiempo de inicio
        self.boton_iniciar.config(state=tk.DISABLED)  # Deshabilitamos el botón de iniciar
        self.boton_detener.config(state=tk.NORMAL)  # Habilitamos el botón de detener

    def detener_prueba(self):
        tiempo_final = timeit.default_timer()  # Registramos el tiempo final
        tiempo_transcurrido = tiempo_final - self.tiempo_inicio  # Calculamos el tiempo transcurrido
        frase_escrita = self.entry_escritura.get()  # Obtenemos la frase escrita por el usuario
        precision = self.evaluar_precision(frase_escrita)  # Evaluamos la precisión de la escritura
        print("Tiempo transcurrido:", tiempo_transcurrido)  # Imprimimos el tiempo transcurrido
        print("Precisión:", precision)  # Imprimimos la precisión
        self.boton_iniciar.config(state=tk.NORMAL)  # Habilitamos el botón de iniciar
        self.boton_detener.config(state=tk.DISABLED)  # Deshabilitamos el botón de detener
        self.entry_escritura.delete(0, tk.END)  # Limpiamos el campo de entrada

    def evaluar_precision(self, frase_escrita):
        # Comparamos la frase escrita por el usuario con la frase de prueba original
        frase_original = self.label_frase.cget("text")
        palabras_originales = frase_original.split()
        palabras_escritas = frase_escrita.split()
        # Calculamos la precisión contando el número de palabras coincidentes
        precision = sum(1 for palabra_original, palabra_escrita in zip(palabras_originales, palabras_escritas) if palabra_original == palabra_escrita) / len(palabras_originales)
        return precision

root = tk.Tk()  # Creamos la ventana principal
app = PruebaEscritura(root)  # Creamos una instancia de la clase PruebaEscritura
root.mainloop()  # Iniciamos el bucle principal de la interfaz gráfica