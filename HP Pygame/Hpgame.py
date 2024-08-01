import sys
import pygame

from scripts.Entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init() #essentially starts pygame with these variables assigned

        pygame.display.set_caption('HP game')
        self.screen = pygame.display.set_mode((1350, 750))#visual window dimensions
        self.display = pygame.Surface((675, 375))
        self.titlecard = True
        self.choosecharacter = False
        self.L1 = False
        self.characterlist = ['Donal', 'Seyi',]#List of character names as appears in selection
        self.characters = ['Assets/images/donal.png', 'Assets/images/seyi.png']#character images/sprites
        self.fps = pygame.time.Clock()
        self.assets = {
            'player': load_image('entities/player.png')
        }
        self.movement = [False, False]
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.i = 0 #increment used to choose character to load

    def run(self):
        while True:
            for event in pygame.event.get():
                self.screen.fill('black')#fills screen black to avoid stacking of elements
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.titlecard:#if no key is pressed
                    self.titletext = pygame.font.Font("Assets/font.ttf", 100).render('HP GAME', True, '#b68f40')#creates text in this font
                    self.enter = pygame.font.Font("Assets/font.ttf", 40).render('Press ANY KEY to START', True, 'white')
                    self.box = self.titletext.get_rect(center=(675, 300))#postion for titletext to render
                    self.box2 = self.enter.get_rect(center=(675, 525))#position for press any key text to render
                    self.screen.blit(self.titletext, self.box)#puts text onto screen at second argument position
                    self.screen.blit(self.enter, self.box2)
                elif self.choosecharacter:#after key is pressed choose character
                    if event.type == pygame.KEYDOWN:#if key is pressed
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:#left key or a key to incorporate wasd
                            self.i -= 1
                            if self.i == -2:
                                self.i = 0
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:#right key or d key
                            self.i += 1
                            if self.i == 2:
                                self.i = 0
                        if event.key == pygame.K_RETURN: #if player presses enter no longer select a character
                            self.choosecharacter = False
                            self.L1 = True
                    self.img = pygame.image.load(self.characters[self.i])
                    self.img_position =  (600, 300)#where should images/sprites render
                    self.arrow_left = pygame.font.Font('Assets/font.ttf', 75).render('<', True, 'white') #implies other characters
                    self.arrow_right = pygame.font.Font('Assets/font.ttf', 75).render('>', True, 'white')
                    self.arrow_left_box = self.arrow_left.get_rect(center=(150 , 375))
                    self.arrow_right_box = self.arrow_right.get_rect(center=(1200, 375))
                    self.entertext = pygame.font.Font('Assets/font.ttf', 37).render('Press ENTER to SELECT CHARACTER', True, 'white')
                    self.charactertext = pygame.font.Font('Assets/font.ttf', 45).render(self.characterlist[self.i], True, 'white')
                    self.characterbox = self.charactertext.get_rect(center=(675, 600))
                    self.enterbox = self.entertext.get_rect(center=(675, 113))
                    self.screen.blit(self.arrow_left, self.arrow_left_box)
                    self.screen.blit(self.arrow_right, self.arrow_right_box)
                    self.screen.blit(self.img, self.img_position)
                    self.screen.blit(self.entertext, self.enterbox)
                    self.screen.blit(self.charactertext, self.characterbox)
                if event.type == pygame.KEYDOWN and self.titlecard: #will show titlecard til player presses a key
                    self.titlecard = False
                    self.choosecharacter = True
                if self.L1:
                    self.display.fill((14, 219, 248))
                    self.player.update((self.movement[1] - self.movement[0], 0))
                    self.player.render(self.display)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = True
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = True
                        if event.key == pygame.K_UP:
                            self.player.velocity[1] = -3
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.movement[0] = False
                        if event.key == pygame.K_RIGHT:
                            self.movement[1] = False
                    self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))                    
                pygame.display.update() #constantly refreshes screen
            self.fps.tick(60)

Game().run() 