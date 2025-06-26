#parse de log UFW

ficheiro=open("ufw.log", "r")
list_ips=list()

for linha in ficheiro:
    #resultado=linha.split()[11][4:-1]
    #resultado = resultado[11]

    resultado=linha.split()[11]
    resultado=resultado.replace("SRC=","")
    list_ips.append(resultado)
    #print(resultado)

    pass

lista_sem_duplicados = set(list_ips)
#print(list_ips)

for ip in lista_sem_duplicados:
    print(ip, "---", list_ips.count(ip))