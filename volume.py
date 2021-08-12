import sys
import time
import pygame
from pygame import mixer

from screen import Screen
import os


def Volume():
    sound = .4
    volume = True
    screen = Screen()
    icon = pygame.image.load(os.path.join("assets", "troll.png")).convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Tower Defence")
    volume1 = pygame.image.load(os.path.join("assets", "volume1.png")).convert_alpha()
    volume2 = pygame.image.load(os.path.join("assets", "volume2.png")).convert_alpha()
    volume3 = pygame.image.load(os.path.join("assets", "volume3.png")).convert_alpha()
    mute = pygame.image.load(os.path.join("assets", "mute.png")).convert_alpha()
    background = pygame.image.load(os.path.join("assets", "bg.png")).convert_alpha()
    text = pygame.image.load(os.path.join("assets", "text.png")).convert_alpha()
    paused = pygame.image.load(os.path.join("assets", "paused.png")).convert_alpha()
    exit = pygame.image.load(os.path.join("assets", "exit.png")).convert_alpha()
    mm = pygame.image.load(os.path.join("assets", "mainmenu.png")).convert_alpha()

    while volume:
        screen.blit(background, (0, 0))
        screen.blit(mute, (825, 10))
        screen.blit(volume1, (870, 10))
        screen.blit(volume2, (915, 10))
        screen.blit(volume3, (960, 10))
        screen.blit(text, (840, 50))
        screen.blit(paused, (150, 200))
        screen.blit(exit, (20, 20))
        screen.blit(mm, (340, 545))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos1, pos2 = pygame.mouse.get_pos()
                if pos1 >= 956 and pos1 <= 992 and pos2 >= 6 and pos2 <= 40:
                    sound = 1
                    mixer.init()
                    mixer.music.load("press.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                    time.sleep(.2)
                    volume = False
                    mixer.music.load("music.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                if pos1 <= 944 and pos1 >= 913 and pos2 >= 6 and pos2 <= 40:
                    sound = 0.4
                    mixer.init()
                    mixer.music.load("press.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                    time.sleep(.2)
                    volume = False
                    mixer.music.load("music.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                if pos1 <= 894 and pos1 >= 870 and pos2 >= 6 and pos2 <= 40:
                    sound = 0.06
                    mixer.init()
                    mixer.music.load("press.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                    time.sleep(.2)
                    volume = False
                    mixer.music.load("music.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                if pos1 <= 857 and pos1 >= 825 and pos2 >= 6 and pos2 <= 40:
                    sound = 0
                    mixer.init()
                    mixer.music.load("press.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                    time.sleep(.2)
                    volume = False
                if pos1 <= 138 and pos1 >= 0 and pos2 >= 0 and pos2 <=153:
                    mixer.init()
                    mixer.music.load("press.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                    time.sleep(.2)
                    volume = False
                    mixer.music.load("music.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                if pos1 <= 635 and pos1 >= 338 and pos2 >= 554 and pos2 <= 611:
                    mixer.init()
                    mixer.music.load("press.wav")
                    mixer.music.set_volume(sound)
                    mixer.music.play()
                    time.sleep(.2)
                    volume = False
                    sound = 5.384739430

    return sound