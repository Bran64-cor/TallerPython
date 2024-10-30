if __name__ == '__main__':
    num=int(input("Proporciona un numero"))
    fact=1
    i=1
    while i<(num+1):
        fact= fact * i
        i=i+1
    print(f"El factorial de {num} es {fact}")