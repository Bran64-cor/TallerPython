if __name__ == '__main__':
    dia=int(input("Proporciona un numero de la semana"))
    nomdia=""
    match dia:
        case 1:nomdia="Lunes"
        case 2:nomdia="Martes"
        case 3:nomdia="Miercoles"
        case 4:nomdia="Jueves"
        case 5:nomdia="Viernes"
        case 6:nomdia="Sabado"
        case 7:nomdia="Domingo"
        case _:nomdia="Dia no valido"
    print(f"El dia de la semana es {nomdia}")