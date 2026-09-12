"""
2. Crie um programa que analise se um ano é bissexto. A regra matemática
exata utiliza uma combinação lógica de divisibilidade:

- Divisibilidade por 4: se o ano é divisível por 4, ele pode ser bissexto,
  com exceção dos séculos.
- Séculos: se o ano termina em "00" (como 1900 ou 2000), ele só será
  bissexto se for divisível por 400.

Exemplos práticos:
- 2024 → divisível por 4 e não é século → bissexto.
- 1900 → é século, mas não é divisível por 400 → não é bissexto.
- 2000 → é século e é divisível por 400 → bissexto.

Em resumo: um ano é bissexto se for divisível por 4, exceto os séculos,
que só são bissextos se forem divisíveis por 400.
"""