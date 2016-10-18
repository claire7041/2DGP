import random
import json
import os

from pico2d import *
from datetime import *

import time
import game_framework
import title_state
import main_state4


name = "MainState"

cookie = None
ground = None
second_background = None
font = None

class Third_Background:
    def __init__(self):
        self.X = 400
        self.Y = 400
        self.Speed = 5
        self.frame = 0
        self.image = load_image('Image\\Third_Background.png')
        self.image2 = load_image('Image\\Third_Background2.png')


    def update(self):
        self.X = self.X + self.Speed
        self.frame = self.frame + 1
        if self.frame % 10 == 0:
            self.Speed += 0.1
        if self.X >= 400 + self.Speed:
            self.X = 405 + self.Speed

    def draw(self):
        self.image.draw(self.X, self.Y)
        self.image2.draw(self.X - 800, self.Y)

class Third_ground:
    def __init__(self):
        self.First = 400
        self.ground_X = -400
        self.ground_Y = 400
        self.scroll_X = 400
        self.Speed = 15
        self.frame = 0
        self.First_ground_1 = load_image('Image\\Third_ground_1.png')
        self.First_ground_2 = load_image('Image\\Third_ground_2.png')
        self.First_ground_3 = load_image('Image\\Third_ground_3.png')
        self.First_ground_4 = load_image('Image\\Third_ground_4.png')
        self.First_ground_5 = load_image('Image\\Third_ground_5.png')
        self.First_ground_6 = load_image('Image\\Third_ground_6.png')

    def update(self):
        self.First = self.First + self.Speed
        self.ground_X = self.ground_X + self.Speed
        self.frame = self.frame + 1
        if self.frame % 10 == 0:
            self.Speed += 0.1
        if self.First >= 1600 + self.Speed:
            self.First = -3185 + self.Speed
        if self.ground_X >= 4400 + self.Speed:
            self.ground_X = -385 + self.Speed

    def draw(self):
        self.First_ground_1.draw(self.First, self.ground_Y)
        self.First_ground_2.draw(self.ground_X, self.ground_Y)
        self.First_ground_3.draw(self.ground_X - (self.scroll_X * 2), self.ground_Y)
        self.First_ground_4.draw(self.ground_X - (self.scroll_X * 4), self.ground_Y)
        self.First_ground_5.draw(self.ground_X - (self.scroll_X * 6), self.ground_Y)
        self.First_ground_6.draw(self.ground_X - (self.scroll_X * 8), self.ground_Y)


class Cookie:
    def __init__(self):
        self.X, self.Y = 650, 560
        self.frame = 0
        self.state = "Run"
        self.image = load_image('Image\\cookie_run3.png')
        self.slide_image = load_image('Image\\cookie_run_slide3.png')
        self.jump_image = load_image('Image\\cookie_run_jump2_3.png')
        self.jump_image2 = load_image('Image\\cookie_run_jump_3.png')
        self.dir = 0
        self.gravityY = 0

    def gravity(self):
        if (self.Y + 45 + self.gravityY) < 605:
            self.gravityY += 4
            self.Y += self.gravityY
        else:
            self.Y = 560
            self.gravityY = 0

    def update(self):
        self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jump" and self.state == "Slide":
            self.frame = 0
        elif self.state == "Jump" and self.Y >= 550:
            self.state = "Run"
        '''self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1'''

    def draw(self):
        if self.state == "Run":
            self.image.clip_draw(self.frame * 75, 0, 75, 87, self.X, self.Y)
        elif self.state == "Slide":
            self.slide_image.draw(self.X, self.Y + 17)
        elif self.state == "Jump":
            if self.dir % 2 == 1:
                self.jump_image.draw(self.X, self.Y)
            elif self.dir % 2 == 0:
                self.jump_image2.draw(self.X, self.Y)

def enter():
    global cookie, ground, Third_background
    cookie = Cookie()
    ground = Third_ground()
    Third_background = Third_Background()


def exit():
    global cookie, ground, Third_background
    del(cookie)
    del(ground)
    del(Third_background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global jump
    global cookie
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                cookie.state = "Slide"
            elif event.key == SDLK_UP:
                cookie.state = "Jump"
                cookie.dir += 1
                if (cookie.Y + 45) == 605:
                    cookie.gravityY = -35
            elif event.key == SDLK_4:
                game_framework.change_state(main_state4)

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                cookie.state = "Run"
            '''elif event.key == SDLK_UP:
                cookie.state = "Run"'''

        '''elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if (cookie.Y - 45) == 195:
                cookie.gravityY = -35'''
                # cookie.state = cookie.JUMP



def update():
    Third_background.update()
    ground.update()
    cookie.update()


def draw():
    clear_canvas()
    Third_background.draw()
    ground.draw()
    cookie.draw()
    update_canvas()
    delay(0.03)





