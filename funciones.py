#creamos la lista donde almacenaremos los vehiculos (listas)
vehiculos=[]
#0.-funcion para validar la patente 
def buscar (patente):
    for i in range(len(vehiculos)):
        if vehiculos[i] ["patente"]==patente:
            return i
    return -1

#1.-agregar

def agregar(patente,tipo,anio,precio):
    #validar que tenga 6 caracteres sin espacios em blanco
    if len(patente )!=6:
        print("Numero de caracteres no valido")
        return
    #validar que no tenga espacios en blanco
    elif " " in patente:
        print("No puede tener espacios en blanco")
        return
    
    #validar que la patente no se repita
    elif buscar(patente)>=0:
        print("No se puede repetir la patente")
        return
    #validar tipo
    elif tipo.lower() not in ("sedan","suv","camioneta"):
        print("Tipo no valido")
        return
    elif anio<2015 or anio>2026:
        print("Año no valido")
        return
    elif precio<=5000000:
        print("Precio no valido")
        return
    #Si los datos son validos creamos el diccionario con los datos 
    auto={"patente":patente,"tipo":tipo,"anio":anio,"precio":precio}
    vehiculos.append(auto)    
    print("Vehiculo Registrado")#alt+z para poder escribir en la misma linea pero hacia debajo
    #Patente existente 
def mostrar(patente):
    posicion=buscar(patente)
    if posicion>=0:
        print(f"Patente encontrada : {vehiculos[posicion]}")
    else: 
        print("Patente no encontrada")
#6.-Listar vehiculos con iva
def listaconiva():
    if len(vehiculos)>0:
        print(f"{"N°"} {"patente":<8} {"tipo":<10} {"año":<6} {"precio":<10}")
        for i in range (len(vehiculos)):
            print(f"{i+1}  {vehiculos[i]["patente"]:<8}   {vehiculos[i]["tipo"]:<10}  {vehiculos[i]["anio"]:<6}  ${round(vehiculos[i]["precio"]*1.19):<10}")
    else:
        print("No hay vehiculos registro")
