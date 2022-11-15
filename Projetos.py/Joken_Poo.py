from random import choice
print("="*40)
print("           JOKEN POO        ")
print("="*40)
jogador = 0
maquiana = 0

def Opcao_jogador():
    escol_jogador = input('Escolha Pedra, Papel ou Tessoura: ')
    escol_jogador.lower()
    if escol_jogador == 'Pedra':
        return escol_jogador
    elif escol_jogador == 'Papel':
        return escol_jogador
    elif escol_jogador == 'Tessoura':
        return escol_jogador
    else:
        print('Opção invalida. Tente novamente')
        Opcao_jogador
        
def Opcao_maquina():
    escol_maquina = choice(["Pedra", "Papel", "Tessoura"])
    return escol_maquina
        
while True:
    print("="*40)
    escol_jogador = Opcao_jogador()
    escol_maquina = Opcao_maquina()
    print("="*40)
    
    if (escol_jogador == "Pedra") and (escol_maquina == "Tessoura") \
        or (escol_jogador == "Papel") and (escol_maquina == "Pedra") \
            or (escol_jogador == "Tessoura") and (escol_maquina == "Papel"):
                
            print(f"Jogador escolheu {escol_jogador} e a maquina escolheu {escol_maquina}"
             " Resultado: Você Ganhou! ")
            jogador +=1
            
    elif escol_jogador == escol_maquina:
        print(f"Jogador escolheu {escol_jogador} e a maquina escolheu {escol_maquina}"
             " Resultado: Empate! ")
        
    else:
        print(f"Jogador escolheu {escol_jogador} e a maquina escolheu {escol_maquina}"
             " Resultado: Você Perdeu! ")
        
        maquiana +=1
        
    
    print("="*40)
    print(f'Vitorias do Jogador {jogador}')
    print(f'Vitorias da maquina {maquiana}')
    print("="*40)
        
    escol_jogador = input('Você quer jogar novamente? ')
    if escol_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif escol_jogador in ["NÃO", "não", "Não", "n", "N"]:
        print("="*40)
        print('           Jogo Finalizado         ')
        print("="*40)
        break
    else:
        break