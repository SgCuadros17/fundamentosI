# # operadores aritméticos
# a= int(input("Ingrese el primer número:"))
# b= int(input("Ingrese el segundo número:"))
# suma=a+b
# resta=a-b
# multiplicacion=a*b
# # #division1 = a \\ b
# division2=a//b 
# residuo=a%b
# potenciacion=a**b
# # "F" se utiliza para imprimir variales mas cadenas de texto de manera correcta. Las variables deben ir en "{}".
# # """" Se utilizan para imprimir un resultado de varias lineas en un solo "print"
# print(f"""La suma de {a} + {b} es igual a {suma} 
#       La resta de {a} - {b} es igual a {resta} 
#       La multiplicacion de {a} * {b} es igual a {multiplicacion} 
#       La division de {a} / {b} es igual a {division2} 
#       El residuo de la division {a} % {b} es igual a {residuo}
#       La potencia de {a} ** {b} es igual a {potenciacion}""")

# # operadores relacionales
# a= int(input("Ingrese el primer número:"))
# b= int(input("Ingrese el segundo número:"))
# mayorq=a>b
# menorq=a<b
# mayoriq=a>=b
# menoriq=a<=b 
# igual=a==b
# diferente=a!=b
# print(f"""{a} es mayor que {b} = {mayorq} 
#       {a} es menot que {b} = {menorq} 
#       {a} es mayor o igual que {b} = {mayoriq} 
#       {a} es menor o igual que {b} = {menoriq} 
#       {a} es igual que {b} = {igual}
#       {a} es diferente que {b} = {diferente}""")

# operadores booleanos
# And = y; or = o; not = no
# cunjucion (And) = ambas relaciones deben ser verdaderdo, de lo contrario sera falso
# disyucion (or) = entre ambas relaciones debe haber al menos alguna verdad para ser True, de lo contrario sera False
# bicondicional = aplica igual que la ley de signos
# condicional = si la relacion entre ambas es True y False es falso, de lo contrario sirempre sera verdaderaro


#interpretar diagrama de flujo

precioCompra= float(input("Ingrese el precio de compra:"))
precioVenta=float(input("Ingrese el precio de venta:"))
ganancia=precioVenta-precioCompra
porGanancia=ganancia // precioCompra*100
print(f""" tu ganancia es de ${ganancia}
      %{porGanancia} de ganancia""")
