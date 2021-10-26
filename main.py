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
                
def input_usuario(fichas2):
    # Pide al usuario un ingreso numerico, devuelve ese numero.
    # Hecha por Camila Zarza, Oriz.
    entero=False
    while not entero:
        try:
            posicion=int(input("Posición: "))
            if validacion(posicion,fichas2):
                entero=True
            else:
                print('Número ingresado inválido.')
        except ValueError:
            print ('Valor inválido.')
        except TypeError:
            print ('Valor inválido.')
    return posicion

def validacion(input_realizado,fichas):
    #recibe el input numérico del usuario y la lista de fichas actualizada, devuelve un bool
    # Dependiendo si es una pos correcta, y si la ficha no está boca arriba.
    # Hecho por Omar Oriz.
    return ((input_realizado-1) in range(len(fichas)) and fichas[input_realizado-1][POSICION_BOOL] != True)

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

def voltear_ficha(lista_fichas,ingreso):
    # Recibe una lista de fichas y un input y devuelve la lista cambiada con la ficha (de pos. ingreso-1) volteada boca arriba.
    # Hecha por Omar Oriz.
    lista_fichas[ingreso-1][POSICION_BOOL]=True
    return lista_fichas

def voltear_fichas_para_abajo(lista_fichas,ingresos):
    # Recibe una lista de fichas y una lista de inputs y devuelve la lista con esas fichas boca abajo.
    # Hecha por Omar Oriz.
    lista_fichas[(ingresos[INGRESO1]-1)][POSICION_BOOL]=False
    lista_fichas[(ingresos[INGRESO2]-1)][POSICION_BOOL]=False
    return lista_fichas

def acierto(fichas, ingresos):
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    # Hecha por Lucas Osorio y Valentina Nieto
    return fichas[ingresos[INGRESO1]-1][POSICION_LETRA] == fichas[ingresos[INGRESO2]-1][POSICION_LETRA]
    
def turno(fichas):
    # Define una ronda de selección de fichas. Devuelve la lista con el par de ELECCIONES y los ingresos realizados.
    # Hecha por Oriz, Conti, Zarza.
    fichas2=fichas
    n=0
    print('Nuevo turno, Sus fichas:')
    mostrar_fichas(fichas)
    ingresos=[]
    while n<2:
        input1=input_usuario(fichas2)
        ingresos.append(input1)
        fichas2=voltear_ficha(fichas2,input1)
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
            print('Acierto!')
            fichas=fichas2
        else:
            fichas=voltear_fichas_para_abajo(fichas,ingresos)

        juego_terminado=revisar_si_ganaste(fichas)
        if juego_terminado:
            print('Fin del juego!')

main()