usuario  = str(input('Nome de usuário: '))
senha = input('Senha do usuário: ')


usuario_bd = 'Joao'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print(f'Bem-vindo, {usuario_bd}.')
else:
    print('Nome do usuario ou senha invalidos ')