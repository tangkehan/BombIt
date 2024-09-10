from cmu_112_graphics import *


class Bomb():
    def __init__(self,person, bombRow, bombCol, board):
        self.image = None # load bomb image 
        self.explodeImage = None # load bomb explode image
        self.row = bombRow 
        self.col = bombCol
        self.board = board
        self.person = person

        #set the explode countdown
        self.explodeWaitTime = 3000
        
        self.startExplode = False

        # set the explode time
        self.explodeTime = 1500
    

        # if bomb is still being or exploded
        self.isExist = True 
        self.isExploding = False

    def drawBomb(self, app, canvas):
        if self.isExist == True:
            x0 = app.margin + self.col * app.cellSize + 20
            y0 = self.row * app.cellSize + 20

            sprite_bomb = app.sprites_bomb[app.spriteBombCounter]
            sprite_bomb = app.scaleImage(sprite_bomb, 0.80)
            canvas.create_image(x0, y0, image=ImageTk.PhotoImage(sprite_bomb))
        



    def bombExplode(self):
        # app.bomb.pop(0)
        row,col = self.row, self.col
        maze = self.board
        explodeArea = []
        directions = [(0,0),(1,0),(0,1),(-1,0),(0,-1)]
        for (drow, dcol) in directions:
            newRow = row + drow
            newCol = col + dcol

            #check bound 
            if (newRow == 0 or newRow == len(maze)-1 
                or newCol == 0 or newCol == len(maze[0])-1):
                continue
            
            # clear path
            explodeArea.append((newRow, newCol))

        return explodeArea

    def changeBoard(self):
        explodeArea = self.bombExplode()
        for (row,col) in explodeArea:
            self.board[row][col] = 0
        return self.board

  
    def drawExplode(self, app, canvas):
        if self.isExploding == True:
            exploreArea = self.bombExplode()
            for (row, col) in exploreArea:
                x0 = app.margin + col * app.cellSize + 20
                y0 = row * app.cellSize + 20

                # sprite_explode = app.sprites_explode[app.spriteExplodeCounter]
                # sprite_explode = app.scaleImage(sprite_explode, 2/3)
                # canvas.create_image(x0, y0, image=ImageTk.PhotoImage(sprite_explode))
                image = app.image_explode
                image = app.scaleImage(image, 0.6)
                canvas.create_image(x0,y0,image = ImageTk.PhotoImage(image))
                # canvas.create_oval(x0-15, y0-15, x0+15,
                #                y0+15, fill='red')
        



        
              



       
         


            



        

  
    # def explode(self,board):
    #     explodeArea = self.getExplodeArea(self, board)
    #     for (row,col) in explodeArea: