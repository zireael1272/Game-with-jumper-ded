import pygame
import sys
from background import Background
from character import Grandpabegit
from HP import Heart
from boost_damage import Booster
from boost_damage import Damage
import random
pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Стрибки")
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
grandpa = Grandpabegit(screen)
HP = Heart(screen)
boosters = []
damages = []
x_offset = 200
for _ in range(100):
    if random.choice([True, False]):
        y = random.randint(200, 450)
        boost_damage = Booster(screen, 500 + x_offset, y)
        boosters.append(boost_damage)
        x_offset += random.randint(200, 800)
    else:
        y = random.randint(200, 450)
        boost_damage = Damage(screen, 500 + x_offset, y)
        damages.append(boost_damage)
        x_offset += random.randint(200, 800)

enter_pressed = False
clock = pygame.time.Clock()
damage_counter = 0
running = False

current_scene = None

def switch_scene(scene):
    global current_scene
    current_scene = scene


def start():
    global running
    running = True
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    background.start = False
                    grandpa.start = False
                    HP.start = False
                    for booster in boosters:
                        booster.start = False
                    for damage in damages:
                        damage.start = False
                    switch_scene(main)
                    play = False
    font = pygame.font.Font(None, 50)
    text = font.render("Press Enter for Start Game", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = SCREEN_WIDTH / 4
    text_rect.y = SCREEN_HEIGHT / 2
    screen.blit(text, text_rect)
    pygame.display.update()


def end():
    global running
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("End Game", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = SCREEN_WIDTH / 2.5
    text_rect.y = SCREEN_HEIGHT / 2
    screen.blit(text, text_rect)
    pygame.display.update()
    running = False


def main():
    global damage_counter, running, enter_pressed
    while running:
        screen.fill((0, 0, 0))
        collision_this_frame = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background.update(screen)
        HP.output(damage_counter)
        grandpa.update()

        for booster in boosters:
            booster.update()
            booster_rect = booster.get_rect()
            if not booster.collected:
                if (grandpa.ded_rect.left < booster_rect.centerx < grandpa.ded_rect.right and
                        grandpa.ded_rect.top < booster_rect.centery < grandpa.ded_rect.bottom):
                    grandpa.point()
                    booster.collect()
                    for boost in boosters:
                        boost.speed += 0.5
                    for damage in damages:
                        damage.speed += 0.6
                    background.background_speed2 += 0.09
                    background.background_speed3 += 0.09
                    background.background_speed4 += 0.09
                    background.background_speed5 += 0.09
                    break

        for damage in damages:
            damage.update()
            damage_rect = damage.get_rect()
            if not damage.collected:
                if grandpa.ded_rect.left < damage_rect.centerx < grandpa.ded_rect.right and grandpa.ded_rect.top < damage_rect.centery < grandpa.ded_rect.bottom:
                    grandpa.damage()
                    damage.collect()
                    damage_counter += 1
                    if damage_counter == 3:
                        HP.output(damage_counter)
                        grandpa.start = True
                        background.start = True
                        HP.start = True
                        for booster in boosters:
                            booster.start = True
                        for damage in damages:
                            damage.start = True
                        end()
                    for booster in boosters:
                        booster.speed -= 0.5
                    for damag in damages:
                        damag.speed -= 0.6
                    background.background_speed2 -= 0.09
                    background.background_speed3 -= 0.09
                    background.background_speed4 -= 0.09
                    background.background_speed5 -= 0.09
                    break

        font = pygame.font.Font(None, 30)
        text = font.render(f"Cakes - {grandpa.collected_boosts}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 780
        text_rect.y = 18
        screen.blit(text, text_rect)

        if grandpa.game_end:
            grandpa.game_end = False
            grandpa.start = True
            background.start = True
            HP.start = True
            for booster in boosters:
                booster.start = True
            for damage in damages:
                damage.start = True
            end()

        pygame.display.update()
        clock.tick(60)

switch_scene(start)
while current_scene is not None:
    current_scene()


pygame.quit()