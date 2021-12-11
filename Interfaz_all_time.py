from os import pathsep
from tkinter import *
from Constantes import *

def leer_linea_all_time(archivo):
    fin_archivo = False
    linea = archivo.readline()
    registro = ['NAN','NAN','NAN',0,0]
    if linea:
        registro = linea.rstrip().split(',')
        registro[POS_ACIERTOS_REGISTRO] = int(registro[POS_ACIERTOS_REGISTRO]) 
        registro[POS_INTENTOS_REGISTRO] = int(registro[POS_INTENTOS_REGISTRO])
    else:
        fin_archivo = True
    return registro,fin_archivo

def gen_dict_all_time_ordenado():
    archivo = open('historial_all_time.txt','r')
    registro,fin_archivo = leer_linea_all_time(archivo)
    dict_all_time = {}
    while not fin_archivo:
        if registro[POS_NOMBRE_REGISTRO] not in dict_all_time:
            dict_all_time[registro[POS_NOMBRE_REGISTRO]] = [registro[POS_INTENTOS_REGISTRO],registro[POS_ACIERTOS_REGISTRO],INICIAR_CANT_PARTIDAS]
        else:
            dict_all_time[registro[POS_NOMBRE_REGISTRO]][INTENTOS] += registro[POS_INTENTOS_REGISTRO]
            dict_all_time[registro[POS_NOMBRE_REGISTRO]][ACIERTOS] += registro[POS_ACIERTOS_REGISTRO]
            dict_all_time[registro[POS_NOMBRE_REGISTRO]][PARTIDAS_JUGADAS]  += 1

        registro,fin_archivo = leer_linea_all_time(archivo)

    return sorted(dict_all_time.items(),key= lambda item: (item[1][ACIERTOS], - item[1][INTENTOS]) , reverse=True)

def coordinar_scroll_con_frame(lienzo):
    # resetear la region de scroll para encompazar el frame
    lienzo.configure(scrollregion=lienzo.bbox("all"))

def poblar_frame(frame_ranking , trofeo_ganador,laurel_derecho,laurel_izquierdo,medalla_plata,medalla_bronce):
    # Recibe el frame, la lista de j. ordenada y la imagen trofeo. Se encarga de mostrar en la interfaz la tabla de ranking 
    # con todas sus estadísticas.
    #---------------------------------- label fijos--------------------------------------------
    espacio = Label(frame_ranking,text='               ',bg='#F2F3F4',pady=15,padx=10)
    espacio.grid(column=0,row=0)

    nombre_jugador = Label(frame_ranking,text='Nombre del Jugador',font=("Lucida Console", 11),bg = '#F2F3F4', borderwidth="1",pady=15,padx=10)
    nombre_jugador.grid(column=2,row=0)

    aciertos_jugador = Label(frame_ranking,text='Aciertos',font=("Lucida Console", 11),bg = '#F2F3F4', borderwidth="1",pady=15,padx=10)
    aciertos_jugador.grid(column=4,row=0)

    intentos_jugador = Label(frame_ranking,text='Intentos',font=("Lucida Console", 11),bg = '#F2F3F4', borderwidth="1",pady=15,padx=10)
    intentos_jugador.grid(column=6,row=0)

    promedio_aciertos_por_intento = Label(frame_ranking,text='Aciertos por intento',font=("Lucida Console", 11),bg = '#F2F3F4', borderwidth="1",pady=15,padx=10)
    promedio_aciertos_por_intento.grid(column=8,row=0)

    promedio_intentos_partida = Label(frame_ranking,text='Intentos por partida',font=("Lucida Console", 11),bg = '#F2F3F4', borderwidth="1",pady=15,padx=10)
    promedio_intentos_partida.grid(column=10,row=0)

    trofeo = Label(frame_ranking,image= trofeo_ganador,bg= '#F2F3F4',height=110,width=125)
    trofeo.grid(column= 0,row= 1)

    laurel_i = Label(frame_ranking,image= laurel_izquierdo,bg= '#F2F3F4',height=100,width=50)
    laurel_i.grid(column= 1,row= 1)

    laurel_d = Label(frame_ranking,image= laurel_derecho,bg= '#F2F3F4',height=100,width=50)
    laurel_d.grid(column= 3,row= 1)

    medalla_p = Label(frame_ranking,image= medalla_plata,bg= '#F2F3F4',height=50,width=50)
    medalla_p.grid(column= 0,row= 2)

    medalla_b = Label(frame_ranking,image= medalla_bronce,bg= '#F2F3F4',height=50,width=50)
    medalla_b.grid(column= 0,row= 3)
    #---------------------------------- label generados--------------------------------------------
    columna_actual = 2
    fila_actual = 1
    lugar = 4
    tamanio_letra = 30
    posicion = 0
    lista_jugadores_ordenada_final = gen_dict_all_time_ordenado()
    for jugador,estadisticas in lista_jugadores_ordenada_final:

        if posicion >=3 and columna_actual==0:
            temp_label = Label(frame_ranking,text=f'{lugar}º',font=("Lucida Console", tamanio_letra-2),bg = '#F2F3F4', borderwidth="1",relief="solid")
            temp_label.grid(column= columna_actual , row= fila_actual)
            columna_actual +=2
            lugar += 1 

        temp_label = Label(frame_ranking,text=f'{jugador}',font=("Lucida Console", tamanio_letra),bg = '#F2F3F4')
        temp_label.grid(column= columna_actual , row= fila_actual)

        temp_label = Label(frame_ranking,text=f'{estadisticas[ACIERTOS]}',font=("Lucida Console", tamanio_letra),bg = '#F2F3F4')
        temp_label.grid(column= columna_actual+2 , row= fila_actual)

        temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]}',font=("Lucida Console", tamanio_letra),bg = '#F2F3F4')
        temp_label.grid(column= columna_actual+4 , row= fila_actual)

        temp_label = Label(frame_ranking,text=f'{estadisticas[ACIERTOS]/estadisticas[INTENTOS]:.2f}',font=("Lucida Console", tamanio_letra),bg = '#F2F3F4')
        temp_label.grid(column= columna_actual+6 , row= fila_actual)
        
        temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]/estadisticas[PARTIDAS_JUGADAS]:.2f}',font=("Lucida Console", tamanio_letra),bg = '#F2F3F4')
        temp_label.grid(column= columna_actual+8 , row= fila_actual)
        
        
        if tamanio_letra > 10:
            tamanio_letra -=3
        fila_actual += 1
        if posicion >=2:
            columna_actual = 0
        else:
            columna_actual = 2
        posicion += 1
    return fila_actual

