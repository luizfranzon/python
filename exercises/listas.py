movies = ["Filme 1", "Filme 2", "Filme 3", "Filme 4"]

movies.append("Filme 5") #Adiciona um item no final do lista
# ["Filme 1", "Filme 2", "Filme 3", "Filme 4", Filme 5]

movies.pop() #Remove o ultimo item do final da lista
# ["Filme 1", "Filme 2", "Filme 3", "Filme 4"]

movies.extend(["Filme 6", "Filme 7"])
# ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 6", "Filme 7"]

print(movies)

movies.remove("Filme 2") #Remove um item especifico 
# ["Filme 1", "Filme 3", "Filme 4", "Filme 6", "Filme 7"]

movies.insert(1, "Filme 2") #Adiciona um item em um index especifico
# ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 6", "Filme 7"]

print(movies)

