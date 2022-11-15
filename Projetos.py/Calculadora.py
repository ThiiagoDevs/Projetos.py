    
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Didite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? S ou N:')
    
    '''if sair == 's':
       break'''
        
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Vocẽ precisa digitar um número.')
        continue
    
    num_1 = int(num_1)
    num_2 = int(num_2)
    
     # +-*/**// %
     
    if operador == '+':
        print(num_1 + num_2)
        if sair == 's':
            print('Calculadora finalizada.')
            break
    elif operador == '-':
        print(num_1 - num_2)
        if sair == 's':
            print('Calculadora finalizada.')
            break
    elif operador == '*':
        print(num_1 * num_2)
        if sair == 's':
            print('Calculadora finalizada.')
            break
    elif operador == '/':
        print(num_1 / num_2)
        if sair == 's':
            print('Calculadora finalizada.')
            break
    elif operador == '**':
        print(num_1 ** num_2)
        if sair == 's':
            print('Calculadora finalizada.')
            break
    elif operador == '//':
        print(num_1 // num_2)
        if sair == 's':
            print('Calculadora finalizada.')
            break
    else:
        print('Operador invalido')
