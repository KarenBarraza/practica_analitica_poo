from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

fg=FiguraGeometrica

menuActivo = True
while menuActivo:
    print("Calculo areas figuras geometricas")
    print("1. Triangulo")
    print("2. Circulo")
    print("3. Rectangulo")
    print("4. Cuadrado")
    print("5. Salir")
    opcion = input("Ingrese una opcion:")

    if opcion == "1":
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        tr=Triangulo(base,altura)
        area = tr.area()
        print("El area es:", area)
    elif opcion == "2":
        radio = float(input("Indique el radio del circulo:"))
        cr = Circulo(radio)
        area = cr.area()
        print("El area es:", area)
    elif opcion == "3":
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        rt=Rectangulo(base, altura)
        area= rt.area()
        print("El area es:", area)   
             
