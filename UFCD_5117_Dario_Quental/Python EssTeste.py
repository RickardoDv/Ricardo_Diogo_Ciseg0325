"""
#CONVERSÃO  OCTAL PARA DECIMAL
print(0o123)
#CONVERSÃO HEXADECIMAL PARA DECIMAL
print(0x123)
#USO DE EXPOENTE
print(3E8)
print(6.62607E-34)
print(0.0000000000000000000001)
"""
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)
"""
"""
user_word = input("Enter a word: ")
user_word = user_word.upper()  

for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    print(letter)
"""
#import os
#os.system('cls' if os.name == 'nt' else 'clear')

#my_list = [[0, 1, 2, 3] for i in range(2)]
#print(my_list[2][0]) 


soma = 0

num1=int(input("insira um numero: "))

for i in range(1, num1):
    if num1 % i == 0:
        soma += i
if soma == num1:
    print("Numero perfeito")
else:
    print("Numero imperfeito")

