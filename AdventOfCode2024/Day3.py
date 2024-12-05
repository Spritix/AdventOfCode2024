import re
from os.path import split

f = open("input_day3.txt","r")

input = f.read()
res = 0

values = (re.findall("mul[(]([0-9]{1,3},[0-9]{1,3})[)]", input))

for value in values:
    L,R = value.split(",")
    print(L,R)
    res += int(L) * int(R)

print(res)
