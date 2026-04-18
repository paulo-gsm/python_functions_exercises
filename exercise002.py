def analisar_lista(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    
    print(f"\nQuantidade de pares: {len(pares)}")
    print(f"Quantidade de ímpares: {len(impares)}")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

# Entrada de dados
quantidade = int(input("Quantos números deseja digitar? "))
lista_user = []

for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    lista_user.append(num)

analisar_lista(lista_user)