# Estruturas de Repetição em Python
# for e while


"""
O que são estruturas de repetição?

Estruturas de repetição são utilizadas quando queremos
que determinado trecho do nosso programa seja executado
várias vezes.

Imagine que precisamos mostrar uma mensagem 10 vezes.

Sem uma estrutura de repetição, precisaríamos escrever:

print("Olá")
print("Olá")
print("Olá")
...

Isso deixaria nosso código muito maior.

Com uma estrutura de repetição, podemos determinar
quantas vezes uma instrução deverá ser executada.

Em Python, as principais estruturas de repetição são:

for
while
"""


# ============================================================
# ESTRUTURA FOR
# ============================================================

"""
O "for" é utilizado quando sabemos ou conseguimos
determinar a quantidade de vezes que queremos repetir
uma determinada instrução.

Para realizar essas repetições, podemos utilizar
a função range().
"""


# ============================================================
# FUNÇÃO range()
# ============================================================

"""
A função range() gera uma sequência de números que pode
ser utilizada para controlar a quantidade de repetições.

Exemplo:

range(5)

Representa os valores:

0
1
2
3
4

Observe que o número 5 não é incluído.

A contagem começa, por padrão, no número 0.
"""


# ============================================================
# FOR COM range()
# ============================================================

"""
Podemos utilizar o range() dentro de um for.

Exemplo:
"""

for numero in range(5):
    print(numero)


"""
Nesse exemplo, o for irá repetir o print() cinco vezes.

A variável "numero" receberá, a cada repetição,
um valor diferente produzido pelo range().

Os valores serão:

0
1
2
3
4
"""


# ============================================================
# REPETINDO UMA INSTRUÇÃO
# ============================================================

"""
Nem sempre precisamos utilizar o valor produzido
pelo range().

Podemos simplesmente utilizar o for para repetir
uma determinada instrução.
"""

for numero in range(5):
    print("Olá, mundo!")


"""
Nesse caso, a mensagem será apresentada 5 vezes.

A variável "numero" existe para controlar as repetições,
mesmo que seu valor não seja utilizado no print().
"""


# ============================================================
# range() COM INÍCIO E FIM
# ============================================================

"""
Podemos informar dois valores para o range():

range(inicio, fim)

O primeiro valor representa onde a contagem começa.

O segundo representa onde a contagem termina.

Porém, o valor final NÃO é incluído.
"""

for numero in range(1, 6):
    print(numero)


"""
O resultado será:

1
2
3
4
5

Observe que o 6 não aparece.

Isso acontece porque o segundo valor do range()
determina o limite da repetição, mas não é incluído.
"""


# ============================================================
# range() COM PASSO
# ============================================================

"""
Também podemos informar um terceiro valor no range():

range(inicio, fim, passo)

O passo determina de quanto em quanto a contagem
será realizada.
"""

for numero in range(0, 11, 2):
    print(numero)


"""
O resultado será:

0
2
4
6
8
10

Nesse caso:

0 -> início
11 -> fim
2  -> passo

A cada repetição, o valor aumenta em 2.
"""


# ============================================================
# CONTAGEM REGRESSIVA COM range()
# ============================================================

"""
Também podemos utilizar um passo negativo para
realizar uma contagem regressiva.
"""

for numero in range(10, 0, -1):
    print(numero)


"""
O resultado será:

10
9
8
7
6
5
4
3
2
1

O -1 faz com que o valor diminua uma unidade
a cada repetição.
"""


# ============================================================
# FOR COM OPERAÇÕES MATEMÁTICAS
# ============================================================

"""
Podemos realizar operações matemáticas dentro
de um laço de repetição.
"""

for numero in range(1, 6):
    resultado = numero * 2
    print(resultado)


"""
Nesse exemplo, a cada repetição o programa:

1. Recebe um novo valor em "numero".

2. Multiplica esse valor por 2.

3. Armazena o resultado na variável "resultado".

4. Mostra o resultado na tela.
"""


# ============================================================
# FOR COM ESTRUTURA CONDICIONAL
# ============================================================

"""
Podemos utilizar estruturas condicionais dentro
de estruturas de repetição.

Exemplo:
"""

for numero in range(1, 11):

    if numero % 2 == 0:
        print(numero, "é par.")


"""
O for irá percorrer os números de 1 até 10.

A cada repetição, o if verifica se o número
é divisível por 2.

O operador "%" representa o resto da divisão.

Quando:

numero % 2 == 0

significa que o número é par.
"""


