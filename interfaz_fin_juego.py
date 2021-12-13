from tkinter import *
from Constantes import *
from Interfaz_all_time import *

def coordinar_scroll_con_frame(lienzo):
    # resetear la region de scroll para encompazar el frame
    lienzo.configure(scrollregion=lienzo.bbox("all"))

def poblar_frame(frame_ranking , medalla_dorada,partidas_jugadas,lista_jugadores_ordenada_final):
    # Recibe el frame, la lista de j. ordenada y la imagen trofeo. Se encarga de mostrar en la interfaz la tabla de ranking 
    # con todas sus estadísticas.
    #---------------------------------- label fijos--------------------------------------------
    espacio = Label(frame_ranking,text='            ',bg='#D4E6F1',pady=15,padx=10)
    espacio.grid(column=0,row=0)

    nombre_jugador = Label(frame_ranking,text='Nombre del Jugador',font=("Lucida Console", 11),bg = '#D4E6F1', borderwidth="1",pady=15,padx=10)
    nombre_jugador.grid(column=1,row=0)

    aciertos_jugador = Label(frame_ranking,text='Aciertos',font=("Lucida Console", 11),bg = '#D4E6F1', borderwidth="1",pady=15,padx=10)
    aciertos_jugador.grid(column=3,row=0)

    intentos_jugador = Label(frame_ranking,text='Intentos',font=("Lucida Console", 11),bg = '#D4E6F1', borderwidth="1",pady=15,padx=10)
    intentos_jugador.grid(column=5,row=0)

    promedio_aciertos_por_intento = Label(frame_ranking,text='% Aciertos por intento',font=("Lucida Console", 11),bg = '#D4E6F1', borderwidth="1",pady=15,padx=10)
    promedio_aciertos_por_intento.grid(column=7,row=0)

    promedio_intentos_partida = Label(frame_ranking,text='Intentos por partida',font=("Lucida Console", 11),bg = '#D4E6F1', borderwidth="1",pady=15,padx=5)
    promedio_intentos_partida.grid(column=9,row=0)

    trofeo = Label(frame_ranking,image= medalla_dorada,bg= '#D4E6F1',height=110,width=125)
    trofeo.grid(column= 0,row= 1)

    #---------------------------------- label generados--------------------------------------------
    columna_actual = 1
    fila_actual = 1
    lugar = 2
    tamanio_letra = 26
            
    for jugador,estadisticas in lista_jugadores_ordenada_final:

        if columna_actual == 0:
            temp_label = Label(frame_ranking,text=f'{lugar}º',font=("Lucida Console", tamanio_letra),bg = '#D4E6F1', borderwidth="1",relief="solid")
            temp_label.grid(column= columna_actual , row= fila_actual)
            columna_actual +=1
            lugar += 1 

        temp_label = Label(frame_ranking,text=f'{jugador}',font=("Lucida Console", tamanio_letra),bg = '#D4E6F1')
        temp_label.grid(column= columna_actual , row= fila_actual)

        temp_label = Label(frame_ranking,text=f'{estadisticas[ACIERTOS]}',font=("Lucida Console", tamanio_letra),bg = '#D4E6F1')
        temp_label.grid(column= columna_actual+2 , row= fila_actual)

        temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]}',font=("Lucida Console", tamanio_letra),bg = '#D4E6F1')
        temp_label.grid(column= columna_actual+4 , row= fila_actual)

        if estadisticas[INTENTOS] > 0:
            temp_label = Label(frame_ranking,text=f'{(estadisticas[ACIERTOS]/estadisticas[INTENTOS])*100:.2f}%',font=("Lucida Console", tamanio_letra),bg = '#D4E6F1')
        else:
            temp_label = Label(frame_ranking,text='No tuvo intentos',font=("Lucida Console", tamanio_letra-10),bg = '#D4E6F1')
        temp_label.grid(column= columna_actual+6 , row= fila_actual)
        
        temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]/partidas_jugadas:.2f}',font=("Lucida Console", tamanio_letra),bg = '#D4E6F1')
        temp_label.grid(column= columna_actual+8 , row= fila_actual)
        
        
        if tamanio_letra > 10:
            tamanio_letra -=3
        fila_actual += 1
        columna_actual = 0
    return fila_actual

def boton_all_time(raiz_ranking_fin,ver_all_time):
    ver_all_time.config(state = DISABLED,bg='grey')
    ranking_all_time(raiz_ranking_fin,ver_all_time) 


def ranking_fin_de_juego (lista_jugadores_ordenada_final,partidas_jugadas):
    #---------------------------------- raíz--------------------------------------------
    raiz_ranking_fin = Tk()
    raiz_ranking_fin.title("RESULTADOS FINALES!")
    raiz_ranking_fin.attributes('-topmost', True)
    raiz_ranking_fin.iconbitmap('fin_race.ico')
    raiz_ranking_fin.resizable(0,1)
    raiz_ranking_fin.geometry("950x300")
    raiz_ranking_fin.config(bg="#D4E6F1")
    #---------------------------------- Scroll--------------------------------------------
    barra_scroll = Scrollbar(raiz_ranking_fin,orient="vertical",)
    #---------------------------------- Lienzo--------------------------------------------
    lienzo = Canvas(raiz_ranking_fin)
    #---------------------------------- frame--------------------------------------------
    frame_ranking = Frame(lienzo)
    frame_ranking.config(bg='#D4E6F1')
    #---------------------------------- Configuracion del scroll--------------------------------------------
    barra_scroll.config(command=lienzo.yview)
    barra_scroll.pack(side="right", fill="y")
    #---------------------------------- Configuracion del lienzo--------------------------------------------
    lienzo.configure(yscrollcommand=barra_scroll.set, bg = '#D4E6F1') # parametro de configuracion yscrollcommand seteando la  barra_scroll como scroller.
    lienzo.pack(side="left", fill="both", expand=True)
    lienzo.create_window((1,1), window=frame_ranking, anchor="n")
    #---------------------------------- relacionar el frame con la barra de scroll.--------------------------------------------
    frame_ranking.bind("<Configure>", lambda event, lienzo=lienzo: coordinar_scroll_con_frame(lienzo))
    #---------------------------------- Imagenes --------------------------------------------
    medalla_dorada = PhotoImage(file='medalla_dorada_cinta1.png')
    #---------------------------------- Poblar Frame --------------------------------------------
    ultima_fila = poblar_frame(frame_ranking , medalla_dorada,partidas_jugadas,lista_jugadores_ordenada_final)
    #---------------------------------- Botones --------------------------------------------

    fila_actual = ultima_fila+1
    salir_del_juego = Button(frame_ranking,text='Salir del juego',command = raiz_ranking_fin.destroy , bg = 'pale violet red',
    fg = 'dark slate blue',activebackground='violetred3' )
    salir_del_juego.grid(column = 9,row = fila_actual,pady= 10)  
    
    ver_all_time = Button(frame_ranking,text='RANKING ALL-TIME',command = lambda: boton_all_time(raiz_ranking_fin,ver_all_time) , 
    bg = 'gold', fg = 'dark slate blue',activebackground = 'yellow')
    ver_all_time.grid(column = 0,row = fila_actual,pady=10,padx=10) 


    raiz_ranking_fin.mainloop()