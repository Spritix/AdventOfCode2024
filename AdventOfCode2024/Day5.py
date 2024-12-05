from multiprocessing.managers import ListProxy

f = open("input_day5.txt", "r")

lines = f.read().splitlines()
listRules = []
listUpdates = []
listWrongUpdates = []

for line in lines:
    if (line.find('|') != -1):
        listRules.append(line)
    elif (line.find(',') != -1):
        listUpdates.append(line)
print(listUpdates)

for rule in listRules:
    L,R = rule.split('|')
    for update in listUpdates:
        findRightValue = False
        values = update.split(',')
        for value in values:
            if value == R:
                findRightValue = True
            if value == L and findRightValue:
                listWrongUpdates.append(listUpdates.pop(listUpdates.index(update)))

print(listWrongUpdates)

ruleIndex = 0

while ruleIndex < len(listRules):
    L,R = listRules[ruleIndex].split('|')
    print(L,R)
    updateIndex = 0
    while updateIndex < len(listWrongUpdates):
        findLeftValue = False
        values = listWrongUpdates[updateIndex].split(',')
        valueIndex = len(values)-1
        while valueIndex >= 0:
            if values[valueIndex] == L:
                findLeftValue = True
                leftValueIndex = valueIndex
            if values[valueIndex] == R and findLeftValue:
                temp = values.pop(leftValueIndex)
                values.insert(valueIndex, temp)
                valueIndex = len(values)
                update = ','.join(values)
                listWrongUpdates[updateIndex] = update
                print(listWrongUpdates)
                findLeftValue = False
                updateIndex = -1
                ruleIndex = -1
            valueIndex -= 1
        updateIndex += 1
    ruleIndex += 1


res = 0

for update in listUpdates:
    if(len(update.split(',')) % 2 != 0):
        res += int(update.split(',')[len(update.split(',')) // 2])
print(res)

print(listWrongUpdates)

res = 0

for update in listWrongUpdates:
    if(len(update.split(',')) % 2 != 0):
        res += int(update.split(',')[len(update.split(',')) // 2])
        print(res)
