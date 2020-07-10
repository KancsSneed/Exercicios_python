#Sistema de recolhimento de dados dos usuários para criação de uma lista.

input('Precione qualquer teclar para começar!')

datebase = []

def cadastro():
    name = input("""Digite seu nome:""")
    senha = input("""Digite sua senha:""")
    novo_cadastro = input("""Deseja fazer o cadastro navamente?""")
    user = f'Name:  {name}', f'Password: {senha}'
    datebase.append(user)
    print(datebase)    
    if novo_cadastro == "Sim":
        cadastro()
cadastro()
