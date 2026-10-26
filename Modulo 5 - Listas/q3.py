"""
Em um sistema de e-commerce, não sabemos quantos itens o usuário vai
comprar. A lista é a estrutura ideal para o "Carrinho". Crie um programa que: 1 –
adicione elementos no carrinho, 2- tire elementos do carrinho, 3 – imprima
elementos do carrinho e saia do programa. (Veja como se usa o match, case)
"""

# Entrada
    # Elementos
# Processamento
    # Tirar elementos
# Saída
    # Elementos


carrinho = []

while True:
    
    opcao = input("""
Menu:

1 - Adicione um elemento no carrinho
2 - Tirar elemento do carrinho
3 - Imprimir o carrinho e finalizar o programa

Opção:
""")

    match(opcao):

        case "1":
            elemento = input("Digite o que vai entrar no carrinho: ")
            carrinho.append(elemento)
            continue

        case "2":
            if (len(carrinho) != 0):
                carrinho.pop()
            continue

        case "3":
            break


print(carrinho)       