# Definição de Variaveis, instruções simples e primitivias


# O simbolo '#' serve para por textos comuns em nosso código, em uma unica linha.

"""
As 3 aspas servem para definir todo o espaço
contido, abaixo e afrente, nela como um comentário
para encerramos este espaço de texto, é necessário
repetir denovo as 3 aspas.
"""


# definição de variaveis

numero_inteiro = 1
texto = "eu sou um texto"
caractere = "a"
numero_real = 2.1
comparacao = (1 == 2) # True ou False

"""
Cada uma desses dados tem um palavra reservada para
podermos nos referir a eles e classifica-los.
"""

numero_inteiro:int

texto:str
caractere:str

numero_real:float

comparacao: bool

# Operações matematicas

resultado = numero_inteiro + 2
resultado = numero_real * 2
resultado = numero_real/2
resultado = numero_inteiro - 1

""" Para que servem as variaveis ?
 
Em vez de escrever um código que processa apenas valores fixos, 
criamos algoritmos genéricos (como `resultado = valor1 + valor2`). 
Dessa forma, o mesmo programa consegue processar dados variados 
fornecidos pelo usuário.
"""