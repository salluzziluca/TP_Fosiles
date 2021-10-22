def generar_fichas():
    #genera y devuelve un listado de Fichas para comenzar el juego.
    return [["D",False],["D",False],["s",False],["s",False]]

def mostrar_las_fichas(fichas):
    # muestra por pantalla el estado actual de las fichas en el juego.
    #Salluzzi
    for ficha in fichas:
        if ficha[1]:
            print(f'[{ficha[0]}]')
    pass

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


def turno(fichas):
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

    return fichas2,ingresos
        
def main():
    #Incluye un ciclo donde transcurre todo el juego.
    # Hecho por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi(era asi?)
    no_parar=True
    fichas=generar_fichas()
    mostrar_las_fichas(fichas) 
    while no_parar:
        fichas2,ingresos=turno(fichas)
        if acierto(fichas,ingresos):
            fichas=fichas2

        no_parar=ganasteinterrogacion(fichas)

main()
