import math 

""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

Añadir las siguientes frutas con sus respectivos precios:

● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

# Aca pense una funcion en agregar frutas a eleccion de el usuario, me enfoque en el codigo mas modularizado.
# Se que asignando dict['key'] = value, puedo asignar directamente mis frutas hardcodeando en este caso.

#FUNCION
def agregar_fruta(dict):
    x = 0
    while x < 3:
        key = input("Ingrese una fruta: ")
        value = int(input("Ingrese el precio de la fruta: "))
        x += 1
        dict[str(key)] = value
    return dict


# #MAIN
precio_frutas = {'banana': 1200, 'Anana':2500, 'Melon': 3000, 'Uva': 1450}
print(agregar_fruta(precio_frutas))

# # ----------------------------------------------------------------------------->

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
#FUNCION
def modificar_precio(dict,frutas_modificadas: int):
    x = 0
    while x < frutas_modificadas:
        fruta = input("Ingrese la fruta a modificar: ") 
        if fruta in dict:
            valor = int(input("Ingrese su nuevo valor: "))
            dict[fruta] = valor
            x += 1
        else:
            print("La fruta no se encuentra en el diccionario, ingrese nuevamente.")
    return dict

#MAIN 

frutas_a_modificar = int(input("Cuantas frutas va a modificar?: "))
print(modificar_precio(precio_frutas,frutas_a_modificar))

# # ----------------------------------------------------------------------------->

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.

"""

valores = precio_frutas.keys()
print(list(valores))

# # ----------------------------------------------------------------------------->

""" 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
años."

"""

class Persona:
    def __init__(self,nombre,pais,edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

usuario = Persona("Cain", "Argentina", 23)
usuario.saludar()

# # ----------------------------------------------------------------------------->

""" 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
"""

class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        print(f"El área del círculo es: {area:.2f}")

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print(f"El perímetro del círculo es: {perimetro:.2f}")

radio = Circulo(200)
radio.calcular_area()
radio.calcular_perimetro()

# # ----------------------------------------------------------------------------->

""" 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
balanceados usando una pila.
"""

class pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else "La pila está vacía"
    
    def apilar(self, elemento):
        self.elementos.append(elemento)

usuario = pila()
usuario.apilar("(")
usuario.apilar(")")




