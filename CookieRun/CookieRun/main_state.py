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
        self.hpBar = player_data[0]['Hp']
        self.hpF = player_data[0]['Hp']
        self.revive = 1
        self.hpC = 52
        self.HpTime = 0
        self.HpCnt = 0
        self.road = 0
        self.finish = 0
        self.finishCnt = 0
        self.result = 0
        self.goSpeed = player_data[0]['Speed']
        self.speed = 3
        self.scoreFrame1 = 0
        self.scoreFrame2 = 0
        self.scoreFrame3 = 0
        self.scoreFrame4 = 0
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
        if(self.hpF == 700 and self.hpBar < 50 and self.HpCnt == 0):
            if(self.revive == 1 and player_data[0]['Pet'] == 2):
                self.revive -= 1
                self.speed = 1
                self.HpCnt = 50
                pet.frame = 0
            else:
                self.finish = 2
        elif(self.hpF == 650 and self.hpBar < 15 and self.HpCnt == 0):
            if (self.revive == 1 and player_data[0]['Pet'] == 2):
                self.revive -= 1
                self.speed = 1
                self.HpCnt = 50
                pet.frame = 0
            else:
                self.finish = 2
        if(self.finish != 2 and self.HpCnt == 0):
            self.road += 10
            self.x -= self.goSpeed
            self.hpBar -= self.speed
            self.HpTime += self.speed
            if(self.hpBar < 500 and self.hpBar > 450):
                self.hpC += 1

        if(self.HpCnt == 0):
            if(self.road % 1000 == 0):
                self.speed += 1
            if(self.x <= - 400 and self.finish == 0):
                self.x = 400
            if(self.finish == 2):
                self.finishCnt += 1
                if(self.finishCnt > 20):
                    self.finish = 1
        elif(self.HpCnt > 0):
            self.HpCnt -= 1
            self.hpBar += 4
            self.HpTime -= 4

        self.numFrame1 = coin.cnt % 10
        self.numFrame2 = coin.cnt // 10
        self.numFrame3 = coin.cnt // 100
        self.numFrame4 = coin.cnt // 1000

        self.scoreFrame1 = (jelly.cnt) % 10
        self.scoreFrame2 = (jelly.cnt) // 10
        self.scoreFrame3 = (jelly.cnt) // 100
        self.scoreFrame4 = (jelly.cnt) // 1000

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x, self.y)
        self.image2.clip_draw(0, 0, 800, 600, self.x + 800, self.y)
        self.image3.clip_draw(0, 0, 800, 600, self.x, self.y)
        self.image3.clip_draw(0, 0, 800, 600, self.x + 800, self.y)
        if(self.hpF == 700):
            self.imageHpB.clip_draw(0, 0, self.hpF + 20, 70, self.hpF - 310, 536)
            self.imageHp.clip_draw(0, 0, self.hpBar, 70, 380 - (self.HpTime / 2), 537)
            self.imageHp2.clip_draw(0, 0, 30, 70, self.hpF + 25 - self.HpTime, 535)
        elif(self.hpF == 650):
            self.imageHpB.clip_draw(0, 0, self.hpF + 20, 70, self.hpF - 260, 536)
            self.imageHp.clip_draw(0, 0, self.hpBar + 20, 70, 380 - (self.HpTime / 2), 537)
            self.imageHp2.clip_draw(0, 0, 30, 70, self.hpF + self.hpC - self.HpTime, 535)
        self.imageHp3.clip_draw(0, 0, 50, 70, 60, 540)
        self.Bonus.clip_draw(0, 0, 200, 50, 120, 580)

        if ((jelly.cnt) < 10):
            self.scoreNumber.clip_draw(self.scoreFrame1 * 60, 0, 50, 120, 420, 560)
        elif ((jelly.cnt) >= 10 and (jelly.cnt) < 100):
            self.scoreNumber.clip_draw(self.scoreFrame1 * 60, 0, 50, 120, 420, 560)
            self.scoreNumber.clip_draw(self.scoreFrame2 * 60, 0, 50, 120, 380, 560)
        elif ((jelly.cnt) >= 100 and (jelly.cnt) < 1000):
            self.scoreNumber.clip_draw(self.scoreFrame1 * 60, 0, 50, 120, 420, 560)
            self.scoreNumber.clip_draw(self.scoreFrame2 * 60, 0, 50, 120, 380, 560)
            self.scoreNumber.clip_draw(self.scoreFrame3 * 60, 0, 50, 120, 340, 560)
        else:
            self.scoreNumber.clip_draw(self.scoreFrame1 * 60, 0, 50, 120, 420, 560)
            self.scoreNumber.clip_draw(self.scoreFrame2 * 60, 0, 50, 120, 380, 560)
            self.scoreNumber.clip_draw(self.scoreFrame3 * 60, 0, 50, 120, 340, 560)
            self.scoreNumber.clip_draw(self.scoreFrame4 * 60, 0, 50, 120, 300, 560)

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

            if ((jelly.cnt) < 10):
                self.ResultNumber.clip_draw(self.scoreFrame1 * 40, 0, 40, 70, 420, 343)
            elif ((jelly.cnt) >= 10 and (jelly.cnt) < 100):
                self.ResultNumber.clip_draw(self.scoreFrame1 * 40, 0, 40, 70, 420, 343)
                self.ResultNumber.clip_draw(self.scoreFrame2 * 40, 0, 40, 70, 400, 343)
            elif ((jelly.cnt) >= 100 and (jelly.cnt) < 1000):
                self.ResultNumber.clip_draw(self.scoreFrame1 * 40, 0, 40, 70, 420, 343)
                self.ResultNumber.clip_draw(self.scoreFrame2 * 40, 0, 40, 70, 400, 343)
                self.ResultNumber.clip_draw(self.scoreFrame3 * 40, 0, 40, 70, 380, 343)
            else:
                self.ResultNumber.clip_draw(self.scoreFrame1 * 40, 0, 40, 70, 420, 343)
                self.ResultNumber.clip_draw(self.scoreFrame2 * 40, 0, 40, 70, 400, 343)
                self.ResultNumber.clip_draw(self.scoreFrame3 * 40, 0, 40, 70, 380, 343)
                self.ResultNumber.clip_draw(self.scoreFrame4 * 40, 0, 40, 70, 360, 343)

        self.mycoin.clip_draw(0, 0, 50, 50, 665, 575)


