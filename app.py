from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_resultado(numeros, operador):
    """Función para calcular la operación entre múltiples números con un solo operador"""
    # Convertimos los números de string a float
    numeros = list(map(float, numeros))

    # Empezamos con el primer número
    resultado = numeros[0]

    # Aplicamos la operación para el resto de los números
    for num in numeros[1:]:
        if operador == '+':
            resultado += num
        elif operador == '-':
            resultado -= num
        elif operador == '*':
            resultado *= num
        elif operador == '/':
            if num != 0:
                resultado /= num
            else:
                return "Error: División por cero"
        else:
            return "Error: Operador no reconocido"
    
    return resultado

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los números y operadores del formulario
        numeros = request.form.getlist('numeros')
        operador = request.form.get('operator')

        # Verificar si la cantidad de operadores es uno menos que la cantidad de números
        if len(numeros) < 2:
            return render_template('index.html', result="Error: Necesitas al menos dos números para operar")
        
        # Llamar a la función para calcular el resultado
        resultado = calcular_resultado(numeros, operador)
        return render_template('index.html', result=resultado)
    
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
