# Peça um número. 
# Mostre a tabuada dele de 1 a 10.

numero = int(input("Digite um número para ver a tabuada: "))
print("Tabuada de", numero,":")
for i in range (1, 11):
    print(numero, "x", i, "=", numero * i)

print("Fim do programa")