class Cookie:
    def __init__(self):
        self.x, self.y = 150, 150
        self.frame = 0
        self.height = 0
        self.dir = 1
        self.crushCnt = 0
        self.jump_time = 0
        self.jumpnum = 0
        self.jump_cnt = 0
        self.slidenum = 0
        self.slide_cnt = 0
        self.mychar = player_data[0]['Cookie']
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
        if(background.finish == 0 and background.HpCnt == 0):
            if(self.crushCnt == 0):
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
            else:
                self.crushCnt -= 1
                self.jump_time = 0
                self.slide_cnt = 0
        elif(background.finish == 2):
            if(self.y > 150):
                self.y -= 15


    def draw(self):
        if (self.mychar == 0):
            if(background.finish == 0):
                if(self.crushCnt != 0):
                    self.crush.clip_draw(0, 0, 100, 150, self.x, self.y)
                else:
                    if(self.jump_time > 0):
                        if(self.jumpnum == 1 or self.jumpnum == 3):
                            self.jump1.clip_draw(0, 0, 75, 100, self.x, self.y)
                        else:
                            self.jump2.clip_draw(0, 0, 75, 100, self.x, self.y)
                    elif(self.slide_cnt == 1):
                        self.slide1.clip_draw(0, 0, 90, 65, self.x, self.y)
                    elif (background.HpCnt != 0):
                        self.die.clip_draw(0, 0, 150, 175, self.x, self.y - 10)
                    else:
                        self.image.clip_draw(self.frame * 75, 0, 75, 100, self.x, self.y)
            elif (background.finish == 2 or  background.HpCnt != 0):
                self.die.clip_draw(0, 0, 150, 175, self.x, self.y - 10)
        else:
            if(background.finish == 0):
                if (self.crushCnt != 0):
                    self.crush.clip_draw(0, 0, 115, 125, self.x, self.y)
                else:
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
                    elif (background.HpCnt != 0):
                        self.die.clip_draw(0, 0, 115, 125, self.x, self.y - 20)
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
        self.mypet = player_data[0]['Pet']
        self.shield = load_image('shield.png')
        self.shieldCnt = 0

        if (self.mypet == 0):
            self.image = load_image('flower.png')
        elif (self.mypet == 1):
            self.image = load_image('ghost.png')
            self.skillimage = load_image('ghost_skill.png')
            self.shieldCnt = 1
        elif (self.mypet == 2):
            self.image = load_image('star.png')
            self.skillimage = load_image('star_skill.png')

    def update(self):
        if(background.finish == 0 and background.HpCnt == 0):
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
        if(background.HpCnt > 0):
            self.frame = (self.frame + 1) % 7


    def draw(self):
        if(background.HpCnt != 0):
            self.skillimage.clip_draw(self.frame * 82, 0, 82, 100, self.x, self.y)
        else:
            if (self.shieldCnt != 0):
                self.shield.clip_draw(0, 0, 150, 150, cookie.x, cookie.y)
            if (self.mypet == 0):
                self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
            elif (self.mypet == 1 or self.mypet == 2):
                self.image.clip_draw(self.frame * 72, 0, 72, 100, self.x, self.y)


    def jump(self):
        if(self.jump_cnt < 2):
            self.height = 0
            self.jump_cnt += 1
            self.jump_time = 22

