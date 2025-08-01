# Multiplication Table
# This program prompts the user to enter two numbers and displays the multiplication table for each.

# Tabuada de multiplicação
# Este programa solicita ao usuário dois números e exibe a tabuada de multiplicação para ambos


x = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{x} x {i} = {x * i}")

x = int(input("Digite outro número: "))
for i in range(1,11):
    print(f"{x} x {i} = {x * i}")
