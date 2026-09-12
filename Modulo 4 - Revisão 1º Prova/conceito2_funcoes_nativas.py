# Funções Nativas do Python
# Funções print() e input()


"""
O que são funções?

Funções são comandos que possuem uma determinada finalidade
dentro do nosso programa.

O Python já possui diversas funções prontas para serem
utilizadas. Essas funções são chamadas de FUNÇÕES NATIVAS.

Alguns exemplos de funções nativas do Python são:

print()
input()
int()
float()
str()

Neste momento, vamos estudar principalmente as funções
print() e input().
"""


# ============================================================
# FUNÇÃO print()
# ============================================================

"""
A função print() é utilizada para exibir informações
na tela do programa.

Tudo aquilo que estiver dentro dos parênteses será
enviado para a saída do programa.

Exemplo:
"""

print("Olá, mundo!")

print("Eu estou aprendendo Python.")

print(10)


"""
Podemos também utilizar variáveis dentro do print().
"""

nome = "João"
idade = 20

print(nome)
print(idade)


"""
Também podemos colocar textos e variáveis juntos
utilizando vírgulas.

A função print() irá separar automaticamente os
valores apresentados.
"""

print("Nome:", nome)
print("Idade:", idade)


# ============================================================
# FUNÇÃO input()
# ============================================================

"""
A função input() é utilizada para receber uma informação
digitada pelo usuário.

Quando o programa encontra um input(), ele fica aguardando
o usuário digitar alguma informação.

Exemplo:
"""

nome = input("Digite seu nome: ")

print("Olá,", nome)


"""
O valor digitado pelo usuário pode ser armazenado
dentro de uma variável.

Dessa forma, podemos utilizar posteriormente
a informação fornecida pelo usuário.
"""


# ============================================================
# input() E TIPOS DE DADOS
# ============================================================

"""
É importante observar que o input() recebe os dados
digitados pelo usuário como TEXTO (str).

Por exemplo:

"""

numero = input("Digite um número: ")

"""
Mesmo que o usuário digite:

10

O Python inicialmente considera esse valor como:

"10"

Ou seja, um texto (str).
"""


# ============================================================
# CONVERSÃO DE TIPOS
# ============================================================

"""
Quando queremos utilizar o valor recebido pelo input()
como um número, precisamos realizar uma conversão.

Para transformar um texto em número inteiro,
utilizamos a função nativa int().
"""

numero = int(input("Digite um número inteiro: "))

print(numero)


"""
Para transformar um texto em número real,
utilizamos a função nativa float().
"""

numero_real = float(input("Digite um número real: "))

print(numero_real)


# ============================================================
# UTILIZANDO input() E print() JUNTOS
# ============================================================

"""
As funções input() e print() podem ser utilizadas
em conjunto para criar programas interativos.

O input() recebe informações do usuário.

O print() apresenta informações na tela.

Exemplo:
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Seu nome é:", nome)
print("Sua idade é:", idade)


# ============================================================
# OPERAÇÕES COM VALORES RECEBIDOS PELO USUÁRIO
# ============================================================

"""
Depois que o valor recebido pelo input() é convertido
para um tipo numérico, podemos realizar operações
matemáticas normalmente.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = numero1 + numero2

print("O resultado da soma é:", resultado)


"""
Observe o funcionamento do programa:

1. input() solicita uma informação ao usuário.

2. int() transforma o texto recebido em um número inteiro.

3. O valor é armazenado em uma variável.

4. O programa realiza uma operação utilizando as variáveis.

5. print() apresenta o resultado na tela.
"""


# ============================================================
# RESUMO
# ============================================================

"""
Funções nativas são funções que já estão disponíveis
na linguagem Python.

print()
    -> Utilizada para apresentar informações na tela.

input()
    -> Utilizada para receber informações do usuário.

int()
    -> Converte um valor para número inteiro.

float()
    -> Converte um valor para número real.

str()
    -> Converte um valor para texto.


Podemos resumir o funcionamento básico assim:

input()  -> ENTRADA de dados
print()  -> SAÍDA de dados


Exemplo:

nome = input("Digite seu nome: ")
print("Olá,", nome)


Nesse exemplo:

input() recebe o dado do usuário.

O dado é armazenado na variável "nome".

print() utiliza essa variável para apresentar
uma mensagem na tela.
"""