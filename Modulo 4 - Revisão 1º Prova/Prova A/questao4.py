"""
4. Uma câmara frigorífica precisa manter materiais biológicos congelados.
A temperatura inicial é de -5°C. O sistema roda em um laço até 1000,
simulando o passar das horas.

Regras:

- A cada hora (iteração do laço), o sistema pergunta qual o estado da
  porta da câmara:
  
  A - Aberta
  F - Fechada
  S - Sistema de Resfriamento Rápido Ativado.

- Se a porta ficar Aberta, a temperatura sobe 4°C.

- Se a porta ficar Fechada, a temperatura desce 1°C.

- Se o Sistema de Resfriamento Rápido for ativado, a temperatura
  desce 6°C.

Lógica de Segurança:

- Se a temperatura subir e passar de 0°C, exibe:
  "ALERTA: Material correndo risco de degelo!".

- Se a temperatura atingir a meta crítica de -20°C ou menos, exibe:
  "Meta de congelamento ideal atingida!" e o programa encerra o laço.
"""