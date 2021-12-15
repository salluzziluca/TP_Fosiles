from tkinter import *
from config.Constantes_config import *
from interfaces.interfaz_de_registro import interfaz_registro

def leer_linea(usuarios_clave):
    # Lee una linea del archivo y la devuelve en formato compatible con el resto del codigo.
    # Hecha por Omar Oriz, Agustin Conti.
    linea = usuarios_clave.readline()
    fin_archivo = False
    registro = ['usuario','clave']
    if linea:
        linea = linea.rstrip('\n')
        registro = linea.split(',')
    else: 
        fin_archivo = True
    return registro, fin_archivo

def validaciones(usuario, contraseña):
    #Valida si el usuario y la contraseña ingresadas corresponden con alguna linea del registro .csv
    #Hecha por Luca Salluzzi
    usuarios_clave = open('CSVs/usuarios.csv','r')
    registro, fin_archivo = leer_linea(usuarios_clave)
    valido = False
    while (not valido) and not fin_archivo:
        if usuario == registro[0] and contraseña == registro[1]:
            valido = True
        else:
            registro, fin_archivo = leer_linea(usuarios_clave)

    usuarios_clave.close()
    return valido

def presionar_enviar(dict_jugadores, usuario, contraseña, listbox_jugadores, mensaje_login):
        #Se ejecuta al presionar el Boton.Si el usuario y la contraseña coinciden con los registros, asigna el contenido de los entry al diccionario de jugadores y a la listbox presente en memoria, ademas notifica al usuario en ambos casos.
        # Hecha por Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        if validaciones(usuario, contraseña) and (usuario not in dict_jugadores.keys()):
            dict_jugadores[usuario] = [0,0]
            mensaje_login.config(bg = '#E9F7EF',fg = 'black', text = 'Usuario ingresado correctamente')
            listbox_jugadores.insert(END, usuario)
        elif (usuario in dict_jugadores.keys()):
            mensaje_login.config(bg = '#E9F7EF',fg = 'black', text = 'El Usuario ya se encuentra\nlogeado')
        else:
            mensaje_login.config(bg = '#E9F7EF',fg = 'black', text = 'Usuario y contraseña \nno coinciden con nuestros \nregistros')

def verificar_cantidad_jugadores(diccionario, boton_envio):
    #Verifica si la cantidad de usuarios logeados (listos para jugar) es igual o mayor a la constante del archivo de configuración. 
    #Hecha por Luca Salluzzi
    if len(diccionario.keys()) >= MAX_JUGADORES:
        boton_envio.config(state = DISABLED)

def presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry):
    # Intercambia funcion e imagen de un mismo botón.
    # Hecha por Omar Oriz, Valentina Nieto.
    mi_clave_entry.config(show = "")
    show_contra.config(image = ojo_tachado,command = lambda: presionar_ojo_tachado(show_contra, ojo_abierto, ojo_tachado, mi_clave_entry),bg="#f1948a")

def presionar_ojo_tachado(show_contra, ojo_abierto, ojo_tachado, mi_clave_entry):
    # Intercambia funcion e imagen de un mismo botón.
    # Hecha por Omar Oriz, Valentina Nieto.
    mi_clave_entry.config(show = "*")
    show_contra.config(image = ojo_abierto, command = lambda:presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry),bg="#d1f2eb")
    
def continuan_logeados(dict_jugadores, listbox_jugadores):
    # Recibe el diccionario con los jugadores logueados y el widget listbox. Inserta los jugadores del primero en el segundo.
    # Hecha por Omar Oriz.
    for jugador in dict_jugadores.keys():
        listbox_jugadores.insert(END, jugador)

def presionar_desloguear(dict_jugadores, listbox_jugadores, boton_envio, boton_inicio):
    # Recibe dict con jugadores logeados, el widget listbox y botones. Elimina al jugador del diccionario de jugadores.
    # Elimina al jugador de la listbox. Controla el estado de los botones que estas acciones conllevan.
    # Hecha por Omar Oriz.
    seleccionado = listbox_jugadores.get(ANCHOR)
    if seleccionado:
        del dict_jugadores[seleccionado]
    listbox_jugadores.delete(ANCHOR)
    boton_envio.config(state = NORMAL)
    if len(dict_jugadores) >= MAX_JUGADORES:
        boton_inicio.config(state = DISABLED)

def cerrar_juego_por_login(dict_jugadores,raiz):
    # Vacía el diccionario de jugadores y cierra la interfaz.
    #hecha por Omar Oriz.
    dict_jugadores.clear()
    raiz.destroy()

