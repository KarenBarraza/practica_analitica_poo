from FiguraGeometrica import FiguraGeometrica
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio=radio
        self.pi=3.1416
    
    def area(self):
        return self.radio**2 *self.pi
