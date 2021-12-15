import time
from interfaces.interfaz_ranking import ranking_de_partida
from interfaces.interfaz_fin_juego import *
from interfaces.Interfaz_login import *
from Interaccion_usuario import *
from config.Constantes_config import *
from Procesamiento_del_juego import *    

def turno(fichas, jugador):
    # Hecha por Oriz, Conti, Zarza.
    # Define una ronda de selección de fichas. Devuelve la lista de fichas con dos de ellas dadas vuelta por el jugador y los ingresos realizados.
    n = 0
    mostrar_fichas(fichas,jugador)
    ingresos = []
    while n < 2:
        input1 = input_usuario(fichas)
        ingresos.append(input1)
        voltear_ficha(fichas, input1)
        mostrar_fichas(fichas, jugador)
        n += 1

    return fichas, ingresos

def ciclo_de_partida(partida_terminada, dict_jugadores, orden_jugadores, tiempo_inicio, fichas, jugador):
    # Recibe parametros para su funcionamiento, ejecuta todos los turnos de una partida.
    # Modularizada por Omar Oriz, Agustin Conti.
    while not partida_terminada: # Ciclo de partida
        
        fichas,ingresos = turno(fichas, jugador)
        dict_jugadores[jugador][INTENTOS] += 1

        if acierto(fichas, ingresos):
            print('Acierto!')
            dict_jugadores[jugador][ACIERTOS] += 1
            timer_delay(1.75) #1.75s para que el jugador pueda ver su elección.
        else:
            fichas = voltear_fichas_para_abajo(fichas, ingresos)
            jugador = cambiar_jugador(orden_jugadores.index(jugador), orden_jugadores)
            timer_delay(1.75)
        partida_terminada = partida_completa(fichas)

        if partida_terminada:
            mensaje_final(tiempo_inicio)

def post_partida(dict_jugadores,partidas_jugadas,juego_terminado,dict_jugadores_total):
    # recibe parametros para repartir en otras funciones. organiza y ejecuta las tareas posteriores a una partida.
    # Modularizada por Omar Oriz, Agustin Conti.
    dict_jugadores_ordenado = sorted(dict_jugadores.items(), key = lambda x: (x[1][ACIERTOS], - x[1][INTENTOS]), reverse = True)
    ranking_de_partida(dict_jugadores_ordenado, partidas_jugadas, juego_terminado)
    juntar_datos_partida(dict_jugadores, dict_jugadores_total)
    guardar_partida_en_csv(dict_jugadores_ordenado, partidas_jugadas)
    resets_stats_jugadores(dict_jugadores)

def estado_de_partida(dict_jugadores, partida_terminada, juego_terminado, cerrar_voluntariamente, orden_jugadores, jugador, fichas, partidas_jugadas):
    # evalua las condiciones para el inicio (o no) de la partida.
    # Modularizada por Omar Oriz, Agustin Conti.
    if (not dict_jugadores): # Si del login se sale sin jugadores logeados, el juego tiene que terminar.
        partida_terminada = True
        juego_terminado.append(1)
        cerrar_voluntariamente = True
    else:
        orden_jugadores = list(dict_jugadores.keys()) 
        jugador = elegir_primero(orden_jugadores) #elección aleatoria del primer jugador.
        fichas = generar_fichas() # Generación de fichas, al azar.

        partidas_jugadas += 1
    return partida_terminada, cerrar_voluntariamente, orden_jugadores, jugador, fichas, partidas_jugadas

def main():
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Incluye un ciclo donde transcurre todo el juego.
    partida_terminada = False
    cerrar_voluntariamente = False
    juego_terminado = [] # comunicacion con interfaz de tkinter.
    dict_jugadores_total = {} # Solo entran jugadores y sus estadisticas. No se borra ninguno.
    dict_jugadores = {} # Entran y salen jugadores
    partidas_jugadas = 0
    
    while not juego_terminado and partidas_jugadas <= MAX_PARTIDAS: # Ciclo de juego general.
        partida_terminada = False
        tiempo_inicio = time.time()
        
        login_y_registro(dict_jugadores) # Interfaz tkinter. Login , deslogueo y registro de jugadores.
        
        orden_jugadores, jugador, fichas, partidas_jugadas = [None, None, None, 0] #Declarado before assingment
        # evalua las condiciones para el inicio (o no) de la partida.
        partida_terminada, cerrar_voluntariamente, orden_jugadores, jugador, fichas, partidas_jugadas = estado_de_partida(dict_jugadores, partida_terminada, juego_terminado, cerrar_voluntariamente, orden_jugadores, jugador, fichas, partidas_jugadas)
        
        ciclo_de_partida(partida_terminada, dict_jugadores, orden_jugadores, tiempo_inicio, fichas, jugador) #Donde transcurren los turnos de los jugadores.

        if not cerrar_voluntariamente: # No se ejecuta si el jugador quiere cerrar el juego.
            post_partida(dict_jugadores, partidas_jugadas, juego_terminado, dict_jugadores_total)

        
    if dict_jugadores_total: # se ejecuta solo si se jugó al menos 1 partida.
        ranking_fin_de_juego(sorted(dict_jugadores_total.items(), key= lambda x: (x[1][ACIERTOS],- x[1][INTENTOS]), reverse = True), partidas_jugadas)

main()