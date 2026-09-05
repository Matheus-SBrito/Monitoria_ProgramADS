"""
### Exercício 1 — O Classificador de Cargas Seguras (Eixo: Logística e Segurança)

**Contexto:**
Uma transportadora de produtos químicos adota regras 
rígidas de segurança para evitar acidentes nas estradas. 
O transporte de qualquer carga depende do **peso total** 
(em toneladas) e do **tipo de substância** transportada. 
As normas internas da empresa estabelecem os seguintes 
critérios de liberação:

*   **Substâncias Inflamáveis (tipo "I"):** Só podem ser transportadas 
se o peso total da carga for de **até 10 toneladas**.

*   **Substâncias Corrosivas (tipo "C"):** Só podem ser transportadas 
se o peso total for de **até 5 toneladas**.

*   **Substâncias Tóxicas (tipo "T"):** Não possuem restrição de 
peso máximo para transporte. Contudo, se a carga pesar 
**mais de 8 toneladas**, é cobrada uma **taxa de segurança 
obrigatória de R\$ 600,00** sobre o frete final.

**O que o programa deve fazer:**

O programa deve ler o **peso da carga** (em toneladas, valor real) 
e o **tipo de substância** (uma única letra: `"I"` para Inflamável, 
`"C"` para Corrosiva ou `"T"` para Tóxica). Em seguida, deve analisar 
as regras condicionais e exibir:

1. O status do transporte: **"AUTORIZADO"** ou **"REPROVADO POR MOTIVOS DE SEGURANÇA"**.
2. Caso o transporte seja **autorizado**, calcular e exibir o **valor final do frete**:

    *   O custo básico do frete é de **R\$ 250,00 por tonelada**.
    *   Lembre-se de somar a taxa adicional de segurança de R\$ 600,00 
    se a substância for do tipo tóxica e o peso for superior a 8 toneladas.

#### Roteiro de Resolução Obrigatório

Antes de escrever o código em Python, faça o planejamento respondendo em seu caderno:

*   **E — Entrada:** Quais dados o programa precisa receber do 
usuário e quais são seus respectivos tipos de dados?

*   **P — Processamento:** 
    *   Quais são as condições lógicas para que o transporte seja **reprovado**? 
    (Identifique os limites de peso para cada tipo).

    *   Como calcular o frete bruto e a taxa adicional para cargas autorizadas?

*   **S — Saída:** O que o programa deve exibir em caso de reprovação? 
E em caso de autorização?

*   **Estrutura de Decisão:** Qual estrutura condicional em 
Python é mais recomendada para testar estas condições consecutivas e por quê?

**Tarefa:**
Faça a análise conceitual acima e, em seguida, **implemente o programa em Python**.
"""
