if __name__ == '__main__':
    num=int(input("Dame in numero"))
    poten=int(input("Dame la potencia"))
    i=1
    while i<poten:
        num=num+num
        i= i+1
    print(f"La potencia es: {num}")