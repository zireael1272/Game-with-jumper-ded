import pygame
import sys

class Background:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.start = True

        self.background1 = pygame.image.load(r"Resource\background\5.png").convert()
        self.background2 = pygame.image.load(r"Resource\background\4.png").convert_alpha()
        self.background3 = pygame.image.load(r"Resource\background\3.png").convert_alpha()
        self.background4 = pygame.image.load(r"Resource\background\2.png").convert_alpha()
        self.background5 = pygame.image.load(r"Resource\background\1.png").convert_alpha()

        self.background2_change = pygame.image.load(r"Resource\background\4.png").convert_alpha()
        self.background3_change = pygame.image.load(r"Resource\background\3.png").convert_alpha()
        self.background4_change = pygame.image.load(r"Resource\background\2.png").convert_alpha()
        self.background5_change = pygame.image.load(r"Resource\background\1.png").convert_alpha()

        self.background2_x = 0
        self.background3_x = 0
        self.background4_x = 0
        self.background5_x = 0

        self.background2_x_change = self.screen_width
        self.background3_x_change = self.screen_width
        self.background4_x_change = self.screen_width
        self.background5_x_change = self.screen_width

        self.background_speed2 = 0.8
        self.background_speed3 = 1
        self.background_speed4 = 1.2
        self.background_speed5 = 1.4

    def update(self, screen):
        if self.start:
            screen.blit(self.background1, (0, 0))
            screen.blit(self.background2, (self.background2_x, 0))
            screen.blit(self.background2_change, (self.background2_x_change, 0))
            screen.blit(self.background3, (self.background3_x, 0))
            screen.blit(self.background3_change, (self.background3_x_change, 0))
            screen.blit(self.background4, (self.background4_x, 0))
            screen.blit(self.background4_change, (self.background4_x_change, 0))
            screen.blit(self.background5, (self.background5_x, 0))
            screen.blit(self.background5_change, (self.background5_x_change, 0))
        else:
            self.background2_x -= self.background_speed2
            self.background2_x_change -= self.background_speed2
            self.background3_x -= self.background_speed3
            self.background3_x_change -= self.background_speed3
            self.background4_x -= self.background_speed4
            self.background4_x_change -= self.background_speed4
            self.background5_x -= self.background_speed5
            self.background5_x_change -= self.background_speed5

            if self.background2_x <= -self.screen_width:
                self.background2_x = self.screen_width
            if self.background2_x_change <= -self.screen_width:
                self.background2_x_change = self.screen_width
            if self.background3_x <= -self.screen_width:
                self.background3_x = self.screen_width
            if self.background3_x_change <= -self.screen_width:
                self.background3_x_change = self.screen_width
            if self.background4_x <= -self.screen_width:
                self.background4_x = self.screen_width
            if self.background4_x_change <= -self.screen_width:
                self.background4_x_change = self.screen_width
            if self.background5_x <= -self.screen_width:
                self.background5_x = self.screen_width
            if self.background5_x_change <= -self.screen_width:
                self.background5_x_change = self.screen_width

            screen.blit(self.background1, (0, 0))
            screen.blit(self.background2, (self.background2_x, 0))
            screen.blit(self.background2_change, (self.background2_x_change, 0))
            screen.blit(self.background3, (self.background3_x, 0))
            screen.blit(self.background3_change, (self.background3_x_change, 0))
            screen.blit(self.background4, (self.background4_x, 0))
            screen.blit(self.background4_change, (self.background4_x_change, 0))
            screen.blit(self.background5, (self.background5_x, 0))
            screen.blit(self.background5_change, (self.background5_x_change, 0))

            pygame.display.update()
