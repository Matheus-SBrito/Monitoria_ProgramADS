# Estruturas Condicionais, Blocos de Código e Lógica Booleana em Python

Para que um programa de computador seja capaz de resolver problemas do mundo real, ele não pode se limitar a executar comandos em uma sequência cega do início ao fim. Ele precisa ter a capacidade de **tomar decisões**, escolhendo diferentes caminhos de execução com base em dados recebidos do usuário ou em resultados de cálculos prévios.

Na linguagem Python, a tomada de decisão é realizada através das **estruturas condicionais** (`if`, `elif`, `else`), que dependem diretamente de **expressões lógicas**, **variáveis booleanas** e da organização estrita de **blocos de código por indentação**.

---

## 1. A Base da Decisão: Tipos Booleanos e Expressões Lógicas

Antes que o computador possa decidir qual caminho seguir, ele precisa avaliar se uma afirmação é verdadeira ou falsa. Essa avaliação resulta em um tipo especial de dado: o **tipo booleano** (`bool`).

### A) O Tipo Booleano (`bool`)

Uma variável do tipo booleano só pode assumir dois valores possíveis na memória:

* `True` (Verdadeiro — representado internamente pelo valor `1`)
* `False` (Falso — representado internamente pelo valor `0`)

Note que em Python esses valores começam obrigatoriamente com letra maiúscula (`True` e `False`).

```python
chovendo = True
pago = False
```

### B) Operadores Relacionais (Comparações)

Para gerar um valor booleano a partir de dados, utilizamos os **operadores relacionais**, que realizam comparações entre dois valores ou variáveis:

| Operador | Significado | Exemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `10 > 20` | `False` |
| `<` | Menor que | `7 < 12` | `True` |
| `>=` | Maior ou igual a | `8 >= 8` | `True` |
| `<=` | Menor ou igual a | `4 <= 2` | `False` |

*Atenção:* Um dos erros mais comuns em programação é confundir o operador de **atribuição** (`=`), usado para guardar valores em variáveis, com o operador relacional de **comparação** (`==`), usado para testar se dois valores são iguais.

### C) Operadores Lógicos (Condições Compostas)

Quando uma tomada de decisão depende de mais de uma condição simultânea, utilizamos os **operadores lógicos** para combinar as expressões:

1. **`and` (E):** Retorna `True` **apenas se todas** as condições envolvidas forem verdadeiras.

    ```python
    idade = 20
    tem_carteira = True
    pode_dirigir = (idade >= 18) and tem_carteira  # Resulta em True
    ```

2. **`or` (OU):** Retorna `True` se **pelo menos uma** das condições for verdadeira.

    ```python
    dia = "Sábado"
    feriado = False
    descanso = (dia == "Sábado") or feriado  # Resulta em True
    ```

3. **`not` (NÃO):** Inverte o valor booleano da expressão. Se o valor for `True`, ele se torna `False`, e vice-versa.

    ```python
    bloqueado = False
    acesso = not bloqueado  # Resulta em True
    ```

---

### 2. O Conceito de Bloco de Código e Indentação

Um **bloco de código** é um conjunto de instruções agrupadas que devem ser executadas juntas sob uma determinada condição.

Diferente de outras linguagens que utilizam chaves `{ }` ou palavras reservadas como `begin` e `end` para delimitar onde um bloco começa e termina, **o Python utiliza exclusivamente a indentação (espaçamento à esquerda)**.

#### A Regra da Indentação em Python

1. **O Sinal de Dois-Pontos (`:`):** Toda instrução condicional (`if`, `elif`, `else`) deve terminar obrigatoriamente com o caractere de dois-pontos `:`. Esse sinal avisa ao interpretador Python que as linhas seguintes farão parte de um novo bloco de código.
2. **O Recuo Obrigatório:** Todas as linhas pertencentes ao bloco de código devem estar alinhadas à direita com o mesmo nível de recuo (o padrão recomendado é de **4 espaços** ou uma tecla `Tab`).
3. **Fim do Bloco:** Para encerrar um bloco de código e retornar ao fluxo normal do programa, basta voltar a escrever a linha de código sem o recuo da margem esquerda.

