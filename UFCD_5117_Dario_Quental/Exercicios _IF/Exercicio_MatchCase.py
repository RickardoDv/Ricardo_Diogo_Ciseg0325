opt=int(input("Insira um numero entre 1 e 12:"))

match opt:
    case int(1):
        print("JANEIRO")
    case int(2):
        print("FEVEREIRO")
    case int(3):
        print("MARÇO")
    case int(4):
        print("ABRIL")
    case int(5):
        print("MAIO")
    case int(6):
        print("JUNHO")
    case int(7):
        print("JULHO")
    case int(8):
        print("AGOSTO")
    case int(9):
        print("SETEMBRO")
    case int(10):
        print("OUTUBRO")
    case int(11):
        print("NOVEMBRO")
    case int(12):
        print("DEZEMBRO")
    case '_':
        print("opção invalida, o valor deverá estar entre 1 e 12")