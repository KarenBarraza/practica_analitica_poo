class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre=nombre

    def area(self):
        raise NotImplementedError ("Este metodo debe ser calculado por la subclase")