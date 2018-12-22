import pygame

class scrollbar:
    def __init__(self,size,pos,maximum,startnum):
        self.size = size
        self.pos = pos
        self.len = startnum
        self.maximum = maximum #사용자가 원하는 최대값 
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,(self.pos,self.size),3)
        pygame.draw.rect(surface,color,(self.pos,(self.pos[0]+self.len,self.size[1])),0)
        
    def detect(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.pos[0]<mouse[0]<self.pos[0]+self.size[0] and self.pos[1]<mouse[1]<self.pos[1]+self.size[1]:
            if click[0] == 1:
                if self.len <self.size[0]:
                    self.len = mouse[0] - self.pos[0]
    def result(self): #사용자 설정결과 출력 
        return self.maximum/self.size[0]*self.len

 
