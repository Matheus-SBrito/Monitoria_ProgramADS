# Estruturas de Repetição em Python (`for` e `while`)

As **estruturas de repetição** (também conhecidas como *laços*, *malhas* ou *loops*) são comandos fundamentais na programação que permitem executar um mesmo bloco de instruções repetidas vezes. Em vez de duplicar linhas de código manualmente para realizar uma tarefa recorrente, utiliza-se uma estrutura de repetição para instruir o computador a executar essas ações de forma automatizada, garantindo eficiência, legibilidade e redução de erros de código.

---

## 1. O Princípio das Estruturas de Repetição

No fluxo sequencial de um programa, as instruções são executadas linha após linha, de cima para baixo. Com as estruturas de repetição, é possível alterar esse fluxo e fazer com que o interpretador **volte** e reexecute um determinado bloco de código enquanto uma condição for satisfeita ou até que uma sequência de dados seja totalmente percorrida.

### A Estratégia de Resolução (EPS + Repetição)

Antes de escrever o código de um laço de repetição, deve-se analisar o problema sob a perspectiva da metodologia **EPS (Entrada, Processamento e Saída)** e responder a quatro perguntas essenciais:

1. **O que precisa ser repetido?** (Identificação do bloco de código subordinado).
2. **Quantas vezes a repetição deve ocorrer?** (Determinação da quantidade fixa ou condicional de iterações).
3. **Quando a repetição deve parar?** (Definição da condição de parada).
4. **Quais variáveis precisam ser inicializadas antes do início do laço?** (Contadores, acumuladores ou sinalizadores).

---

## 2. O Laço `while` (Repetição Condicional)

O laço `while` ("enquanto") é a estrutura indicada quando a repetição depende de uma **condição lógica** que pode ser verdadeira ou falsa, especialmente quando não se sabe previamente o número exato de vezes que o bloco será executado.

### A) Estrutura Sintática do 'while'

No `while`, a expressão lógica é testada antes de cada iteração (**pré-teste**). Enquanto o resultado dessa expressão for `True` (verdadeiro), o bloco subordinado será executado. Quando a condição se tornar `False` (falsa), o laço é encerrado e o programa continua a execução a partir da primeira linha após o laço.

```python
# Sintaxe geral do while
while condicao_logica:
    # Bloco de instruções subordinado (obrigatoriamente indentado)
    instrucao_1
    instrucao_2
    atualizacao_da_condicao
```

### B) Os Três Elementos Obrigatórios do `while`

Para que um laço `while` funcione corretamente e não trave o programa, é indispensável garantir a presença de três etapas:

1. **Inicialização:** A variável que controla a condição deve existir e ter um valor atribuído **antes** de o laço começar.
2. **Teste da Condição:** A expressão lógica é avaliada no cabeçalho do `while`.
3. **Atualização:** O valor da variável de controle deve ser modificado obrigatoriamente **dentro** do corpo do laço, caminhando em direção à condição de parada.

#### Exemplo Prático: Imprimir números de 1 a 5

```python
# 1. Inicialização da variável de controle
contador = 1

# 2. Teste da condição no cabeçalho
while contador <= 5:
    print(f"Número atual: {contador}")
    # 3. Atualização obrigatória para evitar loop infinito
    contador = contador + 1

print("Laço encerrado com sucesso!")
```

### C) O Erro do *Loop* Infinito

Se a atualização da variável de controle for esquecida ou escrita de forma incorreta dentro do corpo do `while`, a condição permanecerá eternamente verdadeira (`True`). Isso gera o chamado **loop infinito**, onde o programa fica preso na mesma repetição até ser interrompido forçadamente ou travar por esgotamento de memória.

### D) O Padrão `while True` e Encerramento com `break`

Em cenários onde a validação da condição precisa acontecer no meio ou no final do bloco (como em menus interativos ou leitura de dados com sentinela), utiliza-se o padrão `while True`. Esse laço executa indefinidamente até encontrar a palavra reservada **`break`**, que força a interrupção imediata da repetição.

