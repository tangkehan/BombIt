# import numpy as np
import random
import copy
from cmu_112_graphics import *
from Maze import *
from Player import *
from bomb import *
from pathfinding import *
from NPC import *

# I write different classes and put them in different files
# in mainGame I import my class files and use them 



# notes from 112 website 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
# Start page Mode and input method from 112 website
# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#ioMethods
# image methods from 112 website
# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageMethods

# background design part
# watch the video https://www.youtube.com/watch?v=a0Vr4Jfyr_s which is a video 
# from the 15112 gallery. I also put two bomb buttons in my welcome page
# which I learned in the video above

def startMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2,app.height/2,image = ImageTk.PhotoImage(app.image_start))

    # canvas.create_rectangle(0, 0, 
                            # app.width  , app.height, 
                            # fill = '#e4ccf1', outline = '#bf86de')

    canvas.create_text(app.width/2, app.height/2+60, text='Bomb It!',
                       font='Courier 66 bold', fill='black')

    canvas.create_text(75, 50, anchor = 'w',
                       text= app.message, font='Courier 20 bold', fill='black')

    # radius = 15
    
    canvas.create_image(45,46,
                        image = ImageTk.PhotoImage(app.image_smallButton))
    
    # canvas.create_oval(35, 35, 65, 65,
    #                         fill = 'white', outline = '#bf86de')
    
    canvas.create_text(app.width-20, app.height-30, anchor = 'e',
                       text= "Kehan Tang\n15112", font='Courier 22 bold', fill='#eda627')

    # palyer location (290, 515) r = 30 
    # lacation (460, 515) rule
    canvas.create_image(app.width/2 - 100 ,app.height/2 + 200,
                        image = ImageTk.PhotoImage(app.image_button))

    canvas.create_image(app.width/2+70,app.height/2 + 200,
                        image = ImageTk.PhotoImage(app.image_button))

    canvas.create_text(app.width/2 - 85 ,app.height/2 + 210,
                       text= "PLAY", font='Courier 15 bold', fill='white')

    # find the radius of the button
    # canvas.create_oval(290-30,515-30,290+30,515+30,
    #                         fill = 'white', outline = '#bf86de')

    canvas.create_text(app.width/2+85,app.height/2 + 210,
                       text= "RULE", font='Courier 15 bold', fill='white')


def startInf(app):
    app.message = 'Click the button to enter your name!'
    app.name = None
    app.buttonLocation = (50, 50)
    app.playButton = (290, 515)
    app.ruleButton = (460, 515)

    # the start image draw by myself
    app.image_start = app.loadImage('start.jpg')
    app.image_start = app.scaleImage(app.image_start, 0.195)

    # image download from http://616pic.com/tupian/katongzhadan.html
    app.image_button = app.loadImage('bomb2.png')
    app.image_button = app.scaleImage(app.image_button, 0.110)
    app.image_smallButton = app.scaleImage(app.image_button, 0.5)

def startMode_mousePressed(app, event):
    (x, y) = app.buttonLocation
    d1 = ((x - event.x)**2 + (y - event.y)** 2) ** 0.5
    if d1 <= 15:
        name = app.getUserInput('What is your name?')
        app.name = name

        if (name == None):
            app.message = 'You canceled!'
                    
        else:
            app.showMessage('You entered: ' + name)
            app.message = f'Hi, {name}!'
        
    d2 = ((app.playButton[0] - event.x)**2 + (app.playButton[1] - event.y)** 2) ** 0.5
    if d2 <= 30 :
        app.mode = 'gameMode'

    d3 = ((app.ruleButton[0] - event.x)**2 + (app.ruleButton[1] - event.y)** 2) ** 0.5
    if d3 <= 30:
        app.mode = 'ruleMode'
    



