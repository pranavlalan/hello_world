import random
import pygame
from pygame.locals import *
from threading import Thread, Event
import time


event = Event()

pygame.init()

screen_width = 800
screen_height = 600
spoon_x = 300
spoon_y = screen_height - 100
raspberry_x = 0
raspberry_y = 0

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Raspberry Catching')

spoon = pygame.image.load('spoon.jpg').convert()
ball = pygame.image.load('raspberry.jpg').convert()

red = 255
green = 255
blue = 255

bg_color = {'RED': red, 'GREEN': green, 'BLUE': blue}

number_of_raspberries = 0
score = 0



class Raspberry:
    def __init__(self, name):
        self.name = name
        self.x = random.randint(10, screen_width)
        self.y = 0
        self.dy = random.randint(3, 7)
        print(self.convert2string())


    def convert2string(self):
        message = self.name + ': ' + '(' + str(self.x) + ',' + str(self.y) + ')' + ' dy=' + str(self.dy)
        return message
        
    def update(self):
        global number_of_raspberries
        
        if self.y >= spoon_y:
            self.y = 0
            self.x = random.randint(10, screen_width)
            
            number_of_raspberries += 1
        
        self.y += self.dy
        
        self.x += random.randint(-5, 5)
        if self.x < 10:
            self.x = 10
        if self.x > screen_width-20:
            self.x = screen_width-20
        
        screen.blit(ball, (self.x, self.y))
        
    def is_caught(self):
        global score
        if self.y >= spoon_y and self.x >= spoon_x and \
            self.x < spoon_x + 50:
            print('caught raspberry: ' + self.convert2string())
            score += 1
        display("Score: " + str(score))

def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, 1, (10, 10, 10))
    screen.blit(text, (0, 0))
    
def check_for_catch(rasps):
    for r in rasps:
        r.is_caught()

def update_spoon():
    global spoon_x
    global spoon_y
    spoon_x, ignore = pygame.mouse.get_pos()
    screen.blit(spoon, (spoon_x,spoon_y))

def update_raspberries(rasps):
    for r in rasps:
        r.update()
    

def check_for_exit():
    try:
        for e in pygame.event.get():
            if e.type == QUIT:
                return True
    except pygame.error:
        return True
            

    
def update_background(bgc):
    
    while True:
        if check_for_exit():
            break
        
        bgc['RED'] = random.randint(0,255)
        bgc['GREEN'] = random.randint(0,255)
        bgc['BLUE'] = random.randint(0,255)
    
        print('update_background' + '     ' + str(bgc['RED']) + ' ' + str(bgc['GREEN']) + ' ' + str(bgc['BLUE']))
        time.sleep(3)
        
    
def catch_raspberries(bgc, rasps):
    clock = pygame.time.Clock()
    while True:
        
        if check_for_exit():
            catch_efficiency = 0.0
            try:
                catch_efficiency = (score/number_of_raspberries)*100
            except ZeroDivisionError:
                catch_efficiency = 0.0
                
            print('Score=' + str(score) + ' catch-efficiency=' + str(catch_efficiency))
            pygame.quit()
            exit()
        
        red = bgc['RED']
        green = bgc['GREEN']
        blue = bgc['BLUE']
        
        
        
        
        #print(str(red) + ' ' + str(green) + ' ' + str(blue))
        screen.fill((red,green,blue))
        update_spoon()
        update_raspberries(rasps)
        check_for_catch(rasps)
        pygame.display.update()
        clock.tick(30)

screen.fill((bg_color['RED'],bg_color['GREEN'],bg_color['BLUE']))

#rasps = [Raspberry('r1'), Raspberry('r2')]
rasps = [Raspberry('r1')]

t_catch_raspberry = Thread(target=catch_raspberries, args=(bg_color, rasps))
t_update_background = Thread(target=update_background, args=(bg_color,))

t_catch_raspberry.start()
t_update_background.start()

print('waiting for t_catch_raspberry to finish')
t_catch_raspberry.join()
print('t_catch_raspberry has finished')

t_update_background.join()
exit()