import math
import pygame

class Mob:
    self.locationX = 0
    self.locationY = 0
    self.health = 0
    self.imageObject = None

    self.colliderRange = 0
    def __init__(self, x, y, health, imageObject):
        self.locationX = x
        self.locationY = y
        self.health = health
        self.imageObject = imageObject

    #collider
    def defineCollider(self,radius):
        self.colliderRange = radius
        
    def isCollide(self,x,y):
        if not colliderRange = 0:
            if math.sqrt((locationX-x)**2+(locationY-y)**2))<colliderRange:
                return True
            else: False

    #move
    def move(self, deltaX, deltaY):
        self.locationX += deltaX
        self.locationY += deltaY

    def setLocation(x,y):
        if not x == "N":
            self.locationX = x
        if not y == "N":
            self.locationY = y
    
    #damage
    def giveDamage(self, damage):
        health -= damage

    def setHealth(self, sethealth):
        health = sethealth
    
    #UPDATE
    def draw(self, surface):
        surface.blit(imageObject, (locationX,locationY))
        
    
