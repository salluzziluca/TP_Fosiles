import random, time
from tkinter import *
from os import system
POSICION_LETRA = 0
POSICION_BOOL=1
INGRESO1 = 0
INGRESO2 = 1
INTENTOS= 0
ACIERTOS=1
TURNO_ACTIVO=2


def generar_fichas():
    # Hecha por Lucas, Omar y Conti.
    # Genera una lista_jugadores de fichas y las devuelve en posiciones aleatorias.
    lista_jugadores=[
    ["D",False],["D",False],["E",False],["E",False],
    ["J",False],["J",False],["Y",False],["Y",False],
    ["A",False],["A",False],["G",False],["G",False],
    ["X",False],["X",False],["V",False],["V",False]
    ]
    random.shuffle(lista_jugadores)
    return lista_jugadores

def mostrar_fichas(fichas):
    # Hecha por Luca Salluzzi, Omar, Lucas, Conti.
    # Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha. Luego, se ejecuta un salto de linea
    # cada cuarta posicion y al final del ciclo.
    n_posicion = 1
    contador=0
    for ficha in fichas:
        if contador==4:
            print('\n\n')
            contador=0
        if ficha[POSICION_BOOL]:
            print(f' {ficha[POSICION_LETRA]}', end='    ')
        else:
            if n_posicion < 10:                           # Condicionales para rectificar imagen de fichas en consola.
                print(f' {n_posicion}', end='    ')
            else:
                print(f'{n_posicion}', end='    ')
        n_posicion+=1
        contador+=1
    print('\n')
               
def input_usuario(fichas2):
    # Hecha por Camila Zarza, Oriz.
    # Pide al usuario un ingreso numerico, devuelve ese numero.
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
    # Hecho por Omar Oriz.
    #recibe el input numérico del usuario y la lista_jugadores de fichas actualizada, devuelve un bool
    # Dependiendo si es una pos correcta, y si la ficha no está boca arriba.
    return ((input_realizado-1) in range(len(fichas)) and fichas[input_realizado-1][POSICION_BOOL] != True)

def revisar_si_ganaste(fichas):
    # Hecha por Agustín Conti
    # Determina si el juego terminó, comprobando que todas las fichas esten "volteadas".
    ganar=True
    pos_maxima=len(fichas)-1
    i=0
    while ganar and i <=pos_maxima:
        if not fichas[i][POSICION_BOOL]:
            ganar=False
        i+=1    
    return ganar

def voltear_ficha(lista_fichas,ingreso):
    # Hecha por Omar Oriz.
    # Recibe una lista_jugadores de fichas y un input y devuelve la lista_jugadores cambiada con la ficha (de pos. ingreso-1) volteada boca arriba.
    lista_fichas[ingreso-1][POSICION_BOOL]=True
    return lista_fichas

def voltear_fichas_para_abajo(lista_fichas,ingresos):
    # Hecha por Omar Oriz.
    # Recibe una lista_jugadores de fichas y una lista_jugadores de inputs y devuelve la lista_jugadores con esas fichas boca abajo.
    lista_fichas[(ingresos[INGRESO1]-1)][POSICION_BOOL]=False
    lista_fichas[(ingresos[INGRESO2]-1)][POSICION_BOOL]=False
    return lista_fichas

def elegir_primero(orden_jugadores):
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Elije el jugador que va a empezar aleatoriamente
    return random.choice(orden_jugadores)

def cambiar_jugador(jugador_anterior_pos,lista_jugadores):
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Devuelve el siguiente jugador en la lista de jugadores
    if jugador_anterior_pos != (len(lista_jugadores)-1):
        jugador_siguiente= lista_jugadores[jugador_anterior_pos+1]
    else:
        jugador_siguiente= lista_jugadores[0]
    
    return jugador_siguiente

def revisar_ganador(diccionario, jugadores):
    # Hecha por Osorio y Salluzzi, Omar.
    # Evalúa aciertos e intentos y devuelve al jugador resultado.
    aciertos_j1, intentos_j1= diccionario[jugadores[0]][ACIERTOS], diccionario[jugadores[0]][INTENTOS]
    aciertos_j2, intentos_j2 = diccionario[jugadores[1]][ACIERTOS], diccionario[jugadores[1]][INTENTOS]
    if  aciertos_j1 > aciertos_j2 :
        resultado = f'{jugadores[0]} ganó'
    elif aciertos_j1 < aciertos_j2:
        resultado = f'{jugadores[1]} ganó'
    else:
        if intentos_j1 < intentos_j2:
            resultado = f'{jugadores[0]} ganó'
        elif intentos_j1 > intentos_j2:
            resultado = f'{jugadores[1]} ganó'
        else:
            resultado = 'empate'
    return resultado

