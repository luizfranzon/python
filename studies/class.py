class Computador:
    def __init__(self, processador, placaDeVideo, RAM):
        self.processador = processador
        self.placaDeVideo = placaDeVideo
        self.ram = RAM
        
    def getComputerInfo(self):
        print("Informações: {processador}, {placaDeVideo}, {memRAM}".format(processador = self.processador, placaDeVideo = self.placaDeVideo, memRAM = self.ram))  
        
    def quebrarComputador(self):
        self.funcionando = "Não"
        self.processador = "Quebrado"
        self.placaDeVideo = "Quebrado"
        self.ram = "Quebrado"

meu = Computador("I9", "RTX 3090Ti", "32gb")

meu.getComputerInfo()
meu.quebrarComputador()
meu.getComputerInfo()
print(meu.placaDeVideo)


