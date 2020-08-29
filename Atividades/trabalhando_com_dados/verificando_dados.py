#Variaveis
user = ['LuisKennedy', 'Lucian123']
password = ['1234', '4321']
database = [
    user , password
]

#Funções
def login():
    login_user = input("Username:     ")
    login_password = input("Password:   ")
    if login_user in user and login_password in password:
        print(f"Welcome {login_user}!")
    else:
        print("Unfortunately your username or password is wrong")


#Execução
print("""
    Hello! 
    Please log writing your username and password!
""")
login()