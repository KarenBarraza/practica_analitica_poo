from FiguraGeometrica import FiguraGeometrica
from math import pi
class Trapecio(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    @property#getter con decorador property
    def basesup(self) -> float:
        return self._basesup
    
    @basesup.setter#seter 
    def basesup(self, basesup: float):
        self._basesup=basesup
        
    @property
    def baseinf(self)-> float:
        return self._baseinf
    
    @baseinf.setter
    def baseinf(self, baseinf: float):
        self._baseinf=baseinf
    
    @property
    def altura(self)-> float:
        return self._altura
    
    @altura.setter
    def altura(self, altura: float):
        self._altura=altura
    
    def area(self):
        return ((self.basesup + self.baseinf) * self.altura) /2
