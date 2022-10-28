peoples = []
older = {"idade": 0}
newest = {"idade": 10000}

while True:
  name = input("\nInsira o nome (ou \"sair\"): ")
  
  if name != "sair":
    age = int(input("Insira a idade: "))
    newPeople = {
      "nome": name,
      "idade": age,
    }
    peoples.append(newPeople)
    print("\n{} adicionado!".format(name))
  else:
    break
  
print("\n-------=Ordenada por idade=-------")

def sortByAge(e):
  return e["idade"]

peoples.sort(key=sortByAge)

for people in peoples:
  print("{nome} | {idade} anos".format(nome = people["nome"], idade = people["idade"]))
  if people["idade"] > older["idade"]:
    older = people
  
  if people["idade"] < newest["idade"]:
    newest = people
    
print("-----------------------------------")
print("* mais novo: {nome} com {idade} anos".format(nome = newest["nome"], idade = newest["idade"]))
print("* mais velho: {nome} com {idade} anos".format(nome = older["nome"], idade = older["idade"]))
print("* Quantidade de pessoas adicionadas: {qnt}".format(qnt = len(peoples)))
print("-----------------------------------")