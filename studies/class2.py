class Pessoa:
    
    def __init__(self, nome, sobrenome, idade):
        if type(idade) == int:
            self.nome = nome
            self.sobrenome = sobrenome
            self.idade = idade
            print("certinho rapaz")
        else:
            print("IDADE TEM QUE SER INT")
            
            
Luiz = Pessoa("Luiz", "Franzon", 10)
