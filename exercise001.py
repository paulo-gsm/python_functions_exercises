def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Exemplo de uso do sistema
print("--- Calculadora ---")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"Soma: {somar(n1, n2)}")
print(f"Subtração: {subtrair(n1, n2)}")
print(f"Multiplicação: {multiplicar(n1, n2)}")
print(f"Divisão: {dividir(n1, n2)}")