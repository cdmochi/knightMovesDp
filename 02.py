import copy

#take input and put each value in tuple
line = input().split()
start = line[0]
end = line[1]

#converted form
sColumn = ord(start[0])
sRow = int(start[1])

eColumn = end[0]
eRow = int(end[1])-1

# 8 * 8 board as the  a-h and 1- 8  
Board = [ [ -1 for i in range(8)] for i in range(8)]

class state:
    def __init__(self,c,r):
        self.column = c
        self.row = int(r)
        self.s = 0
    def getIntColumn(self):
        return ord(self.column)  

#column : Str
#row : Int 
def isValid(column,row):
    #out of index
    intColumn = ord(column)
    if (intColumn % 97 == intColumn):
        return False
    if ( (intColumn  % 97 >= 0 and (intColumn % 97) < 8 and row >= 0 and row < 8) ):
       if (Board[intColumn%97][row] == -1):
           #check if that pos has been checked yet
            return True
    return False



def Goal(x):
    if x.column == eColumn and x.row == eRow:
        return True
    return False


options = [(-1,2),(1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

S = state(start[0],sRow-1)
Q = []
Q.append(S)
while not Goal(S):
    for i in options:
        cMove = i[0]
        rMove = i[1]
        dummyS = copy.deepcopy(S)
        dummyS.column = chr(dummyS.getIntColumn() + cMove)
        dummyS.row += rMove
        if isValid(dummyS.column,dummyS.row):
            dummyS.s += 1
            #Marked the visited area
            Board[dummyS.getIntColumn()%97][dummyS.row] = 1
            Q.append(dummyS)
    S = Q[0]
    del Q[0]
print("To get from {} to {} takes {} knight moves.".format(start,end,S.s))