```python
# Linha fora da condicional (margem zero)
if idade >= 18:
    # Inicio do bloco condicional (indentado com 4 espaços)
    print("Você é maior de idade.")
    print("Pode tirar a carteira de motorista.")
# Fim do bloco condicional (voltou para a margem zero)
print("Programa finalizado com sucesso.")
```

Se você esquecer a indentação logo após os dois-pontos, o Python interromperá a execução e exibirá um erro de sintaxe (*IndentationError*).

---

### 3. As Estruturas Condicionais em Python

Dependendo do número de caminhos possíveis para a solução do problema, utilizamos variações das estruturas condicionais.

#### A) Decisão Simples (`if`)

A estrutura `if` (tradução de "se") é utilizada quando queremos que um bloco de código seja executado **apenas se uma condição for verdadeira**. Caso a condição seja falsa, o bloco é simplesmente ignorado.

```python
nota = float(input("Digite a nota: "))

if nota >= 60.0:
    print("Parabéns! Você foi aprovado.")
```

#### B) Decisão Composta (`if / else`)

A estrutura `if / else` (tradução de "se / senão") é utilizada quando o problema possui **dois caminhos mutuamente exclusivos**. Se a condição for verdadeira, executa-se o bloco do `if`. Se a condição for falsa, o bloco do `else` é executado obrigatoriamente.

```python
nota = float(input("Digite a nota: "))

if nota >= 60.0:
    print("Aprovado!")
else:
    print("Reprovado!")
```

*Nota:* O `else` nunca recebe uma condição própria. Ele é acionado automaticamente sempre que a condição do `if` associado resulta em `False`.

#### C) Decisão Encadeada ou Consecutiva (`if / elif / else`)

Quando nos deparamos com problemas que possuem **três ou mais opções de caminho**, utilizamos a palavra reservada **`elif`** (uma abreviação de *else if*).

O `elif` permite testar uma nova condição caso a condição do `if` anterior tenha falhado. Você pode utilizar quantos `elif` forem necessários.

```python
nota = float(input("Digite a nota: "))

if nota >= 70.0:
    print("Aprovado com Louvor!")
elif nota >= 60.0:
    print("Aprovado!")
elif nota >= 40.0:
    print("Em Recuperação!")
else:
    print("Reprovado!")
```

#### Como o Interpretador Avalia o `if / elif / else`

O Python avalia as condições de cima para baixo de forma estritamente sequencial:

1. Testa a condição do `if`. Se for `True`, executa seu bloco e **pula imediatamente para fora de toda a estrutura condicional**, ignorando todos os `elif` e o `else` abaixo.
2. Se a condição do `if` for `False`, testa o primeiro `elif`. Se for `True`, executa seu bloco e sai da estrutura.
3. Se todas as condições anteriores falharem (`False`), e houver um bloco `else` ao final, o bloco do `else` será executado.

---

### 4. Boas Práticas e Prevenção de Erros Comuns

1. **Evite Condições Redundantes:** Em uma cadeia `if/elif/else`, cada condição só é testada se as anteriores falharam. Portanto, evite repetir testes desnecessários:

    * *Incorreto (Redundante):*

        ```python
        if imc < 18.5:
            print("Abaixo do peso")
        elif imc >= 18.5 and imc < 25.0:  # O 'imc >= 18.5' é desnecessário!
            print("Peso normal")
        ```

    * *Correto (Limpo e Eficiente):*

        ```python
        if imc < 18.5:
            print("Abaixo do peso")
        elif imc < 25.0:  # Se chegou aqui, com certeza imc >= 18.5
            print("Peso normal")
        ```

2. **`if` Sequenciais vs. `elif` Consecutivos:**

    * Use **vários blocos `if` independentes** quando você deseja que mais de uma condição possa ser verdadeira e executada no mesmo programa.
    * Use **`if / elif / else`** quando os caminhos forem mutuamente exclusivos (apenas um deles deve ser executado).

3. **Sempre verifique a presença de `:`** no final das linhas dos comandos `if`, `elif` e `else`.
