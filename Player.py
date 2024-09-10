# draw player should draw in map or just redraw a player

from cmu_112_graphics import *


class Player():
    def __init__(self, name, row, col, maze, areas, selfArea):
        self.name = name
        self.row = row
        self.col = col
        self.bombCol = None
        self.bombCol = None
        self.maze = maze
        self.margin = 150
        self.cellSize = 40
        self.drow = 0
        self.dcol = 0

        self.areas = areas
        self.smallAreas = selfArea
        self.score = 0
        self.life = 3
        self.gameOver = False
        self.win = None
        self.lose = None

    def lossLife(self,row, col):
  
        if self.areas == []:
            return 
        
        for area in self.areas:
  
            if (row, col) in area:
                self.life -= 1
                break

        if self.life <= 0:
            self.gameOver = True
            self.lose = True

        return self.life, self.gameOver, self.lose

    def getScore(self,selfArea):
        for area in selfArea:
            self.score += 5*len(area)
            if self.score >= 2000:
                self.gameOver = True
                self.win = True
        return self.score,self.gameOver,self.win


    def isLegalMove(self,row,col,board):
        if (row < 0 or row > len(board)-1 
            or col < 0 or col > len(board[0]) 
            or board[row][col] != 0):
            return False
        return True

    def move(self, drow, dcol, board):
        newRow = self.row+drow
        newCol = self.col+dcol
        self.drow = drow
        self.dcol = dcol
        if self.isLegalMove(newRow, newCol, board):
            self.row += drow
            self.col += dcol
        return self.row, self.col


    def putBomb(self):
        self.bombRow = self.row
        self.bombCol = self.col
        return (self.bombRow, self.bombCol)
        
    def drawPlayer(self, app, canvas):
        x0 = self.margin + self.col * self.cellSize + 20
        y0 = self.row * self.cellSize + 20


        #if goes down
        if self.drow == -1 and self.dcol == 0:
            sprite1 = app.sprites_up[app.spriteCounter]
            sprite1 = app.scaleImage(sprite1, 2/3)
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(sprite1))
        elif self.drow == 1 and self.dcol == 0:
            sprite2 = app.sprites_down[app.spriteCounter]
            sprite2 = app.scaleImage(sprite2, 2/3)
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(sprite2))
        elif (self.drow == 0 and self.dcol == -1) :
            sprite3 = app.sprites_left[app.spriteCounter]
            sprite3 = app.scaleImage(sprite3, 2/3)
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(sprite3))
        elif self.drow == 0 and self.dcol == 1 or self.drow == self.dcol == 0:
            sprite4 = app.sprites_right[app.spriteCounter]
            sprite4 = app.scaleImage(sprite4, 2/3)
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(sprite4))


    def redrawAll(app, canvas):
        sprite = app.sprites[app.spriteCounter]
        canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))



    # def putBomb(self):
    #     board = Map.getMap
    #     self.bombRow = self.row
    #     self.bombCol = self.col
    #     board[self.bombRow][self.bombCol] == 'b'

    # def drawPlayer(self, app, canvas):
    #     # put the player image to cell
    #     x0 = app.margin + self.col * app.cellSize
    #     y0 = self.row * app.cellSize
    #     x1 = app.margin + (self.col + 1) * app.cellSize
    #     y1 =  (self.row + 1) * app.cellSize
    #     canvas.create_oval()

    # def drawBomb(app,canvas,self):
    #     # put the bomb image to the cell
    #     pass

    ###need to design AI random action











