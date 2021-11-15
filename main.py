import time
from os import system

from Interfaz import solicitar_nombre
from Interaccion_usuario import *
from Constantes import *
from Procesamiento_del_juego import *
    
def turno(fichas, jugador):
    # Hecha por Oriz, Conti, Zarza.
    # Define una ronda de selección de fichas. Devuelve la lista con el par de ELECCIONES y los ingresos realizados.
    n=0
    system('cls')  #limpia pantalla
    print('\n-------------------------------')
    print(f'Turno de {jugador}')
    print('-------------------------------\n')
    mostrar_fichas(fichas)
    ingresos=[]
    while n<2:

        input1=input_usuario(fichas)
        ingresos.append(input1)
        voltear_ficha(fichas,input1)
        system('cls') #limpia pantalla
        print('\n-------------------------------')
        print(f'Turno de {jugador}')
        print('-------------------------------\n')
        mostrar_fichas(fichas)
        n+=1

    return fichas,ingresos

def main():
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Incluye un ciclo donde transcurre todo el juego.
    tiempo_inicio=time.time()
    dict_jugadores={}
    solicitar_nombre(dict_jugadores) # función de interfaz hecha con tkinter. incluye jugadores al diccionario.
    orden_jugadores=list(dict_jugadores.keys()) 
    jugador= elegir_primero(orden_jugadores) #elección aleatoria del primer jugador.
    
    juego_terminado=False
    fichas=generar_fichas() # Generación de fichas, al azar.
    while not juego_terminado: # Ciclo de juego general.
        
        fichas,ingresos=turno(fichas, jugador)
        dict_jugadores[jugador][INTENTOS]+=1

        if acierto(fichas,ingresos):
            print('Acierto!')
            dict_jugadores[jugador][ACIERTOS]+=1
            timer_delay(1.75) #1.75s para que el jugador pueda ver su elección.
        else:
            fichas=voltear_fichas_para_abajo(fichas,ingresos)
            jugador=cambiar_jugador(orden_jugadores.index(jugador),orden_jugadores)
            timer_delay(1.75) #1.75s para que el jugador pueda ver su elección.
        juego_terminado=juego_completo(fichas)

        if juego_terminado:
            resultado = revisar_ganador(dict_jugadores,orden_jugadores)
            mensaje_final(tiempo_inicio, resultado)

main()


