from typing import no_type_check_decorator


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

def main():
   # no_parar=True
    fichas=generar_fichas()
    mostrar_las_fichas(fichas) 
    #while no_parar:
      #  fichas=input_usuario()
      #  fichas=mostrar_las_fichas()
       # no_parar=ganasteinterrogacion()
main()
