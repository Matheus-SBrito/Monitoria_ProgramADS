# Entendendo o problema

Contexto: Empresa logistica

- calcular o custo estimado de combustível de cada rota planejada
  - com base na quilometragem informada pelo despachante.

## EPS - Entrada, Processamento e Saída

- Entrada:
  - Distancia total
  - Litros combustivel
  - Preço do combustivel

- Processamento:
  - calculo -> (distancia/consumo) * preco

- Saída:
  - A quantidade total de litros de combustível que serão consumidos na viagem.
  - O custo financeiro total estimado para o abastecimento do veículo.

```mermaid
graph TD

    I([Inicio])
    I --> E1[/KML, Distancia_percorrida, preco_combustivel/]
    E1 --> P1[Calculo -> Distancia_percorrida/KML]
    P1 --> P2[Resultado -> Calculo x preco_combustivel]
    P2 --> S[\Resultado\]
    S --> F([Fim])
```