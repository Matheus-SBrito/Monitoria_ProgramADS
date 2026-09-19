"""
1. De acordo com um valor fornecido pelo usuário, mostre se ele é
divisível somente por 4, somente por 5, pelos dois (4 e 5), ou por
nenhum deles.
"""

# Entrada: um numero qualquer
# Processamento: Verificar divisibilidade com 4 e 5
# Saída: condicionado pela verificação de divisibilidade


numero = int(input("Digite um numero: "))

if (numero % 4 == 0):
    print("É divisivel por 4")
else:
    if (numero % 5 == 0):
        print("É divisivel por 5")
    else:
        print("Número não é divisevel por 4 ou 5")


