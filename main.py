'''

Nagesh Bansal17:02
Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column contains exactly one instance of the digits from 1 to 9.
Given a partially filled 3×3 2D array ‘grid[3][3]’, the goal is to assign digits (from 1 to 3) to the empty cells so that every row, column contains exactly one instance of the digits from 1 to 3.
grid = { {3, 0, 6, 5, 0, 8, 4, 0, 0}, 
         {5, 2, 0, 0, 0, 0, 0, 0, 0}, 
         {0, 8, 7, 0, 0, 0, 0, 3, 1}, 
         {0, 0, 3, 0, 1, 0, 0, 8, 0}, 
         {9, 0, 0, 8, 6, 3, 0, 0, 5}, 
         {0, 5, 0, 0, 9, 0, 6, 0, 0}, 
         {1, 3, 0, 0, 0, 0, 2, 5, 0}, 
         {0, 0, 0, 0, 0, 0, 0, 7, 4}, 
         {0, 0, 5, 2, 0, 6, 3, 0, 0} }
Output:
          3 1 6 5 7 8 4 9 2
          5 2 9 1 3 4 7 6 8
          4 8 7 6 2 9 5 3 1
          2 6 3 4 1 5 9 8 7
          9 7 4 8 6 3 1 2 5
      >   8 5 1 7 9 2 6 4 3
          1 3 8 9 4 7 2 5 6
          6 9 2 3 5 1 8 7 4
          7 4 5 2 8 6 3 1 9
          
          [[3, 1, 6, 5, 7, 8, 4, 9, 2], 
          [5, 2, 9, 1, 3, 4, 7, 6, 8], 
          [4, 8, 7, 6, 2, 9, 5, 3, 1], 
          [2, 6, 3, 4, 1, 5, 9, 8, 7], 
          [9, 7, 4, 8, 6, 3, 1, 2, 5], 
          [8, 5, 1, 7, 9, 2, 6, 4, 3], 
          [1, 3, 8, 9, 4, 7, 2, 5, 6], 
          [6, 9, 2, 3, 5, 1, 8, 7, 4], 
          [7, 4, 5, 2, 8, 6, 3, 1, 9]]

Approach:
1. Store the digits in each row, col and box 
2. store all the empty spaces inside a ds maybe set or a list
3. Take a decision to fill the empty space, choose a number from 1 to 9, 

mapRowDigit[i] = set of all the digits that occur in the ith row
mapColDigit[i] = set of all the digits that occur in the ith col
Box 1= 0,0 to 3,2
Box 2= 0,3 to 3,5
Box 3= 0,6 to 3,8
Box 4= 3,0 to 5,2
i,j = 5,0
i//3=5//3=1*3=3
box_i, box_j=(i//3)*3, (j//3)*3

'''
def getGridCopy(grid):
    gridCopy=[[0 for _  in range(9)] for __  in range(9)]
    for i in range(9):
        for j in range(9):
            gridCopy[i][j]=grid[i][j]
    return gridCopy
    
