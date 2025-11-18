#Importacion de archivos para poder ejecutar las funciones
from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

fg=FiguraGeometrica

menuActivo = True
while menuActivo:
    #Se realiza un menu para verifica las funciones
    print("---------------------------------")
    print("Calculo areas figuras geometricas")
    print("1. Triangulo")
    print("2. Circulo")
    print("3. Rectangulo")
    print("4. Cuadrado")
    print("5. Salir")
    #Se solicita que ingrese la opcion que va a elegir
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        #Solicitud de datos para calcular el area del triangulo
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        #Se llama la funcion
        tr=Triangulo(base,altura)
        area = tr.area()
        print("El area del triangulo es:", area)
    elif opcion == "2":
        #Solicitud de datos para calcular el area del circulo
        radio = float(input("Indique el radio del circulo: "))
        #Se llama la funcion
        cr = Circulo(radio)
        area = cr.area()
        print("El area del circulo es:", area)
    elif opcion == "3":
        #Solicitud de datos para calcular el area del rectangulo
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        #Se llama la funcion
        rt=Rectangulo(base, altura)
        area= rt.area()
        print("El area del rectangulo es:", area)   
    elif opcion == "4":
        #Solicitud de datos para calcular el area del cuadrado
        lado = float(input("Ingrese la medida de uno de los lados: "))
        #Se llama la funcion
        cd=Cuadrado(lado)
        area=cd.area()
        print("El area del cuadrado es:", area)
    elif opcion =="5":
        #Con esta opcion se sale del programa
        print("Saliendo del programa")
        break


         
