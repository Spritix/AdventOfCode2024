f = open("input_day2.txt", "r")
line_safe=0
line_unsafe=0
sorted_values=[]
reversed_values=[]

lines = f.read().splitlines()

def checkIfUnsafe(list_values):
    unsafe=False
    reversed_values = list_values.copy()
    sorted_values = list_values.copy()
    sorted_values.sort(key=float)
    reversed_values.sort(reverse=True, key=float)
    last_value=0
    if list_values != reversed_values and list_values != sorted_values:
        unsafe = True
    else:
        for value in list_values:
            if (3 < abs(last_value - int(value)) or abs(last_value - int(value)) < 1) and last_value != 0:
                unsafe = True
            last_value = int(value)
    return unsafe

for line in lines:
    file_values = line.split(' ')
    if not checkIfUnsafe(file_values):
        line_safe+=1
    else:
        for i in range (len(file_values)):
            copy_values = file_values.copy()
            copy_values.pop(i)
            if not checkIfUnsafe(copy_values):
                line_safe+=1
                break

print(line_safe)