# Peça números ao usuário e some-os. 
# O programa deve parar quando o usuário digitar um número negativo. 
# Ao final, mostre a soma total. 

soma = 0

while True: 
    numero = float(input("Digite um número (negativo para parar): "))
    if numero < 0:
        break
    soma += numero
print("A soma total é:", soma)

print("Fim do programa")