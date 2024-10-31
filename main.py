


#Ejercicio 1. Crea una función que obtenga el máximo de una lista de números
def maximo(listanumeros):
    mayor = listanumeros[0]
    for i in range(1,len(listanumeros)):
        if listanumeros[i] > mayor:
            mayor = listanumeros[i]
    return mayor


#Ejercicio 2. Crea una función que obtenga la sumatoria de una lista de números
def sumatoria(listanumeros):
    total_sumatoria = 0
    for i in range(len(listanumeros)):
        total_sumatoria += listanumeros[i]
    return total_sumatoria


#Ejercicio 3. Crea una función que dada una distancia en millas calcule su correspondiente en kms
def distancia_en_kms(distancia_en_millas):
    return distancia_en_millas * 1.609344


#Ejercicio 4. Crea una función que determina si una letra es una vocal
def es_vocal(isvalid): #Lo Declaramos, (es un booleano)
    return isvalid in ['a','e','i','o','u']
    #retornara true si la letra que le pasas esta en esa lista si no esta devuelve false


#Ejercicio 5. Crea una función que cuenta la cantidad de números pares de una lista de números.
def contar_pares(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            cont += 1
    return cont

#Ejercicio 6. Crea una función que dados un número y un intervalo (inicio, fin) cuente la cantidad de múltiplos del número en dicho intervalo
def contar_multiplos(numero, inicio, fin):
    cont = 0
    for i in range(inicio,fin+1):
        if i % numero == 0:
            cont += 1
        else:
            cont += 0
    return cont

#Ejercicio 7. Crea una función que dada la longitud de los tres lados de un triángulo determine si el triangulo es rectángulo
def es_triangulo_rectangulo(ladoa, ladob, ladoc):
    if ladoa > ladob and ladoa > ladoc:
        hipotenusa = ladoa
        cateto1 = ladob
        cateto2 = ladoc
    elif ladob > ladoa and ladob > ladoc:
        hipotenusa = ladob
        cateto1 = ladoa
        cateto2 = ladoc
    else:
        hipotenusa = ladoc
        cateto1 = ladoa
        cateto2 = ladob


    return hipotenusa ** 2 == cateto1 ** 2 + cateto2 ** 2

#Ejercicio 8. Crea una función que calcule el máximo común divisor de dos números naturales
def maximo_comun_divisor(numero1, numero2):
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1

#Ejercicio 9. Crea una función que dado un número n imprima los siguientes ‘mosaicos’:
def imprimir_mosaicos(numero1):
    for i in range(1, numero1 + 1):
        print(str(i) * i)

#Ejercicio 10. Crea una función que imprima un mosaico rombo de anchura variable.

def imprimir_rombo(anchura):
    # Parte superior del rombo
    for i in range(anchura):
        print(' ' * (anchura - i - 1) + '*' * (2 * i + 1))

    # Parte inferior del rombo
    for i in range(anchura - 2, -1, -1):
        print(' ' * (anchura - i - 1) + '*' * (2 * i + 1))


print("Ejercicio 1 : ",maximo([1,2,3,4,5]) )
print("Ejercicio 2 : ",sumatoria([1,2,3,4,5]) )
print("Ejercicio 3 : ",distancia_en_kms(10) )
print("Ejercicio 4 : ",es_vocal('t') )
print("Ejercicio 5 : ",contar_pares([1,2,3,4,5]) )
print("Ejercicio 6 : ",contar_multiplos(2,1,12) )
print("Ejercicio 7 : ",es_triangulo_rectangulo(3,3,3) )
print("Ejercicio 8 : ",maximo_comun_divisor(10,5) )
print("Ejercicio 9 : ")
imprimir_mosaicos(5)
print("Ejercicio 10 : ")
imprimir_rombo(2)


##JUEGO DE PIEDRA , PAPEL O TIJERA
import random


def obtener_eleccion_maquina():
    return random.choice(['piedra', 'papel', 'tijera'])


def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == 'piedra' and maquina == 'tijera') or \
            (jugador == 'papel' and maquina == 'piedra') or \
            (jugador == 'tijera' and maquina == 'papel'):
        return "Jugador"
    else:
        return "Máquina"


def jugar_piedra_papel_tijera():
    puntaje_jugador = 0
    puntaje_maquina = 0
    while puntaje_jugador < 3 and puntaje_maquina < 3:
        jugador = input("Elige: piedra, papel o tijera: ").strip().lower()
        while jugador not in ['piedra', 'papel', 'tijera']:
            jugador = input("Entrada no válida. Por favor, elige: piedra, papel o tijera: ").strip().lower()

        maquina = obtener_eleccion_maquina()
        print(f"La máquina eligió: {maquina}")

        resultado = determinar_ganador(jugador, maquina)
        if resultado == "Jugador":
            print("¡Ganaste!")
            puntaje_jugador += 1
        elif resultado == "Máquina":
            print("¡Perdiste!")
            puntaje_maquina += 1
        else:
            print("¡Empate!")

        print(f"Tu puntaje: ",puntaje_jugador)
        print(f"Puntaje de la máquina: ",puntaje_maquina)

    if puntaje_jugador == 3:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("La máquina ganó el juego. ¡Inténtalo de nuevo!")

    volver_a_jugar = input("¿Quieres volver a jugar? (sí/no): ").strip().lower()
    if volver_a_jugar == 'sí':
        jugar_piedra_papel_tijera()
    else:
        print("¡Gracias por jugar!")


print("Empieza el juego")
jugar_piedra_papel_tijera()


## ADIVINA EL NÚMERO SECRETO

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinar cuál es!")

    while not adivinado:
        intento = input("Tu intento: ")

        # Verificamos que la entrada sea un número válido
        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        # Aumentar el contador de intentos
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. ¡Inténtalo de nuevo!")
        elif intento > numero_secreto:
            print("Demasiado alto. ¡Inténtalo de nuevo!")
        else:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

    volver_a_jugar = input("¿Quieres volver a jugar? (sí/no): ").strip().lower()
    if volver_a_jugar == 'sí':
        adivina_el_numero()
    else:
        print("¡Gracias por jugar!")

adivina_el_numero()
