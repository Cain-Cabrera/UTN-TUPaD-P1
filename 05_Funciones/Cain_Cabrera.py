import math


"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.

"""
## FUNCIONES ##
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# MAIN #

# imprimir_hola_mundo()


# --------------------------------------------------->

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.

"""

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}")

# # MAIN #

# usuario = input("Ingrese su nombre: ")
# saludar_usuario(usuario)

# --------------------------------------------------->

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
# # FUNCIONES #

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# # MAIN #

# nombre = input("Ingres su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = int(input("Su edad es: "))
# residencia = input("Ingrese el pais donde vive: ")

# informacion_personal(nombre, apellido, edad, residencia)

# --------------------------------------------------->

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

"""

# FUNCIONES #

# def calcular_area_circulo(radio, pi = 3.1415926535 ):
#     area = pi * radio ** 2
#     return area

# def calcular_perimetro_circulo(radio, pi = 3.1415926535):
#     perimetro = 2 * pi * radio
#     return perimetro

# MAIN #

# radio = float(input("Ingrese el radio: "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)
# print(f"El area del circulo es {area:.2f}")
# print(f"El perimetro del ciruclo es {perimetro:.2f}")
# --------------------------------------------------->

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""

# FUNCIONES #

# def segundos_a_horas(segundos):
#     resultado = segundos / 3600
#     print(f"Su valor en segundos en horas es de: {resultado:.2f} HS")

# def es_positivo(numero):
#     while numero <= 0:
#         numero = int(input(" ERROR . Ingrese un numero positivo: "))
#     return numero

# MAIN #    
# segundos = int(input("Ingrese una cantidad de segundos: "))
# (segundos_a_horas(es_positivo(segundos)))

# --------------------------------------------------->

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

# FUNCIONES #

# def tabla_multiplicar(numero):
#     for i in range(1, 11,1):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado} ")


# MAIN #
# numero_usuario = int(input("Ingrese un numero entero para mostrar la tabla: "))
# tabla_multiplicar(numero_usuario)

# --------------------------------------------------->

""" 7. Crear una función llamada operaciones_basicas(a, b) 
que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
"""
# FUNCIONES #

# def operaciones_basicas(a,b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b
#     resultados = (f"suma: {suma}" ,f"resta: {resta}",f"Multilpicacion: {multiplicacion}",f"Division: {division}")
#     return resultados


# MAIN # 
# num_1 = int(input("Ingrese un numero entero: "))
# num_2 = int(input("Ingrese el segundo numero: "))
# print(operaciones_basicas(num_1,num_2))

# --------------------------------------------------->

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""

# FUNCIONES #
# def calcular_imc(peso,altura):
#     return (peso) / (altura ** 2)

# MAIN # 
# altura = float(input("Indique cuanto mide: "))
# peso =  float(input("Indique su peso en kilogramos: "))
# imc = calcular_imc(peso,altura)
# print(f"Su indice de masa corporal es de: {imc}")  

# --------------------------------------------------->

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.

"""

# FUNCIONES #

# def celsius_a_fahrenheit(temperatura_celcius):
#     return (temperatura_celcius * 9/5) + 32

# MAIN #

# temperatura = int(input("Ingrese su temperatura en celcius: "))
# equivalente = celsius_a_fahrenheit(temperatura)
# print(equivalente)


#--------------------------------------------------->

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.

"""
# FUNCIONES 
# def calcular_promedio(a, b, c):
#     calculo = (a + b + c) / 3
#     return calculo

# MAIN
# num_1 = int(input("Ingrese un numero: "))
# num_2 = int(input("Ingrese un segundo numero: "))
# num_3 = int(input("Ingrese un tercer numero: "))
# promedio = calcular_promedio(num_1, num_2, num_3)
# print(f"El promedio de los numeros ingresados es: {promedio}")