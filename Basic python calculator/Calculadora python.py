## Calculadora Python

numero1 = float(input("Digite um numero: "))
operador = str(input("Digite o operador: +, -, *, /, ^: "))
numero2 = float(input("Digite um numero: "))

if operador == "+":
    print(numero1 + numero2)
elif operador == "-":
    print(numero1 - numero2)
elif operador == "*":
    print(numero1 * numero2)
elif operador == "/":
        if numero2 != 0:
            print(numero1 / numero2)
        else:
            print("Impossivel dividir por 0.")
elif operador == "^":
    print(numero1 ** numero2)
else:
    print("Operador não identificado!")