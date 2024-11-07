def ingresar_participante(pos):
    nombre = input(f"Ingrese el nombre del participante {pos + 1}: ")
    nickname = input(f"Ingrese el nickname del participante {pos + 1}: ")
    edad = int(input(f"Ingrese la edad del participante {pos + 1}: "))
    ranking = int(input(f"Ingrese el ranking del participante {pos + 1}: "))
    genero = input(f"Ingrese el género del participante {pos + 1}: ")
    pais = input(f"Ingrese el país del participante {pos + 1}: ")
    return [nombre, nickname, edad, ranking, genero, pais, 0]  # Puntaje inicializado a 0

def seleccionar_torneo():
    print("Seleccione el torneo:")
    print("1. Need for Speed Heat")
    print("2. EA FC25")
    print("3. F1 25")
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            if opcion in [1, 2, 3]:
                return ["Need for Speed Heat", "EA FC25", "F1 25"][opcion - 1]
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ser un número.")

def mostrar_podium(participantes):
    print("\n--- Podium del Torneo ---")
    print("RANKING NICKNAME, PUNTOS TOTALES")

    # Ordenar participantes por puntaje (descendente)
    participantes.sort(key=lambda p: p[6], reverse=True)

    for i, participante in enumerate(participantes):
        print(f"{i + 1}. {participante[1]}, {participante[6]} puntos")  # nickname y puntaje

# Ingreso de participantes
participantes = []
for i in range(2):  # Solo dos participantes (local y visitante)
    participantes.append(ingresar_participante(i))

# Selección del torneo
torneo = seleccionar_torneo()
print(f"\nTorneo seleccionado: {torneo}")

# Ingreso de resultados de los matches
while True:
    ganador = input("Ingrese el ganador (local/visitante): ").strip().lower()
    
    if ganador == "local":
        participantes[0][6] += 5  # Aumentar puntaje del participante local
    elif ganador == "visitante":
        participantes[1][6] += 5  # Aumentar puntaje del participante visitante
    else:
        print("Ganador no válido. Intente de nuevo.")
        continue

    # Mostrar puntajes actuales
    for participante in participantes:
        print(f"{participante[1]}: {participante[6]} puntos")  # nickname y puntaje

    # Verificar si algún participante ha llegado a 30 puntos
    if participantes[0][6] >= 30 or participantes[1][6] >= 30:
        break

# Mostrar el podio
mostrar_podium(participantes)