desconto = 10  # em %
taxa_juros = 0.05  # 5%

# Listas de parcelas
parcelas_sem_juros = [2, 3, 4, 5]
parcelas_com_juros = [6, 7, 8, 9, 10]

# Solicitando o valor da compra
valor_original = float(input("Digite o valor total da compra: R$ "))

# Calculando o valor com desconto (para pagamentos à vista)
valor_com_desconto = valor_original - (valor_original * desconto / 100)

# Solicitando a forma de pagamento
forma_de_pagamento = input("O pagamento será à vista ou parcelado? ")

if forma_de_pagamento == 'parcelado':
    # Solicitando a quantidade de parcelas
    quantidade_parcelas = int(input(
        "Digite a quantidade de parcelas (2X a 5X sem juros e de 6X a 10X com juros): "
    ))

    # Verificando se a quantidade de parcelas está nas listas predefinidas
    if quantidade_parcelas in parcelas_sem_juros:
        valor_parcela = valor_original / quantidade_parcelas
        print(f"Você escolheu parcelar em {quantidade_parcelas} vezes sem juros.")
        print(f"O valor de cada parcela é: R$ {valor_parcela:.2f}")
        print(f"O valor total da compra parcelada é: R$ {valor_original:.2f}")

    elif quantidade_parcelas in parcelas_com_juros:
        valor_com_juros = valor_original * (1 + taxa_juros)
        valor_parcela_com_juros = valor_com_juros / quantidade_parcelas
        print(f"Você escolheu parcelar em {quantidade_parcelas} vezes com juros.")
        print(f"A taxa de juros aplicada é: {taxa_juros * 100:.0f}%")
        print(f"O valor de cada parcela é: R$ {valor_parcela_com_juros:.2f}")
        print(f"O valor total da compra parcelada com juros é: R$ {valor_com_juros:.2f}")

    else:
        print("Quantidade de parcelas inválida. Digite um valor entre 2 e 10.")

elif forma_de_pagamento == 'à vista':
    print(f"O valor com desconto é: R$ {valor_com_desconto:.2f}")

else:
    print("Opção inválida. Digite À vista ou parcelado.")