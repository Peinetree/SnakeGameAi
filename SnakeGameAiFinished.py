# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 15:50:38 2021

@author: CJ
"""
# CJ Peine
# Snake game (with AI)
# 11-10-20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

colors =[WHITE, GREEN, BLUE, FUCHSIA, GRAY, LIME, MAROON, OLIVE, PURPLE, RED, SILVER, TEAL, YELLOW, ORANGE, CYAN]
import sys
import pygame
import random
 
pygame.init()


fps = 15
fpsClock = pygame.time.Clock()
di = 4
width = 640
height = 480
snake_dim = 20
food_x = 580
food_y = 0

score = 3



arrayx = [60, 60, 60]
arrayy = [0, 20, 40]
comb = []


def gen_food():
    global food_x
    global food_y
    global fps
    global score
    if di == 1:   #right
        arrayx.insert(0, arrayx[0]-snake_dim)
        arrayy.insert(0, arrayy[0])
    if di == 2:   #left
        arrayx.insert(0, arrayx[0]+snake_dim)
        arrayy.insert(0, arrayy[0])
    if di == 3:   #up
         arrayy.insert(0, arrayy[-1]-snake_dim)
         arrayx.insert(0, arrayx[-1])
    if di == 4:   #down
        arrayy.insert(0, arrayy[-1]+snake_dim)
        arrayx.insert(0,  arrayx[-1])
        
    food_x = random.randrange(0, width-snake_dim, 20)
    food_y = random.randrange(0, height-snake_dim, 20)
    fps = fps
    score = score + 1
    print('score is: ', score)
def findPath():
    def isTail(x,y):
        for i in range(0, len(arrayx)):
            if x == arrayx[i] and y == arrayy[i]:
                return True
            
    opx = []
    opy = []
    decision = []
    choice = []
    
    possup = arrayy[-1]-snake_dim
    possdown = arrayy[-1]+snake_dim
    possleft = arrayx[-1]-snake_dim
    possright = arrayx[-1]+snake_dim
    

        
   #print("posup: ", possup)
    #print(arrayy)
    if not isTail(arrayx[-1], possup):
        if not arrayy[-1] == 0:
            opy.append(possup)
            opx.append(arrayx[-1])
            choice.append(3)

    
    if not isTail(arrayx[-1], possdown):
        if not arrayy[-1] == height-snake_dim:
            opy.append(possdown)
            opx.append(arrayx[-1])   
            choice.append(4)
            
    if not isTail(possright, arrayy[-1]):
        if not arrayx[-1] == width-snake_dim:
            opy.append(arrayy[-1])
            opx.append(possright)
            choice.append(1)
    
    if not isTail(possleft, arrayy[-1]):
        if not arrayx[-1] == 0:
            opy.append(arrayy[-1])
            opx.append(possleft)
            choice.append(2)
            
    class object:
        def __init__(self, h, g, f):
            self.h = h
            self.g = g
            self.f = f
            

    def square_init(self, name, h, g, f):
        self.name = name
        self.h = h
        self.g = g
        self.f = f
    
    
    def one():
        global di
        h = (abs(opx[0]-food_x)/snake_dim)+(abs(opy[0]-food_y)/snake_dim)
        g = (abs(opx[0]-arrayx[-1])/snake_dim)+(abs(opy[0]-arrayy[-1])/snake_dim)
        f = str(h+g)
        h = str(h)
        g = str(g)
        new_class = type("Square", (), {"__init__": square_init})
        x = new_class("sq1", h, g, f)
        
        
        di = choice[0]
       
            
        print("<1>", di)

    def two():
        global di
        h1 = (abs(opx[0]-food_x)/snake_dim)+(abs(opy[0]-food_y)/snake_dim)
        g1 = (abs(opx[0]-arrayx[-1])/snake_dim)+(abs(opy[0]-arrayy[-1])/snake_dim)
        f1 = str(h1+g1)
        h1 = str(h1)
        g1 = str(g1)
        h2 = (abs(opx[1]-food_x)/snake_dim)+(abs(opy[1]-food_y)/snake_dim)
        g2 = (abs(opx[1]-arrayx[-1])/snake_dim)+(abs(opy[1]-arrayy[-1])/snake_dim)
        f2 = str(h2+g2)
        h2 = str(h2)
        g2 = str(g2)
        floats = []
        new_class = type("Square", (), {"__init__": square_init})
        x = new_class("sq1", h1, g1, f1)
        y = new_class("sq2", h2, g2, f2)
        
        decision.append(x.f)
        decision.append(y.f)
        for element in decision:
            floats.append(float(element))
        #print(floats)
        low = min(floats)
        if low == floats[0]:
            di = choice[0]
        elif low == floats[1]:
            di = choice[1]
            
        print("<2>", di, low, floats, choice)

    def three():
        global di
        h1 = (abs(opx[0]-food_x)/snake_dim)+(abs(opy[0]-food_y)/snake_dim)
        g1 = (abs(opx[0]-arrayx[-1])/snake_dim)+(abs(opy[0]-arrayy[-1])/snake_dim)
        f1 = str(h1+g1)
        h1 = str(h1)
        g1 = str(g1)
        h2 = (abs(opx[1]-food_x)/snake_dim)+(abs(opy[1]-food_y)/snake_dim)
        g2 = (abs(opx[1]-arrayx[-1])/snake_dim)+(abs(opy[1]-arrayy[-1])/snake_dim)
        f2 = str(h2+g2)
        h2 = str(h2)
        g2 = str(g2)
        h3 = (abs(opx[2]-food_x)/snake_dim)+(abs(opy[2]-food_y)/snake_dim)
        g3 = (abs(opx[2]-arrayx[-1])/snake_dim)+(abs(opy[2]-arrayy[-1])/snake_dim)
        f3 = str(h3+g3)
        h3 = str(h3)
        g3 = str(g3)
        
        floats = []
        
        new_class = type("Square", (), {"__init__": square_init})
        x = new_class("sq1", h1, g1, f1)
        y = new_class("sq2", h2, g2, f2)
        z = new_class("sq3", h3, g3, f3)
        
        decision.append(x.f)
        decision.append(y.f)
        decision.append(z.f)
        for element in decision:
            floats.append(float(element))
        #print(floats)
        low = min(floats)
        #print(x.f)
        
        
       # if floats[0] == floats[1] && floats[1] == floats[2]:    #this is an effort to turn the snake around if its heading away from the food
           # if di == 1
           
           
        if low == floats[0]:
            di = choice[0]
        elif low == floats[1]:
            di = choice[1]
        elif low == floats[2]:
            di = choice[2]
        print("<3>", di, low, floats, choice)



    if len(opx) == 1:
        one()
    if len(opx) == 2:
        two()
    if len(opx) == 3:
        three()
        
            
    

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Game loop.
while True:
    length = len(arrayx)
    randcolor = random.randrange(0, len(colors))
    num = len(comb)
    strike = 0
    findPath()
    


    
    for i in range(0, length):
        thingx = str(arrayx[i])
        thingy = str(arrayy[i])
        comb.append(thingx)
        comb.append(thingy)
    num = len(comb)
    for i in range(0, num, 2):
        string = comb[i]+comb[i+1]
        comb.append(string)
    for i in range(0, num):
        del comb[0]
    
    num2 = len(comb)
    for p in range(0, num2):
            if comb[-1] == comb[p]:
                strike = strike+1
                if strike == 2:
                    pygame.quit()
                    sys.exit()
    comb = []
        
    
    if arrayx[-1] == food_x and arrayy[-1] == food_y:
       gen_food()
    if length == 1:
        if di == 1:   #right
            arrayx[-1] = arrayx[-1]+snake_dim
        if di == 2:   #left
            arrayx[-1] = arrayx[-1]-snake_dim
        if di == 3:   #up
            arrayy[-1] = arrayy[-1]-snake_dim
        if di == 4:   #down
            arrayy[-1] = arrayy[-1]+snake_dim
    else:
        if di == 1:   #right
             del arrayx[0]
             del arrayy[0]
             arrayx.append(arrayx[-1]+snake_dim)
             arrayy.append(arrayy[-1])
        if di == 2:   #left
             del arrayx[0]
             del arrayy[0]
             arrayx.append(arrayx[-1]-snake_dim)
             arrayy.append(arrayy[-1])
             
        if di == 3:   #up
             del arrayx[0]
             del arrayy[0]
             arrayy.append(arrayy[-1]-snake_dim)
             arrayx.append(arrayx[-1])
        if di == 4:   #down
             del arrayx[0]
             del arrayy[0]
             arrayy.append(arrayy[-1]+snake_dim)
             arrayx.append(arrayx[-1])

    screen.fill((0))
    for i in range(0, length):
       pygame.draw.rect(screen, RED, [arrayx[i], arrayy[i], snake_dim, snake_dim])           #snake
       
       
       
       
    pygame.draw.rect(screen, CYAN, [food_x, food_y, snake_dim, snake_dim])   #food
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
          
          if event.key == pygame.K_UP:
            if di == 4 :
                pass
            else:
                di = 3
          if event.key == pygame.K_DOWN:
              if di == 3:
                  pass
              else:
                  di = 4
          if event.key == pygame.K_RIGHT:
              if di == 2:
                  pass
              else:
                  di = 1
          if event.key == pygame.K_LEFT:
              if di == 1:
                  pass
              else:
                  di = 2
          if event.key == pygame.K_SPACE:
              gen_food()
              
                  
    if arrayx[-1] <= -.15:                   
       pygame.quit()
       sys.exit()
    if arrayx[-1]+snake_dim >= width+.15:
       pygame.quit()
       sys.exit()
    if arrayy[-1] <= -.15:                       ###### four Borders
        pygame.quit()
        sys.exit()
    if arrayy[-1]+snake_dim >= height+.15:
       pygame.quit()
       sys.exit()

       
  # Update.
  
  # Draw.
  
    pygame.display.flip()
    fpsClock.tick(fps)