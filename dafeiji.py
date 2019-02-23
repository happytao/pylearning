import pygame,sys,random

from pygame.locals import *

#颜色
whiteColor = pygame.Color(255,255,255)
mikuColor = pygame.Color(102,255,204)
redColor = pygame.Color(255,0,0)
blueColor = pygame.Color(0,255,0)
greenColor = pygame.Color(0,0,255)

def gameOver():
    pygame.quit()
    sys.quit()

def main():
    #初始化
    pygame.init()
    #速度
    fpsClock = pygame.time.Clock()
    #显示层
    playSurface = pygame.display.set_mode((1280,960))
    pygame.display.set_caption('打灰机')
    #初始化变量
    planePosition1 = [640,800]
    planeBody = [[620,800],[630,800],[640,800],[650,800],[660,800],[630,790],[640,790],[650,790],[640,780],[640,810]]
    enemyNumber = 0
    shootFlag = 0
    rightMoveFlag = 0
    leftMoveFlag = 0
    upMoveFlag = 0
    downMoveFlag = 0

while True:
       for event in game.event.get():
           if event.type == QUIT:
               gameOver()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    rightMoveFlag = 1
                if event.key == K_LEFT:
                    leftMoveFlag = 1
                if event.key == K_UP:
                    upMoveFlag = 1
                if event.key == K_DOWN:
                    downMoveFlag = 1
                if event.key == K_x:
                    shootFlag == 1
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        
        #移动飞机
        if rightMoveFlag == 1:
            for i from range(len(planeBody)):
                planeBody[i][0] += 10
        if leftMoveFlag == 1:
            for i from range(len(planeBody)):
                planeBody[i][0] -= 10
        if upMoveFlag == 1:
            for i from range(len(planeBody)):
                planeBody[i][1] -= 10
        if downMoveFlag == 1:
            for i from range(len(planeBody)):
                planeBody[i][1] += 10
        
        #生成敌人
        if enemyNumber <= 5:
            j = random(1,5)
            enemyNumber += j
            while j < 0:
                i = 0
                enemyPosition[i] = [random(1,126),20]
                enemyBody[i] = [enemyPosition[i],[enemyPosition[i][0],enemyPosition[i][1]-10],[enemyPosition[i][0]-10,enemyPosition[i][1]-10]]                             
                i += 1
                j -= 1

        #敌人移动










    