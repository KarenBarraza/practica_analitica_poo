from FiguraGeometrica import FiguraGeometrica
from math import pi
class Cilindro(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    @property#getter con decorador property
    def radio(self) -> float:
        return self._radio
    
    @radio.setter#seter 
    def radio(self, radio: float):
        self._radio=radio
        
    @property
    def altura(self)-> float:
        return self._altura
    
    @altura.setter
    def altura(self, altura: float):
        self._altura=altura
    
    def area(self):
        return 2 * pi * self.radio*(self.radio * self.altura)
    
    

        