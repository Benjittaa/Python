import os

def lim_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def validar_vistas():
    while True:
        try:
            visualizaciones = int(input("Introduce las visualizaciones de la película: "))
            if visualizaciones >= 0:
                return visualizaciones 
            else:
                print("La cantidad debe ser mayor o igual a 0... Inténtalo nuevamente.")
        except ValueError:
            print("Entrada no válida, por favor, introduce un número.")            

def validad_genero():
    generos_validos = ['acción', 'romance', 'terror', 'comedia', 'infantil']
    
    while True:
        genero = input("Introduce el género de la película (acción, romance, terror, comedia, infantil): ").lower()
        
        if genero in generos_validos:
            print(f"Género '{genero}' validado correctamente.")
            return genero
        else:
            print("Opción no válida, inténtelo nuevamente.")

def validar_año():
    while True:
        try:
            año = int(input("Ingrese el año de publicación de la película: "))
            if año < 1950:
                print("El año debe ser superior a 1950... Inténtelo nuevamente.")
            elif año > 2024:
                print("Ese año aún no existe... Inténtelo nuevamente.")
            else:
                return año
        except ValueError:
            print("Debe escribir el año como número entero.")   

def validar_positivos():
    while True:
        try:
            numero = int(input("Introduce la cantidad de películas: "))
            if numero > 0:
                print(f"La cantidad {numero} es positiva.")
                return numero 
            else:
                print("La cantidad debe ser positiva... Inténtalo nuevamente.")
        except ValueError:
            print("Entrada no válida, por favor, introduce un número.")

def calcular_peliculas_vistas(peliculas, vistas):
    if not vistas:
        return None, None 
   
    max_vista = max(vistas)
    min_vista = min(vistas)

    pelicula_mas_vista = peliculas[vistas.index(max_vista)]
    pelicula_menos_vista = peliculas[vistas.index(min_vista)]
    
    return pelicula_mas_vista, pelicula_menos_vista

def calcular_promedio_vistas(vistas):
    if not vistas:
        return 0
    return sum(vistas) / len(vistas)

lim_pantalla()

pelicula = []
protagonista = []
antagonista = []
director = []
genero = []    
año = [] 
visualizaciones = []
cont_accion = 0            
peli_accion = []  

print("Bienvenido a Insuco Streaming")
print("")

n = validar_positivos()
print("")

for i in range(n):
    print(f"PELICULA {i+1}")
    pelicula.append(input("Ingresa el nombre de la película  : "))
    protagonista.append(input(f"Ingrese el protagonista de '{pelicula[i]}': "))
    antagonista.append(input(f"Ingrese el antagonista de '{pelicula[i]}': "))
    director.append(input(f"Ingrese el director de '{pelicula[i]}': "))
    genero.append(validad_genero())
    
    if genero[i] == 'acción':
        peli_accion.append(pelicula[i])
        cont_accion += 1 
        
    visualizaciones.append(validar_vistas())
    año.append(validar_año())
    print("")
    print("")

pelicula_mas_vista, pelicula_menos_vista = calcular_peliculas_vistas(pelicula, visualizaciones)
promedio_vistas = calcular_promedio_vistas(visualizaciones)

for i in range(n):
    print(f"PELICULA {i + 1}")
    print(f"El nombre de la película es: {pelicula[i]}")
    print(f"El protagonista de la película es: {protagonista[i]}")
    print(f"El antagonista de la película es: {antagonista[i]}")
    print(f"El director de la película es: {director[i]}")
    print(f"El género de la película es: {genero[i]}")
    print(f"Visualizaciones de la película: {visualizaciones[i]}")
    print("")

print(f"\nLa película más vista es: {pelicula_mas_vista}")
print(f"La película menos vista es: {pelicula_menos_vista}")
print("")
print(f"\nEl promedio total de visualizaciones es: {promedio_vistas:.2f}")
print(f"{cont_accion} películas fueron de acción")
for j in range(cont_accion):
    print(peli_accion[j])