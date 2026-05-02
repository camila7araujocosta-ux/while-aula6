# Peça números ao usuário até que ele digite 0. 
# Ao final, informe quantos números positivos e quantos negativos foram digitados.

positivos = 0
negativos = 0

while True: 
    numero = float(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1 

print("Números positivos digitados:", positivos)
print("Números negativos digitados:", negativos)

print("Fim do programa")        