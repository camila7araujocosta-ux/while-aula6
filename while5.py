# Peça números ao usuário continuamente. 
# Informe se cada número é par ou ímpar. 
# O programa só deve parar quando o usuário digitar 0.

while True: 
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        print("O número",  numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")

print("Fim do programa")