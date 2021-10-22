def generar_fichas():
    return [["D",True],["D",False],["s",False],["s",False]]

def mostrar_las_fichas(fichas):
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
                
def input_usuario():
    #pide al usuario un ingreso numerico, devuelve ese numero.
    pass

def ganasteinterrogacion():
    #Determina si el juego terminó, el nombre de la función es provisional.
    pass

def cambiar():
    #recibe una lista de fichas y un input y devuelve la lista cambiada con la ficha volteada.
    pass

def acierto():
    #Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    pass


"""def turno(fichas):
    # define una ronda de selección de fichas. Devuelve la lista con el par de ELECCIONES y los ingresos realizados.
    # Hecho por Oriz, Conti, Zarza.
    fichas2=fichas
    n=0
    ingresos=[]
    while n<2:
        input1=input_usuario()
        ingresos.append(input1)
        fichas2=cambiar(fichas2,input1)
        mostrar_las_fichas(fichas2)
        n+=1

    return fichas2,ingresos"""
        
def main():
    #Incluye un ciclo donde transcurre todo el juego.
    # Hecho por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi(era asi?)
    #no_parar=True
    fichas=generar_fichas()
    mostrar_las_fichas(fichas) 
    """while no_parar:
        fichas2,ingresos=turno(fichas)
        if acierto(fichas,ingresos):
            fichas=fichas2

        no_parar=ganasteinterrogacion(fichas)"""

main()
