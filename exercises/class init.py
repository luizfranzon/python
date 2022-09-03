class Pessoa:
    nome = None
    idade = None

    def __init__(self,n,i):
        self.nome = n
        self.idade = i

    def colocarNome(self, nome):
        self.nome = nome
    
    def imprimirNome(self):
        print(self.idade)

    def colocarIdade(self, num):
        self.idade = num
    
    def imprimirIdade(self):
        print(self.idade)

lucas = Pessoa("Lucas Wallace Ribeiro Cavalcante", 19)

print(lucas.nome)                                                                                                                                                                                                                                        