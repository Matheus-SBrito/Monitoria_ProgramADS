"""
1. Ler dois valores numéricos inteiros e apresentar o resultado da diferença
sempre do maior valor pelo menor valor.
"""

# Entrada: dois numeros inteiros
# Processamento: Decobrir que é o maior e o menor
# Saída: Ordenar os valores e exibi-los

numero1 = int(input("1° Número, digite um número: "))
numero2 = int(input("2° Número, digite um número: "))

if (numero1 > numero2):
    print("Diferença entre os valores: ", numero1 - numero2)

else:
    print("Diferença entre os valores: ", numero2 - numero1)