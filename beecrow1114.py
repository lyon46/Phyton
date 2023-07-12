#Escreva um programa que continue lendo uma senha até que ela seja
# válida. Para cada senha errada lida, escreva a mensagem "Senha inválida". Quando a senha
# for digitada corretamente imprima a mensagem "Acesso Permitido"
# e finalize o programa. A senha correta é o número 2002.
#Fixed Password

while True:

    password = input()

    if password == "2002":

        print("Acesso Permitido")
        break
    else:

        print("Senha Invalida")