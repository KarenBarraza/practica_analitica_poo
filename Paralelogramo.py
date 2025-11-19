from FiguraGeometrica import FiguraGeometrica
from math import pi
class Paralelogramo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    @property#getter con decorador property
    def base(self) -> float:
        return self._base
    
    @base.setter#seter 
    def base(self, base: float):
        self._base=base
        
    @property
    def altura(self)-> float:
        return self._altura
    
    @altura.setter
    def altura(self, altura: float):
        self._altura=altura
    
    def area(self):
        return self.base * self.altura
