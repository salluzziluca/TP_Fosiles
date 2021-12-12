import time
from os import system
from interfaz_ranking import ranking_de_partida
from interfaz_fin_juego import *
from Interfaz import *
from Interaccion_usuario import *
from Constantes import *
from Procesamiento_del_juego import *    

def turno(fichas, jugador):
    # Hecha por Oriz, Conti, Zarza.
    # Define una ronda de selección de fichas. Devuelve la lista de fichas con dos de ellas dadas vuelta por el jugador y los ingresos realizados.
    n=0
    mostrar_fichas(fichas,jugador)
    ingresos=[]
    while n<2:
        input1=input_usuario(fichas)
        ingresos.append(input1)
        voltear_ficha(fichas,input1)
        mostrar_fichas(fichas,jugador)
        n+=1

    return fichas,ingresos

def main():
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Incluye un ciclo donde transcurre todo el juego.
    
    partida_terminada=False
    juego_terminado = []
    partidas_jugadas= 0
    dict_jugadores_total = {}

    while (not juego_terminado) and (partidas_jugadas <= MAX_PARTIDAS): # Ciclo de juego general.
        partidas_jugadas += 1
        partida_terminada=False
        tiempo_inicio=time.time()
        dict_jugadores={}
        solicitar_nombre(dict_jugadores) # función de interfaz hecha con tkinter. incluye jugadores al diccionario.
        orden_jugadores=list(dict_jugadores.keys()) 
        jugador= elegir_primero(orden_jugadores) #elección aleatoria del primer jugador.
        fichas=generar_fichas() # Generación de fichas, al azar.

        while not partida_terminada: # Ciclo de partidas
            
            fichas,ingresos=turno(fichas, jugador)
            dict_jugadores[jugador][INTENTOS]+=1

            if acierto(fichas,ingresos):
                print('Acierto!')
                dict_jugadores[jugador][ACIERTOS]+=1
                timer_delay(1.75) #1.75s para que el jugador pueda ver su elección.
            else:
                fichas=voltear_fichas_para_abajo(fichas,ingresos)
                jugador=cambiar_jugador(orden_jugadores.index(jugador),orden_jugadores)
                timer_delay(1.75)
            partida_terminada=partida_completa(fichas)

            if partida_terminada:
                mensaje_final(tiempo_inicio)

        dict_jugadores_ordenado = sorted(dict_jugadores.items(),key= lambda x: (x[1][ACIERTOS], - x[1][INTENTOS]) , reverse=True)
        ranking_de_partida(dict_jugadores_ordenado , partidas_jugadas, juego_terminado)
        juntar_datos_partida(dict_jugadores,dict_jugadores_total)
        guardar_partida_en_csv(dict_jugadores_ordenado)
    
    ranking_fin_de_juego(sorted(dict_jugadores_total.items(),key= lambda x: (x[1][ACIERTOS], - x[1][INTENTOS]) , reverse=True) , partidas_jugadas)

main()


