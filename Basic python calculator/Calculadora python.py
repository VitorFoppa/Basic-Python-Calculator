## Calculadora Python
import tkinter as tk

## Criação da janela da calculadora.
janela = tk.Tk()
janela.title("Calculadora")
janela.focus_set()

janela.grid_rowconfigure(0, weight=1)
for i in range(6):  ## quantidade de linhas da calculadora
    janela.grid_rowconfigure(i, weight=1)

for j in range(4):  # quantidade de colunas
    janela.grid_columnconfigure(j, weight=1)

entrada = tk.Entry(janela, width=25, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")

## Variaveis
numero1 = None
operador = None

def teclado(event):
    tecla = event.char

    # números
    if tecla.isdigit():
        clicar(tecla)

    # operadores
    elif tecla in "+-*/^":
        definir_operador(tecla)

    # decimal
    elif tecla == ".":
        numeros_decimal()

    # Enter = calcular
    elif event.keysym == "Return":
        calcular()

    # Backspace = apagar último
    elif event.keysym == "BackSpace":
        atual = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, atual[:-1])

    # Esc = limpar tudo
    elif event.keysym == "Escape":
        limpar()

janela.bind("<Key>", teclado)

## Clicar em um numero.
def clicar(numero):
     atual = entrada.get()
     entrada.delete(0, tk.END)
     entrada.insert(0, atual + str(numero))

## Numeros decimais
def numeros_decimal():
    atual = entrada.get()
    if atual == "":
        entrada.insert(0, "0.")
    elif "." not in atual:
        entrada.insert(len(atual), ".")

## Função de limpar.
def limpar():
     global numero1, operador
     entrada.delete(0, tk.END)
     numero1 = None
     operador = None

## Definir operador.
def definir_operador(op):
     global numero1, operador
     try:
        numero1 = float(entrada.get())
        operador = op
        entrada.delete(0, tk.END)
     except:
        entrada.insert(0, "Erro")

## Operações.
def calcular():
     global numero1, operador
     try:
        numero2 = float(entrada.get())

        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            if numero2 == 0:
                raise ValueError("Impossivel dividir por 0")
            resultado = numero1 / numero2
        elif operador == "^":
            resultado = numero1 ** numero2
                

            
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))

        numero1 = None
        operador = None

     except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

## Botões numericos
botoes = [ ('7',1,0), ('8',1,1), ('9',1,2), ('4',2,0), ('5',2,1), ('6',2,2), ('1',3,0), ('2',3,1), ('3',3,2), ('0',4,0)]

for (texto, linha, coluna) in botoes:
     tk.Button(janela, text=texto, padx=20, pady=20, command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna, sticky="nsew")

## Operadores.
tk.Button(janela, text="+", padx=20, pady=20, command=lambda: definir_operador("+")).grid(row=1, column=3, sticky="nsew")

tk.Button(janela, text="-", padx=20, pady=20, command=lambda: definir_operador("-")).grid(row=2, column=3, sticky="nsew")

tk.Button(janela, text="*", padx=20, pady=20, command=lambda: definir_operador("*")).grid(row=3, column=3, sticky="nsew")

tk.Button(janela, text="/", padx=20, pady=20, command=lambda: definir_operador("/")).grid(row=4, column=3, sticky="nsew")

tk.Button(janela, text="^", padx=20, pady=20, command=lambda: definir_operador("^")).grid(row=4, column=2, sticky="nsew")

## Clear, igual e decimal
tk.Button(janela, text="C", padx=20, pady=20, command=limpar).grid(row=4, column=1, sticky="nsew")

tk.Button(janela, text="=", padx=20, pady=20, command=calcular).grid(row=5, column=3, sticky="nsew")

tk.Button(janela, text=".", padx=20, pady=20, command=numeros_decimal).grid(row=5, column=2, sticky="nsew")

janela.mainloop()