import random


class barco:
    def __init__(self,tamano):
        self.tamano = tamano

    
    def posicionBaseBarco (self):
        direccion=random.randrange(2) #1 ES HORIZONAL Y 0 ES VERTICAL

        valido=False
        if self.tamano==1:
            while valido==False:
                coordenadaX=random.randrange(10)
                coordenadaY=random.randrange(10)
                coordenadaFinal=[coordenadaX,coordenadaY]
                valido=comprobarPos(matriz,coordenadaFinal[0],coordenadaFinal[1])

        else:
            while valido==False:
                if direccion==1:
                    if self.tamano==3:
                        coordenadaX=random.randrange(8)
                        coordenadaY=random.randrange(10)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY],[coordenadaX+2,coordenadaY]]
                    elif self.tamano==2:
                        coordenadaX=random.randrange(9)
                        coordenadaY=random.randrange(10)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY]]

                elif direccion==0:
                    if self.tamano==3:
                        coordenadaX=random.randrange(10)
                        coordenadaY=random.randrange(8)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX,coordenadaY+1],[coordenadaX,coordenadaY+2]]
                    elif self.tamano==2:
                        coordenadaX=random.randrange(10)
                        coordenadaY=random.randrange(9)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY]]
    

                for array in coordenadaFinal:
                    print(comprobarPos(matriz,array[0],array[1]))
                    sirve=comprobarPos(matriz,array[0],array[1])
                    if sirve==True:
                        valido=True
                    else:
                        break
                    
            
        return coordenadaFinal

    def __repr__(self):
        return 'B'


def comprobarPos(matriz,x,y):
    libre=True 
    if matriz[x][y]!='X':
        libre=False
        return libre    
    if x>0:
        print(matriz[x-1][y])
        if matriz[x-1][y]!='X':
            libre=False
            return libre
    if y>0:
        print(matriz[x][y-1])
        if matriz[x][y-1]!='X':
            libre=False
            return libre
    if  x<9:
        print(matriz[x+1][y])
        if matriz[x+1][y]!='X':
            libre=False
            return libre
    if y<9:
        print(matriz[x][y+1])
        if matriz[x][y+1]!='X':
            libre=False
            return libre

    return libre

matriz=[
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]




portaAvion=barco(3)
buque=barco(2)
submarino=barco(1)

for lista in barco(3).posicionBaseBarco():
    print(lista)
    matriz[lista[0]][lista[1]]=portaAvion

for lista in barco(2).posicionBaseBarco():
    print(lista)
    matriz[lista[0]][lista[1]]=portaAvion

for i in range (4):
    pos=barco(1).posicionBaseBarco()
    print(pos)
    matriz[pos[0]][pos[1]]=submarino





for i in matriz:
    print(i)
'''    
if matriz[1][1]=='X':
    print('estas tocando x')
if matriz[0][0] !='X':
    print('estas tocando algo que parece x pero no lo es') '''





