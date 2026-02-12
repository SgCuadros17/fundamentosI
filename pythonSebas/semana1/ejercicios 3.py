#algoritmo secuencial
# base=float(input("Ingrese la base:"))
# altura=float(input("Ingrese la altura:"))
# area= (base*altura)/2
# print(f"el área del triangulo es: {area}")

#algoritmo modular
# "def" y ":" definir funciones 
# def leer_datos():
#     base=float(input("Ingrese base:"))
#     altura=float(("ingrese altura:"))
#     return base, altura

# def calcular_area(base, altura):
#     return (base*altura)/2

# base, altura= leer_datos()
# area= calcular_area(base,altura)
# print (f"El área del triangulo es: {area}")

#ejercicio1
# def leer_datos():
#     edad=int(input("Ingresa tu edad:"))
#     return edad

# edad= leer_datos()
# print (f"Tienes {edad} años. Bienvenido al mundo de la programción")

#ejercicio2
# def leer_datos():
#     num=int(input("Ingrese el primer número:"))
#     num2=int(input("ingrese el segundo número:"))
#     return num, num2

# def calcular_suma(num,num2):
#     suma= (num+num2)
#     return suma

# num, num2= leer_datos()
# resultado= calcular_suma(num,num2)
# print (f" la suma de {num} + {num2} es: {resultado}")

#ejercicio3
# def leer_datos():
#     num=int(input("Ingrese el primer número:"))
#     num2=int(input("ingrese el segundo número:"))
#     num3=int(input("ingrese el tercer número:"))
#     return num, num2,num3

# def calcular_promedio(num,num2,num3):
#     promedio= (num+num2+num3)/3
#     return promedio

# num, num2, num3= leer_datos()
# resultado= calcular_promedio(num,num2,num3)
# print (f" El promedio de {num}, {num2}, y {num3} es: {resultado}")

#ejercicio4
def leer_datos():
    gradosC=float(input("Ingrese sus grados celsius:"))
    return gradosC

def calcular_grados(gradosC):
    grados_f= (gradosC*9)/5+32
    return grados_f

gradosC= leer_datos()
grados_f= calcular_grados(gradosC)
print (f"{gradosC} grados celsius son igual a {grados_f}")