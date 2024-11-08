import cmath
import math


class General:
    def __init__(self, valor1, valor2, valor3):  # Cambié __int__ a __init__
        self.a = valor1
        self.b = valor2
        self.c = valor3

    def arriba(self) -> float:
        return (self.b * self.b) - (4 * (self.a) * (self.c))

    def dosa(self) -> float:
        return 2 * self.a

    def restab(self) -> float:
        return -(self.b)

    def equisuno(self):
        return (self.restab() + math.sqrt(self.arriba()))/self.dosa()

    def equisdos(self):
        return (self.restab() - math.sqrt(self.arriba()))/self.dosa()

if __name__ == '__main__':
    resultado = General(1, 11, 30)
    print(f"El valor de equis uno es: {resultado.equisuno()}")
    print(f"El valor de equis uno es: {resultado.equisdos()}")
