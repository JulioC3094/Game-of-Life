import numpy as np #Para rellenar las matices
import random as rd #Para obtener las posiciones random
import time #Para el delay
'''Conway's Game of Life'''

#Funcion para crear universo(mundo)
def Universo(LiveCell):
    universo = (np.zeros((30, 30))).astype(np.int64)#Rellena la matriz de 30x30 con celulas muertas
    for cell in range(0,LiveCell): #Ingresa en posiciones random las celulas vivas
        posX = rd.randrange(0,30,1)#Random de 0 a 30 con intervalos de 1
        posY = rd.randrange(0,30,1)
        universo[posX, posY] = 1 #Cambio de la celula muerta por la viva en la posion generada aleatoriamente
    #print(universo)
    return universo #Regresa el universo
#Funcion para ver los vecinos de alrededor de la celula
def Neighbors(universo):
    size = universo.shape #Obtiene el tamaño de la matriz
    newUniverse = (np.zeros((30,30))).astype(np.int64) #Se crea una nueva matriz que sera el nuevo universo
    neighbor=0 #Variable que cuenta los vecinos
    for row in range(0, size[0]):  #Recorre la fila
        for column in range(0, size[1]): #Recorre la columna
        #Condiciones para encontrar los 8 vecinos, y no salir de los indices de la matriz
            if column-1>=0:
                if (universo[row, column-1])==1: #Verificar el vecino superior
                    neighbor+=1 #suma el vecino vivo
            if row+1<size[0] and column-1>=0:
                if (universo[row+1, column-1])==1:#Verificar el vecino superior derecho
                    neighbor+=1
            if row +1< size[0]:
                if(universo[row+1, column])==1: #Verificar el vecino derecho
                    neighbor+=1
            if row +1< size[0] and column+1<size[1]:
                if (universo[row+1, column+1])==1: #Verificar el vecino inferior derecho
                    neighbor+=1
            if column+1<size[1]:
                if (universo[row, column+1])==1: #Verificar el vecino inferior
                    neighbor+=1
            if column-1>=0 and column+1<size[1]:
                if (universo[row-1, column+1])==1: #Verificar el vecino inferior izquierdo
                    neighbor+=1
            if row-1>=0:
                if (universo[row-1, column])==1: #Verificar el vecino izquierdo
                    neighbor+=1
            if row-1>=0 and column-1>=0:
                if (universo[row-1, column-1])==1: #Verificar el vecino superior izquierdo
                    neighbor+=1
            newUniverse[row, column]=LifeDead(neighbor, universo[row, column]) # Cambio de la celula a un nuevo estado segun las condiciones dadas en la funcion LifeDead
            neighbor=0 #Regresa los vecinos a 0
    return newUniverse # Regresa el nuevo universo
#Funcion para determinar si vive, muere o nace.
def LifeDead(neighbor, cell):
    #Para la celulas vivas
    if cell==1:
        #Si tiene menos de dos vecinos muere
        #Si tiene mas de 3 vecinos muere
        if neighbor<2 or neighbor>3:
            return 0 #Regresa el valor de la celula muerta
        #Si la celula tiene dos o 3 vecinos continua viva
        elif neighbor==2 or neighbor==3:
            return 1 #Regresa el valor de la celula viva
    #Para las celulas muertas
    else:
        #Si tiene tres vecinos la celula nace o vuelve a vivir
        if neighbor==3:
            return 1
        else:
            #En caso de que no tenga tres vecinos continua muerta
            return 0


live = int(input('Enter the number of live cells: '))
iterations = int(input('Enter the number of iterations: '))
u=Universo(live) #Llamada para crear el universo dando el numero de las celulas vivas
for n in range(0, iterations):
    print(u) #Imprime el universo en turno
    u=Neighbors(u) #Obtiene los vecinos por lo cual crea el nuevo universo
    print(" ") #Espacio entre universos
    time.sleep(0.3) #Delay
