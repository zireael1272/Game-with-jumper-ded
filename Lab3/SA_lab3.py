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
pygame.mixer.init()
background_music = pygame.mixer.Sound(r"Resource/music/Main Sound.wav")
end_sound = pygame.mixer.Sound(r"Resource/music/Game Over.mp3")
win_sound = pygame.mixer.Sound(r"Resource/music/win.mp3")
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
grandpa = Grandpabegit(screen)
HP = Heart(screen)
boosters = []
damages = []
x_offset = 200


def create_boost_damage():
    global x_offset
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


clock = pygame.time.Clock()
damage_counter = 0
running = False

current_scene = None


def switch_scene(scene):
    global current_scene
    current_scene = scene


def start():
    background_music.play(loops=-1)
    background_music.set_volume(0.1)
    global running, x_offset
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
                    create_boost_damage()
                    background.start = False
                    grandpa.start = False
                    grandpa.ded_x = 80
                    grandpa.acceleration = 0.19
                    x_offset = 200
                    HP.start = False
                    for booster in boosters:
                        booster.start = False
                    for damage in damages:
                        damage.start = False
                    switch_scene(main)
                    play = False


def end(text_win, text_point, result):
    global running, damage_counter
    running = False
    play = True
    with open("Best_result.txt", 'r') as file:
        best_result = int(file.read().strip())
    file.close()
    background_music.stop()
    while play:
        if result == -1:
            end_sound.set_volume(0.08)
            end_sound.play()
        else:
            win_sound.set_volume(0.05)
            win_sound.play()
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("End Game", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(SCREEN_WIDTH / 2.5, 150))
        screen.blit(text, text_rect)
        text_win_rect = text.get_rect(topleft=(SCREEN_WIDTH / 2.5, 210))
        screen.blit(text_win, text_win_rect)
        text_point_rect = text.get_rect(topleft=(275, 270))
        screen.blit(text_point, text_point_rect)
        if best_result < result:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Best result: {result}", True, (255, 255, 255))
            text_best_rect = text.get_rect(topleft=(340, 330))
            screen.blit(text, text_best_rect)
            best = open(''
                        'Best_result.txt', 'wt')
            print(result, file=best)
            best.close()
        else:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Best result: {best_result}", True, (255, 255, 255))
            text_best_rect = text.get_rect(topleft=(340, 330))
            screen.blit(text, text_best_rect)
        boosters.clear()
        damages.clear()
        damage_counter = 0
        grandpa.collected_boosts = 0
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end_sound.stop()
                    win_sound.stop()
                    switch_scene(start)
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
        text_lost = font.render(f" You loser", True, (255, 255, 255))

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
                        text_point = font.render(f"           Try Again", True,(255, 255, 255))
                        end(text_lost, text_point, -1)
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
