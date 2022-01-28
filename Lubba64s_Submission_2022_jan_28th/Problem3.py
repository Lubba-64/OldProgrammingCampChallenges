def getRange(elements: list[int]):
    least = 10000000000
    greatest = 0
    for i in range(0,len(elements)):
        if (elements[i] < least):
            least = elements[i]
        if (elements[i] > greatest):
            greatest = elements[i]
    return greatest - least

def remove_items(list, item):
    res = [i for i in list if i != item]
    return res

def parseCollections(ranges: list[int]):
    collIter = ranges[0]
    dataSetIter = 0
    startPosition = 0
    
    while True:
        numbersToRange = []
        startPosition += 1
        if (ranges[startPosition - 1] == 0):
            return
        for i in range(startPosition, collIter + startPosition):
            numbersToRange.append(ranges[i])
        dataSetIter += 1
        collIter = ranges[startPosition - 1]
        startPosition += collIter
        print(f'Data Set {dataSetIter} has range:{getRange(numbersToRange)}')

_input = input("input the elements for the ranges you want to compute: ").split(' ')
_input = remove_items(_input,'')
for i in range(0,len(_input)):
    _input[i] = int(_input[i])
parseCollections(_input)