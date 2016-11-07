import random
import json
import os

from pico2d import *

import game_framework
import interface_state

name = "MainState"

cookie = None
background = None
pet = None
item = None
font = None

class Background:
    def __init__(self):
        self.x, self.y = 400, 300
        self.hpBar = 700
        self.HpTime = 0
        self.road = 0
        self.finish = 0
        self.finishCnt = 0
        self.result = 0
        self.speed = 3
        self.numFrame = 0
        self.numFrame1 = 0
        self.numFrame2 = 0
        self.numFrame3 = 0
        self.numFrame4 = 0
        self.image = load_image('First_Background.png')
        self.image2 = load_image('First_Background2.png')
        self.image3 = load_image('First_ground.png')
        self.imageHp = load_image('cookie_Hp.png')
        self.imageHpB = load_image('cookie_HpBack.png')
        self.imageHp2 = load_image('cookie_Hpend.png')
        self.imageHp3 = load_image('cookie_HpStart.png')
        self.imageResult = load_image('result.png')
        self.imageResult2 = load_image('resultChoose.png')
        self.imageRecord = load_image('record.png')
        self.Bonus = load_image('BonusTime.png')
        self.Number = load_image('number.png')
        self.scoreNumber = load_image('Scorenumber.png')
        self.ResultNumber = load_image('resultnumber.png')
        self.mycoin = load_image('coin2.png')

    def update(self):
        if(self.hpBar < 50):
            self.finish = 2
        else:
            self.road += 10
            self.x -= 10
            self.hpBar -= self.speed
            self.HpTime += self.speed
        if(self.road % 500 == 0):
            self.speed += 1
        if(self.x <= - 400 and self.finish == 0):
            self.x = 400
        if(self.finish == 2):
            self.finishCnt += 1
            if(self.finishCnt > 20):
                self.finish = 1

        self.numFrame1 = coin.cnt % 10
        self.numFrame2 = coin.cnt // 10
        self.numFrame3 = coin.cnt // 100
        self.numFrame4 = coin.cnt // 1000


    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x, self.y)
        self.image2.clip_draw(0, 0, 800, 600, self.x + 800, self.y)
        self.image3.clip_draw(0, 0, 800, 600, self.x, self.y)
        self.image3.clip_draw(0, 0, 800, 600, self.x + 800, self.y)
        self.imageHpB.clip_draw(0, 0, 740, 70, 390, 536)
        self.imageHp.clip_draw(0, 0, self.hpBar, 70, 380 - (self.HpTime / 2), 537)
        self.imageHp2.clip_draw(0, 0, 30, 70, 724 - self.HpTime, 535)
        self.imageHp3.clip_draw(0, 0, 50, 70, 60, 540)
        self.Bonus.clip_draw(0, 0, 200, 50, 120, 580)
        self.scoreNumber.clip_draw(self.numFrame * 60, 0, 50, 120, 420, 560)

        if(coin.cnt < 10):
            self.Number.clip_draw(self.numFrame1 * 40, 0, 40, 100, 760, 575)
        elif(coin.cnt >= 10 and coin.cnt < 100):
            self.Number.clip_draw(self.numFrame1 * 40, 0, 40, 100, 760, 575)
            self.Number.clip_draw(self.numFrame2 * 40, 0, 40, 100, 740, 575)
        elif(coin.cnt >= 100 and coin.cnt < 1000):
            self.Number.clip_draw(self.numFrame1 * 40, 0, 40, 100, 760, 575)
            self.Number.clip_draw(self.numFrame2 * 40, 0, 40, 100, 740, 575)
            self.Number.clip_draw(self.numFrame3 * 40, 0, 40, 100, 720, 575)
        else:
            self.Number.clip_draw(self.numFrame1 * 40, 0, 40, 100, 760, 575)
            self.Number.clip_draw(self.numFrame2 * 40, 0, 40, 100, 740, 575)
            self.Number.clip_draw(self.numFrame3 * 40, 0, 40, 100, 720, 575)
            self.Number.clip_draw(self.numFrame4 * 40, 0, 40, 100, 700, 575)

        if(self.finish == 1):
            if(self.result == 0):
                self.imageResult.clip_draw(0, 0, 700, 400, 400, 300)
            else:
                self.imageResult2.clip_draw(0, 0, 700, 400, 400, 300)
            if (coin.cnt < 10):
                self.ResultNumber.clip_draw(self.numFrame1 * 40, 0, 40, 70, 640, 263)
            elif (coin.cnt >= 10 and coin.cnt < 100):
                self.ResultNumber.clip_draw(self.numFrame1 * 40, 0, 40, 70, 640, 263)
                self.ResultNumber.clip_draw(self.numFrame2 * 40, 0, 40, 70, 620, 263)
            elif (coin.cnt >= 100 and coin.cnt < 1000):
                self.ResultNumber.clip_draw(self.numFrame1 * 40, 0, 40, 70, 640, 263)
                self.ResultNumber.clip_draw(self.numFrame2 * 40, 0, 40, 70, 620, 263)
                self.ResultNumber.clip_draw(self.numFrame3 * 40, 0, 40, 70, 600, 263)
            else:
                self.ResultNumber.clip_draw(self.numFrame1 * 40, 0, 40, 70, 640, 263)
                self.ResultNumber.clip_draw(self.numFrame2 * 40, 0, 40, 70, 620, 263)
                self.ResultNumber.clip_draw(self.numFrame3 * 40, 0, 40, 70, 600, 263)
                self.ResultNumber.clip_draw(self.numFrame4 * 40, 0, 40, 70, 580, 263)

        self.mycoin.clip_draw(0, 0, 50, 50, 665, 575)


