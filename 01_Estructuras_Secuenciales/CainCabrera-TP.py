import math

" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."

print("Hola Mundo!")

#-------------------------------------------------------------------------#

""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
"""

nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

#-------------------------------------------------------------------------#

""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = (int(input("Ingrese su edad: ")))
residencia = input("Ingrese su lugar de residencia: ")

print(f"Mi nombre es {nombre} {apellido}, Tengo {edad} años, y vivo en {residencia}!")

#-------------------------------------------------------------------------#

""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""


radio = float(input("Ingrese el radio: "))
pi = 3.1415926535
area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#-------------------------------------------------------------------------#

""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""

segundos = int(input("Ingrese la cantidad de segundos: "))
resultado = int(segundos / 3600)
print(f"Su conversion es de {resultado} horas!")

#-------------------------------------------------------------------------#


""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""

num_user = int(input("Ingrese un numero entero: "))

for i in range(0,10):
    multiplciacion = num_user * i
    print(f"{num_user} x {i} = {multiplciacion}")

#-------------------------------------------------------------------------#

""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
"""
num_1 = int(input("Ingrese un numero entero: "))
num_2 = int(input("Ingrese el segundo numero: "))

if num_1 and num_2 != 0:
    suma = num_2 + num_1
    resta = num_2 - num_1
    multiplicacion = num_2 * num_1
    division = (num_2 / num_1)
    print(f"{suma}\n{resta}\n{multiplicacion}\n{division}")

else:
    print("No se permite el numero 0, Vuelva a ingresar un numero nuevamente.")

#-------------------------------------------------------------------------#

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. 
"""

altura = float(input("Indique cuanto mide: "))
peso_corp =  float(input("Indique su peso en kilogramos: "))
IMC = (peso_corp) / altura ** 2 
print(f"Su IMD da un porcentaje de: %{IMC:.2f}")


#-------------------------------------------------------------------------#



""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit.
"""

temperatura = int(input("Ingrese su temperatura: "))
resultado = float(temperatura * 9/5) + 32
print(f"Su temperatura en fahrenheit: {resultado} °F")

#-------------------------------------------------------------------------#

""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""

num_1 = float(input("Ingrese un numero: "))
num_2 = float(input("Ingrese su segundo numero: "))
num_3 = float(input("Ingrese su tercer numero: "))
suma = num_1 + num_2 + num_3
promedio = suma / 3
print(f"El promedio de los 3 numeros es: {promedio:.2f}")
