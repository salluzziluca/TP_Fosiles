def generar_fichas():
    return [["D",True],["D",False],["s",False],["s",False]]

def mostrar_las_fichas(fichas):
    for i in range(len(fichas)):
        if fichas[i][1]:
             print(f'[{fichas[i][0]}]')
        else:
            print(f'[{i+1}]')
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
