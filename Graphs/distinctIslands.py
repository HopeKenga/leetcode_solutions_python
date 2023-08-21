def distinctIsland(grid):
    def depthFirst(r, c, direction):
        if 0 <= r < len(grid) and 0 <= c <len(grid[0]) and grid[r][c] == 1:
            grid[r][c] = 0
            island.append(direction)
            depthFirst(r + 1, c, 'D')#Explore Downward
            depthFirst(r - 1, c, 'U') #Explore Upward
            depthFirst(r, c +1 , 'R') #Explore Right
            depthFirst(r, c -1, 'L') #Explore Left
            island.append('B') #Backtrack
            
    numDistinct = set()
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                island = []
                depthFirst(r, c, 'X') #X is the startingn point
                numDistinct.add(tuple(island))
                
                
    return len(numDistinct)

grid = [
    [1,1,0,0],
    [1,0,0,1],
    [0,1,0,1],
    [1,1,0,0]
]

islands = distinctIsland(grid)
print(islands)