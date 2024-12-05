import re
from os.path import split

f = open("input_day3.txt","r")

file = f.read()
res = 0
unwanted = 0

dontList = re.findall("(?=don[']t[(][)]).*?(?=do[(][)])", file)

for dontString in dontList:
    print(dontString)
    dontValues = (re.findall("mul[(]([0-9]{1,3},[0-9]{1,3})[)]", dontString))
    print(dontValues)
    for value in dontValues:
        L,R = value.split(",")
        unwanted += int(L) * int(R)
    print(unwanted)

values = (re.findall("mul[(]([0-9]{1,3},[0-9]{1,3})[)]", file))
for value in values:
    L,R = value.split(",")
    res += int(L) * int(R)

print(res)
print(res-unwanted)
