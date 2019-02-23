import pygame,sys,random

from pygame.locals import *

class Modle(object):

    def __init__(self,snakePosition = [320,400],snakeBody = [[320,400],[320,420],[320,440]],targetFlag = 1,targetPosition = [300,300]):
        self.snakePosition = snakePosition
        self.snakeBody = snakeBody
        self.targetPosition = targetPosition
        self.targetFlag = targetFlag

    #游戏结束
    @staticmethod
    def gameOver():
        pygame.quit()
        sys.exit()
    

    
    #移动蛇头坐标
    def MovesnakePosition(self,targetSize,direction):
        if direction == 'right':
            self.snakePosition[0] += targetSize
        if direction == 'left':
            self.snakePosition[0] -= targetSize
        if direction == 'up':
            self.snakePosition[1] -= targetSize
        if direction == 'down':
            self.snakePosition[1] += targetSize

    #增加蛇长度/蛇移动
    def IncSnake(self):
        self.snakeBody.insert(0,list(self.snakePosition))

    
    
    

            
    #死亡
    def death(self,resolutionX,resolutionY,targetSize):
        if self.snakePosition[0] > resolutionX-targetSize or self.snakePosition[0] < 0:
            Modle.gameOver()
        elif self.snakePosition[1] > resolutionY-targetSize or self.snakePosition[1] < 0:
            Modle.gameOver()
        i = 1
        while i < len(self.snakeBody):
            if self.snakePosition[0] == self.snakeBody[i][0] and self.snakePosition[1] == self.snakeBody[i][1]:
                Modle.gameOver() 
            i += 1

        

        #生成食物
    def FoodCreate(self,resolutionX,resolutionY,targetSize):
            if self.targetFlag == 0:
                j = 1
                k = 0
                while j == 1:
                    x = random.randrange(1,resolutionX/targetSize)  
                    y = random.randrange(1,resolutionY/targetSize) 
                    self.targetPosition = [int(x*targetSize),int(y*targetSize)]
                    while k < len(self.snakeBody):
                        if self.snakeBody[k][0] == self.targetPosition[0] and self.snakeBody[k][1] == self.targetPosition[1]:
                            j = 1
                            break
                        else:
                            j = 0
                        k += 1
            self.targetFlag = 1
    
    #吃东西
    def Eatfood(self):
        if self.snakePosition[0] == self.targetPosition[0] and self.snakePosition[1] == self.targetPosition[1]:
            self.targetFlag = 0
        else:
            self.snakeBody.pop()

    def get_Modledata(self):
        return self.snakeBody,self.targetPosition



class View(object):


    def __init__(self,resolutionX = 640,resolutionY = 480,targetSize = 20):
        self.resolutionX = resolutionX
        self.resolutionY = resolutionY
        self.targetSize = targetSize



    

    #标题
    def tittle(self):
        pygame.display.set_caption('贪吃蛇')

    #画蛇
    def snakeDraw(self,snakeBody,targetPosition):
        playSurface = pygame.display.set_mode((self.resolutionX,self.resolutionY))
        redColor = pygame.Color(255,0,0)
        whiteColor = pygame.Color(255,255,255)
        blackColor = pygame.Color(0,0,0)
        playSurface.fill(blackColor)
        for position in snakeBody:
            pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],self.targetSize,self.targetSize))
        pygame.draw.rect(playSurface,redColor,Rect(targetPosition[0],targetPosition[1],self.targetSize,self.targetSize))

    #更新显示
    def displayflip(self):
        pygame.display.flip()
    #刷新频率
    def FpsClock(self):
        fpsClock = pygame.time.Clock()
        fpsClock.tick(5)
    
    def get_Viewdata(self):
        return self.resolutionX,self.resolutionY,self.targetSize




class Controller(object):
    def __init__(self,direction = 'up',changeDirection = 'up'):
        self.direction = direction
        self.changeDirection = changeDirection
    #处理事件
    def Dealevent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                Modle.gameOver()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.changeDirection = 'right'
                if event.key == K_LEFT:
                    self.changeDirection = 'left'
                if event.key == K_UP:
                    self.changeDirection = 'up'
                if event.key == K_DOWN:
                    self.changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

    #确定方向
    def DirectionCheck(self):
        if self.changeDirection == 'left' and not self.direction == 'right':
            self.direction = self.changeDirection
        if self.changeDirection == 'right' and not self.direction == 'left':
            self.direction = self.changeDirection
        if self.changeDirection == 'up' and not self.direction == 'down':
            self.direction = self.changeDirection
        if self.changeDirection == 'down' and not self.direction == 'up':
            self.direction = self.changeDirection
    
    def get_Controllerdata(self):
        return self.direction,self.changeDirection
   





#入口函数
def main():
    #初始化
    pygame.init()
    M = Modle()
    V = View()
    C = Controller()



    

    
    #处理事件
    while True:
            C.Dealevent()
            C.DirectionCheck()
            V.tittle()
            M0 = M.get_Modledata()
            V0 = V.get_Viewdata()
            C0 = C.get_Controllerdata()
            M.MovesnakePosition(V0[2],C0[0])
            M.IncSnake()
            M.Eatfood()
            M.FoodCreate(V0[0],V0[1],V0[2])
            V.snakeDraw(M0[0],M0[1])
            V.displayflip()
            M.death(V0[0],V0[1],V0[2])
            V.FpsClock()


 #启动入口函数
if __name__ == '__main__':
    main()

            
            
            
