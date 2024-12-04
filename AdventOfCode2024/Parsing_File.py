from unicodedata import numeric


def parse_file(fileName):
    list_gauche=[]
    list_droite=[]
    f = open(fileName, 'r')
    for x in f:
        list_gauche.append(x.split("   ")[0])
        list_droite.append(x.split("   ")[1].removesuffix("\n"))
    list_gauche.sort()
    list_droite.sort()
    return list_gauche, list_droite