# ============================================================
# ESTRUTURA WHILE
# ============================================================

"""
O "while" também é utilizado para realizar repetições.

Porém, diferente do for, o while continua repetindo
enquanto uma determinada condição for verdadeira.

Podemos pensar da seguinte maneira:

ENQUANTO a condição for verdadeira:
    execute o código.


Exemplo:
"""

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1


"""
Nesse exemplo:

1. A variável "numero" começa com 1.

2. O while verifica:

   numero <= 5

3. Se a condição for verdadeira, o print() é executado.

4. Depois, aumentamos o valor de "numero" em 1.

5. O while verifica novamente a condição.

Esse processo continua até que:

numero <= 5

se torne falso.
"""


# ============================================================
# IMPORTÂNCIA DA ATUALIZAÇÃO DA VARIÁVEL
# ============================================================

"""
É muito importante alterar a variável utilizada
na condição do while.

Observe:
"""

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1


"""
A instrução:

numero = numero + 1

faz com que a variável seja atualizada.

Sem essa atualização, a condição poderia permanecer
verdadeira indefinidamente, fazendo com que o programa
ficasse preso em um laço infinito.

Exemplo de um laço infinito:

numero = 1

while numero <= 5:
    print(numero)

Nesse caso, "numero" nunca muda de valor.
"""


# ============================================================
# WHILE COM INPUT()
# ============================================================

"""
O while é muito útil quando a quantidade de repetições
depende de uma informação fornecida pelo usuário.

Exemplo:
"""

numero = int(input("Digite um número maior que 0: "))

while numero <= 0:
    print("Valor inválido.")

    numero = int(input("Digite um número maior que 0: "))

print("Valor válido:", numero)


"""
Nesse exemplo, o programa continuará solicitando
um número enquanto o usuário fornecer um valor menor
ou igual a zero.

Quando o usuário digitar um número maior que zero,
a condição:

numero <= 0

será falsa.

Então o while será encerrado.
"""


# ============================================================
# FOR E WHILE — DIFERENÇA
# ============================================================

"""
Apesar de ambos serem utilizados para repetição,
existe uma diferença importante entre eles.

FOR:

Normalmente utilizamos quando sabemos a quantidade
de repetições que queremos realizar.

Exemplo:
"""

for numero in range(5):
    print("Repetição")


"""
Nesse caso, sabemos que teremos 5 repetições.
"""


"""
WHILE:

Normalmente utilizamos quando a repetição depende
de uma condição.

Exemplo:
"""

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1


"""
Nesse caso, o laço continuará enquanto:

numero <= 5

for verdadeira.
"""


# ============================================================
# FOR E WHILE COM ESTRUTURAS CONDICIONAIS
# ============================================================

"""
Podemos combinar:

for
while
if
elif
else

Isso permite criar programas mais completos.
"""

for numero in range(1, 11):

    if numero % 2 == 0:
        print(numero, "é par.")
    else:
        print(numero, "é ímpar.")


"""
Nesse programa:

O for controla a quantidade de repetições.

O if verifica uma condição.

O else representa o caminho contrário.

Dessa forma, podemos utilizar diferentes estruturas
da linguagem em conjunto.
"""


# ============================================================
# RESUMO
# ============================================================

"""
Estruturas de repetição são utilizadas para executar
um determinado trecho de código várias vezes.

FOR
    -> Utilizado principalmente quando sabemos
       a quantidade de repetições.

WHILE
    -> Utilizado quando a repetição depende
       de uma condição.


A função range() pode ser utilizada com o for.

range(fim)

range(inicio, fim)

range(inicio, fim, passo)


Exemplos:

range(5)
    -> 0, 1, 2, 3, 4

range(1, 6)
    -> 1, 2, 3, 4, 5

range(0, 11, 2)
    -> 0, 2, 4, 6, 8, 10

range(10, 0, -1)
    -> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


Podemos resumir:

FOR
    -> "Repita uma quantidade determinada de vezes."

WHILE
    -> "Repita enquanto uma condição for verdadeira."


Exemplo de FOR:

for numero in range(5):
    print(numero)


Exemplo de WHILE:

numero = 0

while numero < 5:
    print(numero)
    numero = numero + 1


Nos dois exemplos, temos 5 repetições.

A diferença está na forma como controlamos
essas repetições.
"""