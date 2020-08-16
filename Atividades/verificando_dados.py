#Variaveis
user = ['Luís Kennedy']
password = ['289648137']
database = [
    user , password
]

#Funções
def login():
    login_user = input("User:     ")
    login_password = input("Password:   ")
    if login_user in user and login_password in password:
        print(f"Welcome {login_user}!")


#Execução
login()