```python
while True:
    opcao = input("Digite 'sair' para encerrar o programa: ")
    if opcao.lower() == "sair":
        print("Saindo do sistema...")
        break  # Interrompe e encerra o laço imediatamente
    print(f"Você digitou: {opcao}")
```

---

## 3. O Laço `for` (Repetição por Contagem e Iteração)

O laço `for` ("para") em Python é utilizado quando se conhece a quantidade exata de repetições a serem feitas ou quando se deseja percorrer (*iterar sobre*) os elementos de uma sequência ordenada (como listas, tuplas, dicionários ou cadeias de caracteres/strings).

### A) Estrutura Sintática do 'for'

Diferente de linguagens tradicionais onde é necessário gerenciar manualmente o incremento de índices, em Python o `for` extrai automaticamente um elemento da sequência a cada volta do laço e o atribui a uma variável de iteração.

```python
# Sintaxe geral do for
for variavel_iteradora in sequencia:
    # Bloco subordinado executado para cada item da sequência
    instrucao_1
```

#### Exemplo de Iteração sobre Lista

```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(f"Fruta selecionada: {fruta}")
```

---

## 4. A Função Nativa `range()`

Quando precisamos repetir um bloco um determinado número de vezes e não temos uma lista prévia de dados, utilizamos o laço `for` em conjunto com a função nativa **`range()`**. A função `range()` gera uma sequência numérica configurável na memória de forma eficiente.

A função `range()` pode ser chamada de três maneiras distintas:

| Assinatura | Comportamento | Exemplo de Sequência Gerada |
| :--- | :--- | :--- |
| **`range(fim)`** | Gera números de `0` até `fim - 1`. | `range(5)` $\rightarrow$ `0, 1, 2, 3, 4` |
| **`range(início, fim)`** | Gera números de `início` até `fim - 1`. | `range(1, 6)` $\rightarrow$ `1, 2, 3, 4, 5` |
| **`range(início, fim, passo)`** | Gera números de `início` até `fim - 1`, avançando de `passo` em `passo`. | `range(2, 11, 2)` $\rightarrow$ `2, 4, 6, 8, 10` |

### A) Regra do Limite Superior Não Incluído

Um detalhe crucial sobre a função `range()` é que **o número informado no limite final (`fim`) nunca é incluído na sequência**. Por exemplo, `range(1, 10)` produz os números de `1` a `9`. Se o objetivo for incluir o número `10`, o limite final deve ser ajustado para `11` (`range(1, 11)`).

### B) Contagem Decrescente

Para criar uma contagem regressiva, utiliza-se um valor negativo para o parâmetro `passo`:

```python
# Contagem regressiva do lançamento de um foguete
for i in range(10, 0, -1):
    print(i, end="... ")
print("Fogo!")
# Saída: 10... 9... 8... 7... 6... 5... 4... 3... 2... 1... Fogo!
```

### C) Variável Anônima (`_`)

Se a variável de controle do `for` servir apenas para contar quantas vezes o laço deve rodar, sem que seu valor seja utilizado dentro do bloco de comandos, convenciona-se utilizar o sublinhado (`_`) como nome de variável anônima.

```python
# Repete a mensagem 3 vezes sem usar o número da contagem
for _ in range(3):
    print("Processando dados...")
```

---

## 5. Instruções de Controle de Fluxo: `break` e `continue`

Dentro de qualquer laço de repetição (`while` ou `for`), é possível alterar o comportamento padrão de iteração utilizando duas instruções nativas:

* **`break` (Interrupção Total):** Aborta a execução do laço imediatamente. O controle do programa é transferido para a instrução que está logo após o bloco de repetição.
* **`continue` (Interrupção Parcial / Pulo):** Interrompe apenas a iteração atual. O interpretador ignora as linhas restantes do bloco subordinado e pula diretamente para o início da próxima iteração do laço.

```python
# Exemplo de continue: Imprimir números ímpares e pular os pares
for num in range(1, 8):
    if num % 2 == 0:
        continue  # Pula os números pares e não executa o print abaixo
    print(f"Número ímpar: {num}")
```

