import pygame, sys
from pygame.locals import *



class Termometro():
    def __init__(self):
        self.__custome = pygame.image.load("imagenes/termometro.png")
        
        
    def imagen(self):
        return self.__custome
    
        
        
class Selector():
    def __init__(self, unidad = 'C'):
        self.__unidad = unidad
        self.__custome = {}
        
        self.__custome['C'] = pygame.image.load("imagenes/selectorC.png")
        self.__custome['F'] = pygame.image.load("imagenes/selectorF.png")
        
        
    def imagen(self, valor = None):
        if valor == None:
            return self.__custome[self.__unidad]
        elif valor == 'C' or valor == 'F':
            return self.__custome[valor]
        
        
    def evento(self, event):
        if self.__unidad == 'C':
            self.__unidad = 'F'
        elif self.__unidad == 'F':
            self.__unidad = 'C'
        
        
        
class NumberInput():
    __value = 0
    __strValue = "0"
    __position = [0, 0]
    __size = [0, 0]
    
    
    def __init__(self):
        self.__font = pygame.font.SysFont("Arial", 24)
        
        
    def evento(self, event):
        if event.unicode.isdigit():
            self.__strValue += event.unicode
            self.value(self.__strValue)
        elif event.key == K_BACKSPACE:
            self.__strValue = self.__strValue[0:-1]
            self.value(self.__strValue)
           
           
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        #return {
        #    'fondo' = rect,
        #    'texto' = textBlock
        #    }
        
        
        return (rect, textBlock)
    
    
    def value(self, val = None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                pass
            
            
    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
            
    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
            
            
    def size(self, val = None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
            
            
    def posX(self, val = None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
        
        
    def posY(self, val = None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
         
         
    def pos(self, val = None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass
            
            

class MainApp():
    termometro = None
    entrada = None
    selector = None
    
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__screen.fill((244, 236, 203))
        
        self.__termometro = Termometro()
        self.__entrada = NumberInput()
        self.__entrada.pos((106, 58))
        self.__entrada.size((133, 28))
        
        self.__selector = Selector()
            
            
    def on_close(self):
        pygame.quit()
        sys.exit()
    
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_close()
                    
                elif event.type == pygame.KEYDOWN:
                    self.__entrada.evento(event)
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__selector.evento(event)
                    
            self.__screen.fill((244, 236, 203))
    
            self.__screen.blit(self.__termometro.imagen(), (50, 34))
            
            text = self.__entrada.render()
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0])
            self.__screen.blit(text[1], self.__entrada.pos())
            
            self.__screen.blit(self.__selector.imagen(), (112, 153))
            
            pygame.display.flip()
        


if __name__ == '__main__':
    pygame.init()
    app = MainApp()
    app.start()
                               
                               