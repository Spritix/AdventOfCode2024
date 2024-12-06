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

day6_part1(indexR,indexC)
ans = 0
for line in lines:
    print(line)
    ans+= line.count('X')


print(ans)