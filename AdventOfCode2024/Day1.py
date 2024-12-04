from collections.abc import list_iterator

import Parsing_File

list_sorted=[]

list_gauche, list_droite = Parsing_File.parse_file("input_day1.txt")

def day1_part1():
    list_result=[]
    result=0
    while len(list_gauche)>0:
        list_sorted.append([list_gauche.pop(0),list_droite.pop(0)])
    for value in list_sorted:
        if int(value[1]) > int(value[0]):
            list_result.append(int(value[1])-int(value[0]))
        else:
            list_result.append(int(value[0])-int(value[1]))

    print(list_result)

    for value in list_result:
        result = result + value

    print(result)

def day1_part2():
    list_iterator=[]
    result=0
    for value_gauche in list_gauche:
        iterator = 0
        for value_droite in list_droite:
            if value_droite == value_gauche:
                iterator += 1
        list_iterator.append(iterator * int(value_gauche))
    print(list_iterator)

    for value in list_iterator:
        result = result + int(value)

    print(result)
