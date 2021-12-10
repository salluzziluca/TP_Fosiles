from tkinter import *
from Constantes import *

def ranking_de_partida (lista_jugadores_ordenada,partidas_jugadas,juego_terminado):
   
    def boton_salir():
        juego_terminado.append(1)
        raiz_ranking.destroy()

    def coordinar_scroll_con_frame(lienzo):
        # resetear la region de scroll para encompazar el frame
        lienzo.configure(scrollregion=lienzo.bbox("all"))

    def poblar_frame(frame_ranking,lista_jugadores_ordenada,trofeo_ganador):
        # Recibe el frame, la lista de j. ordenada y la imagen trofeo. Se encarga de mostrar en la interfaz la tabla de ranking 
        # con todas sus estadísticas.
        #---------------------------------- label fijos--------------------------------------------
        espacio = Label(frame_ranking,text='            ',bg='thistle2',pady=15,padx=10)
        espacio.grid(column=0,row=0)

        nombre_jugador = Label(frame_ranking,text='Nombre del Jugador',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        nombre_jugador.grid(column=1,row=0)

        aciertos_jugador = Label(frame_ranking,text='Aciertos',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        aciertos_jugador.grid(column=3,row=0)

        intentos_jugador = Label(frame_ranking,text='Intentos',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        intentos_jugador.grid(column=5,row=0)

        promedio_intentos_jugador = Label(frame_ranking,text='Aciertos por intento',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        promedio_intentos_jugador.grid(column=7,row=0)

        trofeo = Label(frame_ranking,image= trofeo_ganador,bg= 'thistle2',height=77,width=88)
        trofeo.grid(column= 0,row= 1)

        #---------------------------------- label generados--------------------------------------------
        columna_actual = 1
        fila_actual = 1
        lugar = 2
        tamanio_letra = 30
        for jugador,estadisticas in lista_jugadores_ordenada:

            if columna_actual == 0:
                temp_label = Label(frame_ranking,text=f'{lugar}º',font=("Bahnschrift", tamanio_letra),bg = 'thistle2', borderwidth="1",relief="solid")
                temp_label.grid(column= columna_actual , row= fila_actual)
                columna_actual +=1
                lugar += 1 

            temp_label = Label(frame_ranking,text=f'{jugador}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual , row= fila_actual)

            temp_label = Label(frame_ranking,text=f'{estadisticas[ACIERTOS]}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual+2 , row= fila_actual)

            temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual+4 , row= fila_actual)

            temp_label = Label(frame_ranking,text=f'{estadisticas[ACIERTOS]/estadisticas[INTENTOS]:.2f}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual+6 , row= fila_actual)
            if tamanio_letra > 10:
                tamanio_letra -=3
            fila_actual += 1
            columna_actual = 0
        return fila_actual


    #---------------------------------- raíz--------------------------------------------
    raiz_ranking = Tk()
    raiz_ranking.title("Ranking de partida")
    raiz_ranking.attributes('-topmost', True)
    raiz_ranking.resizable(0,0)
    raiz_ranking.geometry("720x400")
    raiz_ranking.config(bg="thistle2")
    #---------------------------------- Scroll--------------------------------------------
    barra_scroll = Scrollbar(raiz_ranking,orient="vertical",)
    #---------------------------------- Lienzo--------------------------------------------
    lienzo = Canvas(raiz_ranking)
    #---------------------------------- frame--------------------------------------------
    frame_ranking = Frame(lienzo)
    frame_ranking.config(bg='thistle2')
    #---------------------------------- Configuracion del scroll--------------------------------------------
    barra_scroll.config(command=lienzo.yview)
    barra_scroll.pack(side="right", fill="y")

    #---------------------------------- Configuracion del lienzo--------------------------------------------
    lienzo.configure(yscrollcommand=barra_scroll.set, bg = 'thistle2') # parametro de configuracion yscrollcommand seteando la  barra_scroll como scroller.
    lienzo.pack(side="left", fill="both", expand=True)
    lienzo.create_window((0,0), window=frame_ranking, anchor="n")

    #---------------------------------- relacionar el frame con la barra de scroll.--------------------------------------------
    frame_ranking.bind("<Configure>", lambda event, lienzo=lienzo: coordinar_scroll_con_frame(lienzo))
    #---------------------------------- Imagenes --------------------------------------------
    trofeo_ganador = PhotoImage(file='trofeo_ganador.png')
    #---------------------------------- Poblar Frame --------------------------------------------
    ultima_fila = poblar_frame(frame_ranking,lista_jugadores_ordenada,trofeo_ganador)
    #---------------------------------- Botones --------------------------------------------

    fila_actual = ultima_fila+1
    salir_del_juego = Button(frame_ranking,text='Cerrar',command = boton_salir , bg = 'pale violet red',fg = 'dark slate blue',activebackground='violetred3' )
    salir_del_juego.grid(column = 1,row = fila_actual,pady=10)

    nueva_partida = Button(frame_ranking,text='Nueva Partida',command = raiz_ranking.destroy , bg = 'dark sea green', fg = 'dark slate blue',activebackground = 'sea green')
    
    if partidas_jugadas < MAX_PARTIDAS:
        nueva_partida.grid(column = 7,row = fila_actual,pady=10)   
    else: 
        nueva_partida.config(bg = 'grey',state = DISABLED)
        nueva_partida.grid(column = 7,row = fila_actual,pady=10)
        
        max_partidas_alcanzadas = Label(frame_ranking,text='Max. partidas alcanzada.',fg= 'red',font=("Bahnschrift", 10),bg = 'thistle2', borderwidth="1",pady=7)
        max_partidas_alcanzadas.grid(column = 7, row= fila_actual+1 )


    raiz_ranking.mainloop()