def findBoxNumber(i,j):
    return (i//3)*3, (j//3)*3

def findNoOfAllValidSudokuSolutions(grid):
    listAllValidSudokuGrids=[]
    def sudukoHelper(index):
        if index>=len(listEmptySpaces):
            listAllValidSudokuGrids.append(getGridCopy(grid))
            return True
        emptySpace_i, emptySpace_j = listEmptySpaces[index]
        for candidateDigit in range(1,10):
            if candidateDigit not in mapRowDigit[emptySpace_i] and candidateDigit not in mapColDigit[emptySpace_j]  and candidateDigit not in mapBoxDigit[findBoxNumber(emptySpace_i, emptySpace_j)]:
                mapRowDigit[emptySpace_i].add(candidateDigit)
                mapColDigit[emptySpace_j].add(candidateDigit)
                mapBoxDigit[findBoxNumber(emptySpace_i, emptySpace_j)].add(candidateDigit)
                grid[emptySpace_i][emptySpace_j]=candidateDigit
                result=sudukoHelper(index+1)
                #if result:
                #    return True
                mapRowDigit[emptySpace_i].remove(candidateDigit)
                mapColDigit[emptySpace_j].remove(candidateDigit)
                mapBoxDigit[findBoxNumber(emptySpace_i, emptySpace_j)].remove(candidateDigit)
                grid[emptySpace_i][emptySpace_j]=0
        return False
        
    mapRowDigit=defaultdict(set)
    mapColDigit=defaultdict(set)
    mapBoxDigit=defaultdict(set)
    listEmptySpaces=[]
    
    n=9
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                listEmptySpaces.append((i,j))
                continue
            mapRowDigit[i].add(grid[i][j])
            mapColDigit[j].add(grid[i][j])
            mapBoxDigit[findBoxNumber(i,j)].add(grid[i][j])
    
    sudukoHelper(0)
    print(len(listAllValidSudokuGrids))
    for gridSol in  listAllValidSudokuGrids:
        for row in gridSol:
            print(row)
        print("==========================")
    return len(listAllValidSudokuGrids)

    


def findASingleSudokuSolution(grid):
    def sudukoHelper(index):
        if index>=len(listEmptySpaces):
            return True
        emptySpace_i, emptySpace_j = listEmptySpaces[index]
        for candidateDigit in range(1,10):
            if candidateDigit not in mapRowDigit[emptySpace_i] and candidateDigit not in mapColDigit[emptySpace_j]  and candidateDigit not in mapBoxDigit[findBoxNumber(emptySpace_i, emptySpace_j)]:
                mapRowDigit[emptySpace_i].add(candidateDigit)
                mapColDigit[emptySpace_j].add(candidateDigit)
                mapBoxDigit[findBoxNumber(emptySpace_i, emptySpace_j)].add(candidateDigit)
                grid[emptySpace_i][emptySpace_j]=candidateDigit
                result=sudukoHelper(index+1)
                if result:
                    return True
                mapRowDigit[emptySpace_i].remove(candidateDigit)
                mapColDigit[emptySpace_j].remove(candidateDigit)
                mapBoxDigit[findBoxNumber(emptySpace_i, emptySpace_j)].remove(candidateDigit)
                grid[emptySpace_i][emptySpace_j]=0
        return False
        
    mapRowDigit=defaultdict(set)
    mapColDigit=defaultdict(set)
    mapBoxDigit=defaultdict(set)
    listEmptySpaces=[]
    
    n=9
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                listEmptySpaces.append((i,j))
                continue
            mapRowDigit[i].add(grid[i][j])
            mapColDigit[j].add(grid[i][j])
            mapBoxDigit[findBoxNumber(i,j)].add(grid[i][j])
    
    sudukoHelper(0)
    return grid


grid = [[3,9,0,2,0,0,0,0,0],
[0,8,0,0,7,0,0,0,0],
[1,0,0,0,0,4,5,0,0],
[8,2,0,1,0,0,0,4,0],
[0,0,4,0,0,2,0,0,0],
[0,5,0,0,0,3,0,2,8],
[0,0,0,3,0,0,0,7,4],
[0,4,0,0,5,0,0,3,0],
[7,0,3,0,1,8,0,0,0]]


def generateASudokuWithASingleValidSolution():
    grid=[[0 for _ in range(9)] for __ in range(9)]
    randomPositionRow, randomPositionCol =random.choice([i for i in range(9)]), random.choice([i for i in range(9)])
    randomDigit=random.choice([i for i in range(1,10)])
    
    solutionGrid=findASingleSudokuSolution(grid)
    
    noOfEmptiedCellsInGrid=0
    prevValue=0
    #randomPositionRow, randomPositionCol =random.choice([i for i in range(9)]), random.choice([i for i in range(9)])
    while findNoOfAllValidSudokuSolutions(solutionGrid)==1:
        while True:
            randomPositionToEmptyRow, randomPositionToEmptyCol =random.choice([i for i in range(9)]), random.choice([i for i in range(9)])
            if solutionGrid[randomPositionToEmptyRow][randomPositionToEmptyCol]!=0:
                prevValue= solutionGrid[randomPositionToEmptyRow][randomPositionToEmptyCol]
                solutionGrid[randomPositionToEmptyRow][randomPositionToEmptyCol]=0
                break
        noOfEmptiedCellsInGrid+=1
    solutionGrid[randomPositionToEmptyRow][randomPositionToEmptyCol]=prevValue
    return solutionGrid
    
'''
@1. make a completely empty grid 
@2. Choose a radmon position inside of the 9x9 grid and fill it with a random no betwn 1 to 9.
@3. Find one of solution for this grid.
4. iterate:: randomly choose a position inside of this filled in grid and make it empty, 

[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]
         
         
         
        [[3, 6, 5, 2, 8, 1, 4, 9, 7], 
         [4, 8, 2, 5, 7, 9, 1, 6, 3], 
         [1, 7, 9, 6, 3, 4, 5, 8, 2], 
         [8, 2, 7, 1, 6, 5, 3, 4, 9], 
         [6, 3, 4, 8, 9, 2, 7, 1, 5], 
         [9, 5, 1, 7, 4, 3, 6, 2, 8], 
         [5, 1, 8, 3, 2, 6, 9, 7, 4], 
         [2, 4, 6, 9, 5, 7, 8, 3, 1], 
         [7, 9, 3, 4, 1, 8, 2, 5, 6]]
         
         '''
generatedGrid=generateASudokuWithASingleValidSolution()
print(generatedGrid)


grid=[[0, 2, 3, 4, 5, 6, 0, 8, 9], 
 [0, 5, 0, 0, 8, 9, 1, 2, 0], 
 [0, 0, 9, 1, 2, 0, 4, 5, 0], 
 [2, 1, 4, 3, 6, 5, 8, 9, 7], 
 [3, 0, 5, 0, 9, 7, 0, 1, 4], 
 [8, 9, 0, 2, 0, 4, 3, 6, 5], 
 [5, 0, 1, 0, 0, 0, 9, 7, 8], 
 [0, 4, 0, 0, 7, 0, 0, 0, 1], 
 [0, 0, 0, 0, 3, 0, 0, 4, 2]]

print(findNoOfAllValidSudokuSolutions(generatedGrid))

