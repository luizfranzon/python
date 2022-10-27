lista = ["Luiz", "Fernando", "Eduardo"]
print("Antes do append: {}".format(lista))

lista.append(["Dale", "Carlos"]) #Adiciona um item ao final da lista
print("Depois do append: {}".format(lista))

lista.pop() # Remove um item ao final da lista
print("Depois do pop: {}".format(lista))

lista.extend(["Armando", "Arthur"]) # Adiciona uma coleção de dados ao final da lista (Precisa ser um item iteravel)
print("Depois do extend: {}".format(lista))

lista.remove("Luiz") # Remove o item especificado
print("Depois do remove: {}".format(lista))

lista.insert(3, "Carlos2") # Adiciona um item ao index especificado
print("Depois do insert: {}".format(lista))