import random, os, time, datetime, argparse

# random: Modulo que implementa la generacion de numeros random
# os: Funcionalidad del sistema
# time: Funciones relacionadas con el tiempo
# datetime: Clases para manipular fechas y tiempos
# argsparse: Implementa el uso de linea de comandos

# Variables
tiradas = 0
cara = 0
cruz = 0

# Lector del comando
parser = argparse.ArgumentParser(description="Simula un coin flip una cantidad de veces")
parser.add_argument("-n", nargs=1)  # Numero de tiradas
parser.add_argument("-o", nargs=1)  # Output visual
args = parser.parse_args()

print("Coin Flip Simulator")


# Funciones para ajustar las opciones del programa
def numero_de_tiradas():
    repeticiones = int(input("Introducir numero de tiradas a realizar: "))
    return repeticiones


def visual_output():
    visualOutputCondition = input("¿Quieres que se muestre información por pantalla? (y/n)").lower()
    return visualOutputCondition


# Funcion del coin flip
def coin_flip(ntimes):
    global tiradas, cara, cruz
    for i in range(ntimes):
        # Genera un numero entre el 0 y el 1
        flip = random.randrange(2)
        tiradas += 1
        if flip == 0:
            cara += 1
        else:
            cruz += 1
        if visual == "y":
            print(flip, end=" ")


# Argumento de número de tiradas por pantalla o por linea de comando
if args.n is None:
    times = numero_de_tiradas()
else:
    times = int(args.n[0])

# Argumento para mostrar la información por pantalla
if args.o is None:
    visual = visual_output()
else:
    visual = args.o[0].lower()

coin_flip(times)

if cara > cruz:
    print("Hay mas caras")
else:
    print("Hay mas cruces")
