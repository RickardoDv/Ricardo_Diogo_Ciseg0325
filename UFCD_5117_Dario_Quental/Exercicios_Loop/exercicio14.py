#Altere o programa anterior 
#para que mostre todas as tabuadas de 1 a 100. (ciclos for).

"""
num1=int(input("Introduza um valor:"))

num2=1
while num2<=10:
    result=num1*num2
    print(num1,"X",num2,"=", result)
    num2+=1
"""
for num1 in range (1,101):
    print("Tabuada do ", num1)
    for num2 in range(1,11):
        num3=num1*num2
        print(f"{num1} X {num2} = {num3}")