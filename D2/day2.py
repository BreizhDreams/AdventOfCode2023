def getInput():
    with open("D2\inputs\day_02.txt") as file:
        return file.readlines()

def clearData(): 
    data = getInput()
    clearData = []
    for number in data:
        if number != '\n':
            clearData.append(number.replace('\n',''))
        else:
            clearData.append('NEW')            
    return clearData


def getQuantityArray():
    totalQuantityArray = []
    total = 0
    data = clearData()
    for number in data:
        if number != 'NEW':
            total = total + int(number)
        else: 
            totalQuantityArray.append(total)
            total=0
    return totalQuantityArray

 
def getSortedQuantityByElves(): 
    data = getQuantityArray()
    quantityByElves = []
    for amount in data:
            quantityByElves.append(amount)
    return sorted(quantityByElves)

def getPodiumQuantity():
    data = getSortedQuantityByElves()
    data.reverse()
    total = data[0] + data[1] + data[2]
    return total
        
print(getPodiumQuantity())
# print(f" Total des trois meilleurs elfes : {getTotalPodium()}")
            
            
    
    

            
    
    

