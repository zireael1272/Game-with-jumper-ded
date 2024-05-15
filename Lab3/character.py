import pygame
class Grandpabegit(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.collected_boosters = 0
        self.start = True
        self.collected_boosts = 0
        self.ded_begit = [
            pygame.image.load(
                r"Resource\old_man\ded_1.png").convert_alpha(),
            pygame.image.load(
                r"Resource\old_man\ded_2.png").convert_alpha(),
            pygame.image.load(
                r"Resource\old_man\ded_3.png").convert_alpha(),
            pygame.image.load(
                r"Resource\old_man\ded_4.png").convert_alpha()
        ]
        self.ded_static = pygame.image.load(
            r"Resource\old_man\ded_1.png").convert_alpha()
        self.ded_x = 80
        self.ded_y = 460
        self.y_gravity = 1
        self.animate_index = 0
        self.animate_speed = 0.19
        self.acceleration = 0.19
        self.height_jump = 25
        self.y_velocity = 0
        self.button_space = False
        self.ded_rect = self.ded_static.get_rect(center=(self.ded_x, self.ded_y))
        self.on_ground = False
        self.game_end = False

    def update(self):
        if self.start:
            self.ded_rect = self.ded_static.get_rect(center=(self.ded_x, self.ded_y))
            self.screen.blit(self.ded_static, self.ded_rect)

        else:
            if self.ded_x > 930:
                self.game_end = True

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_SPACE] and self.on_ground:
                self.y_velocity = -self.height_jump
                self.on_ground = False

            self.ded_y += self.y_velocity
            self.y_velocity += self.y_gravity

            if self.y_velocity >= 0 and self.ded_y >= 460:
                self.y_velocity = 0
                self.ded_y = 460
                self.on_ground = True

            if self.acceleration < 0.01:
                self.game_end = True
            else:
                self.ded_x += self.acceleration

            if self.on_ground:
                self.animate_index += self.animate_speed
                if self.animate_index >= len(self.ded_begit):
                    self.animate_index = 0
                self.ded_rect = self.ded_begit[int(self.animate_index)].get_rect(center=(self.ded_x, self.ded_y))
                image_to_display = self.ded_begit[int(self.animate_index)]
            else:
                self.ded_rect = self.ded_static.get_rect(center=(self.ded_x, self.ded_y))
                image_to_display = self.ded_static

            self.screen.blit(image_to_display, self.ded_rect)

    def point(self):
        self.acceleration += 0.05
        self.collected_boosts += 1

    def damage(self):
        self.acceleration -= 0.04
