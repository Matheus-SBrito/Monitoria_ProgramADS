"""
3. Faça a divisão de dois valores por meio de subtrações sucessivas.
Estes dois valores são passados pelo usuário.

Exemplo:
32 / 4 = 8

Pois consegue-se subtrair de trinta e dois o valor quatro oito vezes.
"""

# Entrada: 2 numeros fornecidos pelo usuário
    # Necessidade de utilizar a função input

# Processamento: obtenção do resultado da divisão
    # Utilização de laço de repetição

# Saída: exibição do resultado da revisão


dividendo = int (input("Digite o valor do dividendo: "))
divisor = int (input("Digite o valor do divisor: "))

# O resultado da divisão será obtido atravé de um laço
# de repetição, através de inumeras repetições para subtrair
# o valor do dividendo pelo valor do divisor.

resultadoDivisao_contador = 0
while (dividendo > 0):

    subtracao = dividendo - divisor
    print(f"\nCalculo: {dividendo} - {divisor} = {subtracao}")


    dividendo = subtracao
    resultadoDivisao_contador +=1
    print(f"Valor/contador da divisão: {resultadoDivisao_contador}")


if (dividendo < 0):
    resultadoDivisao_contador -= 1
print(f"\nResultado da divisão: {resultadoDivisao_contador}")