class Cookie:
    def __init__(self):
        self.x, self.y = 150, 150
        self.frame = 0
        self.height = 0
        self.dir = 1
        self.jump_time = 0
        self.jumpnum = 0
        self.jump_cnt = 0
        self.slidenum = 0
        self.slide_cnt = 0
        self.mychar = player_data[0]["Cookie"]
        if (self.mychar == 0):
            self.image = load_image('cookie_run.png')
            self.jump1 = load_image('cookie_run_jump.png')
            self.jump2 = load_image('cookie_run_jump2.png')
            self.slide1 = load_image('cookie_run_slide.png')
            self.die = load_image('cookie_die.png')
            self.crush = load_image('cookie_crush.png')
        elif (self.mychar == 1):
            self.image = load_image('pink_run.png')
            self.jump1 = load_image('pink_jump.png')
            self.slide1 = load_image('pink_slide.png')
            self.die = load_image('pink_die.png')
            self.crush = load_image('pink_crush.png')
        elif(self.mychar == 2):
            self.image = load_image('moon_run.png')
            self.jump1 = load_image('moon_jump.png')
            self.slide1 = load_image('moon_slide.png')
            self.die = load_image('moon_die.png')
            self.crush = load_image('moon_crush.png')



    def update(self):
        delay(0.05)
        if(background.finish == 0):
            if(self.jump_time > 0 or self.y > 150):
                if (self.jump_time < 11 and self.y > 150):
                    self.dir = -1
                elif (self.jump_time == 11):
                    self.height = 0
                elif (self.jump_time > 11):
                    self.dir = 1
                self.height += 2
                self.y += self.height * self.dir
                self.jump_time -= 1
                if(self.y <= 150):
                    self.y = 150
                    self.jump_time = 0
                    self.jump_cnt = 0
            elif (self.slide_cnt == 1 or self.y < 150):
                self.y = 120
            elif(self.jump_time == 0 or self.slide_cnt == 0):
                self.y = 150

            self.frame = (self.frame + 1) % 6
        elif(background.finish == 2):
            if(self.y > 150):
                self.y -= 15


    def draw(self):
        if (self.mychar == 0):
            if(background.finish == 0):
                if(self.jump_time > 0):
                    if(self.jumpnum == 1 or self.jumpnum == 3):
                        self.jump1.clip_draw(0, 0, 75, 100, self.x, self.y)
                    else:
                        self.jump2.clip_draw(0, 0, 75, 100, self.x, self.y)
                elif(self.slide_cnt == 1):
                    self.slide1.clip_draw(0, 0, 90, 65, self.x, self.y)
                else:
                    self.image.clip_draw(self.frame * 75, 0, 75, 100, self.x, self.y)
            elif (background.finish == 2):
                self.die.clip_draw(0, 0, 150, 175, self.x, self.y - 10)
        else:
            if(background.finish == 0):
                if (self.jump_time > 0):
                    if (self.jumpnum == 0):
                         self.jump1.clip_draw(0, 0, 115, 125, self.x, self.y)
                    elif(self.jumpnum == 1):
                        self.jump1.clip_draw(115, 0, 115, 125, self.x, self.y)
                    elif (self.jumpnum == 2):
                        self.jump1.clip_draw(230, 0, 115, 125, self.x, self.y)
                    else:
                        self.jump1.clip_draw(345, 0, 115, 125, self.x, self.y)
                elif(self.slide_cnt > 0):
                    if (self.slidenum == 0):
                        self.slide1.clip_draw(0, 0, 115, 125, self.x, self.y + 15)
                    elif (self.slidenum == 1):
                        self.slide1.clip_draw(115, 0, 115, 125, self.x, self.y + 15)
                    elif (self.slidenum == 2):
                        self.slide1.clip_draw(230, 0, 115, 125, self.x, self.y + 15)
                    else:
                        self.slide1.clip_draw(345, 0, 115, 125, self.x, self.y + 15)
                else:
                    self.image.clip_draw(self.frame * 117, 0, 115, 110, self.x, self.y + 5)
            elif (background.finish == 2):
                self.die.clip_draw(0, 0, 115, 125, self.x, self.y - 20)

    def jump(self):
        if(self.jump_cnt < 2 and self.slide_cnt == 0):
            self.height = 0
            self.jump_cnt += 1
            self.jump_time = 22
            self.jumpnum = random.randint(0, 3)


    def slide(self):
        if(self.slide_cnt == 0 and self.jump_cnt == 0):
            self.slide_cnt = 1
            self.slidenum = random.randint(0, 3)


