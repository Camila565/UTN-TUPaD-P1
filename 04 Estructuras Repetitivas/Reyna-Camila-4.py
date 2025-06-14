print("///////////////////// Ejercicio1 //////////////////////////////")
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101,1):
    print(i)

print("///////////////////Ejercicio 2 ////////////////////////////////")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un número entero: "))
digitos = len(str(num))
print("El número tiene", digitos, "dígitos.")

print("///////////////////// Ejercicio 3 //////////////////////////////")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 +1, num2):
    suma += i

print("La suma de los números entre", num1 ,"y", num2, "es: ", suma)

print("/////////////////////// Ejercicio 4 ////////////////////////////")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

valor = int(input("Ingrese un número o para detener el programa ingrese un 0: "))
suma = 0
while valor != 0:
    suma += valor
    valor = int(input("Ingrese otro número o 0 para finalizar: "))

print("La suma total es: ", suma)


print("////////////////////// Ejercicio 5 /////////////////////////////")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

acierto = 6
intentos = 0

num = int(input("Adivine el número del 0 al 9: "))
intentos += 1

while num != acierto:
    num = int(input("No acertó, siga intentando: "))
    intentos += 1

print("Acertó, el número es: " , acierto)
print("Acertó, lo logró en: ", intentos, "intentos.")

print("/////////////////////// Ejercicio 6 ////////////////////////////")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,-1,-2):
    print(i)

print("////////////////////// Ejercicio 7 /////////////////////////////")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

suma = 0
num = int(input("Ingrese un número positivo: "))
for i in range(num + 1):
    suma += i

print("La suma de todos los números desde 0 hasta ", num, "es: ", suma)

print("/////////////////////// Ejercicio 8 ////////////////////////////")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

total_numeros = 5

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(total_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Resultados: ")
print("Cantidad de número pares: ", pares)
print("Cantidad de número impares: ", impares)
print("Cantidad de número positivos: ", positivos)
print("Cantidad de número negativos: ", negativos)

print("/////////////////////// Ejercicio 9 ////////////////////////////")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 2

suma_total = 0
contador = 1

while contador <= cantidad_numeros:
    print("Número", contador)
    numero = int(input("Ingrese un número entero: "))
    suma_total += numero
    contador += 1
    media = suma_total / cantidad_numeros

print("La media de los", cantidad_numeros, "números es: ", media)

print("///////////////////// Ejercicio 10 //////////////////////////////")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

digito = int(input("Ingrese un número entero de dos o más dígitos: "))
numero_invertido = int(str(digito)[::-1])

print("Número invertido: ", numero_invertido)

print("///////////////////// FIN ///////////////////////////////")