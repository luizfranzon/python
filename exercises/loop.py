movies = ["Filme 1", "Filme 2", "Filme 3", "Filme 4"]

for movie in movies: #Pega cada item da lista movies e mostra no console.
    print(movie)

print(" ")

for i in range (len(movies)): #Faz a mesma coisa, porém é criado a variável "i" para usar como index na lista
    print(movies[i])

print(" ")

cont = 0
while cont < len(movies): #Executa o bloco de código enquanto a condição for true.
    print(movies[cont])
    cont += 1


