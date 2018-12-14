class player:
    def __init__(self,playerimage):
        self.playerpos = [0,0]
        self.playerimage = playerimage #list
        for i in range(0,len(playerimage)):
            self.playerimage[i] = pygame.image.load(playerimage[i])
        self.imagenumber = 0 #캐릭터 이미지 변환용 변수 
        self.speed = 2
        self.velocity = 0
        
    def Right(self): #오른쪽으로 움직임 
        self.playerpos[0] += self.speed

    def Left(self): #왼쪽으로 움직임 
        self.playpos[0] -= self.speed

    def Jump(self):
        self.velocity -= 50
    
    def gravity(self,groundrect): #중력작용
        playerrect=pygame.Rect(self.playerimage[self.imagenumber].get_rect())
        if playerrect.colliderect(groundrect):
            #플레이어가 땅에 있다면
            self.velocity = 0
        else:
            self.velocity += 5  #떨어지는 속도 나중에 조절할 것 ,떨어짐

        def update(self,surface):
            self.pos[1] +=velocity
            surface.blit(self.playerimage[self.playernumber],self.pos)
            
            