def mensaje_final(tiempo_inicial, resultado):
    # Hecha por Lucas, Omar y Conti.
    # Recibe el tiempo inicial e intentos e imprime el fin del juego con la cantidad de intentos y el tiempo empleado.
    print('Fin del juego!')
    print(f"El juego duró {int(time.time() - tiempo_inicial)} segundos")
    if resultado != 'empate':
        print(f' {resultado}, Felicitaciones!')
    else:
        print(f'El juego terminó en {resultado}')
    
def acierto(fichas, ingresos):
    # Hecha por Lucas Osorio y Valentina Nieto
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    return fichas[ingresos[INGRESO1]-1][POSICION_LETRA] == fichas[ingresos[INGRESO2]-1][POSICION_LETRA]
    
def turno(fichas, jugador):
    # Hecha por Oriz, Conti, Zarza.
    # Define una ronda de selección de fichas. Devuelve la lista_jugadores con el par de ELECCIONES y los ingresos realizados.
    fichas2=fichas
    n=0
    system('cls')  #limpia pantalla
    print('\n-------------------------------')
    print(f'Turno de {jugador}')
    print('-------------------------------\n')
    mostrar_fichas(fichas)
    ingresos=[]
    while n<2:

        input1=input_usuario(fichas2)
        ingresos.append(input1)
        fichas2=voltear_ficha(fichas2,input1)
        system('cls') #limpia pantalla
        print('\n-------------------------------')
        print(f'Turno de {jugador}')
        print('-------------------------------\n')
        mostrar_fichas(fichas2)
        n+=1

    return fichas2,ingresos

def timer_delay(segundos):
    # Omar Oriz
    # Genera un delay de la cantidad de segundos pedida, en la que se "frena" el avance del programa.
    t_inicial = time.time()
    tiempo_transcurrido = 0
    while tiempo_transcurrido < segundos:
        t_actual = time.time()
        tiempo_transcurrido = t_actual - t_inicial
    return None

def solicitar_nombre(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    #raiz.iconbitmap()
    raiz.geometry("310x160")
    raiz.config(bg="yellow")
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    #jugadores j1
    jugador_1=Label(miFrame, text="Primer Jugador: ")
    jugador_1.grid(row=0,column=0, padx=10, pady=10)
    nombre1_var = StringVar()
    jugador_1_entry=Entry(miFrame,textvariable=nombre1_var)
    jugador_1_entry.grid(row=0,column=1,padx=10, pady=10)
    #j2
    jugador_2=Label(miFrame, text="Segundo Jugador: ")
    jugador_2.grid(row=1,column=0,padx=10, pady=10)
    nombre2_var = StringVar()
    jugador_2_entry=Entry(miFrame,textvariable= nombre2_var)
    jugador_2_entry.grid(row=1,column=1,padx=10, pady=10)
    #funciones del boton
    def presionar_enviar():
        # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        #No recibe nada. se ejecuta al presionar el Boton. Asigna el contenido de los entry al diccionario de jugadores. Cierra la interfaz.
        dict_jugadores[nombre1_var.get()] = [0,0]
        dict_jugadores[nombre2_var.get()] = [0,0]
        raiz.destroy()
        return None
    #Boton
    Boton=Button(raiz, text="Enviar",command= presionar_enviar)
    Boton.pack()
    raiz.mainloop()
    return None


def main():
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Incluye un ciclo donde transcurre todo el juego.
    tiempo_inicio=time.time()
    dict_jugadores={}
    solicitar_nombre(dict_jugadores) # función de interfaz hecha con tkinter.
    orden_jugadores=list(dict_jugadores.keys()) 
    jugador= elegir_primero(orden_jugadores) #elección aleatoria del primer jugador.
    
    juego_terminado=False
    fichas=generar_fichas() # Generación de fichas, al azar.
    while not juego_terminado: # Ciclo de juego general.
        
        fichas2,ingresos=turno(fichas, jugador)
        dict_jugadores[jugador][INTENTOS]+=1
        
        if acierto(fichas,ingresos):
            print('Acierto!')
            dict_jugadores[jugador][ACIERTOS]+=1
            fichas=fichas2
            timer_delay(1.75) #1.75s para que el jugador pueda ver su elección.
        else:
            fichas=voltear_fichas_para_abajo(fichas,ingresos)
            jugador=cambiar_jugador(orden_jugadores.index(jugador),orden_jugadores)
            timer_delay(1.75) #1.75s para que el jugador pueda ver su elección.
        juego_terminado=revisar_si_ganaste(fichas)

        if juego_terminado:
            resultado = revisar_ganador(dict_jugadores,orden_jugadores)
            mensaje_final(tiempo_inicio, resultado)

main()


