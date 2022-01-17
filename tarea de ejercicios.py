#Integrantes:
#Vanessa Alejandra Garcia Cortez 
#Dayana Mirle Quintana Moreira
#Ariel David Perez Castro


#Ejercicios para practicar la estructura de control de bucle o repetición condicional (while) usando Python.

#1
#!Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# !Finalmente, mostrar la sumatoria de todos los números ingresados.

total=0
nro=int(input("Número: "))
while nro != 0:
    total+=nro
    nro=int(input("Número: "))

#2
#!Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
#!Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

positivos=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        positivos+=1
    n=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", positivos)

#3
#!Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
#!Informar cuál fue el mayor número ingresado.

mayor=-1
n=int(input("Número positivo:"))
while n>=0:
   if n>mayor:
       mayor=n
   n=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)

#4
#!Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("Suma de los dígitos:", suma)

#5
#!Solicitar al usuario que ingrese números enteros positivos y, 
#!por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. 
#!Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

pares=0
n=int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        pares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("Suma de sus dígitos:", suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares")

#6
#!Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
#!A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
#!Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, 
#!permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, 
#!se interrumpirá la impresión del menú y el programa finalizará.

while True:
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion=int(input("Opción elegida: "))
    if opcion==1:
        print("¡Comenzamos!")
    elif opcion==2:
        print("Listado:")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la próxima")
        break
    else:
        print("Opción incorrecta. Debe ingresar 1, 2 o 3")
#7
#!Solicitar al usuario el ingreso de una frase y de una letra 
#!(que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
#!Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
#!Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

frase=input("Frase: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("No se encontró en la posición", i)
        i+=1
        continue
    print("Se encontró en la posición", i)
    break

#8
#!Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# !(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# !cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#!Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
#!Al finalizar, informar el total a pagar teniendo que cuenta que, 
#!si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total)

#9
#!Crear un programa que solicite el ingreso de números enteros positivos, 
#!hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#!Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

numero=int(input("numero: "))
totalPares=0
totalImpares=0
while numero!=0:
   pares=0
   impares=0
   while numero!=0:   
       ultimodigito=numero%10
       if ultimodigito%2==0:
           pares+=1
           totalPares+=1
       else:
           impares+=1
           totalImpares+=1
       numero=numero//10
   print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
   numero=int(input("Otro número: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)

#Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). 
# Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) 
# se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
# aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron.
# **Ejemplo de ejecución:**
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.

lineas=0
digitos="0123456789"
cantidadDigitos=0
cadena=input("Cadena: ")
while cadena!="*":
    for caracter in cadena:
        if caracter in digitos:
            cantidadDigitos+=1
    if cadena=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    cadena=input("Cadena: ")
print("Se leyeron ",lineas," líneas completas")

#11
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

cantidad=0
n=int(input("Número: "))
while n!=0:
 primo=True
 for i in range(2,n):
   if n%i==0:
     primo=False
     break
 if primo:
   cantidad+=1
 n=int(input("Número: "))
print("primos: ", cantidad)

#12
# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
# Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

frase=input("Frase: ").strip()
cantidad=0
len_p_mas_larga=0
while len(frase) != 0:
    cantidad=cantidad+1
    i=frase.find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra más larga:", p_mas_larga)
print("Cantidad de palabras:", cantidad)

#10 Ejercicios para practicar programación usando funciones, con Python.

#1
# Solicitar al usuario que ingrese su dirección email. 
# Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@".

def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False

#programa principal
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")

#2
# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

#!programa principal
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))

#3
# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.
def sumaDigitos(numero):
  suma=0
  while numero!=0:
    digito=numero%10
    suma=suma+digito
    numero=numero//10
  return suma

#!programa principal
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))

#4
# Requerir al usuario que ingrese un número entero e informar si es primo o no, 
# utilizando una función booleana que lo decida.

def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

#!programa principal
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")

#5
# Solicitar al usuario un número entero y luego un dígito. 
# Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

#!programa principal
num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))

#6 
# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, 
# al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

#!programa principal
cantidad=0
num=int(input("Número (-1 para cortar): "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad,"números")

#7 
# Escribir un programa que pida números positivos al usuario. 
# Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números 
# cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#!programa principal
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
          mayor=suma
          n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
print("Cantidad con sumatoria menor a 10:",cantidad)

#8 
# Solicitar al usuario el ingreso de números primos. 
# La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos. 
# También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#!programa principal
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
          mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))