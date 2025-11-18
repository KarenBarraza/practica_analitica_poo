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
        base = float(input("Ingrese el primer numero: "))
        altura = float(input("Ingrese el segundo numero: "))
        tr=Triangulo(base,altura)
        area = tr.area()
        print("El area es:", area)



