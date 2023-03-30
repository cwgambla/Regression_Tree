import math

def powerSet(set, setSize):

    pow_set_size = (int)(math.pow(2,setSize))
    counter = 0
    j = 0
    powerSet = []
    for counter in range(0, pow_set_size):
        array = []
        for j in range(0,setSize):
            if((counter & (1 << j))>0):
                array.append(set[j])
        powerSet.append(array)
        
    return powerSet

def powerSetNoEmpty(set, setSize):

    pow_set_size = (int)(math.pow(2,setSize))
    counter = 0
    j = 0
    powerSet = []
    for counter in range(0, pow_set_size):
        array = []
        for j in range(0,setSize):
            if((counter & (1 << j))>0):
                array.append(set[j])
        powerSet.append(array)
        

    del powerSet[0]
    return powerSet

arr = powerSetNoEmpty([10,2,3], 3)



