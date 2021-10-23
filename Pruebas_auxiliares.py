POSICION_BOOL = 1
POSICION_LETRA = 0
"""
lista_prueba=[["D",False],["D",False],["s",False],["s",False]]
ingreso_in=2

POS_BOOL = 1

def cambiar(fichas,ingreso):
    #Omar Oriz
    #recibe una lista de fichas y un input y devuelve la lista cambiada con la ficha (de pos. ingreso-1) volteada.
    fichas[ingreso-1][POS_BOOL]=True
    return fichas
print(cambiar(lista_prueba,ingreso_in))
"""

"""def mostrar_las_fichas(fichas):
    #Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha. Si esta ficha es la ultima de todas, se imprime distinto para que haya un salto de linea ante un proximo print
    #hecho por Luca Salluzzi
    for i in range(len(fichas)):
        
        if fichas[i][1]:
            if i != (len(fichas)-1):
                print(f'[{fichas[i][0]}]', end=' ')
                
            else:
                print(f'[{fichas[i][0]}]')
        else:
            if i != (len(fichas)-1):
                print(f'[{i+1}]', end=' ')
                
            else:
                print(f'[{i+1}]')

"""


lista_prueba=[["D",False],["D",True],["s",False],["s",False]]

def mostrar_las_fichas(fichas):
    #Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha.
    #hecho por Luca Salluzzi, O.Oriz.
    n_posicion=1
    for ficha in fichas:

        if ficha[POSICION_BOOL]:
            print(f'[{ficha[POSICION_LETRA]}]', end=' ')
        else:
            print(f'[{n_posicion}]', end=' ')
        n_posicion+=1
    print('\n')
    print('perro')

mostrar_las_fichas(lista_prueba)

"""fichas =[["D",False],["D",False],["s",False],["s",False]]
ingresos = [3,2]
def acierto(fichas, ingresos):
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    # Hecha por
    if fichas[ingresos[0]-1][POSICION_LETRA]== fichas[ingresos[1]-1][POSICION_LETRA]:
        
    
    pass"""