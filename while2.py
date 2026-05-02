# Peça ao usuário para digitar uma senha. 
# Continue solicitando até que ele acerte a senha correta (defina uma senha fixa no código).

senha_correta = ("senha123")
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")

print("Fim do programa")        