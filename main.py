#Importacion de archivos para poder ejecutar las funciones
from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado
from Cilindro import Cilindro
from Paralelogramo import Paralelogramo
from Rombo import Rombo
from Trapecio import Trapecio

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
    print("5. Cilindro")
    print("6. Paralelograma")
    print("7. Rombo")
    print("8. Trapecio")
    print("9. Salir")
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
    elif opcion == "5":
        nombre=input("Confirme el nombre: ")
        cil=Cilindro(nombre)
        cil.radio = float(input("Ingrese el radio del cilindro: "))
        cil.altura = float(input("Ingrese la altura del cilindro: "))
        area=cil.area()  
        print("El area del cilindro es: ", area) 
    elif opcion == "6":
        nombre=input("Confirme el nombre: ")
        pr=Paralelogramo(nombre)
        pr.base = float(input("Ingrese la base del paralelogramo: "))
        pr.altura = float(input("Ingrese la altura del paralelogramo: "))
        area=pr.area()  
        print("El area del paralelogramo es: ", area) 
    elif opcion == "7":
        nombre=input("Confirme el nombre: ")
        rb=Rombo(nombre)
        rb.diagonal1 = float(input("Ingrese la diagonal #1 : "))
        rb.diagonal2 = float(input("Ingrese la diagonal #2 : "))
        area=rb.area()  
        print("El area del Rombo es: ", area) 
    elif opcion == "8":
        nombre=input("Confirme el nombre: ")
        tr=Trapecio(nombre)
        tr.basesup = float(input("Ingrese la base #1 del trapecio : "))
        tr.baseinf = float(input("Ingrese la base #2 del trapecio : "))
        tr.altura = float(input("Ingrese la altura del trapecio: "))
        area=tr.area()  
        print("El area del trapecio es: ", area) 
    elif opcion == "9":
        #Con esta opcion se sale del programa
        print("Saliendo del programa")
        break


         
