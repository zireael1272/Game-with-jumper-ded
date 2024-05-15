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
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("Press Enter for Start Game", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = SCREEN_WIDTH / 4
        text_rect.y = SCREEN_HEIGHT / 2
        screen.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                running = False
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


def end(text_win, text_point, result):
    global running
    running = False
    play = True
    with open("C:/Users/User/Desktop/Game-with-jumper-ded/Lab3/Best_result.txt", 'r') as file:
        best_result = int(file.read().strip())
    file.close()
    while play:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("End Game", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = SCREEN_WIDTH / 2.5
        text_rect.y = 150
        screen.blit(text, text_rect)
        text_win_rect = text.get_rect()
        text_win_rect.x = SCREEN_WIDTH / 2.5
        text_win_rect.y = 210
        screen.blit(text_win, text_win_rect)
        text_point_rect = text.get_rect()
        text_point_rect.x = 275
        text_point_rect.y = 270
        screen.blit(text_point, text_point_rect)
        if best_result < result:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Best result: {result}", True, (255, 255, 255))
            text_point_rect = text.get_rect()
            text_point_rect.x = 335
            text_point_rect.y = 330
            screen.blit(text, text_point_rect)
            best = open('C:/Users/User/Desktop/Game-with-jumper-ded/Lab3/Best_result.txt', 'wt')
            print(result, file=best)
            best.close()
        else:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Best result: {best_result}", True, (255, 255, 255))
            text_point_rect = text.get_rect()
            text_point_rect.x = 335
            text_point_rect.y = 330
            screen.blit(text, text_point_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = True
                    switch_scene(main)
                    play = False


def main():
    global damage_counter, running, enter_pressed
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background.update(screen)
        grandpa.update()
        HP.output(damage_counter)

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

        font = pygame.font.Font(None, 50)
        text_lost = font.render(f"  You loser", True, (255, 255, 255))

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
                        for damage_1 in damages:
                            damage_1.start = True
                        end(text_lost, "", 0)
                    for booster in boosters:
                        booster.speed -= 0.5
                    for dam in damages:
                        dam.speed -= 0.5
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

        font = pygame.font.Font(None, 50)
        text_win = font.render(f"  You win", True, (255, 255, 255))
        text_point = font.render(f" Yours count point - {grandpa.collected_boosts}", True, (255, 255, 255))

        if grandpa.game_end:
            grandpa.game_end = False
            grandpa.start = True
            background.start = True
            HP.start = True
            for booster in boosters:
                booster.start = True
            for damage in damages:
                damage.start = True
            end(text_win, text_point, grandpa.collected_boosts)

        pygame.display.flip()
        clock.tick(60)


switch_scene(start)
while current_scene is not None:
    current_scene()


pygame.quit()
