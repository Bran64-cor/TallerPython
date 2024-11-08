import math

if __name__ == '__main__':
    def Suma(x,y):
        return x+y
    Suma=lambda x,y:x + y

    Resta=lambda x,y:x-y

    Potencia =lambda x: x**2

    x1= lambda a,b,c:(-b + math.sqrt(b**2 *4*a*c))/2*a


    print(f"La suma es {Suma(2,6)}")
    print(f"La resta es {Resta(3, 4)}")
    print(f"La potencia es {Potencia(9)}")
    print(f"La respuesta de la formula general es {x1(1,11,30)}")


