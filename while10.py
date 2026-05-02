# Defina um número fixo no código. 
# Peça ao usuário para adivinhar até acertar. 
# Informe se o palpite é maior ou menor que o número correto.

numero_correto = 42

while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite < numero_correto:
        print("O número correto é maior.")
    elif palpite > numero_correto:
        print("O número correte é menor.")
    else:
        print("Parabéns! Você acertou!")
        break

print("Fim do programa")