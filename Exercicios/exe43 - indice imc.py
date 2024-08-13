
peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está no PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('ATENÇÃO. Você está em SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('CUIDADE. Você está em OBESIDADE. ')
else:
    print('Você está em OBESIDADE MORBIDA. Procure um médico!')







