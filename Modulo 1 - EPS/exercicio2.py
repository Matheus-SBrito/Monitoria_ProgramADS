
"""
### Exercício 2 — O Otimizador de Envase de Sucos (Logística de Produção)

**Nível:** Médio

**Problema:**
Uma cooperativa de sucos artesanais produz suco de uva integral 
e precisa envasar sua produção diária em garrafas de **350 ml**. 
No final do expediente, o encarregado da produção mede o volume 
extraído em **litros (L)**, utilizando copos medidores industriais 
de alta precisão. 

Como o envase é feito por maquinário regulado, as garrafas só podem 
ser seladas se estiverem **completamente cheias** (com exatamente 350 ml). 
Qualquer sobra de suco que não consiga preencher uma garrafa inteira não 
pode ser vendida diretamente e é enviada de volta para um tanque de 
resíduos para processamento de geleias.

**O que o programa deve fazer:**

O programa deve ler a quantidade de **litros de suco de uva** 
produzidos (que pode ser um número real, como `120.5` litros). 
Em seguida, deve realizar as conversões de unidade necessárias e 
calcular:

1. O volume total de suco convertido para **mililitros (ml)** 
(lembrando que \\(1 \text{ litro} = 1000 \text{ mililitros}\\)).

2. A **quantidade máxima de garrafas** de 350 ml que poderão 
ser preenchidas completamente com o suco produzido.

3. A **quantidade de sobra de suco** (em ml) que não conseguiu 
encher uma garrafa e que será enviada para o tanque de resíduos.


*(Dica pedagógica: use as propriedades dos operadores de divisão inteira e resto da divisão estudados no módulo).*

#### Planejamento Requerido (EPS)

Antes de escrever o código, o aluno deve identificar e 
preencher em seu caderno a seguinte estrutura:

*   **E — Entrada:** Quais dados o programa deve 
solicitar do usuário e qual o tipo de dado ideal 
a ser lido para suportar frações de litros?

*   **P — Processamento:** Quais as operações necessárias 
para fazer a conversão de volume, a contagem de garrafas 
cheias e o cálculo do descarte?

*   **S — Saída:** Quais informações finais devem ser 
exibidas ao operador da fábrica?

**Tarefa:**
Desenvolva a análise **EPS** conceitual do problema e, 
em seguida, escreva a solução correspondente em **Python**.
"""