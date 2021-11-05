import random, time

POSICION_LETRA = 0
POSICION_BOOL=1
INGRESO1 = 0
INGRESO2 = 1
INTENTOS= 0
ACIERTOS=1
TURNO_ACTIVO=2


def generar_fichas():
    # Genera una lista_jugadores de fichas y las devuelve en posiciones aleatorias.
    # Hecha por Lucas, Omar y Conti.
    lista_jugadores=[
    ["D",False],["D",False],["E",False],["E",False],
    ["J",False],["J",False],["Y",False],["Y",False],
    ["A",False],["A",False],["G",False],["G",False],
    ["X",False],["X",False],["V",False],["V",False]
    ]
    random.shuffle(lista_jugadores)
    return lista_jugadores

def mostrar_fichas(fichas):
    # Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha. Luego, se ejecuta un salto de linea
    # cada cuarta posicion y al final del ciclo.
    # Hecha por Luca Salluzzi, Omar, Lucas, Conti.
    n_posicion = 1
    contador=0
    for ficha in fichas:
        if contador==4:
            print('\n')
            contador=0
        if ficha[POSICION_BOOL]:
            print(f'[{ficha[POSICION_LETRA]}]', end=' ')
        else:
            print(f'[{n_posicion}]', end=' ')
        
        n_posicion+=1
        contador+=1
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
    #recibe el input numérico del usuario y la lista_jugadores de fichas actualizada, devuelve un bool
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
    # Recibe una lista_jugadores de fichas y un input y devuelve la lista_jugadores cambiada con la ficha (de pos. ingreso-1) volteada boca arriba.
    # Hecha por Omar Oriz.
    lista_fichas[ingreso-1][POSICION_BOOL]=True
    return lista_fichas

def voltear_fichas_para_abajo(lista_fichas,ingresos):
    # Recibe una lista_jugadores de fichas y una lista_jugadores de inputs y devuelve la lista_jugadores con esas fichas boca abajo.
    # Hecha por Omar Oriz.
    lista_fichas[(ingresos[INGRESO1]-1)][POSICION_BOOL]=False
    lista_fichas[(ingresos[INGRESO2]-1)][POSICION_BOOL]=False
    return lista_fichas

def elegir_primero(orden_jugadores):
    # Elije el jugador que va a empezar aleatoriamente 
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    return random.choice(orden_jugadores)

def cambiar_jugador(jugador_anterior_pos,lista_jugadores):
    # Devuelve el siguiente jugador en la lista de jugadores
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    if jugador_anterior_pos != len(lista_jugadores):
        jugador_siguiente= lista_jugadores[jugador_anterior_pos+1]
    else:
        jugador_siguiente= lista_jugadores[0]
    
    return jugador_siguiente

def revisar_ganador(diccionario, jugadores):
    # Evalúa aciertos e intentos y devuelve al jugador ganador.
    # Hecha por Osorio y Salluzzi.
    jugador_1 = jugadores[0]
    jugador_2 = jugadores[1]
    if diccionario[jugador_1][ACIERTOS] > diccionario[jugador_2][ACIERTOS]:
        jugador_ganador = jugador_1
    
    elif diccionario[jugador_1][ACIERTOS] < diccionario[jugador_2][ACIERTOS]:
        jugador_ganador = jugador_2
    
    else:
        if diccionario[jugador_1][INTENTOS] < diccionario[jugador_2][INTENTOS]:
            jugador_ganador = jugador_1
        elif diccionario[jugador_1][INTENTOS] > diccionario[jugador_2][INTENTOS]:
            jugador_ganador = jugador_2
        else:
            jugador_ganador = 'empate'
    return jugador_ganador

def mensaje_final(tiempo_inicial, jugador_ganador):
    # Recibe el tiempo inicial y el jugador ganador. Imprime cuanto duró el juego y quien fue el que que ganó. Contempla el caso de empate
    # Hecha por Osorio, Omar, Conti, Salluzzi.
    print('Fin del juego!')
    print(f"El juego duró {int(time.time() - tiempo_inicial)} segundos")
    if jugador_ganador != 'empate':
        print(f'El/la jugador_ganador/a es {jugador_ganador}')
    else:
        print(f'El juego terminó en {jugador_ganador}')
    
def acierto(fichas, ingresos):
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    # Hecha por Lucas Osorio y Valentina Nieto
    return fichas[ingresos[INGRESO1]-1][POSICION_LETRA] == fichas[ingresos[INGRESO2]-1][POSICION_LETRA]
    
def turno(fichas):
    # Define una ronda de selección de fichas. Devuelve la lista_jugadores con el par de ELECCIONES y los ingresos realizados.
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
    tiempo_inicio=time.time()
    dict_jugadores={"Juan": [0,0], "Pedro": [0,0]}#Este dicc. hay que formarlo con la list de abajo.
    orden_jugadores=list(dict_jugadores.keys()) #Pasar del input del tkinter a la lista orden_jugadores 
    jugador= elegir_primero(orden_jugadores)
    
    juego_terminado=False
    fichas=generar_fichas()
    mostrar_fichas(fichas) 
    while not juego_terminado:
        
        fichas2,ingresos=turno(fichas)
        dict_jugadores[jugador][INTENTOS]+=1

        if acierto(fichas,ingresos):
            print('Acierto!')
            dict_jugadores[jugador][ACIERTOS]+=1
            fichas=fichas2
        else:
            fichas=voltear_fichas_para_abajo(fichas,ingresos)
            jugador=cambiar_jugador(orden_jugadores.index(jugador),orden_jugadores)

        juego_terminado=revisar_si_ganaste(fichas)

        if juego_terminado:
            jugador_ganador = revisar_ganador(dict_jugadores,orden_jugadores)
            mensaje_final(tiempo_inicio, jugador_ganador)
        
        
            

main()

from tkinter import*

def solicitar_nombre():
    #Solicita el ingreso de los nombres de los Jugadores
    #Hecho por Valentina Nieto y Camila Zarza
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    #raiz.iconbitmap()
    raiz.geometry("300x150")
    raiz.config(bg="yellow")
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    #jugadores j1
    jugador_1=Label(miFrame, text="Primer Jugador: ")
    jugador_1.grid(row=0,column=0, padx=10, pady=10)
    jugador_1_entry=Entry(miFrame)
    jugador_1_entry.grid(row=0,column=1,padx=10, pady=10)
    #j2
    jugador_2=Label(miFrame, text="Segundo Jugador: ")
    jugador_2.grid(row=1,column=0,padx=10, pady=10)
    jugador_2_entry=Entry(miFrame)
    jugador_2_entry.grid(row=1,column=1,padx=10, pady=10)
    #Boton
    Boton=Button(raiz, text="Enviar",command = lambda: acierto(jugador_1_entry.get(),jugador_2_entry.get()))
    Boton.pack()
    raiz.mainloop()
    solicitar_nombre()  
