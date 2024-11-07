def validar_sueldo (pre):
    sueldo = 0
    while((sueldo < 1000000) or (sueldo > pre)):
        try:
            sueldo = int(input("Ingrese el sueldo del artista: "))
            if sueldo < 1000000:
                print("El sueldo debe ser igual o superior a 1.000.000....Intentelo de nuevo")
            if sueldo > pre:
                print(f"El sueldo debe igual o inferior a {pre}....Intentelo de nuevo")
        except ValueError:
                print("debe escribir el sueldo como entero")
    return sueldo

def validar_dia():         
    dias_validos = [17-09, 18-09, 19-09, 20-09]  
    
    while True:
        dia = input("Seleccione la fecha de la presentacion(17-09, 18-09, 19-09, 20-09): ")       
        
        if dia in dias_validos:
            print(f"Fecha ´{dia}´ Validada correctamente. " )
            print("")
            return dia
        else 
        print("Fecha invalida, porfavor intentelo de nuevo") 
        
def validar_positivos():
    while True:
        try:
            numero = int(input("Introduce la cantidad de artistas: "))
            if numero > 0:
                return numero
              
            else: 
                print ("Ingrese una cantidad positiva ")     
        except:
            print ("Entrada no valida. Por favor, intentelo de nuevo")   


def control_presupuesto(pre, pago):
     pres_actual = 0
     pres_actual = pre-pago   
     return pres_actual                
 
nombre=[]
apellido=[]
apodo=[]
dia=[]
sueldo=[]

pres = 17000000
print ("Bienvenidooooooo")
print("")

n = validar_positivos()
print("")

for i in range (n):
     print("ARTISTA"i+1 )
     nombre.append(input("Ingrese el nombre del artista: "))
     apellido.append(input("Ingrese el apellido del artista: "))
     apodo.append(input("Ingrese el apodo del artista: "))
     
     sueldo.append(validar_sueldo())
     p = control_presupuesto(pres,sueldo[i])
     pres = p
     dia.append(validar_dia())
     
     
     
     
     print("")
     
 
for i in range(n):
    print(apodo[i])
    print(f"el nombre completo del artista es {nombre[i] +" "+apellido[i]}")    
    print(f"Su sueldo es {sueldo[i]}")    
    print(f"Se presentara {dia[i]}")    
    print("")  