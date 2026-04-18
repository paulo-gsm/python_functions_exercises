def analisar_clima(temperaturas):
    media = sum(temperaturas) / len(temperaturas)
    
    if media < 20:
        status = "Baixa" [cite: 19]
    elif 20 <= media <= 35:
        status = "Ideal" [cite: 20]
    elif 36 <= media <= 50:
        status = "Em alerta" [cite: 21]
    else:
        status = "Risco" [cite: 21]
        
    print(f"\nMédia das temperaturas: {media:.2f}°C")
    print(f"Análise: {status}")

# Coleta de 8 capturas (6h às 00h) [cite: 16]
print("--- Sistema INMET ---")
dados_temp = []
for h in range(8):
    t = float(input(f"Digite a {h+1}ª captura de temperatura: "))
    dados_temp.append(t)

analisar_clima(dados_temp)