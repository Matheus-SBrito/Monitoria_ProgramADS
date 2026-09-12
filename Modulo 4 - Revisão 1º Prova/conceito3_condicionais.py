# Estruturas Condicionais em Python
# if, else e elif


"""
O que são estruturas condicionais?

Estruturas condicionais são utilizadas quando queremos
que o programa tome uma decisão.

Em outras palavras, podemos fazer o programa verificar
uma determinada condição e, dependendo do resultado,
executar ou não determinadas instruções.

Para isso, utilizamos principalmente:

if
else
elif


A ideia básica é:

SE uma condição for verdadeira:
    execute determinado código.

CASO CONTRÁRIO:
    execute outro código.
"""


# ============================================================
# ESTRUTURA IF
# ============================================================

"""
A palavra reservada "if" significa "se".

Ela é utilizada para verificar se uma determinada
condição é verdadeira.

Exemplo:
"""

idade = 18

if idade >= 18:
    print("Você é maior de idade.")


"""
Observe que a condição:

idade >= 18

é uma comparação.

O Python irá verificar se essa comparação é verdadeira
ou falsa.

Como 18 é maior ou igual a 18, a condição é verdadeira.

Portanto, o comando print() será executado.
"""


# ============================================================
# INDENTAÇÃO
# ============================================================

"""
A indentação é muito importante em Python.

Ela serve para indicar quais instruções pertencem
à estrutura condicional.

Exemplo:
"""

idade = 20

if idade >= 18:
    print("Maior de idade.")
    print("Pode continuar.")


"""
Os dois comandos print() estão indentados.

Isso significa que os dois pertencem ao if.

Se a condição for verdadeira, os dois serão executados.
"""


# ============================================================
# IF COM UMA CONDIÇÃO FALSA
# ============================================================

"""
Quando a condição do if for falsa, as instruções
que estão dentro dele não serão executadas.

Exemplo:
"""

idade = 15

if idade >= 18:
    print("Você é maior de idade.")


"""
Nesse caso:

15 >= 18

é falso.

Por isso, o print() não será executado.

O programa simplesmente continuará sua execução
a partir da próxima instrução.
"""


# ============================================================
# ESTRUTURA ELSE
# ============================================================

"""
A palavra reservada "else" significa "senão".

Ela é utilizada quando queremos executar um código
caso a condição do if seja falsa.

Exemplo:
"""

idade = 15

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


"""
Nesse exemplo temos duas possibilidades:

Se idade >= 18:
    executa o primeiro print().

Caso contrário:
    executa o segundo print().


O else não possui uma condição própria.

Ele representa justamente o caminho contrário
ao resultado do if.
"""


# ============================================================
# IF E ELSE COM ENTRADA DO USUÁRIO
# ============================================================

"""
Podemos utilizar input() para receber uma informação
do usuário e depois utilizar essa informação
em uma estrutura condicional.
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


"""
Nesse exemplo:

1. input() recebe a idade.

2. int() transforma o texto recebido em número inteiro.

3. A idade é armazenada na variável "idade".

4. O if verifica se a idade é maior ou igual a 18.

5. Se for verdadeira, executa o primeiro print().

6. Se for falsa, executa o print() que está no else.
"""


# ============================================================
# ESTRUTURA ELIF
# ============================================================

"""
A palavra reservada "elif" significa "senão, se".

Ela é utilizada quando precisamos verificar
mais de uma condição.

Podemos pensar da seguinte maneira:

if
    -> verifica a primeira condição.

elif
    -> verifica outra condição caso a anterior seja falsa.

else
    -> executa caso nenhuma das condições anteriores
       seja verdadeira.
"""


# ============================================================
# EXEMPLO COM IF, ELIF E ELSE
# ============================================================

"""
Vamos criar um programa que analisa a idade de uma pessoa.
"""

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")

elif idade < 18:
    print("Adolescente")

else:
    print("Adulto")


"""
O programa verifica as condições na ordem em que
elas aparecem.

Primeiro:

idade < 12

Se for verdadeira, o programa executa o código
do if e não verifica os próximos caminhos.

Caso seja falsa, verifica:

idade < 18

Se essa condição for verdadeira, executa o elif.

Caso as duas condições sejam falsas, executa o else.
"""


# ============================================================
# MAIS DE UM ELIF
# ============================================================

"""
Podemos utilizar vários elif quando precisamos
analisar várias possibilidades.

Exemplo:
"""

nota = float(input("Digite sua nota: "))

if nota >= 9:
    print("Excelente")

elif nota >= 7:
    print("Bom")

elif nota >= 5:
    print("Regular")

else:
    print("Insuficiente")


"""
Nesse exemplo temos quatro possibilidades:

nota >= 9
    -> Excelente

nota >= 7
    -> Bom

nota >= 5
    -> Regular

Caso nenhuma dessas condições seja verdadeira:
    -> Insuficiente
"""


# ============================================================
# OPERADORES DE COMPARAÇÃO
# ============================================================

"""
As estruturas condicionais normalmente utilizam
operadores de comparação.

Alguns dos principais são:

==    igual
!=    diferente
>     maior
<     menor
>=    maior ou igual
<=    menor ou igual


Exemplos:
"""

numero = 10

if numero == 10:
    print("O número é igual a 10.")

if numero != 5:
    print("O número é diferente de 5.")

if numero > 5:
    print("O número é maior que 5.")

if numero < 20:
    print("O número é menor que 20.")


"""
O resultado de uma comparação sempre será um
valor booleano:

True
ou
False

Por exemplo:

10 > 5

resultado:

True
"""


# ============================================================
# CONDIÇÕES COM TEXTOS
# ============================================================

"""
As estruturas condicionais também podem ser utilizadas
para comparar textos.
"""

senha = input("Digite a senha: ")

if senha == "1234":
    print("Senha correta.")
else:
    print("Senha incorreta.")


"""
Nesse exemplo, o programa compara o texto digitado
pelo usuário com o texto "1234".

Se forem iguais:
    executa o if.

Caso sejam diferentes:
    executa o else.
"""


# ============================================================
# CONDIÇÕES COM OPERADORES LÓGICOS
# ============================================================

"""
Também podemos combinar mais de uma condição utilizando
operadores lógicos.

Os principais são:

and
    -> E

or
    -> OU

not
    -> NÃO


Exemplo utilizando "and":
"""

idade = 20
tem_documento = True

if idade >= 18 and tem_documento == True:
    print("Pode entrar.")


"""
Nesse caso, as duas condições precisam ser verdadeiras:

idade >= 18
E
tem_documento == True
"""


# ============================================================
# RESUMO
# ============================================================

"""
As estruturas condicionais permitem que o programa
tome decisões.

if
    -> verifica uma condição.

elif
    -> verifica uma nova condição caso as anteriores
       sejam falsas.

else
    -> executa quando nenhuma das condições anteriores
       for verdadeira.


Estrutura básica:

if condição:
    código

elif outra_condição:
    código

else:
    código


Podemos resumir o funcionamento assim:

                condição?
                   |
             +-----+-----+
             |           |
           True        False
             |           |
            if         elif?
                         |
                   +-----+-----+
                   |           |
                 True        False
                   |           |
                 elif        else
                   |
                 código


As estruturas condicionais são utilizadas para fazer
o programa escolher diferentes caminhos de acordo
com os dados recebidos.

Exemplo:

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
"""