class Coin:
    def __init__(self):
        self.pos = []
        self.cnt = 0
        #for i in range(1000):
        #    for obstacle in obstacle_data:
        #        if(300 + (i * 50) >= obstacle['x'] and 300 + (i * 50) <= obstacle['x'] + obstacle['Size_x']):
        #            if(obstacle['y'] < 300):
        #                self.pos.append((300 + (i * 50), obstacle['y'] + 100, True, 0))
        #            else:
        #                self.pos.append((300 + (i * 50), 150, False, 0))
        #        else:
        #            self.pos.append((300 + (i * 50), 150, False, 0))
        for i in range(1000):
            if (i >= 6 and i <= 12):
                if(i == 7 or i == 11):
                    self.pos.append((300 + (i * 50), 230, True, 0))
                elif (i == 8 or i == 10):
                    self.pos.append((300 + (i * 50), 250, True, 0))
                elif (i == 9):
                    self.pos.append((300 + (i * 50), 280, False, 1))
                else:
                    self.pos.append((300 + (i * 50), 180, True, 0))
            elif(i >= 21 and i <= 27):
                if (i == 23 or i == 25):
                    self.pos.append((300 + (i * 50), 250, True, 0))
                elif (i == 22 or i == 26):
                    self.pos.append((300 + (i * 50), 230, True, 0))
                elif (i == 24):
                    self.pos.append((300 + (i * 50), 280, False, 1))
                else:
                    self.pos.append((300 + (i * 50), 190, True, 0))
            elif(i >= 33 and i <= 37):
                self.pos.append((300 + (i * 50), 190, True, 0))
            elif(i >= 54 and i <= 59):
                self.pos.append((300 + (i * 50), 220, True, 0))
            else:
                self.pos.append((300 + (i * 50), 150, False, 0))

        self.go = 0
        self.image = load_image('coin.png')

    def update(self):
       if(background.finish == 0  and background.HpCnt == 0):
           self.go += 10
           for i in range(1000):
               if(self.pos[i][2] == True):
                   self.pos[i] = (self.pos[i][0], self.pos[i][1], True, (self.pos[i][3] + 1) % 6)
               if (self.pos[i][0] - self.go >= 100 and self.pos[i][0] - self.go <= 195 and (cookie.y - 20) <= self.pos[i][1] and (cookie.y + 150) >= self.pos[i][1] and self.pos[i][2] == True):
                   if(self.pos[i][2] == True):
                       self.pos[i] = (self.pos[i][0], self.pos[i][1], False, self.pos[i][3])
                       self.cnt += 1

    def draw(self):
        for i in range(1000):
            if(self.pos[i][2] == True):
                self.image.clip_draw(self.pos[i][3] * 44, 0, 44, 53, self.pos[i][0] - self.go, self.pos[i][1])

