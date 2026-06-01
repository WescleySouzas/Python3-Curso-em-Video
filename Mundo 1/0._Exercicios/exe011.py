largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

metro_quadrado = largura * altura

print(f'Sua parede tem {largura}x{altura} e sua area e de {metro_quadrado}m²')

qtd_por_litro = metro_quadrado / 2

print(f'A quantidade necessaria de tinta para pintar essa parede e de {qtd_por_litro}l de tinta')