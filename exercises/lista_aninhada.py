movies = ["Exterminador do futuro", 1985, "Arnold Schwarzenegger", ["Rambo", 1982, "Sylvester Stallone", ["Star Wars", 1977, "Luke Skywalker", ["Tropa de Elite", 2007, "Wagner Mooura"]]]]

#movies = ["Exterminador do futuro", 1985, "Arnold Schwarzenegger"], ["Rambo", 1982, "Sylvester Stallone"], ["Star Wars", 1977, "Luke Skywalker"], ["Tropa de Elite", 2007, "Wagner Mooura"]

#for movie in movies:
#    print(movie)

for movie in movies:
    if isinstance(movie, list):
        for lista in movie:
            if isinstance(lista, list):
                for proximoItem in lista:
                    print(proximoItem)
            else:
                print()
    else:
        print(movie)