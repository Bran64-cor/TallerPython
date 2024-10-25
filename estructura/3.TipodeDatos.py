if __name__ == '__main__':
    #Tipo de datos basicos
    entero = 42               #int
    decimal = 3.14            #float
    complejo = 2 + 3j         #complex
    booleano = True           #bool
    cadena = "Hola, Python!"  #str
    binario = bytes([50, 100, 150]) #bytes

    print("Tipos basicos:")
    print("Entero", entero)
    print("Decimal:", decimal)
    print("Complejo:", complejo)
    print("Booleano:", booleano)
    print("Cadena:", cadena)
    print("Binario:", binario, "\n")

    # Estructuras de datos avanzados
    lista = [1, 2, 3, "cuatro"]             #list
    tupla = (5, 6, 7, "ocho")               #tuple
    conjunto = {9, 10, "once", "doce"}       #set
    diccionario = {"clave1": "valor1", "clave 2": 20}  #dir

    print("Estructura avanzadas:")
    print("Lista: ", lista)
    print("Tupla: ", tupla)
    print("Conjunto: ", conjunto)
    print("Diccionario: ", diccionario, "\n")

    #Otros tipos especiales
    nulo = None          # NoneType
    rango = range(3)     # range (equivale a [0,1,2]

    print("Tipos especiales:")
    print("Nulo: ",nulo)
    print("Rango: ",list(rango)) #Convertimos a lista

    #Ejemplo de iteracion con el tipo range
    print("\nIterando sobre el rango:")

    #Esta es la manera mas corta de recorrer un rango
    for numero in rango:
        print(numero)
