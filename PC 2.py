#Problema 1:
#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

#Problema 2:
#Escriba un programa en Python para construir el siguiente patrón.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5  # Puedes ajustar este valor para cambiar la altura del patrón

# Imprimir la mitad superior del patrón
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Imprimir la mitad inferior del patrón
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#Problema 3:
#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números.
# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de números pares e impares.
# Ejemplo:
# “Desea ingresar un número?”: SI
# “Ingrese el número:” 5
# “¿Desea ingresar un número?”: SI
# “Ingrese el número: ” 7

# “Desea ingresar un número?”: NO
# Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
# Cantidad de números pares: 5
# Cantidad de números impares: 4
# Nota:
# - Quizás a manera de ayuda el uso de una lista le sea de utilidad.
# - El empleo de break sobre condiciones while también le serán de utilidad.

numeros = []
contador_pares = 0
contador_impares = 0

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta == "NO":
        break
    elif respuesta == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)

            if numero % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    else:
        print("Respuesta no válida. Por favor, ingrese SI o NO.")

print(f"\nNúmeros ingresados: {numeros}")
print(f"Cantidad de números pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_impares}")

#Problema 4:
#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.
# Puede usar el siguiente esquema a manera de ejemplo
#  {
#  Alumno: Juan,
#  Notas: [10, 12, 15]
#  }
# Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
# completo de los alumnos.
# Nota:
# El uso de listas con diccionarios le será de utilidad.

alumnos = []

n = int(input("Ingrese el número de alumnos: "))

for i in range(n):
    alumno = input("\nNombre del alumno: ")
    notas = [float(input(f"Nota {j + 1}: ")) for j in range(3)]

    datos_alumno = {"Alumno": alumno, "Notas": notas}
    alumnos.append(datos_alumno)

# Mostrar listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno_info in alumnos:
    print(f"{alumno_info['Alumno']} - Notas: {alumno_info['Notas']}")

#Problema 5:
#Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
#Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
# Ejemplo:
# Número ingresado: 15789000 y Dígito: 0
# Cantidad de veces 0 en el número: 4
# Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método count.

def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad

# Ejemplo de uso
numero_ingresado = 15789000
digito_ingresado = 0

cantidad_veces = contar_digitos(numero_ingresado, digito_ingresado)

print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_ingresado}")
print(f"Cantidad de veces {digito_ingresado} en el número: {cantidad_veces}")

#Problema 6:
#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
#Nota: La secuencia de Fibonacci es la serie de números:
#0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
#Cada número siguiente se obtiene sumando los dos números anteriores.

def fibonacci(n):
    fib_series = [0, 1]

    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

# Obtener la serie de Fibonacci hasta 50
resultado = fibonacci(50)

print("Serie de Fibonacci hasta 50:")
print(resultado)

#Problema 7:
#Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        # Verificar divisibilidad desde 3 hasta la raíz cuadrada del número
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")

# Problema 8:
# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
# función acepta el número como argumento.

def factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

resultado_factorial = factorial(numero_ingresado)

print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")

#Problema 9:
#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.
# Ejemplo:
# - Input: Twitter Output: Twttr
# - Input: What's your name? Output: Wht's yr nm?

def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    resultado = ""

    for char in cadena:
        if char not in vocales:
            resultado += char

    return resultado

# Ejemplo de uso
texto_ingresado = input("Ingrese una cadena de texto: ")

resultado_sin_vocales = omitir_vocales(texto_ingresado)

print(f"Texto original: {texto_ingresado}")
print(f"Texto sin vocales: {resultado_sin_vocales}")

#Problema 10:
#En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
#fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
#lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
#en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
#ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de 1636!
#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en la lista abajo:

#["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

#Luego, genere esa misma fecha en formato AAAA-MM-DD.
# Ejemplos:
# - Input: 9/8/1636 | Output: 1636-09-08
# - Input: Septiembre 8, 1636 | Output: 1636-09-08
# - Input: 1/1/1970 | Output: 1970-01-01
# Nota:
# - Los métodos de listas y string le resultarán de gran utilidad.
# - Nota que si empleamos print(f"{n:02}") , esta completará con 0 valos a la izquierda de un número

def formatear_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    try:
        # Intentar convertir la fecha en formato mes/día/año
        fecha_parts = fecha.split("/")
        mes = int(fecha_parts[0])
        dia = int(fecha_parts[1])
        anio = int(fecha_parts[2])

    except ValueError:
        # Si no se puede convertir, intentar con el formato "Mes dia, año"
        for i, nombre_mes in enumerate(meses, start=1):
            if nombre_mes in fecha:
                mes = i
                dia, anio = map(int, fecha.replace(",", "").split()[-2:])
                break

    # Formatear la fecha como AAAA-MM-DD
    fecha_formateada = f"{anio:04d}-{mes:02d}-{dia:02d}"
    return fecha_formateada

# Ejemplo de uso
fecha_ingresada = input("Ingrese una fecha (en formato mes/día/año o Mes dia, año): ")

fecha_formateada = formatear_fecha(fecha_ingresada)

print(f"Fecha ingresada: {fecha_ingresada}")
print(f"Fecha formateada: {fecha_formateada}")






