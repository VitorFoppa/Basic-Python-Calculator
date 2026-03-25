## Calculadora Python

numero1 = int(input("Digite um numero: "))
operador = str(input("Digite o operador: +, -, *, /, ^: "))
numero2 = int(input("Digite um numero: "))

if operador == "+":
    print(numero1 + numero2)
elif operador == "-":
    print(numero1 - numero2)
elif operador == "*":
    print(numero1 * numero2)
elif operador == "/":
    print(numero1 / numero2)
elif operador == "^":
    print(numero1 ** numero2)
else:
    print("Operador não identificado!")