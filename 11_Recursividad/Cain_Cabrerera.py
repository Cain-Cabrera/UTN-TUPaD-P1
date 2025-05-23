""" Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""
def factorial_de_un_numero(numero):#4
    if numero == 1:
        return 1
    else:
        return numero * factorial_de_un_numero(numero - 1)

numero_usuario = int(input("Ingrese un numero para calcular el factorial: "))
for i in range(1,numero_usuario + 1):
    print(f"El factorial del numero {i} es: {factorial_de_un_numero(i)} ")

# ------------------------------------------------------------------------------>

""" Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0 
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

posicion_del_usuario = int(input("hasta que sucesion quiere del fibo: "))
for i in range(1,posicion_del_usuario + 1):
    print(f"En la posicion {i} es: {fibonacci_recursivo(i)} ")

# ------------------------------------------------------------------------------>

""" Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 
𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
. Prueba esta función en un
algoritmo general.
"""

def calcular_potencia_recursiva(numero,exponente):
    if exponente == 0:
        return 1
    else:
        return numero * calcular_potencia_recursiva(numero, exponente - 1)

print(calcular_potencia_recursiva(5,5))

# ------------------------------------------------------------------------------>

""" Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:

1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1 
"""

def decimal_a_binario(numero):
    if numero == 1:
        return "1"
    elif numero == 0:
        return "0"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)
    
print(decimal_a_binario(10))

# ------------------------------------------------------------------------------>

""" Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""

def es_palindromo(palabra):
    if palabra[0] != palabra[-1]:
        return False
    elif len(palabra) == 1:
        return True
    else:
        return es_palindromo(palabra[1:-1])
print(es_palindromo("reconocer"))

# ------------------------------------------------------------------------------>

""" Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
        
print(suma_digitos(154))

# ------------------------------------------------------------------------------>

""" Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.

"""

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(4))

# ------------------------------------------------------------------------------>

""" Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
"""
def contar_digito(numero,digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
print(contar_digito(5055235,5))