def login_y_registro(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi, Agustín Conti, Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores, muestra por pantalla el boton de registro, el de inicio de juego, el maximo de jugadores posibles, los nombres de los jugadores logueados y ademas, mensajes por pantalla del estado del login.
    #---------------------------------- raíz--------------------------------------------
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.protocol("WM_DELETE_WINDOW", lambda: cerrar_juego_por_login(dict_jugadores, raiz))
    raiz.resizable(0, 0)
    raiz.geometry("415x420")
    raiz.config(bg = "#E9F7EF")
    raiz.iconbitmap('Imagenes/fosil.ico')
    #---------------------------------- Fuente de la interfaz --------------------------------------------
    fuente_elegida = ('Lucida Console', 10)

    #---------------------------------- Frame de usuario contraseña --------------------------------------------
    miFrame = Frame(raiz)
    miFrame.grid(in_=raiz, row=2, column=0, columnspan=3, sticky=NW, padx= 40)
    miFrame.config(cursor="heart", bg= '#E9F7EF')
   
    #casilla usario
    usuario_existente = Label(miFrame, text="Usuario: ", bg= '#E9F7EF',font=fuente_elegida)
    usuario_existente.grid(row=0,column=0, padx=0, pady=0)
    usuario_var = StringVar()
    usuario_existente_entry = Entry(miFrame,textvariable=usuario_var,font=fuente_elegida)
    usuario_existente_entry.grid(row=0,column=1,padx=10, pady=10)
    
    #casilla contraseña
    contraseña = Label(miFrame, text="Contraseña: ", bg= '#E9F7EF',font=fuente_elegida)
    contraseña.grid(row=1,column=0,padx=0, pady=10)
    contraseña_var = StringVar()
    contraseña_entry = Entry(miFrame,textvariable= contraseña_var,font=fuente_elegida)
    contraseña_entry.grid(row=1,column=1,padx=10, pady=10)
    contraseña_entry.config(show="*")
    
    #---------------------------------- Mostrar contraseña--------------------------------------------
    ojo_abierto = PhotoImage(file='Imagenes/ojo_abierto.png')
    ojo_tachado = PhotoImage(file='Imagenes/ojo_tachado.png')
    show_contra = Button(miFrame,image= ojo_abierto,command = lambda: presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,contraseña_entry),bg="#d1f2eb")
    show_contra.grid(row = 1, column = 2)
    
    #---------------------------------- Frame para mensajes.--------------------------------------------
    frame_mensajes = Frame (raiz,bg= '#E9F7EF')
    frame_mensajes.grid( padx= 50,sticky=NW)
    #Mensaje login
    mensaje_login = Label(frame_mensajes, text = '', height=2, width=30)
    mensaje_login.config(bg = '#E9F7EF',fg = 'black',font=fuente_elegida)
    mensaje_login.grid(row=0, column=1, padx=10, pady=10,ipady=10)
    
    #Mensaje max jugadores 
    mensaje_jugadores = Label(frame_mensajes, text = f'El maximo total de jugadores es {MAX_JUGADORES}',font=fuente_elegida)
    mensaje_jugadores.config(bg = '#E9F7EF',fg = 'black')
    mensaje_jugadores.grid(row=1, column=1, padx=10, pady=10)

    #--------------------------------------------Frame para Listbox y boton desloguear.--------------------------------------------
    frame_list_deslog = Frame (raiz,bg= '#E9F7EF')
    frame_list_deslog.grid( padx= 63,sticky=NW)
    #Listbox jugadores
    listbox_jugadores = Listbox(frame_list_deslog)
    
    if dict_jugadores:   # Continuar logeados
        continuan_logeados(dict_jugadores,listbox_jugadores)

    listbox_jugadores.config(selectbackground="#E9F7EF",selectforeground="black",border= 2,font=('Lucida Console',10))
    listbox_jugadores.grid(row=5, column=1, pady=10,padx=20)
    
    #-------------------------------------------- Frame Botones Registro e iniciar.--------------------------------------------
    Frame_botones = Frame(raiz,bg= '#E9F7EF')
    Frame_botones.grid(padx=5,sticky=NW,pady=20)
    #Boton Envio
    longitud_diccionario = len(dict_jugadores.keys()) # Para control de estado de botones en partidas sucesivas.

    boton_envio = Button(Frame_botones, text = "Logearse",font=fuente_elegida)
    boton_envio.config(command= lambda:[presionar_enviar(dict_jugadores, usuario_var.get(), contraseña_var.get(), listbox_jugadores, mensaje_login), verificar_cantidad_jugadores(dict_jugadores, boton_envio)])
    if longitud_diccionario  >= MAX_JUGADORES:  # Para control de estado de botones en partidas sucesivas.
        boton_envio.config(state= DISABLED)
    boton_envio.grid(row=6, column=0, padx=5, pady=10,sticky=W)
    
    # Boton Registro
    boton_registro = Button(Frame_botones, text ="Registrarse",command = lambda: interfaz_registro(raiz),font=fuente_elegida)
    boton_registro.grid(row=6, column=1, padx=40, pady=10,sticky=S)
    
    #Boton Iniciar
    boton_inicio = Button(Frame_botones, text = "Iniciar Partida", state = DISABLED,command = raiz.destroy,font=fuente_elegida)
    if longitud_diccionario <= MAX_JUGADORES:   # Para control de estado de botones en partidas sucesivas.
        boton_inicio.config(state= NORMAL)
    boton_inicio.grid(row=6, column=2, padx=5, pady=10,sticky=E)

    #Boton Desloguear , va en el mismo frame que el listbox, no el de botones.
    boton_desloguear = Button(frame_list_deslog,text= "Desloguear\nJugador",font=fuente_elegida)
    boton_desloguear.config(command= lambda: presionar_desloguear(dict_jugadores,listbox_jugadores,boton_envio,boton_inicio) )
    boton_desloguear.grid(row=5, column=2, pady=10)



    raiz.mainloop()