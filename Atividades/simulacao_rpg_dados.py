#Import's
import random
#Variáveis
dado = random.randint(1,20)


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
        escolher_classe()
    



#Executando o programa
escolher_classe()