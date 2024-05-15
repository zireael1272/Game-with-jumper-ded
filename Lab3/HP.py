import pygame
class Heart:
    def __init__(self, screen):
        self.screen = screen
        self.start = True
        self.HP_animate = [pygame.image.load(r"Resource\HP\heart_1.png").convert_alpha(),
                       pygame.image.load(
                           r"Resource\HP\heart_2.png").convert_alpha(),
                       pygame.image.load(
                           r"Resource\HP\heart_3.png").convert_alpha(),
                       pygame.image.load(
                           r"Resource\HP\heart_4.png").convert_alpha(),
                       pygame.image.load(
                           r"Resource\HP\heart_5.png").convert_alpha(),
                       pygame.image.load(
                           r"Resource\HP\heart_6.png").convert_alpha()
                       ]
        self.HP_empty = pygame.image.load(r"Resource\HP\heart_empty.png").convert_alpha()
        self.animate_index = 0
        self.animate_speed = 0.08

    def output(self, damage_counter):
        self.animate_index += self.animate_speed
        index_int = int(self.animate_index)
        index_int %= len(self.HP_animate)
        if index_int >= len(self.HP_animate):
            self.animate_index = 0

        if self.start == True:
            self.screen.blit(self.HP_animate[0], (10, 10))
            self.screen.blit(self.HP_animate[0], (40, 10))
            self.screen.blit(self.HP_animate[0], (70, 10))
        else:
            if damage_counter == 1:
                self.screen.blit(self.HP_empty, (70, 12))
                self.screen.blit(self.HP_animate[index_int], (10, 10))
                self.screen.blit(self.HP_animate[index_int], (40, 10))
            elif damage_counter == 2:
                self.screen.blit(self.HP_empty, (70, 12))
                self.screen.blit(self.HP_empty, (40, 12))
                self.screen.blit(self.HP_animate[index_int], (10, 10))
            elif damage_counter == 3:
                self.screen.blit(self.HP_empty, (10, 12))
                self.screen.blit(self.HP_empty, (40, 12))
                self.screen.blit(self.HP_empty, (70, 12))
            else:
                self.screen.blit(self.HP_animate[index_int], (10, 10))
                self.screen.blit(self.HP_animate[index_int], (40, 10))
                self.screen.blit(self.HP_animate[index_int], (70, 10))
