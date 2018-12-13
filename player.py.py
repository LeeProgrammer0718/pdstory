import pygame
mapdata = [{"playerpos":"left"},{"playerpos":"right"},{"playerpos":"center"}]
#앙기모띠
i = 0
def playerpos(i):       #시작 위치 정하기
    global mapdata
    if mapdata[i]["playerpos"]=="left":      #left에서 시작
        return [0, 0]
    if mapdata[i]["playerpos"]=="right":     #right에서 시작
        return [2, 0]
    if mapdata[i]["playerpos"]=="center":    #center에서 시작
        return [1, 0]                       #y좌표는 0으로 시작

keys = [False, False]
pos = playerpos(i)   #player 시작 위치


def player():
    global pos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_UP:      # 점프 미완성
                dy = 10
                pos[1] += dy
                dy -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False

    if keys[0]:
            pos[0] += 5    #오른쪽으로 움직이기
    elif keys[1]:
            pos[0] -= 5    #왼쪽으로 움직이기
