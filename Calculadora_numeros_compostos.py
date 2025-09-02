# Calculadora de Juros Compostos

valor_inicial = float(input("Informe o valor inicial do investimento (R$): "))
taxa_juros_percentual = float(input("Informe a taxa de juros mensal (%): "))
tempo_meses = int(input("Informe o tempo do investimento (em meses): "))

# Conversão da taxa de juros para decimal
taxa_juros_decimal = taxa_juros_percentual / 100

# Cálculo do montante final
montante_final = valor_inicial * (1 + taxa_juros_decimal) ** tempo_meses

print(f"\n Após {tempo_meses} meses, o valor acumulado será de R$ {montante_final:.2f}")
