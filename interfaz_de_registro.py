from os import write
from tkinter import*
#################  back #######################
def usuario_existente(nombre_jugador):
    #Recibe un str (nombre del jugador) y verifica si se encuentra registrado en el archivo de usuarios.
    #Devuelve true si lo encuentra, false caso contrario.
    # Hecha por Omar Oriz.
    usuarios_clave = open('usuarios.csv','r')
    linea = usuarios_clave.readline()
    registro = linea.split(',')
    iguales= False
    while (not iguales) and linea:
        if nombre_jugador == registro[0]:
            iguales = True
        else:
            linea = usuarios_clave.readline()
            registro = linea.split(',')
    usuarios_clave.close()
    return iguales 

def guardar_usuario_nuevo(usuario,contrasenia):
    #Recibe nombre de usuario y contraseña. Abre el archivo de usuarios y guarda allí la información (usuario,clave).
    # Hecha por Omar Oriz.
    usuarios_clave = open('usuarios.csv','a')
    usuarios_clave.write(f'\n{usuario},{contrasenia}')
    usuarios_clave.close()
 
def alnum_y_guionbajo(cadena):
    #recibe una cadena y verifica si es alfanumérica o que tenga el guión bajo.
    # si reconoce algo diferente a eso, devuelve false.
    # Hecha por Omar Oriz.
    valido = True
    pos,pos_max = 0,(len(cadena)-1)
    while valido and pos <= pos_max :
        if not cadena[pos].isalnum() and cadena[pos] != '_' : 
            valido = False
        pos += 1
    return valido

def jugador_valido(nombre_jugador):
    #recibe el nombre del jugador y verifica las condiciones de validación. Devuelve true si es valido, caso contrario false.
    #(no prexistente, minimo 4 char, max 15char, formado solo por letras, numeros y el guión bajo.)
    # Hecha por Omar Oriz.
    return 4 <= len(nombre_jugador) <= 15 and alnum_y_guionbajo(nombre_jugador) and (not usuario_existente(nombre_jugador))

