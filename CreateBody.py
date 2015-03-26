################################################################################################################
# Package Imports                                                                                              #
################################################################################################################
from pickle import dump,load
from pygame.locals import *
from math import *
import pygame
import random
import math
import sys
import os

################################################################################################################
# Global Variable Definitions                                                                                  #
################################################################################################################
clock = pygame.time.Clock()
pygame.font.init()
particleList = []

# font initialization
GameOver = pygame.font.SysFont('Ariel', 140, bold=True, italic=False)
font = pygame.font.SysFont('Ariel', 80, bold=True, italic=False)

# Color Definitions
WHITE = (255, 255, 255)
GREY = (119, 136, 153)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen Size
screenWidth = 700
screenHeight = 700

# Find Screen Center
xCenter = screenWidth/2
yCenter = screenHeight/2

# Define the Screen
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Number of Particles
particleNumber = 100

# General Definitions of Variables
gravity = 5



################################################################################################################
# Class Definitions                                                                                            #
################################################################################################################

class Background():  # represents the player, not the game
    def __init__(self,color = WHITE,width = screenWidth,height = screenHeight):
        """ The constructor of the class """
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # the background's position
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

class Particle():  # represents the player, not the game
    def __init__(self,color,x,y,mass = 1,width = 4,height = 4):
        """ The constructor of the class """
        # self.image = pygame.draw.circle(screen,color,[x,y],radius,width=0)
        # the tile's position
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

    def locateX(self):
        if self.x < xCenter:
            # attraction must go right
            return 'right'
        elif self.x > xCenter:
            # attraction must go left
            return 'left'
        else:
            pass

    def locateY(self):
        if self.y < yCenter:
            # attraction must go down
            return 'down'
        elif self.y > yCenter:
            # attraction must go up
            return 'up'
        else:
            pass

    def centerAttraction(self):
        xAttract = self.locateX()
        yAttract = self.locateY()

        if yAttract == 'down':
            self.y +=1
        elif yAttract == 'up':
            self.y -=1
        else:
            pass

        if xAttract == 'right':
            self.x +=1
        elif xAttract == 'left':
            self.x -=1
        else:
            pass

    def particleAttraction(alist):
    	pass


class CenterOfMass():  # represents the player, not the game
    def __init__(self,x,y):
        """ The constructor of the class """
        # self.image = pygame.draw.circle(screen,color,[x,y],radius,width=0)
        # the tile's position
        self.x = x
        self.y = y

################################################################################################################
# Function Definitions                                                                                         #
################################################################################################################

def loadScores():
    filename = './scores.txt'
    data_file = open(filename,'r')
    scorelist = load(data_file)
    data_file.close()
    return scorelist

def saveScore(alist,blist,xtiles,ytiles):
    finalscore = findScore(blist,xtiles,ytiles)
    alist.append(finalscore)
    filename = './scores.txt'
    data_file = open(filename,'w')
    dump(scoreList,data_file)
    data_file.close()

def end_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() # quit the screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit() # quit the screen


def generateParticles(particlenumber,alist,isGameOver = False): # maybe add alist
    # this function generates the colored tiles that make up the game image
    for i in range(particlenumber):
    	
    	particle = Particle(BLACK,0,0)
        particle.x = random.randrange(screenWidth)
        particle.y = random.randrange(screenHeight)
        
        particle.draw(screen)
        alist.append(particle)

def drawAllParticles(alist):
    for particle in alist:
        particle.centerAttraction()
        particle.draw(screen)

    # for col in range(xtiles):
    #     for row in range(ytiles):
    #         baseColor = (WHITE)
    #         # create base tile
    #         tile = Tile(baseColor, width, height, 0, 0, alist[col][row])
    #         # get new tile info
    #         c = tile.getColor(isGameOver)
    #         x = xspace*col + width*col + xspace
    #         y = yspace*row + height*row + yspace
    #         # create new tile
    #         newtile = Tile(c, width, height, x, y, alist[row][col])
    #         # print the tile
    #         newtile.draw(screen)
    #         tile.showValue(x,y,width,height)
    #         # tileList.append(newtile)


################################################################################################################
# Main Loop                                                                                                    #
################################################################################################################

if __name__ == "__main__":
    background = Background()
    generateParticles(particleNumber,particleList)
    while True:
        background.draw(screen)
        drawAllParticles(particleList)
        pygame.display.flip()
        end_game()
        clock.tick(10)