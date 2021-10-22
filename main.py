def generar_fichas():
    return [["D",False],["D",False],["s",False],["s",False]]

def mostrar_las_fichas(fichas):
    for ficha in fichas:
        if ficha[1]:
            print(f'[{ficha[0]}]')
    pass

def input_usuario():
    pass

def ganasteinterrogacion():
    pass

def cambiar():
    pass

def acierto():
    pass

def main():
    no_parar=True
    fichas=generar_fichas()
    mostrar_las_fichas(fichas) 
    while no_parar:
        input1=input_usuario()
        fichas2=cambiar(fichas,input1)
        mostrar_las_fichas(fichas2)

        input2=input_usuario()
        fichas2=cambiar(fichas2,input2)

        if acierto(fichas,input1,input2):
            fichas=fichas2

        no_parar=ganasteinterrogacion(fichas)

main()