class Pet:
    def __init__(self):
        self.x, self.y = 70, 200
        self.frame = 0
        self.height = 0
        self.dir = 1
        self.jump_time = 0
        self.jump_cnt = 0
        self.mypet = player_data[0]["Pet"]

        if (self.mypet == 0):
            self.image = load_image('flower.png')
        elif (self.mypet == 1):
            self.image2 = load_image('ghost.png')
        elif (self.mypet == 2):
            self.image3 = load_image('star.png')

    def update(self):
        if(background.finish == 0):
            if (self.jump_time > 0 or self.y > 200):
                if (self.jump_time < 11 and self.y > 200):
                    self.dir = -1
                elif (self.jump_time == 11):
                    self.height = 0
                elif (self.jump_time > 11):
                    self.dir = 1
                self.height += 2
                self.y += self.height * self.dir
                self.jump_time -= 1
                if (self.y <= 200):
                    self.y = 200
                    self.jump_time = 0
                    self.jump_cnt = 0

            self.frame = (self.frame + 1) % 7

    def draw(self):
        if (self.mypet == 0):
            self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
        elif (self.mypet == 1):
            self.image2.clip_draw(self.frame * 72, 0, 72, 100, self.x, self.y)
        elif (self.mypet == 2):
            self.image3.clip_draw(self.frame * 72, 0, 72, 100, self.x, self.y)

    def jump(self):
        if(self.jump_cnt < 2):
            self.height = 0
            self.jump_cnt += 1
            self.jump_time = 22

class Coin:
    def __init__(self):
        self.cookiePos = 150
        self.pos = []
        self.cnt = 0
        for i in range(100):
            self.pos.append((500 + (i * 50), 140, True, 0))
        self.go = 0
        self.image = load_image('coin.png')

    def update(self):
        if(background.finish == 0):
            self.go += 10
            for i in range(100):
                if(self.pos[i][2] == True):
                    self.pos[i] = (self.pos[i][0], self.pos[i][1], True, (self.pos[i][3] + 1) % 6)
                if (self.pos[i][0] - self.go >= 100 and self.pos[i][0] - self.go <= 195 and (self.cookiePos - 20) <= self.pos[i][1] and (self.cookiePos + 150) >= self.pos[i][1] and self.pos[i][2] == True):
                    self.pos[i] = (self.pos[i][0], self.pos[i][1], False, self.pos[i][3])
                    self.cnt += 1

    def draw(self):
        for i in range(100):
            if(self.pos[i][2] == True):
                self.image.clip_draw(self.pos[i][3] * 44, 0, 44, 53, self.pos[i][0] - self.go, self.pos[i][1])



def enter():
    global cookie, background, pet, coin, player_data
    background = Background()
    f = open('data_file.txt', 'r')
    player_data = json.load(f)
    f.close()
    cookie = Cookie()
    pet = Pet()
    coin = Coin()





def exit():
    global cookie, background, pet, coin
    del(cookie)
    del(background)
    del(pet)
    del(coin)


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y, click
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(interface_state)
            elif event.key == SDLK_SPACE:
                cookie.jump()
                pet.jump()
            elif event.key == SDLK_DOWN:
                cookie.slide()
        elif event.type == SDL_KEYUP:
            if cookie.slide_cnt == 1:
                cookie.slide_cnt = 0
                cookie.y = 150
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
            if (background.finish == 1 and  x >= 295 and x <= 495 and y >= 122 and y <= 180):
                background.result = 1
            else:
                background.result = 0
        elif ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT) and  background.result == 1):
                game_framework.change_state(interface_state)



def update():
    coin.cookiePos = cookie.y
    background.update()
    if(background.finish != 1):
        cookie.update()
        pet.update()
        coin.update()


def draw():
    delay(0.001)
    clear_canvas()
    background.draw()
    if(background.finish != 1):
        coin.draw()
        pet.draw()
        cookie.draw()
    update_canvas()
