# Funções Nativas em Python: `input()` e `print()`

As **funções nativas** (também conhecidas como funções embutidas ou *built-in*) são instruções pré-programadas pertencentes à biblioteca padrão do Python. Elas ficam prontas para uso imediato em qualquer ponto do código, sem a necessidade de criar declarações personalizadas com `def` ou realizar a importação de módulos externos.

No ciclo de **Entrada, Processamento e Saída (EPS)**, duas funções nativas se destacam como a interface básica de comunicação entre o usuário e o computador: **`input()`** e **`print()`**.

---

## 1. Entrada de Dados: A Função `input()`

A função `input()` é o mecanismo padrão para capturar dados fornecidos pelo usuário através do teclado e armazená-los temporariamente na memória RAM.

### Como funciona o 'input'

Ao ser executada, a função `input()` pausa o programa e exibe uma mensagem opcional no console (chamada de *prompt*), aguardando que o usuário digite a informação e pressione a tecla `ENTER`.

```python
nome = input("Digite seu nome: ")
```

### A Regra de Ouro do `input()`

A função `input()` **sempre devolve o dado digitado sob o tipo de texto (`str`)**, independentemente de o usuário ter digitado letras ou números.

### Conversão de Tipos (*Casting*)

Se o dado recebido for utilizado em operações matemáticas ou processamentos numéricos, é obrigatório converter o resultado do `input()` para um tipo numérico apropriado:

* **`int()`**: converte o texto para número inteiro.
* **`float()`**: converte o texto para número real/decimal.

```python
# O texto digitado é imediatamente convertido para inteiro
idade = int(input("Digite sua idade: "))

# O texto digitado é convertido para número decimal
preco = float(input("Digite o preço do produto: R$ "))
```

Se essa conversão for esquecida, tentar somar dois valores lidos via `input()` resultará na concatenação (junção) dos textos em vez de uma adição matemática (por exemplo, `"2" + "4"` resulta em `"24"`).

---

## 2. Saída de Dados: A Função `print()`

A função `print()` é responsável por enviar dados do programa para a unidade de saída visual (o monitor), exibindo mensagens de orientação, resultados de cálculos e conteúdos de variáveis.

### Como funciona o 'print'

Você pode passar múltiplos argumentos para o `print()` separando-os por vírgula. O Python converte automaticamente variáveis e números para texto antes de exibi-los.

```python
idade = 20
print("O usuário tem", idade, "anos.")
```

### Parâmetros Especiais de Formatação

A função `print()` possui dois parâmetros opcionais muito importantes para controlar a exibição:

1. **`sep` (Separador):** Define o caractere colocado entre cada elemento da lista de exibição. Por padrão, o `sep` é um espaço em branco (`' '`).
2. **`end` (Finalizador):** Define o caractere impresso após exibir todos os elementos. Por padrão, o `end` é a quebra de linha (`'\n'`).

```python
# Alterando o separador para hífens e o final para não quebrar a linha
print("21", "03", "2026", sep="-", end=" -> ")
print("Data da aula")
# Saída exibida: 21-03-2026 -> Data da aula
```

### Formatação Moderna com f-strings

Uma das maneiras mais elegantes e legíveis de exibir dados formatados em Python é utilizando **f-strings** (interpolação de texto). Basta colocar a letra `f` antes das aspas da string e inserir as variáveis entre chaves `{}`:

```python
nome = "Maria"
nota = 9.5678

# Formatação simples e com limite de casas decimais (2 casas decimais: :.2f)
print(f"A aluna {nome} obteve a nota {nota:.2f}.")
# Saída exibida: A aluna Maria obteve a nota 9.57.
```

### Diferença Crucial: `print()` não é `return`

Um erro frequente de iniciantes é achar que o `print()` "retorna" um valor para o programa. O **`print()` apenas projeta uma mensagem visual no monitor** do usuário. Ele não envia dados de volta para serem armazenados em variáveis ou reutilizados em outras partes do código.

---

## 3. Resumo do Ciclo de Comunicação Básica (EPS)

O exemplo abaixo demonstra a integração perfeita entre entrada, processamento e saída utilizando `input()`, conversão de tipos e `print()` com f-string:

```python
# 1. ENTRADA (Lê o dado como texto e converte para número decimal)
raio = float(input("Informe o raio do círculo: "))

# 2. PROCESSAMENTO (Calcula a área)
area = 3.14159 * (raio ** 2)

# 3. SAÍDA (Exibe o resultado na tela formatado com 2 casas decimais)
print(f"A área calculada para o raio {raio} é {area:.2f}.")
```
