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

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)


"""

import os
os.system('cls' if os.name == 'nt' else 'clear')


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
