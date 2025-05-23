from statistics import mode, median, mean
import random

""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
edad_usuario = int(input("Ingrese su edad: ")) 
if edad_usuario >= 18:
        print("Es mayor de edad")
else:
        print("Es menor de edad, no ingresa..")
# ------------------------------------------------------------------------------>
"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
"""
nota_usuario = int(input("Ingrese la nota de su ultimo parcial: "))
if nota_usuario >= 6:
        print("Aprobado")
else:
        print("Desaprobado")


# ------------------------------------------------------------------------------>

""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
"""

num_usuario = int(input("Ingrese un numero: "))
if num_usuario % 2 == 0:
    print("Ah ingresado un numero par.")
else:
    print("Ah ingresado un numero inpar.")

# ------------------------------------------------------------------------------>

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""

edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario < 12:
        print("Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
        print("Adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
        print("Adulto/a")
else:
        print("Adulto/a")

# ------------------------------------------------------------------------------>

""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

password = input("Ingrese la contraseña: ")
if len(password) >= 8 and len(password) <= 14:
        print("Contraseña correcta")
else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# ------------------------------------------------------------------------------>

""" La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:

● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.

Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

"""

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)

print("Teniendo en cuenta la lista de numeros al azar.. vamos a calcular cada metodo!")

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
        print("Sesgo positivo")
elif media < mediana and mediana < moda:
        print("Sesgo negativo")
else:
        if media == mediana and moda:
        print("No hay sesgo")

# ------------------------------------------------------------------------------>


""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""
cadena_user = input("Ingrese una frase/palabra: ").lower()
vocales = ["a","e","i","o","u"]
if cadena_user[-1] in vocales:
        print(cadena_user + "!")
else:
        print(cadena_user)

# ------------------------------------------------------------------------------>


""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.

"""

nombre = input("Ingrese su nombre: ")
opcion = input(f"\n '1' --> Si quiere su nombre en mayúsculas \n '2' --> Si quiere su nombre en minúsculas / \n '3' --> Si quiere su nombre con la primera letra mayúscula \n -->  ") 
match opcion:
        case "1":
                nombre = nombre.lower()
                print(nombre)
                
        case "2":
                nombre = nombre.upper()
                print(nombre)
        
        case "3":
                nombre = nombre.title()
                print(nombre)


# ------------------------------------------------------------------------------>


""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:

● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

"""
terremoto = float(input("De que magnitud fue el terremoto dentro de la escala de Richter: "))

if terremoto < 3:
        print("Muy leve (imperceptible)")
elif terremoto >= 3 and terremoto < 4:
        print("Leve (ligeramente perseptible)")
elif terremoto >= 4 and terremoto < 5:
        print("Moderado (sentido por personas, perp generalmente no causa daños)")
elif terremoto >= 5 and terremoto < 6:
        print("Fuerte (puede causar daños en estructuras debiles")
elif terremoto >= 6 and terremoto < 7:
        print("Muy fuerte (puede causar daños significativos). ")
else:
        print("Extremo (puede causar graves daños a gran escala)")


# ------------------------------------------------------------------------------>

""" 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año..
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""

hemisferio = input("En que hemisferio se encuentra (N/S): ").lower()
mes = input("Que mes del año: ").lower()
dia = int(input("Que dia exactamente: "))

if hemisferio == "n":
        if mes == "diciembre":
                if dia >= 21 and dia <= 31:
                        print("Invierno")
                elif dia >= 1 and dia <= 20:
                        print("Otoño")

        elif mes == "marzo":
                if dia >= 1 and dia <= 20:
                        print("invierno")
                elif dia >= 21 and dia <= 31:
                        print("Primavera")
        elif mes == "junio":
                if dia >= 1 and dia <= 20:
                        print("Primavera")
                elif dia >= 21 and dia <= 31:
                        print("Verano")
                
        elif mes == "septiembre":
                if dia >= 1 and dia <= 20:
                        print("Verano")
                elif dia >= 21 and dia <= 31:
                        print("Otoño")

elif hemisferio == "s":
        if mes == "diciembre":
                if dia >= 21 and dia <= 31:
                        print("Verano")
                elif dia >= 1 and dia <= 20:
                        print("Primavera")

        elif mes == "marzo":
                if dia >= 1 and dia <= 20:
                        print("Verano")
                elif dia >= 21 and dia <= 31:
                        print("Otoño")
        elif mes == "junio":
                if dia >= 1 and dia <= 20:
                        print("Otoño")
                elif dia >= 21 and dia <= 31:
                        print("Invierno")
                
        elif mes == "septiembre":
                if dia >= 1 and dia <= 20:
                        print("Invierno")
                elif dia >= 21 and dia <= 31:
                        print("Primavera")
