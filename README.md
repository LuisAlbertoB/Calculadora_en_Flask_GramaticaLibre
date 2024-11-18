# Calculadora Aritmética con Gramática Libre de Contexto

Este proyecto implementa una calculadora aritmética en Flask, utilizando gramáticas libres de contexto (GLC) para procesar las operaciones de entrada, como suma, resta, multiplicación y división.

## Descripción

La aplicación permite al usuario introducir una serie de números y un operador aritmético (como `+`, `-`, `*`, `/`), y luego calcular el resultado aplicando el operador de acuerdo con el orden de las operaciones. Si el usuario ingresa más de dos números, la calculadora aplica el operador de manera secuencial sobre los números introducidos.

## Características

- Admite operaciones aritméticas básicas: suma, resta, multiplicación y división.
- Acepta una cantidad dinámica de números decimales a través de un formulario interactivo.
- La lógica de las operaciones se maneja en el backend con Flask, y el frontend es una simple interfaz en HTML.
- El diagrama de la gramática libre de contexto utilizada en el proyecto se encuentra en el archivo **Tabla.jflap**.

## Instalación

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/LuisAlbertoB/Calculadora_en_Flask_GramaticaLibre.git

