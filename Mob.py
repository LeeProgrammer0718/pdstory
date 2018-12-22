import math
import pygame

class Mob:
    def __init__(self,health,imageObject):
        self.health = health
        self.imageObject = imageObject
        self.health = 0
        self.colliderRange = 0

    #collider
    def setting(self,pos,questlist,itemnum):
        #questlist = None or list , itemnum --캐릭터에게 줄 아이템 이름 list형태로
        self.locationX = pos[0]
        self.locationY = pos[1]
        self.quest = questlist
        self.item = itemnum
        #다른거 사용하기전 무조건 실행
        
    def defineCollider(self,radius):
        self.colliderRange = radius
        
    def Collide(self,x,y):
        if not self.colliderRange == 0:
            if math.sqrt((self.locationX-x)**2+(self.locationY-y)**2)<self.colliderRange:
                return True
            else:
                return False
    #move
    def move(self, deltaX, deltaY):
        self.locationX += deltaX
        self.locationY += deltaY

    def setLocation(x,y):
        if not x == "N":
            self.locationX = x
        if not y == "N":
            self.locationY = y

    def givequest(self):
        return self.quest
    
    def giveitem(self):
        return self.item
    #damage
    
    def giveDamage(self, damage):
        health -= damage

    def setHealth(self, sethealth):
        health = sethealth
    
    #UPDATE
    def draw(self, surface):
        surface.blit(self.imageObject, (self.locationX,self.locationY))
        
    
