try:
  inputData = input("Digite um número: ")
  inputData = int(inputData)
  print("Você digitou o número: {num}".format(num=inputData))
except:
  print("Erro ao ler o número, digite novamente.")