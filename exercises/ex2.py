print("Inicio do programa")
print("")

Fixo = 500
Vendas = float(input("Digite o valor de vendas: "))
Comissao = 6/100
Fat = Fixo + Vendas * Comissao

print("Faturamento do mês: = {0:.2f}".format(Fat))
print("Fim do programa")