# How to play page
def ruleMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2,app.height/2,image = ImageTk.PhotoImage(app.image_rule))
    canvas.create_text(app.width/2, 60, text='How To Play?',
                       font='Courier 66 bold', fill='black')
    canvas.create_text(20, 450, text='To win: Kill the enemy/ Score 2000pts', anchor = 'w',
                       font='Courier 25 bold', fill='black')
    canvas.create_text(20, 500, text='Bombs can both clear the path and make\nplayer or enemy lose life values',
                       anchor = 'w', font='Courier 25 bold', fill='black')
    canvas.create_text(20, 550, text='Stay away from bombs!',anchor = 'w',
                       font='Courier 25 bold', fill='black')

    # home button location (58,68)
    # play button location (58,158)
    canvas.create_image(50 ,60,
                        image = ImageTk.PhotoImage(app.image_ruleButton))
    # canvas.create_oval(58-25,68-25,58+25,68+25,
    #                         fill = 'white', outline = '#bf86de')

    canvas.create_image(50,150,
                        image = ImageTk.PhotoImage(app.image_ruleButton))
    canvas.create_text(60 ,68,
                       text= "HOME", font='Courier 15 bold', fill='white')
    canvas.create_text(60,158,
                       text= "PLAY", font='Courier 15 bold', fill='white')

def ruleInf(app):
    # the rule image is draw by myself
    app.image_rule = app.loadImage('rule.jpg')

    app.image_rule = app.scaleImage(app.image_rule, 0.195)
    app.image_ruleButton = app.scaleImage(app.image_button, 0.8)
    app.homeButton = (58, 68)
    app.playLocation = (58, 158)
   
def ruleMode_mousePressed(app, event):
    d4 = ((app.homeButton[0] - event.x)**2 + (app.homeButton[1] - event.y)** 2) ** 0.5
    if d4 <= 25:
        app.mode = 'startMode'

    d5 = ((app.playLocation[0] - event.x)**2 + (app.playLocation[1] - event.y)** 2) ** 0.5
    if d5 <= 25:
        app.mode = 'gameMode'

    
    




# images found from github in images functions
# https://github.com/ljcduo/CrazyArcade
# https://github.com/HyperMn/Crazy-Arcade-BNB-
def images():
    url_sandbox = 'https://raw.githubusercontent.com/ljcduo/CrazyArcade/master/DemoProject/CrazyArcade/Execute/Resource/SandBox.png'
    url_blueHouse = 'https://github.com/ljcduo/CrazyArcade/blob/master/DemoProject/CrazyArcade/Execute/Resource/TownHouseBlue.png'
    url_redHouse = 'https://raw.githubusercontent.com/ljcduo/CrazyArcade/master/DemoProject/CrazyArcade/Execute/Resource/TownHouseRed.png'
    url_yellowHouse = 'https://raw.githubusercontent.com/ljcduo/CrazyArcade/master/DemoProject/CrazyArcade/Execute/Resource/TownHouseYellow.png'
    url_tree = 'https://raw.githubusercontent.com/ljcduo/CrazyArcade/master/DemoProject/CrazyArcade/Execute/Resource/TownTree.png'
    url_road = 'https://raw.githubusercontent.com/HyperMn/Crazy-Arcade-BNB-/master/img/map/4.png'
   
    return [url_sandbox,url_blueHouse, url_redHouse, url_yellowHouse, url_tree, url_road]

