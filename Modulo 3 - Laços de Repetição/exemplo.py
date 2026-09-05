"""
### Exercício 3 — Módulo 3: Estruturas de Repetição

*   **Nível:** Médio
*   **Conceitos Utilizados:**
    Inicialização de variáveis de controle antes do laço, 
    decisão dentro do laço de repetição, contadores, 
    acumuladores, cálculo de média aritmética e escolha 
    metodológica do laço (`while` controlado por sentinela).

#### 1. Contexto do Problema

O controle de climatização de um berçário de plantas raras monitora 
as temperaturas internas para otimizar o crescimento das mudas. 
O biólogo responsável insere leituras feitas manualmente ao longo 
do dia para obter um diagnóstico geral. Como o número de monitoramentos 
diários varia, o sistema não sabe de antemão quantas leituras 
serão inseridas no programa.

#### 2. Enunciado

Construa um programa que leia uma **quantidade indeterminada de temperaturas** 
(em graus Celsius). Para encerrar a entrada de dados, o operador deve digitar 
o valor sentinela **`-999`**. Quando a leitura for interrompida pelo valor 
sentinela, o programa deve ignorar este valor de parada e calcular:

1.  A **quantidade total de leituras válidas** registradas no dia.

2.  A **quantidade de leituras que indicaram "Temperatura de Alerta"** 
(considerando como alerta qualquer medição abaixo de 15°C ou acima de 28°C).

3.  A **média aritmética de todas as temperaturas válidas** registradas no período.
"""