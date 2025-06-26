segundos=int(input("Qual o valor em segundos? "))

minutos=segundos/3600
hora=segundos/3600
minutos=(segundos%3600)/60
segundo=segundos%60

print("O valor inserido é equivalente a",int(hora),"horas",int(minutos),"minutos","e",int(segundo),"segundos")