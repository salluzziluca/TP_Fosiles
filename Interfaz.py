from tkinter import *
from tkinter import font
from Constantes import MINIMO_JUGADORES
from Constantes_config import MAX_JUGADORES
from interfaz_de_registro import interfaz_registro

def validaciones(usuario, contraseña):
    #Desarollada por Luca Salluzzi
    #Valida si el usuario y la contraseña ingresadas corresponden con alguna linea del registro .csv
    usuarios_clave = open('usuarios.csv','r')
    linea = usuarios_clave.readline()
    linea = linea.rstrip('\n')
    registro = linea.split(',')
    valido = False
    while (not valido) and linea:
        if usuario == registro[0] and contraseña == registro[1]:
            valido = True
        else:
            linea = usuarios_clave.readline()
            linea = linea.rstrip('\n')
            registro = linea.split(',')
    usuarios_clave.close()
    return valido

def presionar_enviar(dict_jugadores, usuario, contraseña, listbox_jugadores, mensaje_login):
        # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        #Se ejecuta al presionar el Boton.Si el usuario y la contraseña coinciden con los registros, asigna el contenido de los entry al diccionario de jugadores y a la listbox presente en memoria, ademas notifica al usuario en ambos casos.
    
        if validaciones(usuario, contraseña) and (usuario not in dict_jugadores.keys()):
            dict_jugadores[usuario] = [0,0]
            mensaje_login.config(bg = '#E9F7EF',fg = 'black',text='Usuario ingresado correctamente')
            listbox_jugadores.insert(END, usuario)
        elif (usuario in dict_jugadores.keys()):
            mensaje_login.config(bg = '#E9F7EF',fg = 'black',text='El Usuario ya se encuentra logeado')
        else:
            mensaje_login.config(bg = '#E9F7EF',fg = 'black',text = 'Usuario y contraseña \nno coinciden con nuestros registros')
                
        return None

def verificar_cantidad_jugadores(diccionario, boton_envio, boton_inicio):
    #Luca Salluzzi
    #Verifica si la cantidad de usuarios logeados (listos para jugar) es igual o mayor a la constante del archivo de configuración. 
    if len(diccionario.keys()) >= (MAX_JUGADORES):
        boton_envio['state']='disabled'
    if len(diccionario.keys()) >= MINIMO_JUGADORES:
        boton_inicio['state'] = 'active'
        
def presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry):
    #intercambia funcion e imagen de un mismo botón.
    # Hecha por Omar Oriz, Valentina Nieto.
    mi_clave_entry.config(show="")
    show_contra.config(image = ojo_tachado,command = lambda: presionar_ojo_tachado(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry),bg="#f1948a")

def presionar_ojo_tachado(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry):
    #intercambia funcion e imagen de un mismo botón.
    # Hecha por Omar Oriz, Valentina Nieto.
    mi_clave_entry.config(show="*")
    show_contra.config(image = ojo_abierto, command = lambda:presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry),bg="#d1f2eb")
    
def continuan_logeados(dict_jugadores,listbox_jugadores):
    # Recibe el diccionario con los jugadores logueados y el widget listbox. Inserta los jugadores del primero en el segundo.
    # Hecha por Omar Oriz.
    for jugador in dict_jugadores.keys():
        listbox_jugadores.insert(END, jugador)

def presionar_desloguear(dict_jugadores,listbox_jugadores,boton_envio,boton_inicio):
    # Recibe dict con jugadores logeados, el widget listbox y botones. Elimina al jugador del diccionario de jugadores.
    # Elimina al jugador de la listbox. Controla el estado de los botones que estas acciones conllevan.
    # Hecha por Omar Oriz.
    seleccionado = listbox_jugadores.get(ANCHOR)
    if seleccionado:
        del dict_jugadores[seleccionado]
    listbox_jugadores.delete(ANCHOR)
    boton_envio.config(state= NORMAL)
    if len(dict_jugadores) >= MAX_JUGADORES:
        boton_inicio.config(state= DISABLED)

def cerrar_juego_por_login(dict_jugadores,raiz):
    # Vacía el diccionario de jugadores y cierra la interfaz.
    #hecha por Omar Oriz.
    dict_jugadores.clear()
    raiz.destroy()

