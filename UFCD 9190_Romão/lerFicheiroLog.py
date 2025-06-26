
ficheiro = open("access.log", "r")

lista_ips=list()

for linha in ficheiro:

    resultado=linha.split()[1]
    lista_ips.append(resultado)
    #resultado=linha[0]
    
    #print(resultado)
    pass

lista_sem_duplicados=set(lista_ips)

for ip in lista_sem_duplicados:
    print(ip, "---", lista_ips.count(ip))