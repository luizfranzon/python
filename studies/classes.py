class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
    
    def mudarCor(self, cor):
        self.cor = cor

    def getCarInfo(self):
        print("\n\nModelo: {modelo} | Cor: {cor}".format(modelo = self.modelo, cor = self.cor))

meuCarro = Carro("Onix", "Azul Escuro")

meuCarro.mudarCor("Vermelho")
meuCarro.getCarInfo()





