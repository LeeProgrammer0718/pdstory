import pygame ,sys
import os
import random
pygame.init()
pygame.display.set_caption("PungDuck  Bowl Story")
width,height = 500,500
surface = pygame.display.set_mode((width,height),pygame.RESIZABLE)
soundfile = os.listdir('data/sounds') #사운드파일 불러옴

mapdata = [{"background":"테스트.jpg","playerpos":"","Item":[],"mob":""}]

def Text():
    pass

def imagebutton(surface,image,size,pos): #image-->이미지 주소 data/images/... ,size ->(width,height)
    buttonimage = pygame.image.load(image)
    buttonimage = pygame.transform.scale(buttonimage,size)
    surface.blit(buttonimage,pos)
    mousepos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos[0]<mousepos[0]<pos[0]+size[0] and pos[1]<mousepos[1]<pos[1]+size[1]:
        if click[0] == 1:
            return True
    else:
        return False

def LoadingBar(surface,num,pos,size):
    #파일 검사용 로딩바
    if num<101:
        try:
            if num<50:
                os.listdir('data/sounds') 
        except:
            if num<50:
                print("사운드파일을 찾을 수 없음")
                num=10
            
    else:
        return True
    pygame.draw.rect(surface,(255,255,255),(pos,size),2)
    pygame.draw.rect(surface,(255,255,255),(pos,(0+size[0]//100*num,size[1])),0)

def START(): #시작 화면 , 파일 검사 
    global surface,width,height
    num = 0
    while True:
        pygame.time.delay(60)
        width = surface.get_width()
        height = surface.get_height()
        logo = pygame.image.load("data/images/logoblack.png")
        logo = pygame.transform.scale(logo,(width//5,width//5))
        surface.blit(logo,(width//2-width//10,height//2-height//6))
        num += random.random()*10
        if LoadingBar(surface,num,((width-width//5*3)//2,height-height//10),(width//5*3,20)):
            print("finish")
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        pygame.display.update()
    return True

def MainActivate(mapnum):
    end = 0
    global surface,width,height,mapdata
    nextnum = 0 # +1 혹은 -1만 올 수 있다. --> +1:다음맵 -1: 이전맵
    stop = False #게임 일시정지 변수 
    while True:
        pygame.time.delay(60)
        width = surface.get_width()
        height = surface.get_height()
        surface.fill((250,250,250))
        '''
        게임 메인구성 
        '''
        try:
            background = pygame.image.load("data/images/{}".format(mapdata[mapnum]["background"])) #배경사진 불러옴 
            background = pygame.transform.scale(background,(width,height)) #가변창의 크게에 맞추기 위한 조정 
            surface.blit(background,(0,0))
        except:
            print("error:: data/images/{} 배경을 가져올 수 없음 ".format(mapdata[mapnum]["background"]))
        if imagebutton(surface,"data/images/stop.png",(width//15,width//15),(width-width//15-width//30,0)): #정지버튼 
            stop = True
        else:
            stop = False
        if stop:
            #일시정지
            print("일시정지")
            pass
        else:
            #움직임 관련 코드는 모두 이 안에 넣으세요
            print("작동중 ")
            pass
        '''
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        pygame.display.update()
        
        if end == 1:
            break
        
    if mapnum+nextnum == "**": #**-->마지막 맵번호 +1
       return
    else:
        MainActivate(mapnum+nextnum)

def main():
    START()
    MainActivate(0)

if __name__ == "__main__":
    main()
