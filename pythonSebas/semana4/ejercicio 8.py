# #                                               **Variables en Python: Tipo Contador y Acumulador**

# En programación, existen variables especiales llamadas **contadores** y **acumuladores**, que permiten llevar el control de repeticiones o sumar valores en un proceso iterativo.

# #                                                              **Variable Contador**

# Un **contador** es una variable que **aumenta o disminuye en un valor constante** en cada iteración de un ciclo. Se usa comúnmente para contar repeticiones.

# ### **Características:**

# - Se inicia en un valor (por lo general 0 o 1).
# - Se actualiza en cada iteración con un incremento o decremento fijo.
# - Se usa dentro de bucles como `while` o `for`.

# WHILE ----> (Mientras que) condiccion de repeticion se cumpla = Haga
# For ----> (Para) que suele utilizarse en los arrewglos o listas

# #----------------------------------
# contador = 1  # Inicialización

# while contador <= 5:  # Condición de repetición
#     print("Número:", contador)
#     contador += 1  # Incremento del contador
#-------------
#                                                               **Variable Acumulador**
# Un **acumulador** es una variable que **suma o resta valores** en cada iteración de un ciclo. Se usa para calcular sumas totales, promedios, etc.

# ### **Características:**

# - Se inicia en 0 (o en otro valor inicial adecuado).
# - Se incrementa o decrementa con un valor variable en cada iteración.
# - Se usa en procesos como sumas acumuladas o almacenamiento de datos.

# acumulador = 0  # Inicialización

# for i in range(1, 6):  # Iteración de 1 a 5
#     acumulador += i  # Suma acumulativa

# print("Suma total:", acumulador) #
# #---------------------
# total = 0
# contador = 0

# while contador <5:
#     numero =int(input("Ingrese un numero: "))
#     total += numero
#     contador +=1

# promedio = total/contador
#---------------------
#Ej 1 
# contador = 0
# acomulador = 0
# while contador <=20:
#     print("el numero", contador)
#     contador +=2
#     acomulador += contador 

# print("la suma total:", acomulador)
# #---------------------
# #Ej 2
# suma = 0

# while suma <100:
#     numero= int(input("Ingrese el número: "))
#     suma += numero 

# print("la sumatorio de los números es:", suma)
#-------------------
tabla = 7
inicio = 1

while inicio <=10:
    resultado = tabla * inicio
    print (tabla, "*", inicio, "=", resultado)
    inicio +=1

print("el producto de la multiplicación es:", resultado)
