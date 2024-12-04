import Parsing_File

list_sorted=[]
list_result=[]
somme = 0

list_sorted = Parsing_File.parse_file("input.txt")

for value in list_sorted:
    if int(value[1]) > int(value[0]):
        list_result.append(int(value[1])-int(value[0]))
    else:
        list_result.append(int(value[0])-int(value[1]))

print(list_result)

for value in list_result:
    somme += value

print(somme)