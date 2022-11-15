nome = str(input('Qual o seu nome: '))
idade = int(input('Qual a sua idada? '))

# idade_limite = 18
idade_menor = 18
idade_maior = 65

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} emprestimo concedido.')
else:
    print(f'{nome} emprestimo não concedido')