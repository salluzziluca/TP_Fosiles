from tkinter import *
from Constantes import *

def leer_linea_all_time(archivo):
    fin_archivo = False
    linea = archivo.readline()
    registro = [0,0,'NAN',0,0]
    if linea:
        registro = linea.rstrip().split(',')
        registro[POS_ACIERTOS_REGISTRO] = int(registro[POS_ACIERTOS_REGISTRO]) 
        registro[POS_INTENTOS_REGISTRO] = int(registro[POS_INTENTOS_REGISTRO])
    else:
        fin_archivo = True
    return registro,fin_archivo

def coordinar_scroll_con_frame(lienzo):
    # resetear la region de scroll para encompazar el frame
    lienzo.configure(scrollregion=lienzo.bbox("all"))

def poblar_frame(frame_ranking , trofeo_ganador,partidas_jugadas,lista_jugadores_ordenada_final):
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

    promedio_aciertos_por_intento = Label(frame_ranking,text='Aciertos por intento',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
    promedio_aciertos_por_intento.grid(column=7,row=0)

    promedio_intentos_partida = Label(frame_ranking,text='Intentos por partida',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
    promedio_intentos_partida.grid(column=9,row=0)

    trofeo = Label(frame_ranking,image= trofeo_ganador,bg= 'thistle2',height=77,width=88)
    trofeo.grid(column= 0,row= 1)

    #---------------------------------- label generados--------------------------------------------
    columna_actual = 1
    fila_actual = 1
    lugar = 2
    tamanio_letra = 30
            
    for jugador,estadisticas in lista_jugadores_ordenada_final:

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
        
        temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]/partidas_jugadas:.2f}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
        temp_label.grid(column= columna_actual+8 , row= fila_actual)
        
        
        if tamanio_letra > 10:
            tamanio_letra -=3
        fila_actual += 1
        columna_actual = 0
    return fila_actual


def ranking_fin_de_juego (lista_jugadores_ordenada_final,partidas_jugadas):
    #---------------------------------- raíz--------------------------------------------
    raiz_ranking = Tk()
    raiz_ranking.title("RESULTADOS FINALES!")
    raiz_ranking.attributes('-topmost', True)
    raiz_ranking.resizable(0,0)
    raiz_ranking.geometry("910x400")
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
    lienzo.create_window((1,1), window=frame_ranking, anchor="n")
    #---------------------------------- relacionar el frame con la barra de scroll.--------------------------------------------
    frame_ranking.bind("<Configure>", lambda event, lienzo=lienzo: coordinar_scroll_con_frame(lienzo))
    #---------------------------------- Imagenes --------------------------------------------
    trofeo_ganador = PhotoImage(file='trofeo_ganador.png')
    #---------------------------------- Poblar Frame --------------------------------------------
    ultima_fila = poblar_frame(frame_ranking , trofeo_ganador,partidas_jugadas,lista_jugadores_ordenada_final)
    #---------------------------------- Botones --------------------------------------------

    fila_actual = ultima_fila+1
    salir_del_juego = Button(frame_ranking,text='Salir del juego',command = raiz_ranking.destroy , bg = 'pale violet red',fg = 'dark slate blue',activebackground='violetred3' )
    salir_del_juego.grid(column = 7,row = fila_actual,pady= 10)  
    raiz_ranking.mainloop()



