valor_original = (float(input("Digite o valor total da compra:R$ ")))
Desconto = 10 # em %
Parcelas_sem_juros = [2, 3, 4, 5]
Parcelas_com_juros = [6, 7, 8, 9, 10]
Valor_com_desconto = valor_original - (valor_original * Desconto / 100)
forma_de_pagamento = (input ("O pagamento será à vista ou parcelado? "))
if forma_de_pagamento == 'parcelado':
  quantidade_parcelas = int(input("Digite a quantidade de parcelas de 2X a 5X sem juros e de 6X à 10X: "))
elif forma_de_pagamento == 'à vista':
  print("O valor com desconto é: R$", Valor_com_desconto)
else:
  print("Opção inválida. Digite À vista ou parcelado.")
  if quantidade_parcelas in Parcelas_sem_juros:
    valor_parcela = valor_original / quantidade_parcelas
    print(f"Você escolheu parcelar em {quantidade_parcelas} vezes sem juros.")
    print(f"O valor de cada parcela é: R$ {valor_parcela:.2f}")
    print(f"O valor total da compra parcelada é: R$ {valor_original:.2f}")
elif quantidade_parcelas in Parcelas_com_juros:
    taxa_juros = 0.05
    valor_total_com_juros = valor_original * (1 + taxa_juros * (quantidade_parcelas - len(Parcelas_sem_juros)))
    valor_parcela_com_juros = valor_total_com_juros / quantidade_parcelas
    print(f"Você escolheu parcelar em {quantidade_parcelas} vezes com juros.")
    print(f"A taxa de juros aplicada é: {taxa_juros*100}%")
    print(f"O valor de cada parcela é: R$ {valor_parcela_com_juros:.2f}")
    print(f"O valor total da compra parcelada com juros é: R$ {valor_total_com_juros:.2f}")
else:
    print("Quantidade de parcelas inválida.")