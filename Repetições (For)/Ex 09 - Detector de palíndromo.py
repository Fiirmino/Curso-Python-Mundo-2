frase = input('Digite um nome ou frase: ').strip()
nova_frase1 = frase.replace(' ','')
frase_formatada = nova_frase1.upper()
frase_invertida = frase_formatada[::-1]

if frase_formatada == frase_invertida:
    print('É um palíndromo !!!')
else:
    print('Não é um palíndromo !!!')