def pass_valida(contrasenia):
    #recibe la contraseña ingresada y verifica las condiciones de validación. Devuelve true si es valida, caso contrario false.
    #(debe tener entre 8 y 12 char, estar formada solo por char alfanuméricos, sin letras 
    #acentuadas, puede tener '-' y '_', debe tener al menos 1 mayuscula, una minúscula, un núm.
    #y un guión medio y un guión bajo.
    # Hecha por Omar Oriz, Valentina Nieto.
    valido = False
    if (8 <= len(contrasenia) <= 12):
        valido = True
        vocales_acentuadas = ['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
        #requisitos = ['mayus','lower','num','-','_']
        pos,pos_max = 0,(len(contrasenia)-1)
        mayus_ok,lower_ok,digit,guion_medio,guion_bajo = False,False,False,False,False
        while valido and pos <= pos_max :
            if not contrasenia[pos].isalnum() and contrasenia[pos] != '_' and contrasenia[pos] != '-' : 
                valido = False
            elif contrasenia[pos] in vocales_acentuadas:
                valido = False
            elif contrasenia[pos].isupper() and not mayus_ok:
                mayus_ok = True
            elif contrasenia[pos].islower() and not lower_ok:
                lower_ok = True
            elif contrasenia[pos].isdigit() and not digit:
                digit = True
            elif contrasenia[pos] == '-' and not guion_medio:
                guion_medio = True
            elif contrasenia[pos] == '_' and not guion_bajo:
                guion_bajo = True
            pos += 1

        if not (mayus_ok and lower_ok and digit and guion_medio and guion_bajo):
            valido = False

    return valido

    #---------------------------------- INTERACCION CON USUARIO--------------------------------------------
def interaccion_usuario(validacion,msg_final,usario_nuevo_entry,mi_clave_entry,mi_clave_re_entry):
    # recibe la tupla con los resultados de las validaciones y se comunica con el usuario de manera acorde.
    # Hecha por Omar Oriz, Valentina Nieto.
    if validacion[0] and validacion[1] and validacion[2]:
        msg_final.config(bg='#d4e6f1',fg='green',text='Registro exitoso!')
        msg_final.pack(padx= 70, pady=0)
        # si el registro es exitoso se limpian los campos.
        usario_nuevo_entry.delete(0, 'end')
        mi_clave_entry.delete(0, 'end')
        mi_clave_re_entry.delete(0, 'end')
    elif not validacion[0]:
        msg_final.config(bg='#d4e6f1',fg='red',text='Nombre de usuario inválido.\nPuede contener letras y numeros y el _.\nDebe tener entre 4 y 15 caracteres.\nNo puede ser un nombre de usuario existente.')
        msg_final.pack(padx= 70, pady=0)
    elif not validacion[1]:
        msg_final.config(bg='#d4e6f1',fg='red',text='Clave no valida.\ndebe tener al menos una mayuscula, una minuscula, un numero, - y _\nDebe tener entre 8 y 12 caracteres.')
        msg_final.pack(padx= 70, pady=0)
    elif not validacion[2]:
        msg_final.config(bg='#d4e6f1',fg='red',text='Las contraseñas no son iguales.')
        msg_final.pack(padx= 70, pady=0)
    return None
def get_usuario_contra(var_usuario_nuevo,var_pass,var_pass_re):
    #obtiene los datos ingresados en los campos de la interfaz al momento de la llamada de esta función.
    # Hecha por Omar Oriz.
    return (var_usuario_nuevo.get(),var_pass.get(),var_pass_re.get())

def presionar_boton_registrarse(var_usuario_nuevo,var_pass,var_pass_re,msg_final,usario_nuevo_entry,mi_clave_entry,mi_clave_re_entry):
    # organiza la secuencia de desencadenadores al apretar el botón 'Registrarse'.
    # Hecha por Omar Oriz.
    usuario_nuevo,contrasenia,contrasenia_re=get_usuario_contra(var_usuario_nuevo,var_pass,var_pass_re)
    es_valido = (jugador_valido(usuario_nuevo), pass_valida(contrasenia),(contrasenia == contrasenia_re)) # tupla con tres booleanos validadores.
    interaccion_usuario(es_valido,msg_final,usario_nuevo_entry,mi_clave_entry,mi_clave_re_entry)
    if es_valido[0] and es_valido[1] and es_valido[2]:
        guardar_usuario_nuevo(usuario_nuevo,contrasenia) # si es válido se guarda en el archivo de usuarios.
    return None

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
    
    
########################################

#################  Front #######################
def interfaz_registro(raiz_importada):
    #interfaz de registro "hija" de la interfaz de login.
    # Hecha por Omar Oriz, Valentina Nieto.
    #---------------------------------- raíz--------------------------------------------
    raiz_registro=Toplevel(raiz_importada)
    raiz_registro.title("Registro de Jugador")
    raiz_registro.resizable(0,0)
    raiz_registro.geometry("515x315")
    raiz_registro.iconbitmap("fosil.ico")
    raiz_registro.config(bg="#d4e6f1")
    #---------------------------------- frame--------------------------------------------
    frame_registro=Frame(raiz_registro,bg="#eaf2f8")
    frame_registro.pack(padx= 10, pady=20)

    frame_registro.rowconfigure(0,pad=10)
    frame_registro.rowconfigure(2,minsize = 80)
    frame_registro.rowconfigure(4,minsize=40)
    frame_registro.columnconfigure(0,pad=10)
    frame_registro.columnconfigure(3,minsize = 10)

    #---------------------------------- usuario--------------------------------------------
    usario_nuevo=Label(frame_registro, text = "Nombre del Jugador: ",font=("Lucida console", 11),bg="#eaf2f8")
    usario_nuevo.grid(row=0,column=0)
    var_usuario_nuevo=StringVar()
    usario_nuevo_entry=Entry(frame_registro, textvariable = var_usuario_nuevo,font=("Lucida console", 11),bg="#eaf2f8",fg= "#273746",cursor="heart")
    usario_nuevo_entry.grid(row=0,column=1)


    #---------------------------------- contraseña--------------------------------------------
    mi_clave=Label(frame_registro, text="Clave: ",font=("Lucida console", 11),bg="#eaf2f8")
    mi_clave.grid(row=2,column=0)
    var_pass=StringVar()
    mi_clave_entry=Entry(frame_registro, textvariable=var_pass,font=("Lucida console", 11),bg="#eaf2f8",fg= "#273746",cursor="heart")
    mi_clave_entry.config(show="*")
    mi_clave_entry.grid(row=2,column=1)

    #---------------------------------- Mostrar contraseña--------------------------------------------
    ojo_abierto = PhotoImage(file='ojo_abierto.png')
    ojo_tachado = PhotoImage(file='ojo_tachado.png')
    show_contra = Button(frame_registro,image= ojo_abierto,command = lambda: presionar_ojo_abierto(show_contra,ojo_abierto,ojo_tachado,mi_clave_entry),bg="#d1f2eb")
    show_contra.grid(row = 2,column = 2 )
    
    #---------------------------------- REINGRESAR contraseña--------------------------------------------
    mi_clave_re=Label(frame_registro, text="Reingresar Clave: ",font=("Lucida console", 11),bg="#eaf2f8")
    mi_clave_re.grid(row=4,column=0)
    var_pass_re=StringVar()
    mi_clave_re_entry=Entry(frame_registro, textvariable = var_pass_re,font=("Lucida console", 11),bg="#eaf2f8",fg= "#273746",cursor="heart")
    mi_clave_re_entry.config(show="*")
    mi_clave_re_entry.grid(row=4,column=1)

    #---------------------------------- Show contraseña--------------------------------------------
    show_contra_re = Button(frame_registro,image= ojo_abierto,command = lambda: presionar_ojo_abierto(show_contra_re,ojo_abierto,ojo_tachado,mi_clave_re_entry),bg="#d1f2eb")
    show_contra_re.grid(row = 4,column = 2 )



    #---------------------------------- Label dador de resultado--------------------------------------------
    msg_final=Label(raiz_registro, text='')
    msg_final.config(bg='#d4e6f1',fg='white')
    msg_final.pack(padx= 70, pady=0)
    
    #---------------------------------- botón REGISTRAR/CERRAR--------------------------------------------
    frame_de_boton=Frame(raiz_registro,bg="#d4e6f1")
    frame_de_boton.pack(anchor=S)
    boton_de_registro = Button(frame_de_boton,text= "Registrarse",font=("Lucida console", 11), command = lambda: presionar_boton_registrarse(var_usuario_nuevo,var_pass,var_pass_re,msg_final,usario_nuevo_entry,mi_clave_entry,mi_clave_re_entry),bg="#eafaf1",activebackground="#a2d9ce")
    boton_de_registro.grid(column = 3,row = 0,padx=60)
    boton_de_cerrar = Button(frame_de_boton,text= "Cerrar",font=("Lucida console", 11), command = raiz_registro.destroy,bg="#e8daef",activebackground="#d2b4de")
    boton_de_cerrar.grid(column = 0,row = 0,padx=60)


    raiz_registro.mainloop()
    return None

########################################