def gameInf(app):
    app.row = app.col = 14
    app.maze = Maze(14)
    app.maze.generateMaze()
    app.board = app.maze.matrix
    app.margin = 150
    app.cellSize = 40
    app.width = app.margin + app.col * app.cellSize 
    app.height= app.row * app.cellSize 
    # sandbox
    app.image1 = app.loadImage(images()[0])
    # redhouse
    app.image2 = app.loadImage(images()[2])
    # yellowhouse
    app.image3 = app.loadImage(images()[3])
    # tree
    app.image4 = app.loadImage(images()[4])
    # road
    app.image5 = app.loadImage(images()[5])
    # app.image5 = app.loadImage('road.png')
    # app.image5 = app.scaleImage(app.image5, 0.5)
    app.mapImage = [app.image1, app.image2, app.image3, app.image4]

    app.explodeArea = []
    app.playerExplode = []

    app.playerRow = 1
    app.playerCol = 1
    
  
   # go to OH, TA helps me save my entered name and use it in Player object

    app.player = Player(app.name, app.playerRow, app.playerCol, app.board, app.explodeArea, app.playerExplode)
    app.playerLife = app.player.life
    app.score = app.player.score
   

    app.enemyRow = 13
    app.enemyCol = 13
    app.npc1 = (Enemy(app.enemyRow, app. enemyCol, app.board,
                     app.playerRow, app.playerCol, 
                     app.explodeArea))
    app.enemyLife = app.npc1.npcLife
    
  
    

    # flipImage codes from 112 notes from line 223-238 
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#flipImage
    # images found from https://raw.githubusercontent.com/HyperMn/Crazy-Arcade-BNB-/master/img/player/1.png
    url_player = 'https://raw.githubusercontent.com/HyperMn/Crazy-Arcade-BNB-/master/img/player/1.png'
    spritestrip = app.loadImage(url_player)
    app.sprites_up = [ ]
    app.sprites_down = [ ]
    app.sprites_left = [ ]
    app.sprites_right = [ ]
    for i in range(6):
        sprite1 = spritestrip.crop((48*i, 0, 46+48*i, 64))
        sprite2 = spritestrip.crop((48*i, 64, 46+48*i, 64*2))
        sprite3 = spritestrip.crop((48*i, 64*2, 46+48*i, 64*3))
        sprite4 = spritestrip.crop((48*i, 64*3, 46+48*i, 64*4))
        app.sprites_up.append(sprite1)
        app.sprites_down.append(sprite2)
        app.sprites_left.append(sprite3)
        app.sprites_right.append(sprite4)

    app.spriteCounter = 0

    # image found from https://raw.githubusercontent.com/SCNU-A225/CrazyArcade/master/img/boom/1.png
    url_bomb = 'https://raw.githubusercontent.com/SCNU-A225/CrazyArcade/master/img/boom/1.png'

    spritestripBomb = app.loadImage(url_bomb)
    app.sprites_bomb = [ ]
    
    for i in range(4):
        spriteBomb = spritestripBomb.crop((32*i, 0, 32+32*i, 48))
        app.sprites_bomb.append(spriteBomb)
    app.spriteBombCounter = 0
    
    # go to OH, Ta suggests me to put bomb objects in a class
    app.bomb = []
    
    app.timerDelay = 1000

    # image download from # https://github.com/ljcduo/CrazyArcade
    app.image_explode = app.loadImage('Explode.png')


    # image get from https://github.com/SineYuan/BnBonline/blob/master/public/game/Pic/Role1Ani.png
    app.image6 = app.loadImage("28.png")
    app.spriteAniCounter = 0


    # found pictures from https://github.com/younasong/crazyarcade/master/graphics/monsters/bombFront2.png
    url_enemy = 'https://raw.githubusercontent.com/younasong/crazyarcade/master/graphics/monsters/bombFront2.png'
    app.image_enemy = app.loadImage(url_enemy)


    app.gameOver = app.player.gameOver
    app.win = app.player.win
    app.lose = app.player.lose
    app.npcLose = app.npc1.isdead
    app.paused = False
    app.homeLocation = (78, 548)
 
    

def gameMode_keyPressed(app, event):
    if event.key == 'r':
        game_appStarted(app)

# pause feature in 112 website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    elif event.key == 'p':
        app.paused = not app.paused

    elif event.key == 'Down':
        if not app.paused:
            app.playerRow, app.playerCol = app.player.move(+1, 0, app.board)
            app.npc1.getPath(app.board,app.playerRow, app.playerCol)


    elif event.key == 'Left':
        if not app.paused:
            app.playerRow, app.playerCol = app.player.move(0, -1, app.board)
            app.npc1.getPath(app.board,app.playerRow, app.playerCol)
        
    elif event.key == 'Right':
        if not app.paused:
            app.playerRow, app.playerCol = app.player.move(0, +1, app.board)
            app.npc1.getPath(app.board,app.playerRow, app.playerCol)
        
    elif event.key == 'Up':
        if not app.paused:
            app.playerRow, app.playerCol = app.player.move(-1, 0, app.board)   
            app.npc1.getPath(app.board,app.playerRow, app.playerCol)
        
        
    elif event.key == 'Space':
        (row, col) = app.player.putBomb()
        app.bomb.append(Bomb('player',row, col, app.board))

    elif app.gameOver == True:
        return



