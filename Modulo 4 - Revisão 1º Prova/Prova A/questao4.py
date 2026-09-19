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

# Entrada: estado_da_porta
# Processamento: condicionais inflenciadoras da temperatura.
  # Loop de repetição, pergunta estado_da_porta 1000 vezes
    # Se porta aberta -> aumento de temperatura em 4°C
    # Se porta fechada -> diminuição de temperatura em 1°C
    # Se sistema resfreamento = ligado -> diminuição da temperatura em 6°C

# Saída: Alertas de segurança:
  # Temperatura > 0 => "ALERTA: Material correndo risco de degelo!".
  # Temperatura < -20 => "Meta de congelamento ideal atingida!" 
    # e o programa encerra o laço.


TEMPERATURA_INICIAL = -5

temperatura = TEMPERATURA_INICIAL
for repeticao in range (1000):
    
    estado_da_porta = input(
    """Digite uma das seguintes opções, sobre o estado da porta:

    A - Aberta
    F - Fechada
    S - Sistema de Resfriamento Rápido Ativado.
    \n""" +
    "Qual Estado se encontra a porta:"
    )

    if (estado_da_porta.upper() == "A"):
        temperatura += 4

    elif (estado_da_porta.upper() == "F"):
        temperatura -= 1

    elif (estado_da_porta.upper() == "S"):
        temperatura -= 6

    else: print("\nEscolha somente uma das opções exibidas.\n")


    if (temperatura > 0):
        print("ALERTA: Material correndo risco de degelo!")

    elif (temperatura <= -20):
        print("Meta de congelamento ideal atingida!" )
        break

    print(f"Temperatura atual: {temperatura}")
