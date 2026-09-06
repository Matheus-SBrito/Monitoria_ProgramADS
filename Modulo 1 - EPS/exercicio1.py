

"""### Exercício 1 — O Faturamento da Conta de Água (Gestão de Serviços)

**Nível:** Médio

**Problema:**

A concessionária de abastecimento de água local cobra uma taxa tarifária 
de **R\$ 5,50 por metro cúbico (\\(m^3\\))** de água consumida em uma residência. 
Além disso, a legislação municipal estabelece que o usuário deve pagar uma 
**taxa de esgoto correspondente a 80% do valor do consumo de água**, e uma 
**taxa de iluminação pública de valor fixo (R\$ 12,50)**. 

A concessionária realiza a leitura do hidrômetro mensalmente, 
mas não fornece o consumo direto ao sistema de faturamento; 
ela apenas registra os valores medidos. Você foi designado 
para programar a etapa inicial desse faturamento rápido.

**O que o programa deve fazer:**

O sistema deve solicitar que o usuário digite a 
**leitura anterior do hidrômetro** (em \\(m^3\\)) 
e a **leitura atual do hidrômetro** (em \\(m^3\\)). 
O programa deve calcular e exibir na tela:

1. O consumo total de água no período (em \\(m^3\\)).
2. O valor financeiro bruto cobrado apenas pelo consumo de água (R\$).
3. O valor referente à taxa de esgoto (R\$).
4. O valor final total da fatura que o consumidor deverá pagar (R\$), 
somando o consumo, o esgoto ea  taxa fixa de iluminação pública.

#### Planejamento Requerido (EPS)
Antes de escrever o código, o aluno deve identificar e 
preencher em seu caderno a seguinte estrutura:

*   **E — Entrada:** Quais dados o programa deve solicitar do usuário 
e quais seus respectivos tipos de dados?

*   **P — Processamento:** Quais equações matemáticas e 
lógicas devem ser aplicadas passo a passo?

*   **S — Saída:** Quais dados e mensagens formatadas 
o programa deve exibir no console?

**Tarefa:**
Desenvolva a análise **EPS** conceitual do problema e, em seguida, 
escreva a solução correspondente em **Python**.
"""

# Contexto: Tarifa, 5 * numero_qualquer(metro cubico)
# tarifa * 0.80
# total + 12

# EPS

# Entradas: leitura_anterior, leitura_atual (float)
# Processamento: 
        # consumo
            #leitura anterior
            #Leitura atual

        # tarifa_agua = consumo * 5.50
        # taxa_esgoto = tarifa_agua * 0.80
        # taxa_iluminacao = 12.50
        # total = tarifa_agua + taxa_esgoto + taxa_iluminacao
# saida: consumo, tarifa_agua, taxa_esgoto, total


anterior = float (input ("Informe o valor da leitura anterior: "))
atual = float (input ("Informe o valor da leitura atual: "))

consumo = anterior - atual # Consumo de agua
TAXA_ILUMINACAO = 12.50

tarifa_agua = consumo * 5.50 # Quantidade a pagar pelo consumo
tarifa_esgoto = tarifa_agua * 0.80 # Tarifa esgoto, oq é pago

total = tarifa_agua + tarifa_esgoto + TAXA_ILUMINACAO

print("Consumo de agua: ", consumo)
print("Tarifa de agua: ", tarifa_agua)
print("Tarifa esgoto: ", tarifa_esgoto)
print("Total pago: ", total)