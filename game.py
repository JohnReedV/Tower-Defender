import math
import os
import subprocess
import sys
import random
import pygame
import time
from pygame import mixer

from volume import Volume
from screen import Screen


class Game:
    def gameWorks(self):
        screen = Screen()
        background = pygame.image.load(os.path.join("assets", "bg.png")).convert_alpha()
        pygame.display.set_caption("Tower Defence")
        icon = pygame.image.load(os.path.join("assets", "troll.png")).convert_alpha()
        pygame.display.set_icon(icon)
        pause = pygame.image.load(os.path.join("assets", "pause.png"))
        bone = pygame.image.load(os.path.join("assets", "bone.png")).convert_alpha()
        tower1s = pygame.image.load(os.path.join("assets", "tower1s.png"))
        tower1b = pygame.image.load(os.path.join("assets", "tower1b.png"))
        tower2s = pygame.image.load(os.path.join("assets", "tower2s.png"))
        tower2b = pygame.image.load(os.path.join("assets", "tower2b.png"))
        tower3s = pygame.image.load(os.path.join("assets", "tower3s.png"))
        tower3b = pygame.image.load(os.path.join("assets", "tower3b.png"))
        font = pygame.font.Font('freesansbold.ttf', 32)

        volumelevel = .4
        mixer.init()
        mixer.music.load("music.wav")
        mixer.music.set_volume(volumelevel)
        mixer.music.play()

        drawert1 = 1000
        drawert2 = 1000
        drawert3 = 2000
        drawert4 = 2000
        drawert5 = 3000
        drawert6 = 4000

        smile = False
        frown = False
        stare = False

        enemyamount = 3
        enemy1x = []
        enemy1y = []
        enemy1 = []
        enemy1xchange = []
        enemy1ychange = []
        kills = 0
        enemy2amount = 4
        enemy2 = []
        enemy2x = []
        enemy2y = []
        enemy2xchange = []
        enemy2ychange = []

        def distance1(x1, x2, y1, y2):
            dist = math.hypot(x1 - x2, y1 - y2)
            if dist <= 170:
                return True
            else:
                return False

        def distance2(x1, x2, y1, y2):
            dist = math.hypot(x1 - x2, y1 - y2)
            if dist <= 250:
                return True
            else:
                return False

        for i in range(enemyamount):
            enemy1.append(pygame.image.load(os.path.join("assets", "enemy1.png")).convert_alpha())
            enemy1x.append(random.randrange(-50, 210))
            enemy1y.append(330)
            enemy1xchange.append(.15)
            enemy1ychange.append(.15)
            enemy2.append(pygame.image.load(os.path.join("assets", "boss.png")).convert_alpha())
            enemy2x.append(random.randrange(-50, 210))
            enemy2y.append(330)
            enemy2xchange.append(.15)
            enemy2ychange.append(.15)

        def enemy9(x, y, i):
            screen.blit(enemy1[i], (x, y))

        def enemy8(x, y, i):
            screen.blit(enemy2[i], (x, y))

        def score():
            score1 = font.render("Score : " + str(kills), True, (0, 0, 0))
            screen.blit(score1, (420, 10))

        on = True
        while on:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos1, pos2 = pygame.mouse.get_pos()
                    if pos1 >= 931 and pos1 <= 995 and pos2 >=3 and pos2 <= 74:
                        mixer.music.load("press.wav")
                        mixer.music.set_volume(volumelevel)
                        mixer.music.play()
                        time.sleep(.15)
                        Volume()
                        volumelevel = Volume()
                        if volumelevel == 5.384739430:
                            on = False
                            subprocess.call([sys.executable, os.path.realpath("main.py")] + sys.argv[1:])
                            quit()
                    if pos1 >= 382 and pos1 <= 442 and pos2 >= 625 and pos2 <= 687:
                        smile = True
                    if pos1 >= 462 and pos1 <= 521 and pos2 >= 625 and pos2 <= 687:
                        frown = True
                    if pos1 >= 539 and pos1 <= 604 and pos2 >= 625 and pos2 <= 687:
                        stare = True

            screen.blit(background, (0, 0))
            screen.blit(pause, (930, 10))
            screen.blit(bone, (380, 625))
            screen.blit(tower1s, (390, 635))
            screen.blit(bone, (460, 625))
            screen.blit(tower2s, (470, 635))
            screen.blit(bone, (540, 625))
            screen.blit(tower3s, (550, 635))
            score()

            if smile:
                pos1, pos2 = pygame.mouse.get_pos()
                screen.blit(tower1s, (pos1, pos2))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        drawert1, drawert2 = pygame.mouse.get_pos()
                        smile = False


            if drawert1 <= 288 and drawert1 >= 230 and drawert2 <= 261 and drawert2 >= 191:
                screen.blit(tower1b, (210, 180))
            if drawert1 <= 194 and drawert1 >= 131 and drawert2 <= 564 and drawert2 >= 503:
                screen.blit(tower1b, (115, 480))
            if drawert1 <= 448 and drawert1 >= 387 and drawert2 <= 517 and drawert2 >= 459:
                screen.blit(tower1b, (370, 435))
            if drawert1 <= 708 and drawert1 >= 652 and drawert2 <= 113 and drawert2 >= 51:
                screen.blit(tower1b, (633, 30))
            if drawert1 <= 710 and drawert1 >= 646 and drawert2 <= 440 and drawert2 >= 276:
                screen.blit(tower1b, (632, 353))
            if drawert1 <= 953 and drawert1 >= 887 and drawert2 <= 356 and drawert2 >= 295:
                screen.blit(tower1b, (873, 273))

            if frown:
                pos1, pos2 = pygame.mouse.get_pos()
                screen.blit(tower2s, (pos1, pos2))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        drawert3, drawert4 = pygame.mouse.get_pos()
                        frown = False

            if drawert3 <= 288 and drawert3 >= 230 and drawert4 <= 261 and drawert4 >= 191:
                screen.blit(tower2b, (210, 180))
            if drawert3 <= 194 and drawert3 >= 131 and drawert4 <= 564 and drawert4 >= 503:
                screen.blit(tower2b, (115, 480))
            if drawert3 <= 448 and drawert3 >= 387 and drawert4 <= 517 and drawert4 >= 459:
                screen.blit(tower2b, (370, 435))
            if drawert3 <= 708 and drawert3 >= 652 and drawert4 <= 113 and drawert4 >= 51:
                screen.blit(tower2b, (633, 30))
            if drawert3 <= 710 and drawert3 >= 646 and drawert4 <= 440 and drawert4 >= 276:
                screen.blit(tower2b, (632, 353))
            if drawert3 <= 953 and drawert3 >= 887 and drawert4 <= 356 and drawert4 >= 295:
                screen.blit(tower2b, (873, 273))

            if stare:
                pos1, pos2 = pygame.mouse.get_pos()
                screen.blit(tower3s, (pos1, pos2))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        drawert5, drawert6 = pygame.mouse.get_pos()
                        stare = False

            if drawert5 <= 288 and drawert5 >= 230 and drawert6 <= 261 and drawert6 >= 191:
                screen.blit(tower3b, (210, 180))
            if drawert5 <= 194 and drawert5 >= 131 and drawert6 <= 564 and drawert6 >= 503:
                screen.blit(tower3b, (115, 480))
            if drawert5 <= 448 and drawert5 >= 387 and drawert6 <= 517 and drawert6 >= 459:
                screen.blit(tower3b, (370, 435))
            if drawert5 <= 708 and drawert5 >= 652 and drawert6 <= 113 and drawert6 >= 51:
                screen.blit(tower3b, (633, 30))
            if drawert5 <= 710 and drawert5 >= 646 and drawert6 <= 440 and drawert6 >= 276:
                screen.blit(tower3b, (632, 353))
            if drawert5 <= 953 and drawert5 >= 887 and drawert6 <= 356 and drawert6 >= 295:
                screen.blit(tower3b, (873, 273))


            for i in range(enemyamount):
                if enemy1x[i] <= 230:
                    enemy1x[i] += enemy1xchange[i]
                elif enemy1y[i] <= 550 and enemy1x[i] <= 231:
                    enemy1y[i] += enemy1ychange[i]
                elif enemy1x[i] <= 537:
                    enemy1x[i] += enemy1xchange[i]
                elif enemy1y[i] >= 162 and enemy1x[i] <= 538:
                    enemy1y[i] -= enemy1ychange[i]
                elif enemy1x[i] <= 760:
                    enemy1x[i] += enemy1xchange[i]
                elif enemy1y[i] < 540:
                    enemy1y[i] += enemy1ychange[i]
                elif enemy1x[i] < 1000:
                    enemy1x[i] += enemy1xchange[i]
                if enemy1x[i] > 1000:
                    enemy1x[i] = -50
                    enemy1y[i] = 330
                enemy9(enemy1x[i], enemy1y[i], i)

                if distance1(drawert1, enemy1x[i], drawert2, enemy1y[i]) \
                        or distance1(drawert3, enemy1x[i], drawert4, enemy1y[i]) \
                        or distance1(drawert5, enemy1x[i], drawert6, enemy1y[i]):
                    enemy1x[i] = random.randrange(-50, 210)
                    enemy1y[i] = 330
                    kills += 1

            if kills >= 18:
                for i in range(enemyamount):
                    if enemy2x[i] <= 230:
                        enemy2x[i] += enemy2xchange[i]
                    elif enemy2y[i] <= 550 and enemy2x[i] <= 231:
                        enemy2y[i] += enemy2ychange[i]
                    elif enemy2x[i] <= 537:
                        enemy2x[i] += enemy2xchange[i]
                    elif enemy2y[i] >= 162 and enemy2x[i] <= 538:
                        enemy2y[i] -= enemy2ychange[i]
                    elif enemy2x[i] <= 760:
                        enemy2x[i] += enemy2xchange[i]
                    elif enemy2y[i] < 540:
                        enemy2y[i] += enemy2ychange[i]
                    elif enemy2x[i] < 1000:
                        enemy2x[i] += enemy2xchange[i]
                    if enemy2x[i] > 1000:
                        enemy2x[i] = -50
                        enemy2y[i] = 330
                    enemy8(enemy2x[i], enemy2y[i], i)
                    if distance1(drawert1, enemy2x[i], drawert2, enemy2y[i]) \
                            or distance1(drawert3, enemy2x[i], drawert4, enemy2y[i]) \
                            or distance1(drawert5, enemy2x[i], drawert6, enemy2y[i]):
                        enemy2x[i] = random.randrange(-50, 210)
                        enemy2y[i] = 330
                        kills += 1

            pygame.display.update()