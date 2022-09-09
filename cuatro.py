# Crear Menu empanadas 

contador = 0 
empanadas=[]

print("****Menú empanadas****")
print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. Salir")



while (contador != 3):
    ingredientes=[]
    empanada={}
    contador= int(input("Digite la opción: "))
    if (contador==1):
        print("Agregar empanadas")
        empanada['Nombre']=input("Ingrese nombre empanada: ")
        for i in range (3):
            ingredientes.append(input(f'Digite el ingrediente {i+1}: ' ))
        empanada['Ingresdientes']=ingredientes
        empanada['precio']= int(input("Ingrese precio de empanada: "))
        empanadas.append(empanada)
    elif(contador==2):
        print("Mostrar empanadas")
        print(empanadas)
    elif(contador==3):
        print("Salir")
        break
    else:
        print("Ingrese una opcion valida")