class Jelly:
    def __init__(self):
        self.pos = []
        self.cnt = 0
        #for i in range(1000):
        #    for obstacle in obstacle_data:
        #        if(300 + (i * 50) >= obstacle['x'] and 300 + (i * 50) <= obstacle['x'] + obstacle['Size_x']):
        #            if(obstacle['y'] < 300):
        #                self.pos.append((300 + (i * 50), obstacle['y'] + 100, False, 0))
        #            else:
        #                self.pos.append((300 + (i * 50), 150, False, 0))
        #        else:
        #            self.pos.append((300 + (i * 50), 150, True, 0))
        for i in range(1000):
            if (i == 9):
                self.pos.append((300 + (i * 50), 280, True, 1))
            elif (i == 24):
                self.pos.append((300 + (i * 50), 280, True, 1))
            elif (i >= 6 and i <= 12 and i != 9):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif(i >= 21 and i <= 27 and i != 24):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif(i >= 33 and i <= 37):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif(i >= 54 and i <= 59):
                self.pos.append((300 + (i * 50), 150, False, 0))
            else:
                self.pos.append((300 + (i * 50), 150, True, 0))
        self.go = 0
        self.image = load_image('Jelly.png')
        self.image2 = load_image('Jelly2.png')
        self.heart = load_image('heart.png')

    def update(self):
       if(background.finish == 0  and background.HpCnt == 0):
           self.go += 10
           for i in range(1000):
               if(self.pos[i][2] == True):
                   self.pos[i] = (self.pos[i][0], self.pos[i][1], True, self.pos[i][3])
               if (self.pos[i][0] - self.go >= 100 and self.pos[i][0] - self.go <= 195 and (cookie.y - 20) <= self.pos[i][1] and (cookie.y + 150) >= self.pos[i][1] and self.pos[i][2] == True):
                   if(self.pos[i][3] == 1):
                       background.hpBar += 50
                       background.HpTime -= 50
                   self.pos[i] = (self.pos[i][0], self.pos[i][1], False, self.pos[i][3])
                   if (background.hpBar > 400):
                       self.cnt += 1
                   else:
                       self.cnt += 2

    def draw(self):
        for i in range(1000):
            if(self.pos[i][2] == True):
                if (self.pos[i][3] == 1):
                    self.heart.clip_draw(0, 0, 44, 53, self.pos[i][0] - self.go, self.pos[i][1])
                else:
                    if(background.hpBar > 400):
                        self.image2.clip_draw(0, 0, 30, 35, self.pos[i][0] - self.go, self.pos[i][1])
                    else:
                        self.image.clip_draw(0, 0, 30, 35, self.pos[i][0] - self.go, self.pos[i][1])


class Obstacle:
    def __init__(self):
        self.go = 0
        self.change = 1
        self.change2 = 0
        for obstacle in obstacle_data:
            if (obstacle['Type'] == 1):
                self.imageOb1 = load_image('ob1_Fork.png')
            elif (obstacle['Type'] == 2):
                self.imageOb2 = load_image('ob2_Fork.png')
            elif (obstacle['Type'] == 3):
                self.imageOb3 = load_image('ob3_Fork.png')
            elif (obstacle['Type'] == 4):
                self.imageOb4 = load_image('ob4_thorn.png')
            elif (obstacle['Type'] == 5):
                self.imageOb5 = load_image('ob5_thorn.png')
            elif (obstacle['Type'] == 6):
                self.imageOb6 = load_image('ob6_thorn.png')
            elif (obstacle['Type'] == 7):
                self.imageOb7 = load_image('ob7_thorn.png')
            elif (obstacle['Type'] == 8):
                self.imageOb8 = load_image('ob8_thorn.png')
            elif (obstacle['Type'] == 9):
                self.imageOb9 = load_image('ob9_thorn.png')


    def update(self):
        if(background.finish == 0  and background.HpCnt == 0):
            self.go += 10
            for obstacle in obstacle_data:
                if(obstacle['Type'] == 9):
                    if(self.change == 1):
                        obstacle['y'] -= 1
                    else:
                        obstacle['y'] += 1
                    if(obstacle['y'] > 127):
                        self.change = 1
                    elif(obstacle['y'] < 112):
                        self.change = 0
                if (obstacle['Type'] == 2):
                    if (self.change2 == 1):
                        obstacle['y'] -= 5
                    else:
                        obstacle['y'] += 5
                    if (obstacle['y'] == 360):
                        self.change2 = 1
                    elif (obstacle['y'] == 340):
                        self.change2 = 0
                if (obstacle['x'] - self.go >= 100 and obstacle['x'] - self.go <= 195 and (cookie.y - 30) <= obstacle['y'] and (cookie.y + 200) >= obstacle['y'] and obstacle['Crash'] == True):
                    obstacle['Crash'] = False
                    if(pet.shieldCnt != 0):
                        pet.shieldCnt = 0
                    else:
                        background.hpBar -= 50
                        background.HpTime += 50
                        cookie.crushCnt = 10
    def draw(self):
        for obstacle in obstacle_data:
            if(obstacle['Type'] == 1):
                self.imageOb1.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 2):
                self.imageOb2.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 3):
                self.imageOb3.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 4):
                self.imageOb4.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 5):
                self.imageOb5.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 6):
                self.imageOb6.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 7):
                self.imageOb7.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 8):
                self.imageOb8.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])
            elif (obstacle['Type'] == 9):
                self.imageOb9.clip_draw(0, 0, obstacle['Size_x'], obstacle['Size_y'], obstacle['x'] - self.go, obstacle['y'])


