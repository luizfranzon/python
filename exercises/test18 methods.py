forevers = ["Classe", "Emerson", "Almeida", "Alessandro"]

#adiciona um item ao final da lista
forevers.append("Kyota")
print(forevers)

#remove um item do final da lista
forevers.pop()
print(forevers)

#adiciona varios itens ao final da lista.
forevers.extend(["Alex Almeida", "Felipe Valeta"])
print(forevers)

forevers.remove("Emerson")
print(forevers)

forevers.insert(0,"Emerson")
print(forevers)
