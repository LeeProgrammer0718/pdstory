import pygame ,sys 
import player as play
import os
import random
import scrollbar
import player
import MOB
pygame.init()
pygame.display.set_caption("PungDuck  Bowl Story")
width,height = 500,500
surface = pygame.display.set_mode((width,height),pygame.RESIZABLE)
soundfile = os.listdir('data/sounds') #사운드파일 불러옴
volume = 50 #소리값
FPS = 60
FPSCLOCK=pygame.time.Clock()
questimage = pygame.image.load("data/images/questimage.jpg")
First = True #처음시작시 

musicrun = pygame.mixer.Sound("data/sounds/footsteps(3).wav")

mapdata = [{"mapname":'1층 복도끝',"background":"1Fleft4.jpg","playerpos":"Left","Item":[],"mob":{}},\
           {"mapname":'1층 엘리베이터',"background":"1Fleft2-1.jpg","playerpos":"Left","Item":[],"mob":{"mobname":"mob1","mobitem":[],"mobquest":{'questname':"승호어리바리 없애기","itemname":[0],'complete':False,'pass':False},"mobstartpos":(10,10)}},\
           {"mapname":'1-3반 교실복도',"background":"1Fleft2.jpg","playerpos":"Left","Item":[],"mob":{}},\
           {"mapname":'1-4반 교실복도',"background":"1Fleft1.jpg","playerpos":"Left","Item":[(14,(100,100))],"mob":{}},\
           {"mapname":'중앙홀',"background":"1FHome.jpg","playerpos":"Center","Item":[(0,(10,10)),(2,(100,100)),(6,(200,200))],"mob":{}},\
           {"mapname":'교장실 복도',"background":"1Fright1.jpg","playerpos":"Center","Item":[(0,(10,10)),(2,(100,100)),(6,(200,200))],"mob":{}},\
           {"mapname":'보건실 복도',"background":"1Fright2.jpg","playerpos":"Center","Item":[(0,(10,10)),(2,(100,100)),(6,(200,200))],"mob":{}},\
           {"mapname":'복도',"background":"background3.jpg","playerpos":"Right","Item":[(0,(10,10)),(2,(100,100)),(6,(200,200))],"mob":{}}] #item :(아이템고유번호,(x,y))


itemimagelist = ['ball','fish1','fish2','fish3','fish4','water','shoes','pill',\
                 'bucket','glass','cristar','cristar2','cristar3','cristar4','rudolphmark'] #아이템 고유번호가 인덱스번호
itemimage =[]
itemname = {'ball':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'fish1':['마법의 공','상대방을 치료한다']\
                    ,'rudolphmark':['루돌프의 혼','쿠키를 얻을 수 있다!!']} #아이템 한글이름
for i in range(0,len(itemimagelist)):
    itemimage.append(pygame.image.load("data/images/items/{}.jpg".format(itemimagelist[i]))) #아이템 이미지들 불러옴
#아이템이미지는 아이템이름으로 저장

player1 = play.player(["data/images/player/mot2.png","data/images/player/mot3.png","data/images/player/mot4.png",\
                           "data/images/player/mot5.png","data/images/player/mot6.png","data/images/player/mot7.png",\
                           "data/images/player/mot8.png","data/images/player/mot9.png","data/images/player/o1.png",\
                           "data/images/player/o2.png","data/images/player/o3.png","data/images/player/o4.png",\
                           "data/images/player/o5.png","data/images/player/o6.png","data/images/player/o7.png",\
                           "data/images/player/o8.png","data/images/player/o9.png","data/images/player/o10.png",\
                           "data/images/player/stop motion1.png","data/images/player/stop motion2.png"])
moborder = ['mob1']
mobnames = ['mob1']
mobimages= ['mob1']

for i in range(0,len(mobimages)):
    mobimages[i] = pygame.image.load("data/images/mob/{}.png".format(mobimages[i]))
    
for i in range(0,len(mobnames)):
    mobnames[i] = MOB.Mob(100,mobimages[i])

