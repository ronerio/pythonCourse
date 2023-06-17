largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
balde = 2
area = largura * altura
baldes = area//balde

print('Você irá precisar de {} baldes de tinta para pintar sua parede'.format(baldes))
