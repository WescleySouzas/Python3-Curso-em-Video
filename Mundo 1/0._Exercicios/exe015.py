dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

total = (dias_alugados * 60) + (km_rodados * 0.15)

print(f"O total a pagar e de R${total:.2f}")