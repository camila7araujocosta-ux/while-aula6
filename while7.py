# Peça várias notas ao usuário (encerra quando digitar -1).
# Calcule a média das notas válidas.

soma = 0 
contador = 0

while True:
    nota = float(input("Digite um número (ou -1 para parar): "))
    if (nota == -1):
        break
    soma += nota 
    contador += 1
    
if (contador > 0):
    media = soma / contador
    print("A média das notas válidas é:", media)
else:
    print("Nenhuma nota válida foi digitada.")

print("Fim do programa")