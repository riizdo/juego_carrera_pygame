import pygame, sys

class Game():
    
    corredores = []
    
    
    def __init__(self):
        
        pygame.init()#inicializacion de pygame
        #creamos la pantalla con medidas en tupla
        self.__screen = pygame.display.set_mode((640, 480))
        #pondriamos color de fondo con rgb
        #self.__screen.fill(255, 0, 0)
        #ponemos nombre en la ventana
        pygame.display.set_caption("Carrera")
        #ponemos imagen en el fondo de la pantalla
        self.background = pygame.image.load("imagenes/background.png")
        
        #ponemos imagen en un atributo 
        self.runner = pygame.image.load("imagenes/prueba.png")
        
        
        
    def competir(self):
        
        x = 0
        ganador = False
        
        while not ganador:
            #comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            #refrescas pantalla
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runner, (x, 240))
            #refrescamos la pantalla
            pygame.display.flip()
            
            x += 3
            if x >= 630:
                ganador = True
                
        #al terminar el programa cerramos la pantalla y python        
        pygame.quit()
        sys.exit()
            
            
if __name__ == '__main__':
    game = Game()
    game.competir()