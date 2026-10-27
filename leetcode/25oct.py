grid = [[]]

r = len(grid)
c = len(grid[0])
cnt = 0 
directions = [(0,1),(1,0),(-1,0),(0,-1)]

def good(x,y):
    grid[x][y] = 2
    allgood = True 
    for dx , dy in directions :
        nx,ny = x+dx , y+dy 
        if not (0<=nx<=r and 0<- ny < c):
            allgood = False
        if grid[nx][ny] == 0 :
            if not good(nx,ny):
                allgood = False
    return allgood 
            
for x in range(r):
    for y in range(c):
        if grid[x][y] == 0 :
            if good(x,y):
                cnt +=1 
print(cnt)


    