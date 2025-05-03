""" Ejercicio_1) Dada una lista de numeros, genera una nueva lista con sus cuadrados.
"""

lista_numeros = [2,6,8,2,9]
lista_cuadrado = []
for i in lista_numeros:
    cuadrado_de_numero = i * i
    lista_cuadrado.append(cuadrado_de_numero)
print(lista_cuadrado)

# Con listas comprimidas.

lista_numeros = [2,6,8,2,9]
lista_cuadrado = [x**2 for x in lista_numeros]
print(lista_cuadrado)

# --------------------------------------------------->

""" Ejercicio_2) A partir de una lista, guarda solamente los numeros mayores a 10.
"""

lista_numeros = [1,2,8,5,20,10,2,46,8,100,70,23]
lista_mayores_a_10 = [i for i in lista_numeros if i > 10]
print(lista_mayores_a_10)
print(lista_numeros)

# --------------------------------------------------->

""" Ejercicio_3) Contar cuantos nombres en en una lista tienen mas de 5 letras.
"""

lista_de_nombres = ["Cain","Lautaro","Nehemias","Ruth","Gonzalo"]
contador_letras = [i for i in lista_de_nombres if len(i) > 5]
print(f"los nombres que cumplen la condiicion son: {len(contador_letras)}")