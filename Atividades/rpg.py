#Import's
import random
#Variáveis

    #Classes
guerreiro = [
        #Nome(0)               Vida(1)
        'Guerreiro',            50,
        #Ataque básico(2)      dano(3)
        'Corte de espada',      10,
        #Ataque especial(4)    dano(5)
        'Lamina ardente',       20    
        ]
arqueiro = [
        #Nome(0)               Vida(1)
        'Arqueiro',             50,
        #Ataque básico(2)      dano(3)
        'Flecha veloz',         10,
        #Ataque especial(4)    dano(5)
        'Three shot',           20
    ]
mago = [
        #Nome(0)               Vida(1)
        'Mago',                 50,
        #Ataque básico(2)      Dano(3)
        'Bola de fogo',         10,
        #Ataque especial(4)    Dano(5)
        'Maldição',             20
    ]

oponente = [
        #Nome(0)               Vida(1)
        'Sr.Maldade',           100,
        #Ataque básico(2)      Dano(3)
        'Pedrada',              10,
        #Ataque especial(4)    Dano(5)
        'Lapada',               20    
]
#Funções 
def escolher_classe():
        print("""
            1. Guerreiro
            2. Arqueiro
            3. Mago
        """)
        classe = input('Escolha sua classe de acordo ao número.')
    while classe != ("1" or "2") or "3":
        print("Porfavor escolha sua classe de acordo com a numeração.")
        escolher_classe()
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
        print("Dados iguiais! Relancando dados...")
        batalha()

#Executando o programa
escolher_classe()