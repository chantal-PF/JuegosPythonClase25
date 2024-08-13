

from random import randint

def adivina_el_numero():
    numero_secreto = randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        distancia = abs(numero_secreto - intento)
        
        if intento < numero_secreto:
            if distancia <= 10:
                print("Demasiado bajo y estas cerca, intentalo de nuevo.")
            else:
                print("Demaasiado bajo y estas lejos, intentalo de nuevo.")
        elif intento > numero_secreto:
            if distancia <= 10:
                print("Demasiado alto y estas cerca, intentalo de nuevo.")
            else:
                print("Demaasiado alto y estas lejos, intentalo de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()