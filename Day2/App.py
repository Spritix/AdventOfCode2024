f = open("input.txt", "r")
line_safe=0
line_unsafe=0
sorted_values=[]
reversed_values=[]

lines = f.read().splitlines()

for line in lines:
    file_values = line.split(' ')
    unsafe=False
    last_value=0
    sorted_values = file_values.copy()
    reversed_values = file_values.copy()
    sorted_values.sort()
    reversed_values.sort(reverse=True)
    if file_values != reversed_values and file_values != sorted_values:
        unsafe = True
    else:
        for value in file_values:
            if (3 < abs(last_value - int(value)) or abs(last_value - int(value)) < 1) and last_value != 0:
                unsafe = True
            last_value = int(value)
    if unsafe is False:
        line_safe+=1
    else:
        line_unsafe+=1

print(line_safe)