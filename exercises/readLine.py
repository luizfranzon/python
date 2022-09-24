import os

print(os.getcwd()) #Mostra o diretorio atual
os.chdir("C:\\Users\\autologon\\Desktop\\python")
data = open("sketch.txt")

print (data.readline(), end='') #lê a primeira linha
print (data.readline(), end='') #lê a segunda linha

for cada_linha in data: #Vai em cada linha do arquivo
    print(cada_linha, end='')

data.close()