def enter():
    global cookie, background, pet, coin, jelly, obs, player_data, obstacle_data
    f = open('cookie_data.txt', 'r')
    player_data = json.load(f)
    f.close()
    obstacle_data = [
        {"x": 1100, "y": 350, "Type": 1, "Size_x": 80, "Size_y": 348, "Crash": True},
        {"x": 1200, "y": 350, "Type": 1, "Size_x": 80, "Size_y": 348, "Crash": True},
        {"x": 2400, "y": 340, "Type": 2, "Size_x": 67, "Size_y": 241, "Crash": True},
        {"x": 2500, "y": 340, "Type": 2, "Size_x": 67, "Size_y": 241, "Crash": True},
        {"x": 2600, "y": 340, "Type": 2, "Size_x": 67, "Size_y": 241, "Crash": True},
        {"x": 3000, "y": 125, "Type": 3, "Size_x": 50, "Size_y": 60, "Crash": True},
        {"x": 1400, "y": 125, "Type": 4, "Size_x": 34, "Size_y": 50, "Crash": True},
        {"x": 1500, "y": 145, "Type": 5, "Size_x": 42, "Size_y": 94, "Crash": True},
        {"x": 1600, "y": 125, "Type": 4, "Size_x": 34, "Size_y": 50, "Crash": True},
        {"x": 2000, "y": 125, "Type": 6, "Size_x": 30, "Size_y": 50, "Crash": True},
        {"x": 2050, "y": 125, "Type": 6, "Size_x": 30, "Size_y": 50, "Crash": True},
        {"x": 2100, "y": 125, "Type": 6, "Size_x": 30, "Size_y": 50, "Crash": True},
        {"x": 3100, "y": 139, "Type": 7, "Size_x": 42, "Size_y": 78, "Crash": True},
        {"x": 3200, "y": 128, "Type": 8, "Size_x": 50, "Size_y": 60, "Crash": True},
        {"x": 700, "y": 122, "Type": 9, "Size_x": 50, "Size_y": 60, "Crash": True},
        {"x": 750, "y": 122, "Type": 9, "Size_x": 50, "Size_y": 60, "Crash": True},
        {"x": 800, "y": 122, "Type": 9, "Size_x": 50, "Size_y": 60, "Crash": True}

    ]

    f = open('obstacle_data.txt', 'w')
    json.dump(obstacle_data, f)
    f.close()

    f = open('obstacle_data.txt', 'r')
    obstacle_data = json.load(f)
    f.close()
    background = Background()
    cookie = Cookie()
    pet = Pet()
    coin = Coin()
    jelly = Jelly()
    obs = Obstacle()


def exit():
    global cookie, background, pet, coin, obs, jelly
    del(cookie)
    del(background)
    del(pet)
    del(coin)
    del(jelly)
    del(obs)


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
            #if event.key == SDLK_ESCAPE:
            #    game_framework.change_state(interface_state)
            if event.key == SDLK_SPACE:
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
        jelly.update()
        obs.update()


def draw():
    delay(0.001)
    clear_canvas()
    background.draw()
    if(background.finish != 1):
        coin.draw()
        jelly.draw()
        pet.draw()
        obs.draw()
        cookie.draw()

    update_canvas()
