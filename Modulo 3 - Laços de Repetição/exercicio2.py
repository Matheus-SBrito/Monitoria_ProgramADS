"""
### Exercício 2 — O Monitor de Eficiência de Frotas (Eixo: Logística e Transportes)
**Contexto:**
Uma transportadora de encomendas monitora diariamente a eficiência de combustível de sua frota de entregas urbanas durante uma **semana de trabalho padrão de 5 dias** (de segunda a sexta-feira). 

Diariamente, o motorista relata dois dados para o sistema: 

a **distância percorrida** (em km) e a **quantidade de combustível consumida** 
(em litros) naquele dia. A eficiência diária é medida pela razão:

Eficiência = (Distância Percorrida/ Combustível Consumido) *(km/L)

A empresa estabeleceu uma meta de consumo: o veículo deve fazer **pelo menos 12.0 km/L** de média diária.

**O que o programa deve fazer:**
Sabendo que o ciclo de análise cobre exatamente **5 dias**, o programa deve ler 
a quilometragem e o combustível de cada um dos dias e, ao final, calcular e exibir:

1.  O **consumo médio total de combustível** do caminhão ao longo 
de toda a semana (soma de todos os litros consumidos dividida por 5).

2.  A **quantidade de dias** em que o veículo **não atingiu** a meta 
mínima de 12.0 km/L (para fins de auditoria de manutenção).

3.  A **melhor eficiência diária (km/L)** obtida pelo 
veículo durante a semana. *(Nota: identifique o maior 
valor computado ao longo dos dias sem usar funções prontas 
como `max()`).*

#### Etapas de Planejamento Requeridas (Folha de Ataque ao Problema)
Antes de codificar, estruture a solução respondendo em seu caderno:
*   **E — Entrada:** Quais dados devem ser coletados a cada dia e 
quantas vezes essa etapa será executada?

*   **P — Processamento:**
    *   Como calcular a eficiência do dia e verificar se ela bate a meta corporativa?
    *   Como rastrear a "melhor eficiência" linha a linha de forma comparativa dentro do laço?
    *   Qual estrutura de controle de repetição é a mais adequada neste cenário e 
    por quê (`for` ou `while`)?

*   **S — Saída:** Quais informações consolidadas de desempenho logístico 
devem ser apresentadas para a diretoria?

*   **Decisões:** Quais condições determinam a contagem de dias ruins e a 
atualização do recorde de melhor eficiência?

*   **Repetições:** O que se repete e qual o intervalo numérico de controle do laço?

**Tarefa:**
Desenvolva a análise de planejamento acima e **implemente a solução em Python**.
"""

