#Import's
import random
#Variáveis
dado = random.randint(1,20)
    #Classes
guerreiro = {
        'Guerreiro',
        #ataque básico    #dano
        'Corte de espada', 12,
        #Ataque especial  #dano
        'Espada luminosa', 23
    }



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
    



#Executando o programa
escolher_classe()