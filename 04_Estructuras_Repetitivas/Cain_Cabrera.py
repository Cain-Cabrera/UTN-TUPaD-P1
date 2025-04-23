import random
""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

"""

for i in range(0,100 + 1):
    print(i)

#----------------------------------------------------------------------------------------->

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene

"""
numero_usuario = int(input("Ingrese un numero entero: "))
numero_usuario = str(numero_usuario)
cont = 0

for i in range(len(numero_usuario)):
    cont += 1
print(cont)

#----------------------------------------------------------------------------------------->

""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""



num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: ")) 
cont = 0

if (num_1 > 0 and num_2 > 0) and (num_1 != num_2): 
    if num_1 > num_2:
        max_num = num_1
        min_num = num_2 
    elif num_2 > num_1:
            max_num = num_2
            min_num = num_1    
    for i in range(min_num + 1, max_num):
        cont += i
else:
    print("Vuelva a ingresar numeros diferentes de si mismos, o de 0.")
print(cont)

#----------------------------------------------------------------------------------------->

""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
num_usuario = int(input("Ingrese numeros enteros: "))
contador = 0
while num_usuario != 0:
        contador += num_usuario
        num_usuario = int(input("Ingrese numeros enteros: "))
print(f"La suma acumulada es: {contador}")

# #----------------------------------------------------------------------------------------->

""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

print(" ------ > BIENVENIDO A 'RONDONUMBER'<---------")
print("El juego consiste en adivinar un numero, entre el 0 y el 9 inclusive..")

numero_usuario = int(input("Ingrese su numero: "))
cont = 1
numero_correcto = random.randint(0,9)
if (numero_usuario >= 0 and numero_usuario <= 9):
    while numero_usuario != numero_correcto:
        numero_usuario = int(input("Ingrese su numero: "))
        cont += 1

    print(f"Fueron necesarios {cont} intentos, para acertar al numero.")
else:
    print("Se permite el ingreso de numero entre el 0 y el 9 inclusive.. Vuelva a ingresar un numero.")

#----------------------------------------------------------------------------------------->

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""

for i in range(100,0-2,-2):
    print(i)

#----------------------------------------------------------------------------------------->

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

numero_usuario = int(input("Ingrese un numero entero: "))
cont = 0
if numero_usuario < 0:
    print("Ingrese un numero positivo.")
elif numero_usuario == 0:
    print("Ingrese un numero que no sea 0.")
else:    
    for i in range(0, numero_usuario + 1):
        cont += i
    print(cont)

#----------------------------------------------------------------------------------------->

""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros.

Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
"""

cont_negativos = 0
cont_positivos = 0 
cont_pares = 0
cont_inpar = 0
for i in range(100):
    num_usuario = int(input("Ingrese un numero: "))
    if num_usuario % 2 == 0:
        cont_pares += 1
    if num_usuario % 2 != 0:
        cont_inpar += 1
    if num_usuario >= 0:
        cont_positivos += 1
    if num_usuario < 0:
        cont_negativos += 1
print(f"Los numeros negativos fueron: {cont_negativos}")
print(f"Los numeros positivos fueron: {cont_positivos}")
print(f"Los numeros pares fueron: {cont_pares}")
print(f"Los numeros inpar fueron: {cont_inpar}")

#----------------------------------------------------------------------------------------->

""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
cont = 0
CANTIDAD = 100
for i in range(CANTIDAD):
    num_usuario = int(input("Ingrese un numero: "))
    cont += num_usuario
promedio = cont / CANTIDAD
print(f"El promedio de los numeros ingresados, es de: {promedio:.2f} ")

#----------------------------------------------------------------------------------------->

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero_usuario = (input("Ingrese un numero que desee: "))
cadena_vacia = ""

for i in (numero_usuario):
    cadena_vacia = i + cadena_vacia
print(cadena_vacia)

#3