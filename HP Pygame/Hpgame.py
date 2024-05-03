import sys
import pygame

from scripts.Entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init() #essentially starts pygame with these variables assigned

        pygame.display.set_caption('HP game')
        self.screen = pygame.display.set_mode((900, 500))#visual window dimensions
        self.display = pygame.Surface((450, 250))
        self.titlecard = True
        self.choosecharacter = False
        self.tutorial = False
        self.characterlist = ['Bailey', 'Danila', 'Dennis','Donal', 'Eris','Raz', 'Seyi', 'Szymon']#List of character names as appears in selection
        self.characters = ['Assets/images/bailey.png', 'Assets/images/danila.png', 'Assets/images/dennis.png', 'Assets/images/donal.png', 'Assets/images/eris.png', 'Assets/images/raz.png', 'Assets/images/seyi.png', 'Assets/images/szymon.png']#character images/sprites
        self.fps = pygame.time.Clock()
        #self.assets = {
        #    'player': load_image('entities/player.png')
        #}
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.i = 0#increment used to choose character to load

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
                    self.box = self.titletext.get_rect(center=(450,200))#postion for titletext to render
                    self.box2 = self.enter.get_rect(center=(450,350))#position for press any key text to render
                    self.screen.blit(self.titletext, self.box)#puts text onto screen at second argument position
                    self.screen.blit(self.enter, self.box2)
                elif self.choosecharacter:#after key is pressed choose character
                    if event.type == pygame.KEYDOWN:#if key is pressed
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:#left key or a key to incorporate wasd
                            self.i -= 1
                            if self.i == -8:
                                self.i = 0
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:#right key or d key
                            self.i += 1
                            if self.i == 8:
                                self.i = 0
                        if event.key == pygame.K_RETURN:#if player presses enter no longer select a character
                            self.choosecharacter = False
                            self.tutorial = True
                    self.img = pygame.image.load(self.characters[self.i])
                    self.img_position =  (400, 200)#where should images/sprites render
                    self.arrow_left = pygame.font.Font('Assets/font.ttf', 50).render('<', True, 'white')#implies other characters
                    self.arrow_right = pygame.font.Font('Assets/font.ttf', 50).render('>', True, 'white')
                    self.arrow_left_box = self.arrow_left.get_rect(center=(100 , 250))
                    self.arrow_right_box = self.arrow_right.get_rect(center=(800, 250))
                    self.entertext = pygame.font.Font('Assets/font.ttf', 25).render('Press ENTER to SELECT CHARACTER', True, 'white')
                    self.charactertext = pygame.font.Font('Assets/font.ttf', 30).render(self.characterlist[self.i], True, 'white')
                    self.characterbox = self.charactertext.get_rect(center=(450, 400))
                    self.enterbox = self.entertext.get_rect(center=(450, 75))
                    self.screen.blit(self.arrow_left, self.arrow_left_box)
                    self.screen.blit(self.arrow_right, self.arrow_right_box)
                    self.screen.blit(self.img, self.img_position)
                    self.screen.blit(self.entertext, self.enterbox)
                    self.screen.blit(self.charactertext, self.characterbox)
                if self.tutorial:
                    pass
                if event.type == pygame.KEYDOWN and self.titlecard:#will show titlecard til player presses a key
                    self.titlecard = False
                    self.choosecharacter = True

                pygame.display.update()#constantly refreshes screen
            self.fps.tick(60)

Game().run() 