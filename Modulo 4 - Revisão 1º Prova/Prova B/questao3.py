"""
3. Escreva um algoritmo que realize a potência de A por B, ou seja, A^B,
através de multiplicações. Esses dois valores são inseridos pelo usuário,
tanto a base quanto o expoente.

Exemplo: se o usuário digitar 4 e 3, então deve realizar a operação
multiplicando o 4 três vezes (4 * 4 * 4) de forma acumulativa.
"""

# Entrada: base e expoente
# Processamento: realizar uma exponenciação com um laço de repetição
    # Multiplicar a base por ela mesma, a repetição do loop será
    # igual ao valor do expoente - 1, ou seja, repetição = expoente -1
# Saída: Resultado da Exponeciação, potência.

base = int ( input("Digite o valor da base: ") )
expoente = int ( input("Digite o valor do expoente: ") )

resultado = base
for repeticao in range (expoente - 1):

    print(f"Processo de Potenciação: {resultado} x {base} = {resultado*base}")
    resultado = resultado * base

print(f"Calculo: {base}^{expoente} = {resultado}")