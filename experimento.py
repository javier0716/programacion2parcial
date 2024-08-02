import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinanza = None

    print("¡Bienvenido al juego de adivinanza!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")

    while adivinanza != numero_secreto:
        try:
            adivinanza = int(input("Ingresa tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

adivina_el_numero()