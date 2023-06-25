dados = []
for c in range(1,6):
    peso = float(input(f'Informe o peso da {c}° pessoa:'))
    dados.append(peso)
print(f'O maior peso é {max(dados)}Kg')
print(f'O menor peso foi {min(dados)}Kg')