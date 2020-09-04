#Import's
import random
#Variáveis
dado = random.randint(1,20)
    #Classes
guerreiro = [
        #Nome(0)
        'Guerreiro',
        #ataque básico(1) #dano(2)
        'Corte de espada', 10,
        #Ataque especial(3)  #dano(4)
        'Lamina ardente', 20    
        ]
arqueiro = [
        #Nome(0)
        'Arqueiro',
        #ataque básico(1) #dano(2)
        'Flecha veloz', 10,
        #Ataque especial(3)  #dano(4)
        'Three shot', 20
    ]
mago = [
        #Nome(0)
        'Mago',
        #ataque básico(1) #dano(2)
        'Bola de fogo', 10,
        #Ataque especial(3)  #dano(4)
        'Maldição', 20
    ]

#Funções 
def escolher_classe():
    try:
        print("""
            1. Guerreiro
            2. Arqueiro
            3. Mago
        """)
        classe = int(input('Escolha sua classe de acordo ao número.'))
    except ValueError:
	    print("Somente números sao aceitos. Tente novamente.")
    if classe == 1 :
        print("Sua classe é guerreiro")
    elif classe == 2:
        print("Sua classe é arqueiro")
    elif classe == 3:
        print("Sua classe é mago")

def batalha():
    oponente = random.randint(1,20)
    player = random.randint(1,20)
    print(oponente)
    print(player)
    if oponente > player:
        print("Você tomou dano!")
    elif player > oponente:
        print("Causou dano!")
    else:
        print("Dados iguiais! Relancando dado...")
        batalha()

#Executando o programa
