def getInput():
    with open("D3\inputs\day_03.txt") as file:
        return file.readlines()

def clearData(): 
    data = getInput()
    clearData = []
    for number in data:
        if number != '\n':
            clearData.append(number.replace('\n',''))        
    return clearData

data = clearData()

# Récupération de chaque ligne

# Séparation des lignes en deux

# Déterminer le caractère commun entre les deux lignes

# Déterminer la valeur du caractère commun

test = "SALUTE"

for char in test:
    print(char)