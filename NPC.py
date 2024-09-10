from cmu_112_graphics import *
from pathfinding import *
from bomb import*
import random

# do the NPC part

class Enemy():
    def __init__(self, row, col, maze, playerRow, playerCol,areas):
        self.row = row
        self.col = col
        self.targetRow = playerRow
        self.targetCol = playerCol
        self.maze = maze
        self.moveTime = 0
        self.areas = areas
        self.npcLife = 3
        self.gameOver = False
        self.isdead = False
        self.actTime = 1000
        self.act = [(1,0),(-1,0),(0,1),(0,-1),'bomb']
        self.escape = [(1,1),(-1,1),(-1,1),(-1,-1),(0,2),(0,-2),(2,0),(-2,0)]
       
        
    def getPath(self,maze,palyerRow,playCol):
        p = Dijkstra(maze, (self.row,self.col), (palyerRow, playCol))
        path = p.pathFinding()
        return path

    def getNextPosition(self,maze,playerRow, playerCol):
        # p = AStar(self.maze, (self.row,self.col), (self.targetRow, self.targetCol))
        # path = p.pathFinding()
        # (self.row, self.col) = path[1]

        (self.row, self.col) = self.getPath(maze,playerRow, playerCol)[1]

    def positionHelper(self,maze,playerRow, playerCol):
        return self.getPath(maze,playerRow, playerCol)[1]

    
    def getEscapePath(self):
        (drow, dcol)= random.choice(self.escape)
        targetRow = self.row + drow
        targetCol = self.col + dcol
        e = Dijkstra(self.maze, (self.row,self.col), (targetRow, targetCol))
        escapePath = e.pathFinding()
        return escapePath

  

    def lossLife(self):
        if self.areas == []:
            return 
        
        for area in self.areas:

            if (self.row, self.col) in area:
                self.npcLife -= 1
                break

        if self.npcLife <= 0:
            self.gameOver = True
            self.isdead = True

        return self.npcLife, self.gameOver, self.isdead

     


    def isLegalMove(self,row,col,board):
        if (row < 0 or row > len(board)-1 
            or col < 0 or col > len(board[0]) 
            or board[row][col] != 0):
            return False
        return True

    def move(self, action):
        (drow, dcol) = action
        newRow = self.row+drow
        newCol = self.col+dcol
        if self.isLegalMove(newRow, newCol, self.maze):
            self.row += drow
            self.col += dcol
        return self.row, self.col

    def putBomb(self):
        return (self.row, self.col)

    def randomAction(self, app):
        if self.actTime > 0:
            self.actTime -= 1000
        action = random.choice(self.act)
        if action in [(1,0),(-1,0),(0,1),(0,-1)]:
            if self.actTime == 0:
                self.row, self.col = self.move(action)
                self.actTime = 1000
        elif action == 'bomb':
            if self.actTime == 0:
                (row, col) = self.putBomb()
                app.bomb.append(Bomb('enemy',row, col, app.board))
                self.actTime = 1000



    def drawEnemy(self, app, canvas):
        x0 = app.margin + self.col * app.cellSize + 20
        y0 = self.row * app.cellSize + 20


        image = app.image_enemy
        image = app.scaleImage(image, 0.12)
        canvas.create_image(x0,y0,image = ImageTk.PhotoImage(image))

