real = int(input('Digite o valor que você tem em reais. '))
dolar = 3.27
conversao = real//dolar
sobra = real-(conversao*3.27)
print('Você consegue comprar um total de {} dólares e irá sobrar {} reais. '.format(conversao, sobra))