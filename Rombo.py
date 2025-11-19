from FiguraGeometrica import FiguraGeometrica
from math import pi
class Rombo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    @property#getter con decorador property
    def diagonal1(self) -> float:
        return self._diagonal1
    
    @diagonal1.setter#seter 
    def diagonal1(self, diagonal1: float):
        self._diagonal1=diagonal1
        
    @property
    def diagonal2(self)-> float:
        return self._diagonal2
    
    @diagonal2.setter
    def diagonal2(self, diagonal2: float):
        self._diagonal2=diagonal2
    
    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2
