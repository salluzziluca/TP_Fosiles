POSICION_BOOL=1
POSICION_LETRA = 0
INGRESO1 = 0
INGRESO2 = 1

def generar_fichas():
    return [["D",False],["D",False],["s",False],["s",False]]

def mostrar_fichas(fichas):
    # Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha. Luego, se ejecuta un salto de linea
    # Hecha por Luca Salluzzi, Omar
    n_posicion = 1
    for ficha in fichas:

        if ficha[POSICION_BOOL]:
            print(f'[{ficha[POSICION_LETRA]}]', end=' ')
        else:
            print(f'[{n_posicion}]', end=' ')
        n_posicion+=1
    print('\n')
                
def input_usuario():
    # Pide al usuario un ingreso numerico, devuelve ese numero.
    # Hecha por Zarza
    primera_posicion=int(input("1° Posición: "))
    segunda_posicion=int(input("2° Posición: "))
    pass

def revisar_si_ganaste(fichas):
    # Determina si el juego terminó, comprobando que todas las fichas esten "volteadas".
    # Hecha por Agustín Conti
    ganar=True
    pos_maxima=len(fichas)-1
    i=0
    while ganar and i <=pos_maxima:
        if not fichas[i][POSICION_BOOL]:
            ganar=False
        i+=1    
    return ganar

def cambiar(fichas,ingreso):
    # Recibe una lista de fichas y un input y devuelve la lista cambiada con la ficha (de pos. ingreso-1) volteada.
    # Hecha por Omar Oriz
    fichas[ingreso-1][POSICION_BOOL]=True
    return fichas

def acierto(fichas, ingresos):
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    # Hecha por Lucas Osorio y Valentina Nieto
    return fichas[ingresos[INGRESO1]-1][POSICION_LETRA] == fichas[ingresos[INGRESO2]-1][POSICION_LETRA]
    


def turno(fichas):
    # Define una ronda de selección de fichas. Devuelve la lista con el par de ELECCIONES y los ingresos realizados.
    # Hecha por Oriz, Conti, Zarza.
    fichas2=fichas
    n=0
    ingresos=[]
    while n<2:
        input1=input_usuario()
        ingresos.append(input1)
        fichas2=cambiar(fichas2,input1)
        mostrar_fichas(fichas2)
        n+=1

    return fichas2,ingresos
        
def main():
    # Incluye un ciclo donde transcurre todo el juego.
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi(era asi?)
    juego_terminado=False
    fichas=generar_fichas()
    mostrar_fichas(fichas) 
    while not juego_terminado:
        fichas2,ingresos=turno(fichas)
        if acierto(fichas,ingresos):
            fichas=fichas2

        juego_terminado=revisar_si_ganaste(fichas)

main()