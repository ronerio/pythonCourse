text = input('Digite algo: ')
print('O tipo desse carcatere é {} .'.format(type(text)))
print('Ele é alpha? {} .'.format(text.isalpha()))
print('Ele é alphanum? {} .'.format(text.isalnum()))
print('Ele está todo em caixa alta? {} .'.format(text.isupper()))
print('Ele está todo minúsculo? {} .'.format(text.islower()))