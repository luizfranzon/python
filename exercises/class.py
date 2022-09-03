class Pessoa:
    nome = None
    idade = 20

    def colocarNome(self, nome):
        self.nome = nome
    
    def imprimirNome(self):
        print(self.idade)

    def colocarIdade(self, num):
        self.idade = num
    
    def imprimirIdade(self):
        print(self.idade)

lucas = Pessoa()
lucas.colocarIdade(19)
lucas.colocarNome("Lucas Wallace Ribeiro Cavalcante")

print(lucas.nome)