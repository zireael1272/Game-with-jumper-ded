import pygame
class Booster:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.start = True
        self.collected = False
        self.collected_booster = None
        self.speed = 1.3
        self.booster_1 = pygame.image.load(
        r"C:\Users\User\Desktop\Систем анализ\Lab3\Resource\booster\Ghostpixxells_pixelfood\tortik.png").convert_alpha()

    def update(self):
        if not self.start and not self.collected:
            self.x -= self.speed
            self.screen.blit(self.booster_1, (self.x, self.y))


    def get_rect(self):
        return self.booster_1.get_rect(topleft=(self.x, self.y))

    def collect(self):
        if not self.collected:
            self.collected = True
            return True
        return False


class Damage:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.start = True
        self.collected = False
        self.collected_damage = None
        self.speed = 1.3
        self.damage_1 = pygame.image.load(
            r"C:\Users\User\Desktop\Систем анализ\Lab3\Resource\damage\damage_1.png").convert_alpha()

    def update(self):
        if not self.start and not self.collected:
            self.x -= self.speed
            self.screen.blit(self.damage_1, (self.x, self.y))

    def get_rect(self):
        return self.damage_1.get_rect(topleft=(self.x, self.y))

    def collect(self):
        if not self.collected:
            self.collected = True
            return True
        return False
