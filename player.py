import pygame
import time
import math
class player:
    def __init__(self,playerimage):
        self.playerpos = [0,0]
        self.playerimage = playerimage #list
        self.playerhealth = 100
        for i in range(0,len(playerimage)):
            self.playerimage[i] = pygame.transform.scale(pygame.image.load(playerimage[i]),(300,300))
        self.imagenumber = 18 #캐릭터 이미지 변환용 변수
        self.isjump = 0
        self.speed =12
        self.velocity = 0
        self.pasttime = time.time()
        self.sequencenumright = 0
        self.sequencenumleft = 0
        self.itemlist = [] #사용자가 가지고 있는 아이템리스트
        self.questlist = [] #사용자가 가지고 있는 퀘스트리스트
        self.special = pygame.image.load("data/images/rudolph.png") #이스터에그
        self.specialdy = math.radians(0)
        self.specialpos = 'Right' #스페셜 캐릭터 배치
        
    def set_pos(self,surface,pos): #시작위치
        if pos == "Right":
            self.playerpos[0] = surface.get_width()//20*17
        elif pos == "Left":
            self.playerpos[0] = surface.get_width()//20
        elif pos == "Center":
            self.playerpos[0] = (surface.get_width()-300)//2
        self.playerpos[1] = surface.get_height()-400
        
            
    def Right(self): #오른쪽으로 움직임 
        self.playerpos[0] += self.speed
        self.specialpos = 'Right'
        
    def Left(self): #왼쪽으로 움직임 
        self.playerpos[0] -= self.speed
        self.specialpos = 'Left'
        
    def Jump(self):
        if self.isjump == 0 :
            self.isjump = 1
            self.velocity = -15
            
    def playerimageupdateright(self): #right 움직임
        playerimagesequenceright = [0,1,2,3,4,5,6,7,4,3]
        if time.time() - self.pasttime > 0.1:
            self.imagenumber = playerimagesequenceright[self.sequencenumright]
            self.sequencenumright += 1
            if self.sequencenumright > 9:
                self.sequencenumright = 0
            self.pasttime = time.time()
            
    def playerimageupdateleft(self): #left 움직임
        playerimagesequenceleft = [8,9,10,11,12,13,14,15,16,17]
        if time.time() - self.pasttime > 0.1:
            self.imagenumber = playerimagesequenceleft[self.sequencenumleft]
            self.sequencenumleft += 1
            if self.sequencenumleft > 9:
                self.sequencenumleft = 0
            self.pasttime = time.time()
    
    def gravity(self,groundrect): #중력작용
        
        if groundrect.collidepoint((self.playerpos[0],self.playerpos[1]+300)):
            #플레이어가 땅에 있다면
            self.velocity = 0
            while groundrect.collidepoint((self.playerpos[0],self.playerpos[1]+300)):
                self.playerpos[1]-=1
            self.isjump = 0
        else:
            self.velocity += 1  #떨어지는 속도 나중에 조절할 것 ,떨어짐
            
    def health(self):
        return self.playerhealth
    
    def iscollide(self,rect):
        #다른 물체와의 충돌감지
        #colliderect
        playerrect = self.playerimage[0].get_rect()
        if rect.colliderect(playerrect):
            return True
        else:
            return False
        
    def itemcheck(self):
        return self.itemlist

    def itemamount(self):
        return len(self.itemlist)

    def itemappend(self,itemnum): #itemnum = 아이템 고유번호
        self.itemlist.append(itemnum)

    def addquest(self, quest):
        self.questlist.append(quest)
        
        #questlist = [{'questname': q ,itemname:['a','b'] ,'complete':True},{},...]
    def checkquestcomplete(self):       
        for q in self.questlist:
            try:
                for i in q['itemname']:
                    self.itemlist.index(i)
                return q['questname']
            except:
                pass
                
    def playerpositon(self):
        pos = tuple(self.playerpos)
        return pos

    def returnquest(self):
        list = []
        for i in range(0,len(self.questlist)):
            list.append(self.questlist[i]['questname'])
        return list

    def get_specialitem(self):
        try:
            self.itemlist.index(14)
            return True
        except:
            return False
    
    def specialitem(self,surface):
        image = pygame.transform.scale(self.special,(70,70))
        self.specialdy += math.radians(1)
        #print(math.sin(self.specialdy))
        if self.specialpos  == 'Right':
            surface.blit(image,(self.playerpos[0]-70,self.playerpos[1]+100-30*math.sin(self.specialdy)))
        elif self.specialpos == 'Left':
            surface.blit(pygame.transform.flip(image,True,False),(self.playerpos[0]+300,self.playerpos[1]+100-30*math.sin(self.specialdy)))
        
    def update(self,surface):
        self.playerpos[1] +=self.velocity
        surface.blit(self.playerimage[self.imagenumber],self.playerpos)
        #print(self.playerpos)
'''
player1 = player(["data/images/player/mot2.png"])
print(player1.playerpositon())'''

