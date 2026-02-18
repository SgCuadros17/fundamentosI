#variables type lista "[]" y type diicionario
# personas={"nombre": "edad", "edad": 30, "ciudad": "medellin"}
# print(f"tu nombre es {personas['nombre']}, y tienes {personas['edad']} y vives en {personas['ciudad']}")
#---------------------------------------------------------
#reglas para definir un variable en Python
#Deben empezar con letra o gion bajo(no puede iniciar con números)


#Concatenación de Cadenas (Strings)
#-------------------------------------------
#Las variables de tipo `string` pueden combinarse con el operador `+`:
# nombre = "Sofía"
# apellido = "Martínez"
# nombre_completo = nombre + " " + apellido  # Concatenación
# print(nombre_completo)  # Salida: Sofía Martínez
#-----------------------------------------
#También se pueden usar f-strings para formatear textos:
# nombre= "sebastian"
# edad = 22
# mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
# print(mensaje)
#------------------------------------------
#variables type contador:
# contador = 0
# contador += 1  # Es lo mismo que: contador = contador + 1
# print("Contador actualizado:", contador)
#-------------------------------------------
# *Listas "list"
#Estructura ordenada y mutable que almacena varios elementos.
# frutas = ["Manzana", "Banana", "Cereza"]
#Operaciones con listas
# frutas.append("Naranja")  # Agregar un elemento
# frutas.append("Sandia")  # Agregar un elemento
# frutas.remove("Banana")   # Eliminar un elemento
# print(frutas[2])          # Acceder al primer elemento ('Manzana')
#--------------------------------------------
### Tuplas (tuple)
#Estructura ordenada e inmutable (no se puede modificar después de su creación).
#coordenadas = (10, 20)
#print(type(coordenadas))  # <class 'tuple'>
#-----------------------------------------------
## **Conjuntos (`set`)**
# Estructura **no ordenada** y **sin elementos duplicados**.
# numeros = {1, 2, 3, 3, 4}
# print(numeros)  # {1, 2, 3, 4}
# Operaciones con conjuntos
# numeros.add(5)     # Agregar un elemento
# numeros.remove(2)  # Eliminar un elemento
# #-----------------------------------------
# ## Diccionarios (dict)
# Estructura de datos que almacena pares clave-valor.
# persona = {"nombre": "Juan", "edad": 25, "Ciudad": "Medellin"}
# # <class 'dict'>
# # Acceder y modificar valores**
# #print(persona["nombre"])  # imprime 'Juan'
# # persona["edad"] = 26      # Modificar un valor
# persona["Universidad"] = "UPB" #add una nueva clase valor
# #del persona ["Ciudad"]  #del = eliminar una clave
# #Universidad =persona.get("Universidad", "Dato no encontrado") #.get buscar un valor en especifico
# print(persona.keys()) #obtener todas las llaves
# print(persona.values()) # Obtener todos los valores
# print(persona.items()) # Obtener todos los pares clave-valor

