def classificar_ph(lista_ph):
    acidos = [] [cite: 25]
    neutros = [] [cite: 25]
    basicos = [] [cite: 25]
    
    for ph in lista_ph:
        if ph < 7:
            acidos.append(ph) [cite: 27]
        elif ph == 7:
            neutros.append(ph) [cite: 28]
        elif 7 < ph <= 14:
            basicos.append(ph) [cite: 29]
            
    print("\nRelatório de Análise:")
    print(f"Produtos Ácidos: {acidos}")
    print(f"Produtos Neutros: {neutros}")
    print(f"Produtos Básicos: {basicos}")

# Recebendo 12 valores [cite: 24]
ph_digitados = []
print("--- Análise Farmacêutica ---")
for i in range(12):
    valor = float(input(f"Digite o valor do pH do produto {i+1}: "))
    ph_digitados.append(valor)

classificar_ph(ph_digitados)