def gameMode_timerFired(app):
    if app.gameOver == True:
        return 

    # code from 112 notes from line 159 - 160
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#flipImage
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites_up)
    app.spriteBombCounter = (1 + app.spriteBombCounter) % len(app.sprites_bomb)
    
   
    if not app.paused:
        for bomb in app.bomb:
            if bomb.explodeWaitTime <= 0:
                continue
            bomb.explodeWaitTime -= 1000
            if bomb.explodeWaitTime <= 0:
                bomb.startExplode = True
                bomb.isExist = False
                bomb.isExploding = True
                app.board = bomb.changeBoard()
                a = bomb.bombExplode()
                
                app.explodeArea.append(a)
            
                # print(app.explodeArea)
                if bomb.person == 'player':
                    b = bomb.bombExplode()
                    app.playerExplode.append(b)

        for bomb in app.bomb:
            # print('.....')
            if bomb.startExplode == True:
                bomb.explodeTime -= 1000
                if bomb.explodeTime <= 0:
                    bomb.startExplode = False
                    bomb.isExploding = False
                    
                    app.enemyLife, app.gameOver, app.npcLose = app.npc1.lossLife()

                    if app.gameOver == True:
                        return
                    # print(app.enemyLife, app.gameOver, app.npcLose)
                    app.score, app.gameOver, app.win = app.player.getScore(app.playerExplode)
                    if app.gameOver == True:
                        return
                    #  print(app.score, app.gameOver, app.win) 
                    app.playerLife, app.gameOver, app.lose = app.player.lossLife(app.playerRow,app.playerCol)
                    if app.gameOver == True:
                        return
                    
                    # print(app.win)
                    app.bomb.pop(0)
                    app.explodeArea.pop(0)
                

                    if bomb.person == 'player':
                        app.playerExplode.pop(0)

        
        app.npc1.moveTime += 1000
        if app.npc1.moveTime % 10000 == 0:
            (row, col) = app.npc1.putBomb()
            app.bomb.append(Bomb('enemy',row, col, app.board))
            (app.enemyRow, app.enemyCol) = (app.playerRow, app.playerCol)

        if app.npc1.moveTime % 1000 == 0:
            length = len(app.npc1.getPath(app.board,app.playerRow, app.playerCol))
            if length == 1:
                (row, col) = app.npc1.putBomb()
                app.bomb.append(Bomb('enemy',row, col, app.board))
                (app.enemyRow, app.enemyCol) = (app.playerRow, app.playerCol)

            else:
                app.npc1.getNextPosition(app.board,app.playerRow, app.playerCol)

            
                 
def drawbomb(app, canvas):
    for bomb in app.bomb:
        bomb.drawBomb(app,canvas)
        if bomb.startExplode == True:
            bomb.drawExplode(app, canvas) 



def drawPlayer(app, canvas):
    app.player.drawPlayer(app,canvas)


def drawboard(app,canvas):
    # draw background
    canvas.create_rectangle(0, 0, app.width + 40, app.height + 50,
                            fill = 'azure3', outline = 'black')
    # draw gamebackground
    # canvas.create_rectangle(app.margin, 0,
                            # app.width,app.height,fill = 'MistyRose2', outline = 'black')

def drawMaze(app,canvas):
    rows = len(app.board)
    cols = len(app.board[0])
    for row in range(rows):
       
        for col in range(cols):
            x0 = app.margin + col * app.cellSize
            y0 = row * app.cellSize
            x1 = app.margin + (col + 1) * app.cellSize
            y1 =  (row + 1) * app.cellSize

            # draw boxes
            if app.board[row][col] == -1:
                n = (5*row + 3*col ) % 4
                canvas.create_image(x0+20,y0+20,image = ImageTk.PhotoImage(app.mapImage[n]))

            # draw pathes
            elif app.board[row][col] == 0:
                canvas.create_image(x0+20,y0+20,image = ImageTk.PhotoImage(app.image5))
               