def text(surface,TEXT,COLOR,SIZE,POS):
    pygame.font.init()
    #try:
        #font = pygame.font.Font(None,SIZE)
    #except:
    font = pygame.font.Font("data/font/Binggrae_font/BinggraeTaom.ttf",SIZE)
    text = font.render(TEXT,False,COLOR)
    surface.blit(text,POS)
    
def textsize(TEXT,SIZE):
    font = pygame.font.Font("data/font/Binggrae_font/BinggraeTaom.ttf",SIZE)
    fontsize = font.size(TEXT)
    return fontsize

def itemexbox(surface,itemnum,POS,SIZE): #아이템 명과 설명
    global itemimage,itemname
    pygame.draw.polygon(surface, (0,0,0), ((POS[0], POS[1]), (POS[0] + SIZE[0], POS[1]), \
                                                   (POS[0] + SIZE[0], POS[1] + SIZE[1]), (POS[0], POS[1] + SIZE[1])), 0)
    pygame.draw.polygon(surface, (255, 255, 255), ((POS[0], POS[1]), (POS[0] + SIZE[0], POS[1]), \
                                                   (POS[0] + SIZE[0], POS[1] + SIZE[1]), (POS[0], POS[1] + SIZE[1])), 2)
    fontsize = textsize(itemname[itemimagelist[itemnum]][0],SIZE[1]//4)
    fontsize2 = textsize(itemname[itemimagelist[itemnum]][1],SIZE[1]//4)
    text(surface,itemname[itemimagelist[itemnum]][0],(255,255,255),SIZE[1]//4,POS)
    text(surface,itemname[itemimagelist[itemnum]][1],(255,255,255),SIZE[1]//4,(POS[0],POS[1]+fontsize[1]))

def imagebutton(surface,image,size,pos,itemnum): #image-->이미지 로드한 것 ,아이템 설명전용
    buttonimage = image
    buttonimage = pygame.transform.scale(buttonimage,size)
    surface.blit(buttonimage,pos)
    mousepos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos[0]<mousepos[0]<pos[0]+size[0] and pos[1]<mousepos[1]<pos[1]+size[1]:
        itemexbox(surface,itemnum,(pos[0],pos[1]-size[1]*2),(surface.get_width()//6,80))
        if itemnum != None:
            pass
        #text(surface,itemimagelist[itemnum],(0,0,0),size[1]//3,(pos[0],pos[1]+size[1]//3*2))
        if click[0] == 1:
            return True
    else:
        return False


def itembutton(surface,pos,radius): #아이템 선택할 수 있는 반경
    mousepos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos[0]-10<mousepos[0]<pos[0]+radius and pos[1]-10<mousepos[1]<pos[1]+radius:
        #text(surface,TEXT,COLOR,SIZE,POS)
        if click[0] == 1:
            return True

def findbutton(surface,pos,radius,hint): #계단 탐색및 엘리베이터 탐색버튼
    mousepos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos[0]-10<mousepos[0]<pos[0]+radius and pos[1]-10<mousepos[1]<pos[1]+radius:
        #text(surface,TEXT,COLOR,SIZE,POS)
        if click[0] == 1:
            return True

def textbutton(surface,TEXT,SIZE,POS):
    font = pygame.font.Font("data/font/startfont.ttf",SIZE[1]//2)
    fontsize = font.size(TEXT)
    mousepos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if POS[0]<mousepos[0]<POS[0]+SIZE[0] and POS[1]<mousepos[1]<POS[1]+SIZE[1]:
        pygame.draw.polygon(surface,(255,255,255),((POS[0],POS[1]),(POS[0]+SIZE[0],POS[1]),(POS[0]+SIZE[0],POS[1]+SIZE[1]),(POS[0],POS[1]+SIZE[1])),0)
        text = font.render(TEXT,False,(0,0,0))
        if click[0] == 1:
            return True
    else: 
        pygame.draw.polygon(surface,(255,255,255),((POS[0],POS[1]),(POS[0]+SIZE[0],POS[1]),(POS[0]+SIZE[0],POS[1]+SIZE[1]),(POS[0],POS[1]+SIZE[1])),5)
        text = font.render(TEXT,False,(255,255,255))
    surface.blit(text,(POS[0]+(SIZE[0]-fontsize[0])//2,POS[1]+(SIZE[1]-fontsize[1])//2))

def itembox(surface,itemlist):#가지고 있는 아이템 표현
    global itemimagelist,itemimage
    dx = 0
    width = surface.get_width()
    height = surface.get_height()
    for i in itemlist:
        imagebutton(surface,itemimage[i],(surface.get_width()//30,surface.get_width()//30),(surface.get_width()//4+dx, surface.get_height()-40-width//20),i)
        '''item = pygame.transform.scale(itemimage[i],(surface.get_width()//30,surface.get_width()//30))
        surface.blit(item,(surface.get_width()//4+dx, surface.get_height()-40-width//20))'''
        dx += surface.get_width()//25


def Item_draw(surface,mapnum): # 아이템 화면그리기+아이템선택
    item_num = len(mapdata[mapnum]['Item']) # 아이템 개수 세기
    for j in range(0, item_num): # 아이템 개수 만큼 반복하여 그림
        if itembutton(surface,mapdata[mapnum]['Item'][j][1],30):
            itemnumber = mapdata[mapnum]['Item'][j][0]
            del(mapdata[mapnum]['Item'][j]) #아이템 주으면 없애기
            return itemnumber #아이템 고유번호 리턴
    




def questbox(surface,questlist):
    #quest당 텍스트 한 줄만 허용
    #최대 5개
    dy = 0
    global questimage
    questimage = pygame.transform.scale(questimage,(surface.get_width()//3,surface.get_height()//3))
    surface.blit(questimage,(50,surface.get_height()//3*2-50))
    text(surface,"QUEST",(0,0,0),surface.get_height()//27,(60,surface.get_height()//3*2-45))
    for i in range(0,len(questlist)):
        dy += height//25
        text(surface,"{}.".format(i+1)+questlist[i],(0,0,0),surface.get_height()//30,(60,surface.get_height()//3*2-45+dy))


def mapnameblock(surface,mapname):
    text(surface,mapname,(255,255,255),surface.get_width()//35,(0,0))
            
def healthbar(surface,pos,size,health,maximumhealth):
    color = [255,255,255]
    if health/maximumhealth < 0.2:
        color = [255,0,0]
    elif 0.2<= health/maximumhealth <0.5:
        color = [242,150,97]
    else:
        color = [188,229,92]
    pygame.draw.rect(surface,color,(pos,(0+size[0]//maximumhealth*health,size[1])),0)   
    pygame.draw.rect(surface,(255,255,255),(pos,size),2)


def ground(surface,height): #height == ground 높이
    ground = pygame.Rect(-200,surface.get_height()-height,surface.get_width()+400,height)
    #pygame.draw.rect(surface,(0,0,0),ground,0)
    return ground #땅 함수

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

def STOPSCREEN(surface):
    global volume
    pygame.draw.polygon(surface,(0,0,0),((0,0),(surface.get_width(),0),(surface.get_width(),surface.get_height()),(0,surface.get_height())),0)
    text(surface,"소리설정",(255,255,255),surface.get_width()//30,(0,0))
    text(surface,str(volume),(255,255,0),surface.get_width()//25,(surface.get_width()//25,surface.get_width()//30))
    minusbutton = True
    plusbutton = True
    if textbutton(surface,"-",(surface.get_width()//25,surface.get_width()//25),(0,surface.get_width()//30)):
        if minusbutton: #한번에 여러번 작동하는거 처리하기
            if volume-5>=0: #볼륨 최솟값:0
                volume -= 5
            minusbutton = False

    if textbutton(surface,"+",(surface.get_width()//25,surface.get_width()//25),(surface.get_width()//25+surface.get_width()//25+10,surface.get_width()/30)):
        if plusbutton: #한번에 여러번 작동하는거 처리하기
            if volume+5<=100: #볼륨 최댓값:100
                volume += 5
            plusbutton = False

    if textbutton(surface,'뒤로가기',(surface.get_width()//3,70),(surface.get_width()//3*2-30,surface.get_height()-80)):
        return True

def DEVELOPER(surface): 
    global volume
    pygame.draw.polygon(surface,(0,0,0),((0,0),(surface.get_width(),0),(surface.get_width(),surface.get_height()),(0,surface.get_height())),0)
    text(surface,'총책임자: 이재호 ',(255,255,255),surface.get_width()//30,(0,0))
    text(surface,'기획: 김태현 ',(255,255,255),surface.get_width()//30,(0,surface.get_width()//30+10))
    text(surface,'개발자들: 안세혁,이승호,신승호,나태건,김윤중,전대현,임주환,이성학',(255,255,255),surface.get_width()//30,(0,surface.get_width()//15+20))
    text(surface,'디자인: 한정은,임유경 ',(255,255,255),surface.get_width()//30,(0,surface.get_width()//15*2+15))
    text(surface,'사운드: 최영훈,이응도,신현서',(255,255,255),surface.get_width()//30,(0,surface.get_width()//15*3+10))
    if textbutton(surface,'뒤로가기',(surface.get_width()//3,70),(surface.get_width()//3*2-30,surface.get_height()-80)):
        return True

def START(): #시작 화면 , 파일 검사
    global surface,width,height
    num = 0
    while True:
        pygame.time.delay(20)
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

def DarkText(text1): #검은화면에 텍스트만 나타낼 시 사용 ,text =['안녕','하세요', ...] 스페이스 바 누를 시 넘겨짐
    global surface
    textnum = 0
    while True:
        FPSCLOCK.tick(FPS)
        width = surface.get_width()
        height = surface.get_height()
        surface.fill((0,0,0))

        try:
            text(surface,text1[textnum],(255,255,255),width//30,(width/2-(textsize(text1[textnum],width//30)[0])/2, height/2-(textsize(text1[textnum],width//30)[1])/2))
        except:
            break
        size = textsize('스페이스바를 눌러 다음으로 진행',width//60)
        text(surface,'스페이스바를 눌러 다음으로 진행',(200,200,200),width//60,((width-size[0])//2,height-size[1]))       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    textnum += 1
        pygame.display.update()

    return True

def STARTSCREEN():
    global surface,FPS,volume
    pygame.font.init()
    setting = False
    pygame.mixer.init()
    pygame.mixer.music.load('data/sounds/05. School.wav')
    pygame.mixer.music.set_volume(volume*0.01)
    try:
        pygame.mixer.music.play(0)
    except:
        print("오디오장치를 연결해주세요")
    background = pygame.image.load("data/images/background/startscreen.jpg")
    width = surface.get_width()
    height = surface.get_height()
    beforewidth = width
    beforeheight = height
    while True:
        FPSCLOCK.tick(FPS)
        width = surface.get_width()
        height = surface.get_height()
        if beforewidth != width or beforeheight != height: #화면 해상도 변경시 이미지 재로드
            background = pygame.image.load("data/images/background/startscreen.jpg") #배경사진 불러옴
        background = pygame.transform.scale(background,(width,height)) #가변창의 크게에 맞추기 위한 조정
        surface.blit(background,(0,0))
        fontsize = width//10
        font = pygame.font.Font("data/font/startfont.ttf",fontsize)
        text = font.render('풍',False,(255,255,255))
        text2 = font.render('덕',False,(255,255,255))
        text3 = font.render('고',False,(255,255,255))
        text4 = font.render('어',False,(255,255,255))
        text5 = font.render('항',False,(255,255,255))
        text6 = font.render('이',False,(255,255,255))
        text7 = font.render('야',False,(255,255,255))
        text8 = font.render('기',False,(255,255,255))
        surface.blit(text,(width//50,20))
        surface.blit(text2,(width//50,20+fontsize))
        surface.blit(text3,(width//50,20+fontsize*2))
        surface.blit(text4,(width//50+fontsize,20))
        surface.blit(text5,(width//50+fontsize,20+fontsize))
        surface.blit(text6,(width//50+fontsize*2,20))
        surface.blit(text7,(width//50+fontsize*2,20+fontsize))
        surface.blit(text8,(width//50+fontsize*2,20+fontsize*2))
        if textbutton(surface,'시작하기',(width//3,70),(width-width//3-30,height-height//2)):
            return 0
        if textbutton(surface,'개발자들',(width//3,70),(width-width//3-30,height-height//3)):
            if setting == False:
                setting = True
        if setting == True:
            if DEVELOPER(surface):
                setting = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        beforewidth = width
        beforeheight = height
        pygame.display.update()
        
    return True

def MainActivate(mapnum):
    end = 0
    global surface,width,height,mapdata,FPS,player1,mobnames,mobimages,moborder
    nextnum = 0 # +1 혹은 -1만 올 수 있다. --> +1:다음맵 -1: 이전맵
    stop = False #게임 일시정지 변수
    stopscreen = False #StopScreen보일지 결정
    key = [False,False,False,False,False] #Right,Left,Jump,QUESTbutton,Stopbutton
    keybefore = [False, False] #이전 상태 확인 Right, Left
    itemkey = [False,False,False,False,False,False,False,False,False,False]
    stopnum = 0 # 정지버튼 한번 누름 :0 두번누름:1
    background = pygame.image.load("data/images/background/{}".format(mapdata[mapnum]["background"])) #배경사진 불러옴
    beforewidth = width
    beforeheight = height

    player1.set_pos(surface,mapdata[mapnum]['playerpos'])
    mobis = False
    if mapdata[mapnum]['mob'] == {}:
        #몹 없음
        mobis = False
    else:
        mobnames[moborder.index(mapdata[mapnum]['mob']['mobname'])].setting(mapdata[mapnum]['mob']['mobstartpos'],\
                                                                             mapdata[mapnum]['mob']['mobquest'],\
                                                                             mapdata[mapnum]['mob']['mobitem'])
        mobis = True
    while True:
        pygame.mixer.music.set_volume(volume*0.01)
        FPSCLOCK.tick(FPS)
        width = surface.get_width()
        height = surface.get_height()
        surface.fill((250,250,250))
        '''
        게임 메인구성
        '''
        try:
            if beforewidth != width or beforeheight != height: #화면 해상도 변경시 이미지 재로드
                background = pygame.image.load("data/images/background/{}".format(mapdata[mapnum]["background"])) #배경사진 불러옴
            background = pygame.transform.scale(background,(width,height)) #가변창의 크게에 맞추기 위한 조정
            surface.blit(background,(0,0))
        except:
            print("error:: data/images/background/{} 배경을 가져올 수 없음 ".format(mapdata[mapnum]["background"]))
        
        if stop:
            #일시정지
            pass
        else:
            #움직임 관련 코드는 모두 이 안에 넣으세요
            plusitemnum=Item_draw(surface,mapnum) #사용자가 아이템 클릭시 아이템추가
            
            if plusitemnum != None:
                if player1.itemamount()<11:
                    player1.itemappend(plusitemnum) #사용자 아이템변수에 아이템 추가

            if key[0]:
                player1.Right()
                keybefore[0] = True
                player1.playerimageupdateright()
            if key[1]:
                player1.Left()
                keybefore[1] = True
                player1.playerimageupdateleft()
            if key[2]:
                player1.Jump()
                #print("Jump")

            else:
                if keybefore[0] and not key[0]:
                    player1.imagenumber = 18
                    keybefore[0] = False
                if keybefore[1] and not key[1]:
                    player1.imagenumber = 19
                    keybefore[1] = False
            player1.gravity(ground(surface,100)) #중력 작용 
            #print(ground(surface,100))
            player1.update(surface) #플레이어 그리기

            if player1.get_specialitem():
                player1.specialitem(surface)

            if mobis: #몹 동작
                mobnames[moborder.index(mapdata[mapnum]['mob']['mobname'])].draw(surface)
                mobnames[moborder.index(mapdata[mapnum]['mob']['mobname'])].defineCollider(300)
                if mobnames[moborder.index(mapdata[mapnum]['mob']['mobname'])].Collide(player1.playerpositon()[0],player1.playerpositon()[1]):
                    #몹과 플레이어가 닿을 때
                    if not mapdata[mapnum]['mob']['mobquest']['pass']:
                        player1.addquest(mapdata[mapnum]['mob']['mobquest'])
                        mapdata[mapnum]['mob']['mobquest']['pass'] = True
            #print("작동중 ")

        mapnameblock(surface,mapdata[mapnum]['mapname'])

                
        #pygame.draw.rect(surface,(0,0,0),(width//20*19,0,width//15,height),0)
        
        if width//20*19<player1.playerpositon()[0]:
            end = 1
            nextnum = 1
            mapdata[mapnum+nextnum]['playerpos'] = "Left"

        if player1.playerpositon()[0]<width//40:
            if mapnum != 0:
                end = 1
                nextnum = -1
                mapdata[mapnum+nextnum]['playerpos'] = "Right"

        healthbar(surface, (width // 4, height - 40), (width // 2, 30), player1.health(), 100)  # 체력바 그리기
        itembox(surface, player1.itemcheck())  # 아이템박스 뛰움

        if key[3]:  # Q 누르면 퀘스트 박스 보이기
            questbox(surface,player1.returnquest())

        if textbutton(surface, "||", (width // 20, width // 20), (width * 19 // 20, 0)) or key[4]:
            stop = True
            stopscreen = True  # 멈춤버튼

        if stopscreen:
            if STOPSCREEN(surface):
                stopscreen = False
                stop = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    key[0] = True
                if event.key == pygame.K_a:
                    key[1] = True
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    musicrun.play(-1)
                if event.key == pygame.K_w:
                    key[2] = True
                if event.key == pygame.K_q:
                    key[3] = True
                if event.key == pygame.K_z:
                    key[4] = True
                if event.key == pygame.K_1:
                    itemkey[0]=True
                if event.key == pygame.K_2:
                    itemkey[1]=True
                if event.key == pygame.K_3:
                    itemkey[2]=True
                if event.key == pygame.K_4:
                    itemkey[3]=True
                if event.key == pygame.K_5:
                    itemkey[4]=True
                if event.key == pygame.K_6:
                    itemkey[5] = True
                if event.key == pygame.K_7:
                    itemkey[6] = True
                if event.key == pygame.K_8:
                    itemkey[7] = True
                if event.key == pygame.K_9:
                    itemkey[8] = True
                if event.key == pygame.K_0:
                    itemkey[9]= True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    key[0] = False
                if event.key == pygame.K_a:
                    key[1] = False
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    musicrun.stop()
                if event.key == pygame.K_w:
                    key[2] = False
                if event.key == pygame.K_q:
                    key[3] = False
                if event.key == pygame.K_z:
                    key[4] = False
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        pygame.display.update()
        beforewidth = width
        beforeheight = height
        if end == 1:
            break

    if mapnum+nextnum == "**": #**-->마지막 맵번호 +1
        return
    else:
        MainActivate(mapnum+nextnum)
        
def main():
    START()
    STARTSCREEN()
    pygame.mixer.init()
    pygame.mixer.music.load('data/sounds/02. Normal_Day_at_School.wav')
    pygame.mixer.music.set_volume(volume*0.01)
    try:
        pygame.mixer.music.play(-1)
    except:
        print("오디오장치를 연결해주세요")
    if First:
        DarkText(['무슨 소리가 났다','뭐지','일단 계단쪽으로 가보자'])
    MainActivate(4)

if __name__ == "__main__":
    main()
