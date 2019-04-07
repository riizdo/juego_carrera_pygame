import pygame, sys

class Game():
    
    runners = []
    __starLine = 20
    __finishLine = 620
    
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        self.__screen.fill((0, 255, 0))
        self.__background = pygame.image.load("imagenes/background.png")
        pygame.display.set_caption("Carreras de pygame")
        
        
    def competir(self):
        
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.__screen.blit(self.__background, (0, 0))
            
            pygame.display.flip()
            
        
if __name__ == '__main__':
    
    game = Game()
    pygame.init()
    game.competir()