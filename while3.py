# Peça um número inteiro positivo N 
# Mostre todos os números de 1 até N usando repetição.

N = int(input("Digite um número inteiro positivo: "))

if (N > 0):
    print("Números de 1 até", N,":")
    i = 1
    while i <= N:
        print(i)
        i += 1
else:
    print("Número inválido. Por favor, tente novamente.")
    
print("Fim do programa")