def cerrar_all_time(ver_all_time,raiz_all_time):
    raiz_all_time.destroy()
    ver_all_time.config(state = NORMAL,bg = 'gold')

def ranking_all_time(raiz_ranking_fin,ver_all_time):

    #---------------------------------- raíz--------------------------------------------
    raiz_all_time = Toplevel(raiz_ranking_fin)
    raiz_all_time.title("RANKING ALL-TIME!")
    raiz_all_time.attributes('-topmost', True)
    raiz_all_time.iconbitmap('laureles.ico')
    raiz_all_time.resizable(0,0)
    raiz_all_time.geometry("1050x400")
    raiz_all_time.config(bg="#F2F3F4")
    #---------------------------------- Scroll--------------------------------------------
    barra_scroll = Scrollbar(raiz_all_time,orient="vertical",)
    #---------------------------------- Lienzo--------------------------------------------
    lienzo = Canvas(raiz_all_time)
    #---------------------------------- frame--------------------------------------------
    frame_ranking = Frame(lienzo)
    frame_ranking.config(bg='#F2F3F4')
    #---------------------------------- Configuracion del scroll--------------------------------------------
    barra_scroll.config(command=lienzo.yview)
    barra_scroll.pack(side="right", fill="y")
    #---------------------------------- Configuracion del lienzo--------------------------------------------
    lienzo.configure(yscrollcommand=barra_scroll.set, bg = '#F2F3F4') # parametro de configuracion yscrollcommand seteando la  barra_scroll como scroller.
    lienzo.pack(side="left", fill="both", expand=True)
    lienzo.create_window((1,1), window=frame_ranking, anchor="n")
    #---------------------------------- relacionar el frame con la barra de scroll.--------------------------------------------
    frame_ranking.bind("<Configure>", lambda event, lienzo=lienzo: coordinar_scroll_con_frame(lienzo))
    #---------------------------------- Imagenes --------------------------------------------
    trofeo_ganador = PhotoImage(file='trofeo_transparente.png')
    laurel_derecho = PhotoImage(file='laurel_derecho.png')
    laurel_izquierdo = PhotoImage(file='laurel_izquierdo.png')
    medalla_plata = PhotoImage(file='medalla_silver.png')
    medalla_bronce = PhotoImage(file='medalla_bronce.png')
    #---------------------------------- Poblar Frame --------------------------------------------
    ultima_fila = poblar_frame(frame_ranking , trofeo_ganador,laurel_derecho,laurel_izquierdo,medalla_plata,medalla_bronce)
    #---------------------------------- Botones --------------------------------------------

    fila_actual = ultima_fila+1
    salir_del_juego = Button(frame_ranking,text='Cerrar ventana',command = lambda: cerrar_all_time(ver_all_time,raiz_all_time) , bg = 'pale violet red',fg = 'dark slate blue',activebackground='violetred3' )
    salir_del_juego.grid(column = 10,row = fila_actual,pady= 10)  
    raiz_all_time.mainloop()
