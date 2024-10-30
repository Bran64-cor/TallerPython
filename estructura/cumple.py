if __name__ == '__main__':
    nom= input("Proporciona el nombre ")
    nom=nom.upper()

    print(nom)
    fecnom=""
    match nom:
        case "ASHLEY":fecnom="19/01/2002"
        case "HILARIO":fecnom="25/09/1976"
        case "LOURDES":fecnom="09/02/1980"
        case "ROSAURA":fecnom="02/10/1935"
        case "LEOBARDO":fecnom="05/01/1980"
        case _:fecnom="invalido"
    print(f"La fecha de nacimeinto de {nom} es {fecnom}")