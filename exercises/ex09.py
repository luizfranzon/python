numeroMaximo = int(input("Insira um número inteiro: "))
listaDeNumeros = []

n = 1

while n <= numeroMaximo:
    if n % 2 == 0:
        listaDeNumeros.append(n)
    n += 1

numeroProcurar = int(input("Qual número quer encontrar? "))

try:
    listaDeNumeros.index(numeroProcurar)
    print("Número encontrado")
except:
    print("Número não encontrado")
