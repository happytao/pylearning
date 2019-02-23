import pygame,sys,random

from pygame.locals import *
# 颜色
redColor = pygame.Color(255,0,0)
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)

# 游戏结束
def gameOver():
    pygame.quit()
    sys.exit()

#入口函数
def main():
    #初始化
    pygame.init()

    #速度
    fpsColck = pygame.time.Clock()

    #显示层
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('贪吃蛇')

    #初始化变量
    snakePosition = [320,400]
    snakeBody = [[320,400],[320,420],[320,440]]
    targetPosition = [300,300]
    targetFlag = 1
    direction = 'up'
    changeDirection = direction

    #处理事件
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                gameOver()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
            
            #确定方向
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

            #移动蛇头坐标
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

            #增加蛇长度/蛇移动
        snakeBody.insert(0,list(snakePosition))   

            #吃东西
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetFlag = 0
        else:
            snakeBody.pop()

            #生成食物
        if targetFlag == 0:
            j = 1
            k = 0
            while j == 1:
                    x = random.randrange(1,32)  
                    y = random.randrange(1,24) 
                    targetPosition = [int(x*20),int(y*20)]
                    while k < len(snakeBody):
                        if snakeBody[k][0] == targetPosition[0] and snakeBody[k][1] == targetPosition[1]:
                            j = 1
                            break
                        else:
                            j = 0
                        k += 1
            targetFlag = 1
            
            #显示层
        playSurface.fill(blackColor)
        print(type(snakeBody))
        for position in snakeBody:
            pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20))
        pygame.draw.rect(playSurface,redColor,Rect(targetPosition[0],targetPosition[1],20,20))

            #更新显示
        pygame.display.flip()

            #死亡
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver()
        i = 1
        while i < len(snakeBody):
            if snakePosition[0] == snakeBody[i][0] and snakePosition[1] == snakeBody[i][1]:
                gameOver() 
            i += 1
            
            
        fpsColck.tick(5)


 #启动入口函数
if __name__ == '__main__':
    main()

            
            
            
