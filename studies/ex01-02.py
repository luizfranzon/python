MonthSalesValue = float(input("Digite o valor de vendas: "))
FixedSalary = 500
ComissionPercentValue = 0.06
ComissionValue = (MonthSalesValue - FixedSalary) * ComissionPercentValue

print("\nValor a ser recebido em comissão R${0:.2f}".format(ComissionValue))
