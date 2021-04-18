#Main programing... ¨Função de voltar ao menu
#Aluno: Luís Kennedy Ramos da Silva
#Série: 2°A
def main():
    print("Olá! Seja bem-vindo ao menu do programa!")
    atividade = int(input("""
        Escolha um das atividades de acordo com sua numeração:
            1. Programa que mostre a mensagem "OlÁ ETE PORTO DIGITAL!" na tela.
            2. Programa que peça um número e então mostre a mensagem O número informado foi [número].
            3. Programa que peça dois números e imprima a soma.
            4. Programa que peça as 4 notas bimestrais e mostre a média.
            5. Programa que converta metros para centímetros.
            6. Programa que peça o raio de um círculo, calcule e mostre sua área.
            7. Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
            8. Programa Calcule e mostre o total do seu salário no referido mês.
            9. Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
            10. Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
            11. Programa que verifique se uma letra digitada é vogal ou consoante
    """))
    if atividade == 1:
        atividade_1()
    elif atividade == 2:
        atividade_2()
    elif atividade == 3:
        atividade_3()
    elif atividade == 4:
        atividade_4()
    elif atividade == 5:
        atividade_5()
    elif atividade ==  6:
        atividade_6()
    elif atividade == 7:
        atividade_7()
    elif atividade == 8:
        atividade_8()
    elif atividade == 9:
        atividade_9()
    elif atividade == 10:
        atividade_10()
    elif atividade == 11:
        atividade_11()
                                                        #Atividades

def escolha():
    print("""
        1. Rever atividade
        2. Voltar para o menu
        3.Finalizar
    """)
    escolha = int(input("O que deseja agora?   "))
    if escolha == 1:
        atividade_1()
    elif escolha == 2:
        main()
    elif escolha == 3:
        print("Finalizado.")

#Atividade 1
def atividade_1():
    print("Olá Mundo!")
    escolha()

#Atividade 2
def atividade_2():
    number = float(input("Digite um número:   ")) 
    print(f"O número informado foi {number}")
    escolha()

#Atividade 3
def atividade_3():
    number1 = float(input("Digite o primeiro número:  "))
    number2 = float(input("Digite o segundo número:   "))
    print(f"A soma entre {number1} e {number2} é {number1 + number2}")
    escolha()

#Atividade 4
def atividade_4():
    nota1 = float(input("Digite a nota da sua primeira unidade:     "))
    nota2 = float(input("Digite a nota da sua segunda unidade:     "))
    nota3 = float(input("Digite a nota da sua terceira unidade:     "))
    nota4 = float(input("Digite a nota da sua quarta unidade:     "))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A sua média é de {media}")
    if media < 5:
        print("Você infelismente foi reprovado!")
    else: 
        print("Parabéns! Você passou!")
    escolha()

#Atividade 5
def atividade_5():
    medida_metros = float(input("Digite a medida para ser convertida:  "))
    medida_centimetros = medida_metros * 100
    print(f"A medida em metros convertida para centímentros é de {medida_centimetros}.")
    escolha()

#Atividade 6
def atividade_6():
    raio = float(input("Digite o tamanho do raio:       "))
    area = 2 * 3.14 * raio**2
    print(f"A área do círculo é de {area}.")
    escolha()

#Atividade 7
def atividade_7():
    lado = float(input("Digite o tamanho de um dos lados do quadrado:      "))
    area = lado**2
    print(f"O dobro da área do quadrado é {area * 2}")
    escolha()

#Atividade 8
def atividade_8():
    dinheiro_por_horas = float(input("Digite quanto você ganha por hora:      "))
    horas_trabalhadas = float(input("Digite quantas horas por mês você trabalha:    "))
    salario = dinheiro_por_horas * horas_trabalhadas
    print(f"Você recebe R${salario} por mês.")
    escolha()

#Atividade 9
def atividade_9():
    number = float(input("Digite um número:   "))
    if number < 0:
        print(f"O valor {number} é negativo.")
    elif number == 0:
        print(f"O valor não é positivo e nem negativo.")
    elif number > 0:
        print(f"O valor {number} é positivo.")
    escolha()

#Atividade 10
def atividade_10():
    sexo = input('Digite seu sexo, tal que "M" para masculino ou "F" para feminino:     ')
    if sexo != "M" and "m" or "F" and "f":
        print("Sexo inválido.")
        atividade_10()
    elif sexo == "M" or "m":
        print("Seu sexo é masculino.")
    elif sexo == "F" or "f":
        print("Seu sexo é feminino.")
    escolha()

#Atividade 11
def atividade_11():
    letra = input("Digite a letra desejada:     ")
    vogais = ("a","A", "e", "E", "I", "i", "U", "u")
    consoantes = ("Q", "q", "W", "w", "R", "r", "T", "t", "Y", "y", "P", "p" "S", "s", "D", "d", "F", "f", "G", "g", "H","h", "J", "j", "K", "k", "L", "l", "Ç", "ç", "Z", "z", "X", "x", "C", "c", "V", "v", "B", "b","N", "n", "M", "m" )
    if letra in vogais:
        print("Vogal!")
    elif letra in consoantes:
        print("Consoante!")
    escolha()



#Execução do programa
main()




    

