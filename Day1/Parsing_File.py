from unicodedata import numeric


def parse_file(fileName):
    list_gauche=[]
    list_droite=[]
    list_sorted = []
    f = open(fileName, 'r')
    for x in f:
        list_gauche.append(x.split("   ")[0])
        list_droite.append(x.split("   ")[1].removesuffix("\n"))
    list_gauche.sort()
    list_droite.sort()
    while len(list_gauche)>0:
        list_sorted.append([list_gauche.pop(0),list_droite.pop(0)])
    return list_sorted