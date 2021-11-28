
from os import write
from tkinter import*

#################  back #######################
def usuario_existente(nombre_jugador):
    #Recibe un str (nombre del jugador) y verifica si se encuentra registrado en el archivo de usuarios.
    #Devuelve true si lo encuentra, false caso contrario.
    usuarios_clave = open('usuarios.txt','r')
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
    usuarios_clave = open('usuarios.txt','a')
    usuarios_clave.write(f'\n{usuario},{contrasenia}')
    usuarios_clave.close()
 
def alnum_y_guionbajo(cadena):
    #recibe una cadena y verifica si es alfanumérica o que tenga el guión bajo.
    # si reconoce algo diferente a eso, devuelve false.
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
    return 4 <= len(nombre_jugador) <= 15 and alnum_y_guionbajo(nombre_jugador) and (not usuario_existente(nombre_jugador))

def pass_valida(contrasenia):
    #recibe la contraseña ingresada y verifica las condiciones de validación. Devuelve true si es valida, caso contrario false.
    #(debe tener entre 8 y 12 char, estar formada solo por char alfanuméricos, sin letras 
    #acentuadas, puede tener '-' y '_', debe tener al menos 1 mayuscula, una minúscula, un núm.
    #y un guión medio y un guión bajo.
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


########################################

#################  Front #######################
def interfaz_registro():
    #---------------------------------- raíz--------------------------------------------
    raiz=Tk()
    raiz.title("Registro de Jugador")
    raiz.resizable(0,0)
    raiz.geometry("515x315")
    raiz.iconbitmap("fosil.ico")
    raiz.config(bg="green")
    #---------------------------------- frame--------------------------------------------
    mi_frame=Frame(raiz)
    mi_frame.pack(padx= 10, pady=20)

    mi_frame.rowconfigure(0,pad=10)
    mi_frame.rowconfigure(2,minsize = 80)
    mi_frame.rowconfigure(4,minsize=40)
    mi_frame.columnconfigure(0,pad=10)
    mi_frame.columnconfigure(3,minsize = 10)

    #---------------------------------- usuario--------------------------------------------
    usario_nuevo=Label(mi_frame, text = "Nombre del Jugador: ",font=("Bahnschrift", 15))
    usario_nuevo.grid(row=0,column=0)
    var_usuario_nuevo=StringVar()
    usario_nuevo_entry=Entry(mi_frame, textvariable = var_usuario_nuevo,font=("Bahnschrift", 15))
    usario_nuevo_entry.grid(row=0,column=1)
    #---------------------------------- contraseña--------------------------------------------
    mi_clave=Label(mi_frame, text="Clave: ",font=("Bahnschrift", 15))
    mi_clave.grid(row=2,column=0)
    var_pass=StringVar()
    mi_clave_entry=Entry(mi_frame, textvariable=var_pass,font=("Bahnschrift", 15))
    mi_clave_entry.config(show="*")
    # para implementar el boton ojito. mi_clave_entry.config(show= str)
    mi_clave_entry.grid(row=2,column=1)
    #---------------------------------- REINGRESAR contraseña--------------------------------------------
    mi_clave_re=Label(mi_frame, text="Reingresar Clave: ",font=("Bahnschrift", 15))
    mi_clave_re.grid(row=4,column=0)
    var_pass_re=StringVar()
    mi_clave_re_entry=Entry(mi_frame, textvariable = var_pass_re,font=("Bahnschrift", 15))
    mi_clave_re_entry.grid(row=4,column=1)
    #---------------------------------- Label dador de resultado--------------------------------------------
    msg_final=Label(raiz, text='')
    msg_final.config(bg='green',fg='white')
    msg_final.pack(padx= 70, pady=0)
    #---------------------------------- interaccion con usuario.--------------------------------------------
    def interaccion_usuario(validacion):
        # recibe la tupla con los resultados de las validaciones y se comunica con el usuario de manera acorde.
        if validacion[0] and validacion[1] and validacion[2]:
            msg_final.config(bg='green',fg='white',text='Registro exitoso!')
            msg_final.pack(padx= 70, pady=0)
        elif not validacion[0]:
            msg_final.config(bg='green',fg='white',text='Nombre de usuario inválido.\nPuede contener letras y numeros y el _.\nDebe tener entre 4 y 15 caracteres.\nNo puede ser un nombre de usuario existente.')
            msg_final.pack(padx= 70, pady=0)
        elif not validacion[1]:
            msg_final.config(bg='green',fg='white',text='Clave no valida.\ndebe tener al menos una mayuscula, una minuscula, un numero, - y _\nDebe tener entre 8 y 12 caracteres.')
            msg_final.pack(padx= 70, pady=0)
        elif not validacion[2]:
            msg_final.config(bg='green',fg='white',text='Las contraseñas no son iguales.')
            msg_final.pack(padx= 70, pady=0)
        return None

    #---------------------------------- funciones del  botón--------------------------------------------
    def get_usuario_contra():
        #obtiene los datos ingresados en los campos de la interfaz al momento de la llamada de esta función.
        return (var_usuario_nuevo.get(),var_pass.get(),var_pass_re.get())

    def presionar_boton_registrarse():
        # organiza la secuencia de desencadenadores al apretar el botón 'Registrarse'.
        usuario_nuevo,contrasenia,contrasenia_re=get_usuario_contra()
        es_valido = (jugador_valido(usuario_nuevo), pass_valida(contrasenia),(contrasenia == contrasenia_re)) # tupla con tres booleanos validadores.
        interaccion_usuario(es_valido)
        if es_valido[0] and es_valido[1] and es_valido[2]:
            guardar_usuario_nuevo(usuario_nuevo,contrasenia) # si es válido se guarda en el archivo de usuarios.
        return None
    #---------------------------------- botón REGISTRAR--------------------------------------------
    
    boton = Button( text= "Registrarse",font=("Bahnschrift", 11), command = presionar_boton_registrarse )
    boton.pack(anchor = S)
    
    raiz.mainloop()
    return None
########################################
