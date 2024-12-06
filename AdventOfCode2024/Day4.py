from logging import NullHandler

f = open("input_day4.txt","r")

lines = f.read().strip().split("\n")

print(lines)

R = len(lines)
C = len(lines[0])

def day4_part1(r,c):
    ans = 0
    # horizontale est
    if r + 3 < R and lines[r][c] == 'X' and lines[r + 1][c] == 'M' and lines[r + 2][c] == 'A' and lines[r + 3][c] == 'S':
        ans += 1
    # horizontale ouest
    if r - 3 >= 0 and lines[r][c] == 'X' and lines[r - 1][c] == 'M' and lines[r - 2][c] == 'A' and lines[r - 3][c] == 'S':
        ans += 1
    # diagonale nord-ouest
    if r - 3 >= 0 and c - 3 >= 0 and lines[r][c] == 'X' and lines[r - 1][c - 1] == 'M' and lines[r - 2][c - 2] == 'A' and lines[r - 3][c - 3] == 'S':
        ans += 1
    # diagonale nord est
    if r - 3 >= 0 and c + 3 < C and lines[r][c] == 'X' and lines[r - 1][c + 1] == 'M' and lines[r - 2][c + 2] == 'A' and lines[r - 3][c + 3] == 'S':
        ans += 1
    # diagonale sud-ouest
    if r + 3 < R and c - 3 >= 0 and lines[r][c] == 'X' and lines[r + 1][c - 1] == 'M' and lines[r + 2][c - 2] == 'A' and lines[r + 3][c - 3] == 'S':
        ans += 1
    # diagonale sud est
    if r + 3 < R and c + 3 < C and lines[r][c] == 'X' and lines[r + 1][c + 1] == 'M' and lines[r + 2][c + 2] == 'A' and lines[r + 3][c + 3] == 'S':
        ans += 1
    # verticale sud
    if c + 3 < C and lines[r][c] == 'X' and lines[r][c + 1] == 'M' and lines[r][c + 2] == 'A' and lines[r][c + 3] == 'S':
        ans += 1
    # verticale nord
    if c - 3 >= 0 and lines[r][c] == 'X' and lines[r][c - 1] == 'M' and lines[r][c - 2] == 'A' and lines[r][c - 3] == 'S':
        ans += 1
    return ans

def day4_part2(r,c):
    ans=0
    if r+1<R and c-1>=0 and r-1>= 0 and c+1<C:
        if lines[r][c] == 'A' and lines[r+1][c+1] == 'S' and lines[r-1][c-1] == 'M' and lines[r+1][c-1] == 'S' and lines[r-1][c+1] == 'M':
            ans = 1
        if lines[r][c] == 'A' and lines[r-1][c+1] == 'S' and lines[r+1][c-1] == 'M' and lines[r+1][c+1] == 'S' and lines[r-1][c-1] == 'M' :
            ans = 1
        if lines[r][c] == 'A' and lines[r-1][c-1] == 'S' and lines[r+1][c+1] == 'M' and lines[r-1][c+1] == 'S' and lines[r+1][c-1] == 'M':
            ans = 1
        if lines[r][c] == 'A' and lines[r+1][c-1] == 'S' and lines[r-1][c+1] == 'M' and lines[r-1][c-1] == 'S' and lines[r+1][c+1] == 'M':
            ans = 1
    return ans

answer = 0
for r in range(R):
    for c in range(C):
       answer += day4_part2(r,c)

print(answer)


