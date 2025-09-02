credito = 0.0
debito = 0.0
saldo = 0.0

nome = input("Digite o nome da pessoa: ")

credito = float(input("Digite o valor de crédito: "))
debito = float(input("Digite o valor de débito: "))

saldo = credito - debito

print("--- RESUMO DA CONTA ---")
print(f"Nome: {nome}")
print(f"Valor em Crédito: R$ {credito}")
print(f"Valor em Débito: R$ {debito}")
print(f"Saldo atualizado: R$ {saldo}")
