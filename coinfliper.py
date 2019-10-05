import random, os, time, datetime, argparse
    #random: Modulo que implementa la generacion de numeros random
    #os: Funcionalidad del sistema
    #time: Funciones relacionadas con el tiempo
    #datetime: Clases para manipular fechas y tiempos
    #argsparse: Implementa el uso de linea de comandos

#Variables


#Lector del comando
parser = argparse.ArgumentParser(description="Simula un coin flip una cantidad de veces")
parser.add_argument("-n", nargs=1) #Numero de tiradas
parser.add_argument("-o", nargs=1) #Output visual

print("Coin Flip Simulator")

def numeroDeTiradas():
    repeticiones = int(input("Introducir numero de tiradas a realizar: "))
    return repeticiones

def visualOutput():
    visualOutput = input("¿Quieres que se muestre información por pantalla? (y/n)").lower()
    return visualOutput

if args.n == None:
    times = numeroDeTiradas()
else
    times = int(args.n[0])