def drawScore(app,canvas):
 
    canvas.create_rectangle(5, 5, 145, 275,
                            fill = 'pale goldenrod', outline = 'black')
    canvas.create_image(40, 40, image=ImageTk.PhotoImage(app.image6))
    # canvas.create_text(70, 90, text='Player',
    #                    fill='purple', font='Helvetica 26 bold underline')
    canvas.create_text(70, 95, text= (f"Name: {app.name}"),
                       font="Courier 15 bold", fill="darkblue")
    canvas.create_text(70, 145, text= (f"Life: {app.playerLife}"),
                       font="Courier 15 bold", fill="darkblue")
    canvas.create_text(70, 195, text= (f"Score: {app.player.score}"),
                       font="Courier 15 bold", fill="darkblue")
    canvas.create_rectangle(5,285 ,145, app.height+40,
                            fill = 'wheat', outline = 'black')
    image_enemy = app.scaleImage(app.image_enemy, 0.180)
    canvas.create_image(40, 330, image=ImageTk.PhotoImage(image_enemy))
    canvas.create_text(70, 380, text= (" Name: Evil Bomb"),
                       font="Courier 15 bold", fill="darkblue")
    canvas.create_text(70, 420, text= (f"Life:{app.enemyLife}"),
                       font="Courier 15 bold", fill="darkblue")
    
    # (70, 540) radius = 26
    canvas.create_image(70, 540, image=ImageTk.PhotoImage( app.image_ruleButton ))
    canvas.create_text(80 ,548,
                       text= "HOME", font='Courier 15 bold', fill='white')
    # get the location of home image
    # canvas.create_oval(78 - 25, 548-25,78+25, 548+25, fill = 'red')

def drawFrozen(app, canvas):
    canvas.create_rectangle(app.margin,app.height/2 - 80, 
                            app.width + 40 , app.height/2 + 80, 
                            fill = 'sky blue', outline = 'deep sky blue')
    canvas.create_text( app.width/2+75, 300, text= ("Frozen Time!"),
                       font="Courier 45 bold", fill="blue")
    canvas.create_text( app.width/2+75, 340, text= ("Press 'p' again to play!"),
                       font="Courier 18 bold", fill="#ffffff")

    
    
def drawWin(app, canvas):
    canvas.create_rectangle(app.margin,app.height/2 - 80, 
                            app.width + 40 , app.height/2 + 80, 
                            fill = '#e4ccf1', outline = '#bf86de')
    canvas.create_text( app.width/2+75, 300, text= ("GREAT! YOU WIN !"),
                       font="Courier 45 bold", fill="red")
    canvas.create_text( app.width/2+75, 340, text= ("Press 'r' to play again!"),
                       font="Courier 18 bold", fill="#ffffff")
                    
def drawLose(app, canvas):
    canvas.create_rectangle(app.margin,app.height/2 - 80, 
                            app.width+40, app.height/2 + 80, 
                            fill = '#e4ccf1', outline = '#bf86de')
    canvas.create_text( app.width/2+75, 300, text= ("YOU LOSE!"),
                       font="Arial 45 bold", fill="darkblue")
    canvas.create_text( app.width/2+75, 340, text= ("Press 'r' to play again!"),
                       font="Arial 18 bold", fill="darkblue")

                
def gameMode_redrawAll(app, canvas):
    drawboard(app,canvas)
    drawMaze(app,canvas)
    drawPlayer(app,canvas)
    drawbomb(app, canvas)
    app.npc1.drawEnemy(app,canvas)
    drawScore(app,canvas)
    if app.paused == True:
        drawFrozen(app, canvas)
    
    if app.gameOver == True:
        if app.npcLose == True or app.win == True:
            drawWin(app, canvas)
        elif app.lose == True:
            drawLose(app, canvas)
    


def gameMode_mousePressed(app,event):
    (x, y) = app.homeLocation
    d = ((x - event.x)**2 + (y - event.y)** 2) ** 0.5
    if d < 26:
        app.mode = 'startMode'


def game_appStarted(app):
    gameInf(app)

def appStarted(app):
    app.mode = 'startMode'

    startInf(app)
    ruleInf(app)
    gameInf(app)

def play():
    runApp(width= 750, height= 610)


play()

