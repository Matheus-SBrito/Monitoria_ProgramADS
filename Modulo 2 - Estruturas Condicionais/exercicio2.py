"""
### Exercício 2 — O Tarifador de Energia Elétrica Inteligente (Eixo: Utilidade Pública)

**Contexto:**

Uma cooperativa de energia elétrica implementou um 
sistema de cobrança inteligente para incentivar o 
uso racional da eletricidade. O valor básico cobrado 
por energia consumida é de **R\$ 0,60 por kWh**. 
Entretanto, a fatura final sofre acréscimos ou descontos 
de acordo com a **faixa de consumo mensal** e o **horário 
de utilização predominante** informado pelo cliente.

As regras de faturamento são aplicadas da seguinte forma:

*   **Faixa 1 — Consumo abaixo de 100 kWh:** 
O cliente é classificado como *"Consumidor Econômico"*. 
Se o horário de consumo predominante for **fora de pico** 
(tipo `"F"`), ele ganha **15% de desconto** sobre o 
valor bruto do consumo. Se for em horário de **pico** (tipo `"P"`), 
não recebe desconto (paga a tarifa básica).

*   **Faixa 2 — Consumo de 100 até 300 kWh:** 
O cliente é classificado como *"Consumidor Padrão"*. 
O valor cobrado é exatamente a tarifa básica de 
R\$ 0,60 por kWh, independente do horário de consumo.

*   **Faixa 3 — Consumo acima de 300 kWh:** O cliente é 
classificado como *"Alto Consumo"*. Por sobrecarregar a 
rede elétrica, se o horário predominante de consumo for 
em horário de **pico** (tipo `"P"`), há um **acréscimo 
de 20%** sobre o valor de consumo bruto. Se for **fora 
de pico** (tipo `"F"`), o acréscimo é de **apenas 5%**.


**O que o programa deve fazer:**
O programa deve ler o **consumo mensal** (em kWh, valor real) e 
o **horário predominante de consumo** (uma letra: `"P"` 
para pico ou `"F"` para fora de pico). O programa deve 
avaliar as faixas de consumo e o horário para calcular e 
exibir:

1. O valor bruto do consumo (consumo multiplicado pelo valor básico de R\$ 0,60).
2. A classificação de consumo do cliente (*"Econômico"*, *"Padrão"* ou *"Alto Consumo"*).
3. O valor final faturado (após a aplicação dos descontos ou acréscimos correspondentes).


#### Roteiro de Resolução Obrigatório

Antes de escrever o código em Python, faça o planejamento respondendo em seu caderno:
*   **E — Entrada:** Quais dados devem ser solicitados e de quais tipos eles devem ser?
*   **P — Processamento:**
    *   Como mapear as três faixas de consumo usando operadores lógicos e relacionais?
    *   De que forma as decisões aninhadas (*estrutura if dentro de outro if*) ou consecutivas ajudam a testar o horário após a validação da faixa de consumo?
*   **S — Saída:** Quais informações detalhadas devem ser exibidas ao consumidor na tela?

**Tarefa:**
Faça a análise conceitual acima e, em seguida, **implemente o programa em Python**.
"""