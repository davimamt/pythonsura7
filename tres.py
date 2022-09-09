#Crear un menú 

contador = 0 

print("****Enamorate de Antioquia****")
print("Menú")
print("1. Agregar pueblos")
print("2. Mostrar rutas")
print("3. Salir")
pueblos=[]

while (contador != 3):
    pueblo={}
    contador = int(input("Digite una opción"))
    if (contador == 1):
        print("Agregando Pueblo")
        pueblo['nombre'] = input("ingrese el nombre del pueblo: ")
        pueblo['distancia'] = int(input("ingrese la distancia del pueblo: "))
        pueblo['poblacion'] = int(input("ingrese el numero de personas del pueblo: "))
        pueblos.append(pueblos)
    elif(contador == 2):
        print("Agregando Pueblo")
    elif(contador == 3):
        print("Saliendo")
        break
    else:
        print("Ingrese una opcion valida")
    
    
    