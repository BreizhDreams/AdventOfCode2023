def get_input():
    with open("D1\inputs\day_01.txt") as file:
        return file.readlines()

def clearData(): 
    data = get_input()
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

def getBiggestQuantity(): 
    data = getQuantityArray()
    highestQuantity = 0
    for amount in data:
        if amount >= highestQuantity:
            highestQuantity = amount
    return highestQuantity

print(f"Biggest quantity is : {getBiggestQuantity()}")
            
    
    

