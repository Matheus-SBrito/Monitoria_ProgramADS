

"""
Monitorando a rede elétrica do rack de servidores, o sistema registrou
flutuações de tensão ao longo de 10 minutos. Dada uma lista de tensões, por
exemplo: [218, 220, 224, 230, 221, 190, 220, 235].

    a. Identifique e exiba a maior e a menor tensão registrada.

    b. Crie uma nova lista chamada anomalias que contenha apenas as
    tensões que estejam fora da faixa ideal (entre 210V e 230V).

    c. Se a lista de anomalias não estiver vazia, exiba um alerta de
    "Manutenção Necessária".

"""

# Entrada - Não tem
# Processamento
# Saída

tensoes = [218, 220, 224, 230, 221, 190, 220, 235]
anomalia = []

tensoes.sort() # Ordena do menor para o maior

maior = tensoes[-1]
menor = tensoes[0]

for tensao in tensoes:

    if (tensao < 210 or tensao > 230):
        anomalia.append(tensao)


if (len(anomalia) != 0):
    print("Manutenção necessária")

print(tensoes)
print(maior)
print(menor)