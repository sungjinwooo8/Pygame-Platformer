import sys
import pygame

from scripts.Entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:
    def __init__(self):
        pygame.init() #essentially starts pygame with these variables assigned

        pygame.display.set_caption('HP game')
        self.screen = pygame.display.set_mode((1350, 750))#visual window dimensions
        self.display = pygame.Surface((675, 375))#allows assets to be drawn larger by using a smaller screen that is then adjusted to fit the main screen
        self.titlecard = True
        self.choosecharacter = False
        self.L1 = False
        self.characterlist = ['Donal', 'Seyi',]#List of character names as appears in selection
        self.characters = ['Assets/images/donal.png', 'Assets/images/seyi.png']#character images/sprites
        self.fps = pygame.time.Clock()
        self.i = 0 #increment used to choose character to load
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds' : load_images('clouds')
        }

        self.movement = [False, False]

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

        self.clouds = Clouds(self.assets['clouds'], count=16)

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 25
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 25
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)
            self.tilemap.render(self.display, offset=render_scroll)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
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
                if self.titlecard and event.type == pygame.KEYDOWN: #will show titlecard til player presses a key
                    self.titlecard = False
                    self.choosecharacter = True
                if self.L1: 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = True
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = True
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            self.player.velocity[1] = -3
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.movement[0] = False
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.movement[1] = False
            if self.L1:
                self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))#creates a display to increase size of small assets                  
            pygame.display.update() #constantly refreshes screen
            self.fps.tick(60)

Game().run() 