#VARIABLE CON ELEMENTOS DEL MISMO TIPO

numerosPares=[]

#Genere un ciclo while que de 10 vueltas 

contador=0

while (contador<10):
    n = int(int(input("Indique un numero par: ")))
    if (n % 2 == 0):
        numerosPares.append(n); #agregar elementos a una lista
        contador=contador+1
for observador in numerosPares:
    print(observador)