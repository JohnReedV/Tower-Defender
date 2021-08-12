import os
import pygame
from pygame import mixer
from screen import Screen
from volume import Volume
from game import Game
import time


class MenuBackground():

    def menuFunc(self):

        def enemy9(x, y):
            screen.blit(enemy1, (x, y))

        def enemy8(x, y):
            screen.blit(enemy2, (x, y))

        def enemy7(x, y):
            screen.blit(enemy3, (x, y))

        screen = Screen()
        background = pygame.image.load(os.path.join("assets", "bg.png")).convert_alpha()
        pygame.display.set_caption("Tower Defence")
        icon = pygame.image.load(os.path.join("assets", "troll.png")).convert_alpha()
        pygame.display.set_icon(icon)

        quit2 = pygame.image.load(os.path.join("assets", "quit2.png"))
        play = pygame.image.load(os.path.join("assets", "play.png"))
        pause = pygame.image.load(os.path.join("assets", "pause.png"))
        logo = pygame.image.load(os.path.join("assets", "td.png"))

        volumelevel = .4
        mixer.music.load("music.wav")
        mixer.music.set_volume(volumelevel)
        mixer.music.play()

        enemy1x = -50
        enemy1y = 330
        enemy1 = pygame.image.load(os.path.join("assets", "enemy1.png")).convert_alpha()
        enemy1xchange = .6
        enemy1ychange = .6

        enemy2x = 537
        enemy2y = 200
        enemy2 = pygame.image.load(os.path.join("assets", "soup.png")).convert_alpha()
        enemy2xchange = .6
        enemy2ychange = .6

        enemy3x = 250
        enemy3y = 550
        enemy3 = pygame.image.load(os.path.join("assets", "boss.png")).convert_alpha()
        enemy3xchange = .6
        enemy3ychange = .6

        inMenu = True
        while inMenu:
            if enemy1x <= 230:
                enemy1x += enemy1xchange
            elif enemy1y <= 550 and enemy1x <= 231:
                enemy1y += enemy1ychange
            elif enemy1x <= 537:
                enemy1x += enemy1xchange
            elif enemy1y >= 162 and enemy1x <= 538:
                enemy1y -= enemy1ychange
            elif enemy1x <= 760:
                enemy1x += enemy1xchange
            elif enemy1y < 540:
                enemy1y += enemy1ychange
            elif enemy1x < 1000:
                enemy1x += enemy1xchange
            if enemy1x > 1000:
                enemy1x = -50
                enemy1y = 330

            if enemy2x <= 230:
                enemy2x += enemy2xchange
            elif enemy2y <= 550 and enemy2x <= 231:
                enemy2y += enemy2ychange
            elif enemy2x <= 537:
                enemy2x += enemy2xchange
            elif enemy2y >= 162 and enemy2x <= 538:
                enemy2y -= enemy2ychange
            elif enemy2x <= 760:
                enemy2x += enemy2xchange
            elif enemy2y < 540:
                enemy2y += enemy2ychange
            elif enemy2x < 1000:
                enemy2x += enemy2xchange
            if enemy2x > 1000:
                enemy2x = -50
                enemy2y = 330

            if enemy3x <= 230:
                enemy3x += enemy3xchange
            elif enemy3y <= 550 and enemy3x <= 231:
                enemy3y += enemy3ychange
            elif enemy3x <= 537:
                enemy3x += enemy3xchange
            elif enemy3y >= 162 and enemy3x <= 538:
                enemy3y -= enemy3ychange
            elif enemy3x <= 760:
                enemy3x += enemy3xchange
            elif enemy3y < 540:
                enemy3y += enemy3ychange
            elif enemy3x < 1000:
                enemy3x += enemy3xchange
            if enemy3x > 1000:
                enemy3x = -50
                enemy3y = 330

            screen.blit(background, (0, 0))
            enemy9(enemy1x, enemy1y)
            enemy8(enemy2x, enemy2y)
            enemy7(enemy3x, enemy3y)
            screen.blit(play, (370, 450))
            screen.blit(quit2, (462, 600))
            screen.blit(pause, (930, 10))
            screen.blit(logo, (270, 20))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos1, pos2 = pygame.mouse.get_pos()
                    if pos1 >= 931 and pos1 <= 995 and pos2 >=3 and pos2 <= 74:
                        mixer.music.load("press.wav")
                        mixer.music.set_volume(volumelevel)
                        mixer.music.play()
                        time.sleep(.15)
                        Volume()
                        volumelevel = Volume()
                    if pos1 >= 465 and pos1 <= 519 and pos2 >= 599 and pos2 <= 654:
                        mixer.music.load("press.wav")
                        mixer.music.set_volume(volumelevel)
                        mixer.music.play()
                        time.sleep(.25)
                        quit()
                    elif pos1 >= 379 and pos1 <= 613 and pos2 >= 479 and pos2 <= 534:
                        mixer.music.load("press.wav")
                        mixer.music.set_volume(volumelevel)
                        mixer.music.play()
                        time.sleep(.15)
                        mixer.music.load("wave.wav")
                        mixer.music.set_volume(volumelevel)
                        mixer.music.play()
                        time.sleep(4.6)
                        mixer.quit()
                        inMenu = False
                        Game().gameWorks()
            pygame.display.update()
