
"""
Program: Gran Carrera del Kilómetro
Version: 1.0 alpha
Author: Emiliano Vivas Rodríguez
Contact: a01424732@tec.mx
Date: 2021/11/23
"""

import random, time, os

turno, corral, caballos, nombres, LIMITE = 1, None, [{"nombre": '\u0000', "distancia": 0}], ["Babieca", "Solovino", "Casimiro", "Doroteo", "Silviano", "Bimbollo", "Cacahuate", "Maní", "Molito", "Humberto", "Froebel", "Pistacho", "Quesillo", "Ukelele", "Batata", "Chipotle", "Galleta", "Nutella", "Manzana", "Paca", "Padrino", "Madrina", "Torombolo", "Arepa", "Frijol", "Frijolito", "Totopo", "Bolillo", "Telera", "Dinamita", "Jefazo", "Confleis"], 11

def imprimirEstado():
    print("\n\n\n\u2658 \u2690\tGran Carrera del Kilómetro.\n\n", turno, "° turno.", sep = '\u0000', end = 4*"\n" + 205*'_' + 2*"\n" + "\t")
    for index in range(LIMITE): print("\t", index*100, "m.", sep = "\u0000", end = "\t|")
    print("\t" + 3*"\u2691 ", 205*"_", sep = "\n", end=3*"\n")
    for index in range(len(caballos)):
        print(caballos[index]["nombre"] + "\t" if len(caballos[index]["nombre"]) < 7 else caballos[index]["nombre"], "\t", end="\u0000")
        for i in range(len(corral[0])): print(corral[index][i], end = 2*"\t")
        print(end=2*"\n")
    print(205*'_', end = "\u0000")

def actualizarEstado():
    global corral
    corral = []
    for index in range(len(caballos)):
        jinete = []
        for i in range(caballos[index]["distancia"]): jinete.append('\u0000')
        jinete.append('\u265e')
        for i in range(len(jinete), LIMITE): jinete.append("\u0000")
        corral.append(jinete)

def comenzar():
    global caballos, corral
    caballos[0]["nombre"] = input("\n\n\n\u2658 \u2690\tGran Carrera del Kilómetro.\n\nBienvenido a la carrera para los jinetes más experimentados en aritmética.\n\n¿Cuál es el nombre de su caballo? \u2658\n")
    index = int(input("\n¿Con cuántos participantes deseas concursar en la carrera?\n")) + 1
    corral = index * [ LIMITE * ['\u0000']]
    corral[0][0] = '\u265e'
    print("\nTu posición es la primera. Mucha suerte, ", caballos[0]["nombre"], ".\n¡Venga! ¡Comencemos con la competencia! \u2691", sep = "\u0000", end = 3*"\n")
    for index in range(1, index):
        i = random.randint(0, len(nombres) - 1)
        caballos.append({"nombre": '\u0000', "distancia": 0})
        caballos[index]["nombre"] = nombres[i] if len(corral) > len(nombres) else nombres.pop(i)
        corral[index][0] = '\u265e'

def desafiar():
    global turno
    operacion = ('+' if random.randint(0,10)%2==0 else '-') if random.randint(0, 1) == 0 else ('x' if random.randint(0,10)%2==0 else '/')
    numeros = [random.randint(-50, 50), random.randint(-10, 10)]
    if operacion == '/':
        while numeros[1] == 0 or numeros[0] % numeros[1] != 0: numeros = [random.randint(-50, 50), random.randint(-10, 10)]
    resultado = float(input("\n\nReto a superar:\n" + str(numeros[0]) + ' ' + operacion + ' ' + str(numeros[1]) + " = "))
    if (operacion == '+' and resultado == numeros[0] + numeros[1]) or (operacion == '-' and resultado == numeros[0] - numeros[1]) or (operacion == 'x' and resultado == numeros[0] * numeros[1]) or (operacion == '/' and resultado == numeros[0] / numeros[1]):
        caballos[0]["distancia"] += 1
        print("\n\u2714   Respuesta correcta.", end = "\u0000")
    else: print("\n\u2717   Respuesta incorrecta.", end = "\u0000")
    turno += 1

def actualizarDistancia():
    for index in range(1, len(caballos)):
        if random.randint(0,1) == 0: caballos[index]["distancia"] += 1

def verificarDistancia():
    for index in range(len(caballos)):
        if caballos[index]["distancia"] > LIMITE - 1: return False
    return True

def main():
    os.system("cls")
    time.sleep(0.5)
    comenzar()
    time.sleep(3.5)
    while(verificarDistancia()):
        os.system("cls")
        imprimirEstado()
        desafiar()
        actualizarDistancia()
        actualizarEstado()
        time.sleep(1)
    print(5*"\n" + 15*'_\t', end = 3*"\n")
    if caballos[0]["distancia"] > LIMITE - 1: print("¡Felicidades, jinete!", caballos[0]["nombre"], "y tú son un excelente equipo. ¡Enhorabuena! \u265a \u265e")
    else: print("Lo siento, jinete.", caballos[0]["nombre"], "y tú no lo han conseguido. ¡Suerte para la próxima! \u261b \u261a")
    print("\nContestaron ", caballos[0]["distancia"], " respuesta"+ ('s' if caballos[0]["distancia"] != 1 else "\u0000") +" correctamente.\n", turno - caballos[0]["distancia"] - 1, " reto"+ ('s' if turno - caballos[0]["distancia"] - 1 != 1 else "\u0000") +" no han sido satisfactorios.", sep="\u0000", end = 3*"\n")

main()