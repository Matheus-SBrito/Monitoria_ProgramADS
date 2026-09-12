"""
4. Um investidor quer acumular uma meta financeira usando juros compostos
simulados manualmente passo a passo.

Regras:

- O usuário define uma Meta Financeira (ex.: R$ 10.000) e um Aporte Mensal
  fixo (ex.: R$ 500).

- O laço roda simulando o passar dos meses. A cada mês, o saldo atual
  recebe o Aporte Mensal.

- Além do aporte, aplica-se o rendimento baseado no saldo acumulado:
    - Se o saldo for menor que R$ 2.000: rende 1% naquele mês.
    - Se o saldo for de R$ 2.000 até R$ 5.000: rende 2% naquele mês.
    - Se o saldo for maior que R$ 5.000: rende 3% naquele mês.

- Os juros devem ser aplicados antes da soma do aporte mensal.

- O laço deve parar assim que o saldo atingir ou ultrapassar a Meta
  Financeira.

- No final, exiba quantos meses foram necessários.
"""