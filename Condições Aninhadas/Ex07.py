#CALCULO DE IMC (BASICO)
peso = float(input('Informe seu peso: '))
altura = float(input('informe sua altura: '))
imc = (peso/altura**2)

print(f'Seu imc é {imc:.2f}')

if imc<18.5:
    print('Você está abaixo do peso')
elif imc==18.5 and imc <=24.9:
    print('Você está no peso ideal')
elif imc >=25 and imc <=29.9:
    print('Sobrepeso')
elif imc>=30 and imc <=40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
