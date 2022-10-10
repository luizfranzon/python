numbersData = input("Digite três números: ")
numbersArray = [0] * 3

numbersDataSplited = numbersData.split(" ")
numbersDataSplited = numbersDataSplited[0:3]

for i in range(3):
    numbersArray[i] = int(numbersDataSplited[i])

print("A={numA} | B={numB} | C={numC}".format(
    numA=numbersArray[0],
    numB=numbersArray[1],
    numC=numbersArray[2])
)