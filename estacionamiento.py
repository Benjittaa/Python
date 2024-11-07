class Cliente:
    def __init__(self, nombre, patente, hora_inicio, hora_salida):
        self.nombre = nombre
        self.patente = patente
        self.hora_inicio = hora_inicio
        self.hora_salida = hora_salida

def calcular_costo(hora_inicio, hora_salida, valor_por_minuto):
    # Calcular la duración en minutos
    tiempo_total = (hora_salida - hora_inicio).total_seconds() / 60
    return tiempo_total * valor_por_minuto

from datetime import datetime

def obtener_hora(mensaje):
    while True:
        try:
            hora_str = input(mensaje)
            hora = datetime.strptime(hora_str, '%H:%M')
            return hora
        except ValueError:
            print("Formato de hora incorrecto. Por favor, ingrese la hora en formato HH:MM.")

def main():
    # Ingresar la cantidad de plazas disponibles
    plazas = int(input("Ingrese la cantidad de plazas para aparcar: "))
    clientes = []
    
    # Definir el valor por minuto
    valor_por_minuto = 25.0

    while True:
        if len(clientes) >= plazas:
            print("No hay plazas disponibles. No se puede agregar más clientes.")
            break

        nombre = input("Ingrese el nombre del cliente: ")
        patente = input("Ingrese la patente del auto: ")
        
        # Ingresar horas de inicio y salida
        hora_inicio = obtener_hora("Ingrese la hora de inicio (HH:MM): ")
        hora_salida = obtener_hora("Ingrese la hora de salida (HH:MM): ")
        
        # Crear el cliente y calcular el costo
        cliente = Cliente(nombre, patente, hora_inicio, hora_salida)
        costo_total = calcular_costo(hora_inicio, hora_salida, valor_por_minuto)
        
        clientes.append((cliente, costo_total))
        
        print(f"Cliente agregado: {nombre} | Patente: {patente} | Costo total: ${costo_total:.2f}")
        
        if len(clientes) < plazas:
            continuar = input("¿Desea ingresar otro cliente? (s/n): ")
            if continuar.lower() != 's':
                break

    print("\nResumen de clientes:")
    for cliente, costo in clientes:
        print(f"Cliente: {cliente.nombre}, Patente: {cliente.patente}, Costo total: ${costo:.2f}")

if __name__ == "__main__":
    main()