#Ej 1
# num=int(input("Ingrese un número:"))
# if num>5:
#     print("Mayor a 5")
# else:
#     print("Menor a 5")
#---------------------------
#Ej 2
# edad=int(input("Ingresa tu edad: "))
# if edad >=18:
#     print("eres mayor de edad")
# else:
#     print("Eres menor de edad")
#----------------------------
#Ej 3
# numero= int(input("Ingrese un número: "))
# if numero % 2 == 0:
#     print("El número es par")
# else:
#     print("El número es impar")
#------------------------------
#Ej 4
# nota = 85
# if nota >= 90:
#     print("Excelente")
# elif nota >= 70:
#     print("Aprobado")
# else:
#     print("Reprobado")
#------------------------------
#Ej 5
# num=float(input("Ingrese el número: "))
# if num>0:
#     print("El número es positivo")
# elif num<0:
#     print("El número es negativo") 
# else:
#     print("El numero es cero")
#------------------------------
#Ej 6
# nota1=float(input("Ingrese su primer nota: "))
# nota2=float(input("Ingrese su segunda nota: "))
# nota3=float(input("Ingrese su tercer nota: "))
# nota4=float(input("Ingrese su cuarta nota: "))
# nota5=float(input("Ingrese su quinta nota: "))
# nota6=float(input("Ingrese su sexta nota: "))

# promedio=(nota1*0.1+nota2*0.2+nota3*0.15+nota4*0.15+nota5*0.15+nota6*0.25)

# print(f"Su promedio es: {promedio}")

# if promedio>=3.0:
#     print("¡felicidades!Aprobo el curso")
# else:
#     print("Usted reprobro el curso")
#Ej 7
nomCliente=input("Ingrese el nombre del cliente: ")
edad=int(input("Ingrese la edad del cliente: "))
gastos=float(input("Ingrese los gastos mensuales del cliente: "))

if gastos < 100:
    categoria = "Cliente Básico"
    mensaje = "Te recomendamos aprovechar nuestras ofertas y descuentos especiales."
elif 100 <= gastos <= 500:
    categoria = "Cliente Frecuente"
    mensaje = "Tienes acceso a promociones especiales cada mes."
elif 501 <= gastos <= 1000:
    categoria = "Cliente Premium"
    mensaje = "Acumulas puntos de recompensa para futuras compras."
else:
    categoria = "Cliente VIP"
    mensaje = "Disfruta de beneficios exclusivos y atención personalizada."

# Mostrar resultados
print(f"\n🎉 ¡Hola, {nomCliente}! 🎉")
print(f"🏅 Categoría: {categoria}")
print(f"💡 {mensaje}")

# Mensaje adicional según la edad
if edad < 18:
    print("👦 Revisa nuestra sección juvenil para encontrar productos a tu medida.")
else:
    print("🛍️ También puedes consultar nuestros beneficios exclusivos para adultos.")

print("\n✅ Gracias por ser parte de nuestra tienda.")
