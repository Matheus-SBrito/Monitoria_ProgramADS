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

# Entrada: meta_financeira e aporte_mensal (salario mensal)
# Processamento:
  # - Acrescimos de juros ao saldo
    # . Se saldo < 2000 : Saldo recebe 1% do que já se tem guardado.
    # . Se saldo >= 2000 e saldo <= 5000 : Saldo recebe 1% do que já se tem guardado.
    # . Se saldo > 5000 : Saldo recebe 3% do que já se tem guardado.

  # - Acrescimo do salario mensal / aporte mensal
  # - A cada repetição temos um acrescimo no contador, o contador representa a passagem do mês
  # - Caso a meta seja alcançado encerramos o loop

# Saída: Exibição do nosso contador que represntava os meses

meta_financeira = float (input("Digite sua meta financeira: "))
aporte_mensal = float (input("Digite o quanto você recebe mensalmente: "))


meses_passados = 0
saldo_atual = 0
acresmo_juros = 0
while (saldo_atual < meta_financeira):

  meses_passados += 1
  saldo_atual += aporte_mensal


  if (saldo_atual < 2000):
    acresmo_juros = saldo_atual * (1/100)

  elif (saldo_atual >= 2000 and saldo_atual <= 5000):
    acresmo_juros = saldo_atual * (2/100)

  else:
    acresmo_juros = saldo_atual * (3/100)

  saldo_atual += acresmo_juros



  print("Acrescimo pela renda mensal dos juros sobre o saldo:", acresmo_juros)
  print("Aporte mensal:", aporte_mensal)
  print("Saldo atual:", saldo_atual)

  print(f"{meses_passados}° Mês da simulação.")
  print("______________________________\n")
