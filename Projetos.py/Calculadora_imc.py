
print('             Calculando IMC')
print('-' * 40)
nome = ''
idade = 0
altura = 0
peso = 0
data_atual = '17/10/2022'
nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a dua idade: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
indice_massa_corporal = peso / (altura ** 2)
print('-' * 40)
print(f'Olá {nome}')
print(f'voce tem {idade} anos e seu imc é {indice_massa_corporal:.2f}')
