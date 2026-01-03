#calculadora br bonitona

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: ')) 

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print('A soma é: {}'.format(soma))
print('A subtração é: {}'.format(sub))
print('A multiplicação é: {}'.format(mult))
print('A divisão é: {:.2f}'.format(div))
print('Fim da calculadora.')