# Peça vários números ao usuário (encerra com 0).
# Informe qual foi o maior número digitado.

maior = None

while True: 
    numero = float(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if maior is None or numero > maior:
        maior = numero
        if maior is not None:
            print("O maior número até agora é:", maior)

print("Fim do programa")