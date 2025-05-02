import random


equipo1 = [input("Ingrese el nombre del Equipo 1: "), 0, 0, 0]
equipo2 = [input("Ingrese el nombre del Equipo 2: "), 0, 0, 0]

def RegistraSet(numeroEquipo):
    if numeroEquipo == 1:
        equipo1[3] += 1
    else:
        equipo2[3] += 1

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    equipo1[3] = 0
    equipo2[3] = 0
    while equipo1[3] < 3 and equipo2[3] < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()
        print("\nSet nuevo:", equipo1[0], puntos1, "-", puntos2, equipo2[0])
        if puntos1 >= 25 and puntos1 > puntos2:
            print("Gana el set", equipo1[0])
            RegistraSet(1)
        elif puntos2 >= 25 and puntos2 > puntos1:
            print("Gana el set", equipo2[0])
            RegistraSet(2)
        else:
            while True:
                extra1 = PuntosExtras()
                extra2 = PuntosExtras()
                puntos1 += extra1
                puntos2 += extra2
                print("Puntos extra:", equipo1[0], "+", extra1, "(", puntos1, ")", "-", equipo2[0], "+", extra2, "(", puntos2, ")")
                if puntos1 >= 25 and puntos1 > puntos2:
                    print("Gana el set", equipo1[0])
                    RegistraSet(1)
                    break
                elif puntos2 >= 25 and puntos2 > puntos1:
                    print("Gana el set", equipo2[0])
                    RegistraSet(2)
                    break
    if equipo1[3] == 3:
        equipo1[1] += 1
        equipo2[2] += 1
        print("\n", equipo1[0], "gana el partido!\n")
    else:
        equipo2[1] += 1
        equipo1[2] += 1
        print("\n", equipo2[0], "gana el partido!\n")

def ResultadoTorneo():
    print("\n=== Resultado del Torneo ===")
    print(equipo1[0], ": Ganados", equipo1[1], ", Perdidos", equipo1[2])
    print(equipo2[0], ": Ganados", equipo2[1], ", Perdidos", equipo2[2])

cantidad = int(input("¿Cuántos partidos deben jugar? "))
for i in range(cantidad):
    print("\n--- Partido", i+1, "---")
    JugarPartido()
ResultadoTorneo()
