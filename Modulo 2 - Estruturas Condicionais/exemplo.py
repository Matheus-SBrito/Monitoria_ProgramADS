"""
### Exercício 2 — Módulo 2: Estruturas Condicionais

*   **Nível:** Médio
*   **Conceitos Utilizados:** Integração de EPS, 
    estruturas de decisão aninhadas ou consecutivas 
    (`if`, `elif`, `else`), operadores relacionais (`<=`, `>`, `==`) 
    e operadores lógicos (`and`, `or`).

#### 1. Contexto do Problema

O aeroporto internacional de uma grande cidade adota 
regras estritas de segurança para a pesagem de bagagens 
de mão levadas a bordo pelos passageiros. Para garantir a 
acomodação segura nos compartimentos superiores da aeronave, 
as malas sofrem diferentes triagens de acordo com a pesagem 
realizada na sala de embarque.

#### 2. Enunciado

Desenvolva um programa de triagem automatizada para o 
balcão de embarque. O sistema deve ler o **peso da mala de 
mão** do passageiro (em kg) e processar as 
seguintes condições regulamentares:

*   Mala com peso de **até 10.0 kg (inclusive)**: 
está isenta de taxas adicionais e é classificada como 
**"Bagagem Liberada: Embarque Autorizado"**.

*   Mala com peso **entre 10.1 kg e 12.0 kg (inclusive)**: 
o passageiro pode levá-la a bordo, mas mediante 
o pagamento de uma **taxa de conveniência de R\$ 60,00**. 
O status deve ser **"Embarque Autorizado mediante Taxa 
Adicional"**.

*   Mala com peso **acima de 12.0 kg**: excede o limite 
máximo físico de segurança interna do avião. O status 
deve ser **"Embarque Negado: Despacho Obrigatório no 
Porão"**.

"""