"""
### Exercício 1 — O Inspetor Automatizado de Fundição (Eixo: Controle de Qualidade Industrial)

**Contexto:**
Em uma metalúrgica, uma esteira transportadora leva esferas de 
aço recém-fundidas para um sensor eletrônico de pesagem. 
Para serem comercializadas na categoria premium, as esferas 
devem ter um peso **entre 100g e 150g (inclusive)**.

*   Esferas com peso **abaixo de 100g** são descartadas 
permanentemente por estarem abaixo do limite de tolerância 
técnica.

*   Esferas com peso **acima de 150g** são desviadas para um 
cadinho de refusão para serem derretidas e moldadas novamente.


Como o processo de fundição opera de forma contínua, o operador não 
sabe previamente quantas peças passarão pela esteira em um turno. 
O sistema encerra as medições do dia somente quando o sensor 
registrar o valor sentinela de **peso igual a `0`**, que indica 
o fim do expediente.


**O que o programa deve fazer:**

O programa deve ler consecutivamente o peso (em gramas, valor real) 
de cada peça. Ao ler o peso `0`, a leitura deve parar imediatamente 
e o programa deve exibir:

1.  A **quantidade de peças aprovadas** (premium).
2.  A **quantidade de peças descartadas** (< 100g).
3.  A **quantidade de peças enviadas para refusão** (> 150g).
4.  O **peso médio** apenas das peças que foram **aprovadas** (premium). 
*(Atenção: evite divisões por zero se nenhuma peça premium for inserida).*


#### Etapas de Planejamento Requeridas (Folha de Ataque ao Problema)

Antes de codificar, estruture a solução respondendo em seu caderno:

*   **E — Entrada:** Quais dados serão informados repetidamente e 
qual o valor que interrompe essa coleta?

*   **P — Processamento:**
    *   Como acumular pesos e contar peças individualmente de acordo com as faixas de peso?
    *   Qual laço de repetição é o ideal para essa situação e por quê (`for` ou `while`)?
    *   Como tratar o cálculo da média final se o usuário digitar `0` logo na primeira leitura?
    
*   **S — Saída:** Quais estatísticas estruturadas serão apresentadas ao inspetor da fábrica?
*   **Decisões:** Quais são as condições lógicas que definem o destino de cada peça?
*   **Repetições:** O que se repete e qual é o gatilho de parada?

**Tarefa:**
Desenvolva a análise de planejamento acima e **implemente a solução em Python**.
"""