---

## 6. Variáveis de Apoio: Contadores e Acumuladores

Durante o processamento dentro de um laço de repetição, é muito comum precisar acompanhar a contagem de eventos ou a soma progressiva de valores. Para isso, utilizam-se duas categorias funcionais de variáveis:

### A) Contador

É uma variável utilizada para contar quantas vezes um evento específico ocorreu. Ela é inicializada com o valor `0` antes do início do laço e incrementada em um valor **fixo** (geralmente `+1`) a cada iteração confirmada.

```python
contador_pares = 0

for num in range(1, 11):
    if num % 2 == 0:
        contador_pares += 1  # Incremento fixo de 1 (contador)

print(f"Total de números pares encontrados: {contador_pares}")
```

### B) Acumulador

É uma variável utilizada para somar ou agrupar valores **variáveis** calculados ou lidos ao longo do laço. Assim como o contador, o acumulador deve ser inicializado antes do laço (com `0` para somas ou `1` para produtos).

```python
soma_total = 0.0  # Acumulador de soma

for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}: "))
    soma_total += nota  # Soma valores variáveis (acumulador)

media = soma_total / 3
print(f"A média final do aluno é: {media:.2f}")
```

---

## 7. Critérios de Escolha: `for` vs. `while`

Saber decidir qual estrutura de repetição aplicar é uma habilidade fundamental para o desenvolvimento da lógica de programação. A tabela a seguir estabelece as diretrizes práticas de escolha:

| Critério de Avaliação | Estrutura Recomendada | Exemplo Prático |
| :--- | :--- | :--- |
| **Quantidade de repetições é conhecida previamente** | **`for`** | Ler 10 notas de uma turma de tamanho fixo. |
| **Iteração sobre uma lista ou sequência de dados** | **`for`** | Exibir todos os nomes cadastrados em um banco de dados. |
| **Quantidade de repetições é desconhecida** | **`while`** | Ler números do usuário até que ele digite o valor `0`. |
| **Repetição depende de uma validação de entrada** | **`while`** | Solicitar a senha do usuário até que ele acerte. |

---

## 8. Laços Aninhados (*Nested Loops*)

O aninhamento de laços ocorre quando uma estrutura de repetição é posicionada **dentro** do bloco subordinado de outra estrutura de repetição.

Nessa configuração, para cada iteração do **laço externo**, o **laço interno** executará todo o seu ciclo do início ao fim. Laços aninhados são amplamente utilizados no processamento de matrizes (tabelas com linhas e colunas) ou na geração de combinações.

```python
# Gerando a tabuada completa de 1 a 3 usando laços aninhados
for tabuada in range(1, 4):
    print(f"--- Tabuada do {tabuada} ---")
    for multiplicador in range(1, 11):
        resultado = tabuada * multiplicador
        print(f"{tabuada} x {multiplicador} = {resultado}")
    print()  # Imprime uma linha em branco entre as tabuadas
```

---

## 9. Erros Comuns e Boas Práticas

Para garantir a qualidade e a funcionalidade de códigos com estruturas de repetição, atente-se aos seguintes pontos:

1. **Esquecer de inicializar variáveis:** Contadores e acumuladores devem ser criados e inicializados antes da linha do `while` ou do `for`. Tentar usá-los dentro do laço sem inicialização prévia causará um erro de variável não definida (`NameError`).
2. **Não atualizar a variável de controle no `while`:** Lembre-se de sempre modificar o valor da condição dentro do bloco para evitar a paralisia do sistema por *loop* infinito.
3. **Confusão com o limite final do `range()`:** Lembre-se de que `range(1, 5)` executa 4 vezes (`1, 2, 3, 4`). Caso precise rodar até o número 5, utilize `range(1, 6)`.
4. **Erros de indentação:** Lembre-se de que o Python utiliza o recuo para definir o que está **dentro** do laço e o que é executado **fora** (após o término do laço).
