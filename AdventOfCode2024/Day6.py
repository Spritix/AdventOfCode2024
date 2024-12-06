f = open("input_day6.txt","r")

lines = f.read().strip().split("\n")

R = len(lines)
C = len(lines[0])


for r in range(R):
    for c in range(C):
        if lines[r][c] == "^" or lines[r][c] == "<" or lines[r][c] == ">" or lines[r][c] == "v":
            indexR, indexC = r,c

def day6_part1(r,c):
    exitFound=False
    while not exitFound:
        match lines[r][c]:
            case '^':
                if r-1 < 0:
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    exitFound=True
                    break
                elif lines[r-1][c] == '#':
                    lines[r] = lines[r][:c] + '>' + lines[r][c+1:]
                else :
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    lines[r-1] = lines[r-1][:c] + '^' + lines[r-1][c+1:]
                    r-=1
            case 'v':
                if r+1 >= R:
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    exitFound=True
                    break
                elif lines[r+1][c] == '#':
                    lines[r] = lines[r][:c] + '<' + lines[r][c+1:]
                else :
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    lines[r+1] = lines[r+1][:c] + 'v' + lines[r+1][c+1:]
                    r+=1
            case '<':
                if c-1 < 0:
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    exitFound=True
                    break
                elif lines[r][c-1] == '#':
                    lines[r] = lines[r][:c] + '^' + lines[r][c+1:]
                else :
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    lines[r] = lines[r][:c-1] + '<' + lines[r][c:]
                    c-=1
            case '>':
                if c+1 >= C:
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    exitFound=True
                    break
                elif lines[r][c+1] == '#':
                    lines[r] = lines[r][:c] + 'v' + lines[r][c+1:]
                else :
                    lines[r] = lines[r][:c] + 'X' + lines[r][c+1:]
                    lines[r] = lines[r][:c+1] + '>' + lines[r][c+2:]
                    c += 1

def day6_part2(r, c):
    ans = 0
    memorizeR, memorizeC = r,c
    for row in range(R):
        for column in range(C):
            exitFound = False
            numberRotation = 0
            previousChar = '.'
            copyLines = lines.copy()
            r,c = memorizeR, memorizeC
            if copyLines[row][column] == '.':
                copyLines[row] = copyLines[row][:column] + 'O' + copyLines[row][column + 1:]
                print(row,column)
                while not exitFound and numberRotation < 4:
                    match copyLines[r][c]:
                        case '^':
                            if r - 1 < 0:
                                copyLines[r] = copyLines[r][:c] + '|' + copyLines[r][c + 1:]
                                exitFound = True
                            elif copyLines[r - 1][c] == '#' or copyLines[r - 1][c] == 'O':
                                copyLines[r] = copyLines[r][:c] + '>' + copyLines[r][c + 1:]
                                if previousChar == '+':
                                    numberRotation += 1
                                else :
                                    numberRotation = 0
                                    previousChar = '|'
                            else:
                                if previousChar == '-' or previousChar =='+':
                                    copyLines[r] = copyLines[r][:c] + '+' + copyLines[r][c + 1:]
                                else:
                                    copyLines[r] = copyLines[r][:c] + '|' + copyLines[r][c + 1:]
                                previousChar = copyLines[r-1][c]
                                copyLines[r - 1] = copyLines[r - 1][:c] + '^' + copyLines[r - 1][c + 1:]
                                r -= 1
                        case 'v':
                            if r + 1 >= R:
                                copyLines[r] = copyLines[r][:c] + '|' + copyLines[r][c + 1:]
                                exitFound = True
                            elif copyLines[r + 1][c] == '#' or copyLines[r + 1][c] =='O':
                                copyLines[r] = copyLines[r][:c] + '<' + copyLines[r][c + 1:]
                                if previousChar == '+':
                                    numberRotation += 1
                                else :
                                    numberRotation = 0
                                    previousChar = '|'
                            else:
                                if previousChar == '-' or previousChar =='+':
                                    copyLines[r] = copyLines[r][:c] + '+' + copyLines[r][c + 1:]
                                else:
                                    copyLines[r] = copyLines[r][:c] + '|' + copyLines[r][c + 1:]
                                previousChar = copyLines[r+1][c]
                                copyLines[r + 1] = copyLines[r + 1][:c] + 'v' + copyLines[r + 1][c + 1:]
                                r += 1
                        case '<':
                            if c - 1 < 0:
                                copyLines[r] = copyLines[r][:c] + '-' + copyLines[r][c + 1:]
                                exitFound = True
                            elif copyLines[r][c - 1] == '#' or copyLines[r][c - 1] =='O':
                                copyLines[r] = copyLines[r][:c] + '^' + copyLines[r][c + 1:]
                                if previousChar == '+':
                                    numberRotation += 1
                                else :
                                    numberRotation = 0
                                    previousChar = '-'
                            else:
                                if previousChar == '|' or previousChar =='+':
                                    copyLines[r] = copyLines[r][:c] + '+' + copyLines[r][c + 1:]
                                else:
                                    copyLines[r] = copyLines[r][:c] + '-' + copyLines[r][c + 1:]
                                previousChar = copyLines[r][c-1]
                                copyLines[r] = copyLines[r][:c - 1] + '<' + copyLines[r][c:]
                                c -= 1
                        case '>':
                            if c + 1 >= C:
                                copyLines[r] = copyLines[r][:c] + '-' + copyLines[r][c + 1:]
                                exitFound = True
                            elif copyLines[r][c + 1] == '#' or copyLines[r][c + 1] =='O':
                                copyLines[r] = copyLines[r][:c] + 'v' + copyLines[r][c + 1:]
                                if previousChar == '+':
                                    numberRotation += 1
                                else :
                                    numberRotation = 0
                                    previousChar = '-'
                            else:
                                if previousChar == '|' or previousChar =='+':
                                    copyLines[r] = copyLines[r][:c] + '+' + copyLines[r][c + 1:]
                                else:
                                    copyLines[r] = copyLines[r][:c] + '-' + copyLines[r][c + 1:]
                                previousChar = copyLines[r][c+1]
                                copyLines[r] = copyLines[r][:c + 1] + '>' + copyLines[r][c + 2:]
                                c += 1
                if numberRotation >= 4:
                    ans+=1
               # for line in copyLines:
                #    print(copyLines.index(line),line)
                #print()
    return ans

#day6_part1(indexR,indexC)
#ans = 0
#for line in lines:
   # print(line)
    #ans+= line.count('X')

print(day6_part2(indexR,indexC))