def solicitar_nombre(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi, Agustín Conti, Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores, muestra por pantalla el boton de registro, el de inicio de juego, el maximo de jugadores posibles, los nombres de los jugadores logueados y ademas, mensajes por pantalla del estado del login.
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.protocol("WM_DELETE_WINDOW", lambda: cerrar_juego_por_login(dict_jugadores,raiz))
    raiz.resizable(0,0)
    raiz.geometry("415x400")
    raiz.config(bg="#E9F7EF")
    raiz.iconbitmap('fosil.ico')
    
    #frame
    miFrame=Frame(raiz)
    miFrame.grid(in_=raiz, row=2, column=0, columnspan=3, sticky=NSEW, padx= 40)

    miFrame.config(cursor="heart", bg= '#E9F7EF')
   
    #casilla usario
    usuario_existente=Label(miFrame, text="Usuario: ", bg= '#E9F7EF')
    usuario_existente.grid(row=0,column=0, padx=0, pady=0)
    usuario_var = StringVar()
    usuario_existente_entry=Entry(miFrame,textvariable=usuario_var)
    usuario_existente_entry.grid(row=0,column=1,padx=10, pady=10)
    
    #casilla contraseña
    contraseña=Label(miFrame, text="Contraseña: ", bg= '#E9F7EF')
    contraseña.grid(row=1,column=0,padx=10, pady=10)
    contraseña_var = StringVar()
    contraseña_entry=Entry(miFrame,textvariable= contraseña_var)
    contraseña_entry.grid(row=1,column=1,padx=10, pady=10)
    contraseña_entry.config(show="*")
    
    #Mostrar contraseña
    ojo_abierto = PhotoImage(file='ojo_abierto.png')
    ojo_tachado = PhotoImage(file='ojo_tachado.png')
    show_contra = Button(miFrame,image= ojo_abierto,command = lambda: presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,contraseña_entry),bg="#d1f2eb")
    show_contra.grid(row = 1, column = 2)
    
    #Mensaje login
    mensaje_login = Label(raiz, text = '', height=2, width=30)
    mensaje_login.config(bg = '#E9F7EF',fg = 'black')
    mensaje_login.grid(row=3, column=1, padx=10, pady=10)
    
    #Mensaje max jugadores 
    mensaje_jugadores = Label(raiz, text = f'El maximo total de jugadores es {MAX_JUGADORES}')
    mensaje_jugadores.config(bg = '#E9F7EF',fg = 'black')
    mensaje_jugadores.grid(row=4, column=1, padx=10, pady=10)
    
    #Listbox jugadores
    listbox_jugadores = Listbox(raiz)
    
    if dict_jugadores:   # Continuar logeados
        continuan_logeados(dict_jugadores,listbox_jugadores)
    listbox_jugadores.config(selectbackground="#E9F7EF",selectforeground="black",border= 2,font=('Lucida Console',10))
    listbox_jugadores.grid(row=5, column=1, pady=10)
    
    #Boton Envio
    longitud_diccionario = len(dict_jugadores) # Para control de estado de botones en partidas sucesivas.
    boton_envio=Button(raiz, text = "Logearse")
    boton_envio.config(command= lambda:[presionar_enviar(dict_jugadores, usuario_var.get(), contraseña_var.get(), listbox_jugadores, mensaje_login), verificar_cantidad_jugadores(dict_jugadores, boton_envio, boton_inicio)])
    if longitud_diccionario  >= MAX_JUGADORES:  # Para control de estado de botones en partidas sucesivas.
        boton_envio.config(state= DISABLED)
    boton_envio.grid(row=6, column=0, padx=10, pady=10)
    
    # Boton Registro
    boton_registro=Button(raiz, text ="Registrarse",command = lambda: interfaz_registro(raiz))
    boton_registro.grid(row=6, column=1, padx=10, pady=10)
    
    #Boton Iniciar
    boton_inicio=Button(raiz, text = "Iniciar Partida", state = DISABLED,command = raiz.destroy)
    if longitud_diccionario >= MAX_JUGADORES:   # Para control de estado de botones en partidas sucesivas.
        boton_inicio.config(state= NORMAL)
    boton_inicio.grid(row=6, column=2, padx=10, pady=10)

    #Boton Desloguear
    boton_desloguear = Button(raiz,text= "Desloguear\nJugador")
    boton_desloguear.config(command= lambda: presionar_desloguear(dict_jugadores,listbox_jugadores,boton_envio,boton_inicio) )
    boton_desloguear.grid(row=5, column=2, pady=10)



    raiz.mainloop()
    return None
