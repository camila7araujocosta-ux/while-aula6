# Solicite uma nota de 0 a 10
# Continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Informe uma nota de 0 a 10: "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Nota inválida. Por favor, tente novamente.")

print("Fim do programa")