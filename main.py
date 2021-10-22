from typing import no_type_check_decorator


def generar_fichas():
    return [["D",False],["D",False],["s",False],["s",False]]

def mostrar_las_fichas(fichas):
    for ficha in fichas:
        if ficha[1]:
            print('[{}]'.format(ficha[0]))
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

