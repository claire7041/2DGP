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
coin = None
jelly = None
obs = None
input = None
item = None
font = None

class Background:
    def __init__(self):
        self.bgm = load_music('resource/sound/bgm_main_rockstar.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.reviveSound = load_wav('resource/sound/r_unlock.wav')
        self.reviveSound.set_volume(128)
        self.dieSound = load_wav('resource/sound/die_sound.wav')
        self.dieSound.set_volume(128)
        self.rank = load_wav('resource/sound/r_medal.wav')
        self.rank.set_volume(128)
        self.soundCnt = 0
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
        self.image = load_image('resource/image/First_Background.png')
        self.image2 = load_image('resource/image/First_Background2.png')
        self.image3 = load_image('resource/image/First_ground.png')
        self.imageHp = load_image('resource/image/cookie_Hp.png')
        self.imageHpB = load_image('resource/image/cookie_HpBack.png')
        self.imageHp2 = load_image('resource/image/cookie_Hpend.png')
        self.imageHp3 = load_image('resource/image/cookie_HpStart.png')
        self.imageResult = load_image('resource/image/result.png')
        self.imageResult2 = load_image('resource/image/resultChoose.png')
        self.imageRecord = load_image('resource/image/record.png')
        self.Bonus = load_image('resource/image/BonusTime.png')
        self.Number = load_image('resource/image/number.png')
        self.scoreNumber = load_image('resource/image/Scorenumber.png')
        self.ResultNumber = load_image('resource/image/resultnumber.png')
        self.mycoin = load_image('resource/image/coin2.png')

    def update(self):
        if(self.hpF == 700 and self.hpBar < 50 and self.HpCnt == 0):
            if(self.revive == 1 and player_data[0]['Pet'] == 2):
                self.revive -= 1
                self.speed = 1
                self.HpCnt = 50
                pet.frame = 0
                self.reviveSound.play(2)
            else:
                if (self.soundCnt == 0):
                    self.dieSound.play(1)
                    self.soundCnt += 1
                self.finish = 2
        elif(self.hpF == 650 and self.hpBar < 15 and self.HpCnt == 0):
            if (self.revive == 1 and player_data[0]['Pet'] == 2):
                self.revive -= 1
                self.reviveSound.play(2)
                self.speed = 1
                self.HpCnt = 50
                pet.frame = 0
            else:
                if (self.soundCnt == 0):
                    self.dieSound.play(1)
                    self.soundCnt += 1
                    print("%d", self.finish)
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
                    if (self.soundCnt == 1):
                        self.rank.play(1)
                        self.soundCnt += 1
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

class Input:
    def __init__(self):
        self.inputkey = load_image('resource/image/input.png')
        self.name = load_image('resource/image/English.png')
        self.cnt = 0
        self.myname = []
        self.x, self.y = 150, 150

    def update(self):
        pass


    def draw(self):
        if(background.finish == 1):
            self.inputkey.clip_draw(0, 0, 250, 250, self.x, self.y)

            if(self.cnt == 1):
                self.name.clip_draw(self.myname[0] * 50, 0, 50, 50, 640, 163)
            elif(self.cnt == 2):
                self.name.clip_draw(self.myname[1] * 50, 0, 50, 50, 640, 163)
                self.name.clip_draw(self.myname[0] * 50, 0, 50, 50, 610, 163)
            elif(self.cnt == 3):
                self.name.clip_draw(self.myname[2] * 50, 0, 50, 50, 640, 163)
                self.name.clip_draw(self.myname[1] * 50, 0, 50, 50, 610, 163)
                self.name.clip_draw(self.myname[0] * 50, 0, 50, 50, 580, 163)


class Cookie:
    def __init__(self):
        self.x, self.y = 150, 150
        self.frame = 0
        self.height = 0
        self.dir = 1
        self.crushCnt = 0
        self.jumpTime = 0
        self.jumpNum = 0
        self.jumpCnt = 0
        self.slideNum = 0
        self.slideCnt = 0
        self.mychar = player_data[0]['Cookie']
        if (self.mychar == 0):
            self.image = load_image('resource/image/cookie_run.png')
            self.jump1 = load_image('resource/image/cookie_run_jump.png')
            self.jump2 = load_image('resource/image/cookie_run_jump2.png')
            self.slide1 = load_image('resource/image/cookie_run_slide.png')
            self.die = load_image('resource/image/cookie_die.png')
            self.crush = load_image('resource/image/cookie_crush.png')
            self.JumpSound1 = load_wav('resource/sound/ch03jump.wav')
            self.JumpSound1.set_volume(128)
            self.JumpSound2 = load_wav('resource/sound/ch06jump.wav')
            self.JumpSound2.set_volume(128)
            self.SlideSound1 = load_wav('resource/sound/ch03slide.wav')
            self.SlideSound1.set_volume(128)
            self.SlideSound2 = load_wav('resource/sound/ch01slide.wav')
            self.SlideSound2.set_volume(128)
        elif (self.mychar == 1):
            self.image = load_image('resource/image/pink_run.png')
            self.jump1 = load_image('resource/image/pink_jump.png')
            self.slide1 = load_image('resource/image/pink_slide.png')
            self.die = load_image('resource/image/pink_die.png')
            self.crush = load_image('resource/image/pink_crush.png')
            self.JumpSound1 = load_wav('resource/sound/ch24jump_woman.wav')
            self.JumpSound1.set_volume(128)
            self.JumpSound2 = load_wav('resource/sound/ch24jump.wav')
            self.JumpSound2.set_volume(128)
            self.SlideSound1 = load_wav('resource/sound/ch24slide.wav')
            self.SlideSound1.set_volume(128)
            self.SlideSound2 = load_wav('resource/sound/ch24slide_woman.wav')
            self.SlideSound2.set_volume(128)
        elif(self.mychar == 2):
            self.image = load_image('resource/image/moon_run.png')
            self.jump1 = load_image('resource/image/moon_jump.png')
            self.slide1 = load_image('resource/image/moon_slide.png')
            self.die = load_image('resource/image/moon_die.png')
            self.crush = load_image('resource/image/moon_crush.png')
            self.JumpSound1 = load_wav('resource/sound/ch18jump.wav')
            self.JumpSound1.set_volume(128)
            self.JumpSound2 = load_wav('resource/sound/ch20jump.wav')
            self.JumpSound2.set_volume(128)
            self.SlideSound1 = load_wav('resource/sound/ch20slide.wav')
            self.SlideSound1.set_volume(128)
            self.SlideSound2 = load_wav('resource/sound/ch18slide.wav')
            self.SlideSound2.set_volume(128)


    def update(self):
        delay(0.05)
        if(background.finish == 0 and background.HpCnt == 0):
            if(self.crushCnt == 0):
                if(self.jumpTime > 0 or self.y > 150):
                    if (self.jumpTime < 11 and self.y > 150):
                        self.dir = -1
                    elif (self.jumpTime == 11):
                        self.height = 0
                    elif (self.jumpTime > 11):
                        self.dir = 1
                    self.height += 2
                    self.y += self.height * self.dir
                    self.jumpTime -= 1
                    if(self.y <= 150):
                        self.y = 150
                        self.jumpTime = 0
                        self.jumpCnt = 0
                elif (self.slideCnt == 1 or self.y < 150):
                    self.y = 120
                elif(self.jumpTime == 0 or self.slideCnt == 0):
                    self.y = 150
                self.frame = (self.frame + 1) % 6
            else:
                self.crushCnt -= 1
                self.jumpTime = 0
                self.slideCnt = 0
        elif(background.finish == 2):
            if(self.y > 150):
                self.y -= 15


    def draw(self):
        if (self.mychar == 0):
            if(background.finish == 0):
                if(self.crushCnt != 0):
                    self.crush.clip_draw(0, 0, 100, 150, self.x, self.y)
                else:
                    if(self.jumpTime > 0):
                        if(self.jumpNum == 1 or self.jumpNum == 3):
                            self.jump1.clip_draw(0, 0, 75, 100, self.x, self.y)
                        else:
                            self.jump2.clip_draw(0, 0, 75, 100, self.x, self.y)
                    elif(self.slideCnt == 1):
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
                    if (self.jumpTime > 0):
                        if (self.jumpNum == 0):
                             self.jump1.clip_draw(0, 0, 115, 125, self.x, self.y)
                        elif(self.jumpNum == 1):
                            self.jump1.clip_draw(115, 0, 115, 125, self.x, self.y)
                        elif (self.jumpNum == 2):
                            self.jump1.clip_draw(230, 0, 115, 125, self.x, self.y)
                        else:
                            self.jump1.clip_draw(345, 0, 115, 125, self.x, self.y)
                    elif(self.slideCnt > 0):
                        if (self.slideNum == 0):
                            self.slide1.clip_draw(0, 0, 115, 125, self.x, self.y + 15)
                        elif (self.slideNum == 1):
                            self.slide1.clip_draw(115, 0, 115, 125, self.x, self.y + 15)
                        elif (self.slideNum == 2):
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
        if(self.jumpCnt < 2 and self.slideCnt == 0):
            self.height = 0
            self.jumpCnt += 1
            self.jumpTime = 22
            self.jumpNum = random.randint(0, 3)
            if(self.jumpNum <= 1 ):
                self.JumpSound1.play(1)
            else:
                self.JumpSound2.play(1)


    def slide(self):
        if(self.slideCnt == 0 and self.jumpCnt == 0):
            self.slideCnt = 1
            self.slideNum = random.randint(0, 3)
            if(self.slideNum <= 1):
                self.SlideSound2.play(1)
            else:
                self.SlideSound1.play(1)


class Pet:
    def __init__(self):
        self.x, self.y = 70, 200
        self.frame = 0
        self.height = 0
        self.dir = 1
        self.jumpTime = 0
        self.jumpCnt = 0
        self.mypet = player_data[0]['Pet']
        self.shield = load_image('resource/image/shield.png')
        self.shieldCnt = 0

        if (self.mypet == 0):
            self.image = load_image('resource/image/flower.png')
        elif (self.mypet == 1):
            self.image = load_image('resource/image/ghost.png')
            self.skillimage = load_image('resource/image/ghost_skill.png')
            self.shieldCnt = 1
        elif (self.mypet == 2):
            self.image = load_image('resource/image/star.png')
            self.skillimage = load_image('resource/image/star_skill.png')

    def update(self):
        if(background.finish == 0 and background.HpCnt == 0):
            if (self.jumpTime > 0 or self.y > 200):
                if (self.jumpTime < 11 and self.y > 200):
                    self.dir = -1
                elif (self.jumpTime == 11):
                    self.height = 0
                elif (self.jumpTime > 11):
                    self.dir = 1
                self.height += 2
                self.y += self.height * self.dir
                self.jumpTime -= 1
                if (self.y <= 200):
                    self.y = 200
                    self.jumpTime = 0
                    self.jumpCnt = 0
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
        if(self.jumpCnt < 2):
            self.height = 0
            self.jumpCnt += 1
            self.jumpTime = 22

class Coin:
    def __init__(self):
        self.coinsound = load_wav('resource/sound/g_coin.wav')
        self.coinsound.set_volume(64)
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
            elif (i >= 69 and i <= 75):
                if (i == 71 or i == 73):
                    self.pos.append((300 + (i * 50), 250, True, 0))
                elif (i == 70 or i == 74):
                    self.pos.append((300 + (i * 50), 230, True, 0))
                elif (i == 72):
                    self.pos.append((300 + (i * 50), 280, False, 1))
                else:
                    self.pos.append((300 + (i * 50), 190, True, 0))
            else:
                self.pos.append((300 + (i * 50), 150, False, 0))

        self.go = 0
        self.image = load_image('resource/image/coin.png')

    def update(self):
       if(background.finish == 0  and background.HpCnt == 0):
           self.go += 10
           for i in range(1000):
               if(self.pos[i][2] == True):
                   self.pos[i] = (self.pos[i][0], self.pos[i][1], True, (self.pos[i][3] + 1) % 6)
               if (self.pos[i][0] - self.go >= 100 and self.pos[i][0] - self.go <= 195 and (cookie.y - 50) <= self.pos[i][1] and (cookie.y + 75) >= self.pos[i][1] and self.pos[i][2] == True):
                   if(self.pos[i][2] == True):
                       self.coinsound.play(1)
                       self.pos[i] = (self.pos[i][0], self.pos[i][1], False, self.pos[i][3])
                       self.cnt += 1

    def draw(self):
        for i in range(1000):
            if(self.pos[i][2] == True):
                self.image.clip_draw(self.pos[i][3] * 44, 0, 44, 53, self.pos[i][0] - self.go, self.pos[i][1])

class Jelly:
    def __init__(self):
        self.jellysound = load_wav('resource/sound/g_jelly.wav')
        self.jellysound.set_volume(64)
        self.ijellysound = load_wav('resource/sound/g_ijelly.wav')
        self.ijellysound.set_volume(64)
        self.itemsound = load_wav('resource/sound/i_large_energy.wav')
        self.itemsound.set_volume(64)
        if(cookie.mychar == 1):
            self.bgm = load_music('resource/sound/bgm_fever2.mp3')
            self.bgm.set_volume(128)
        elif(cookie.mychar == 2):
            self.bgm = load_music('resource/sound/bgm_fever3.mp3')
            self.bgm.set_volume(128)
        self.pos = []
        self.cnt = 0
        self.moonItem = load_image('resource/image/moon_item.png')
        self.pinkItem = load_image('resource/image/pink_item.png')
        self.randPos = []
        for i in range(100):
            self.randPos.append((random.randint(0,1200), random.randint(50,500), True, 1))
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
            elif (i == 72):
                self.pos.append((300 + (i * 50), 280, True, 1))
            elif (i >= 6 and i <= 12 and i != 9):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif(i >= 21 and i <= 27 and i != 24):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif(i >= 33 and i <= 37):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif(i >= 54 and i <= 59):
                self.pos.append((300 + (i * 50), 150, False, 0))
            elif (i >= 69 and i <= 75):
                self.pos.append((300 + (i * 50), 150, False, 0))
            else:
                self.pos.append((300 + (i * 50), 150, True, 0))
        self.go = 0
        self.image = load_image('resource/image/Jelly.png')
        self.image2 = load_image('resource/image/Jelly2.png')
        self.heart = load_image('resource/image/heart.png')

    def update(self):
       if(background.finish == 0  and background.HpCnt == 0):
           self.go += 10

           if(self.go >= 1300 and self.go <= 1305):
               if (cookie.mychar == 1 or cookie.mychar == 2):
                   self.bgm.repeat_play()

           if (self.go == 2000):
                background.bgm.repeat_play()

           if (self.go >= 1300 and self.go <= 2000 and cookie.mychar != 0):
               for i in range(100):
                   if (self.randPos[i][2] == True):
                       self.randPos[i] = (self.randPos[i][0], self.randPos[i][1], True, self.randPos[i][3])
                       if (self.randPos[i][0] - self.go + 1300 >= 100 and self.randPos[i][0] - self.go + 1300 <= 195 and (cookie.y - 50) <= self.randPos[i][1] and (cookie.y + 75) >= self.randPos[i][1] and self.randPos[i][2] == True):
                           self.randPos[i] = (self.pos[i][0], self.pos[i][1], False, self.pos[i][3])
                           self.cnt += 1
                           self.ijellysound.play(1)

           for i in range(1000):
               if(self.pos[i][2] == True):
                   self.pos[i] = (self.pos[i][0], self.pos[i][1], True, self.pos[i][3])
               if (self.pos[i][0] - self.go >= 100 and self.pos[i][0] - self.go <= 195 and (cookie.y - 50) <= self.pos[i][1] and (cookie.y + 75) >= self.pos[i][1] and self.pos[i][2] == True):
                   if(self.pos[i][3] == 1):
                       background.hpBar += 50
                       background.HpTime -= 50
                       self.itemsound.play(1)

                   self.pos[i] = (self.pos[i][0], self.pos[i][1], False, self.pos[i][3])
                   if (background.hpBar > 400):
                       self.cnt += 1
                       self.jellysound.play(1)
                   else:
                       self.cnt += 2
                       self.ijellysound.play(1)

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

        if (self.go >= 1300 and self.go <= 2000):
            for i in range(100):
                if (self.randPos[i][2] == True):
                    if(cookie.mychar == 1):
                        self.pinkItem.clip_draw(0, 0, 44, 39, self.randPos[i][0] - self.go + 1300, self.randPos[i][1])
                    elif(cookie.mychar == 2):
                        self.moonItem.clip_draw(0, 0, 59, 67, self.randPos[i][0] - self.go + 1300, self.randPos[i][1])


class Obstacle:
    def __init__(self):
        self.shieldSound = load_wav('resource/sound/shield_sound.wav')
        self.shieldSound.set_volume(128)
        self.obSound1 = load_wav('resource/sound/g_obs1.wav')
        self.obSound1.set_volume(128)
        self.obSound2 = load_wav('resource/sound/g_obs2.wav')
        self.obSound2.set_volume(128)
        self.obSound3 = load_wav('resource/sound/g_obs3.wav')
        self.obSound3.set_volume(128)
        self.go = 0
        self.change = 1
        self.change2 = 0
        for obstacle in obstacle_data:
            if (obstacle['Type'] == 1):
                self.imageOb1 = load_image('resource/image/ob1_Fork.png')
            elif (obstacle['Type'] == 2):
                self.imageOb2 = load_image('resource/image/ob2_Fork.png')
            elif (obstacle['Type'] == 3):
                self.imageOb3 = load_image('resource/image/ob3_Fork.png')
            elif (obstacle['Type'] == 4):
                self.imageOb4 = load_image('resource/image/ob4_thorn.png')
            elif (obstacle['Type'] == 5):
                self.imageOb5 = load_image('resource/image/ob5_thorn.png')
            elif (obstacle['Type'] == 6):
                self.imageOb6 = load_image('resource/image/ob6_thorn.png')
            elif (obstacle['Type'] == 7):
                self.imageOb7 = load_image('resource/image/ob7_thorn.png')
            elif (obstacle['Type'] == 8):
                self.imageOb8 = load_image('resource/image/ob8_thorn.png')
            elif (obstacle['Type'] == 9):
                self.imageOb9 = load_image('resource/image/ob9_thorn.png')


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
                if(obstacle['Type'] == 2):
                    if (self.change2 == 1):
                        obstacle['y'] -= 1
                    else:
                        obstacle['y'] += 1
                    if (obstacle['y'] == 360):
                        self.change2 = 1
                    elif (obstacle['y'] == 350):
                        self.change2 = 0
                if (obstacle['x'] - self.go >= 100 and obstacle['x'] - self.go <= 195 and (cookie.y - 80) <= obstacle['y'] and (cookie.y + 200) >= obstacle['y'] and obstacle['Crash'] == True):
                    obstacle['Crash'] = False
                    if(pet.shieldCnt != 0):
                        self.shieldSound.play(1)
                        pet.shieldCnt = 0
                    else:
                        if(cookie.mychar == 0):
                            self.obSound1.play(1)
                        elif (cookie.mychar == 1):
                            self.obSound3.play(1)
                        elif (cookie.mychar == 2):
                            self.obSound2.play(1)

                        background.x += 30
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
    global cookie, background, pet, coin, jelly, obs, player_data, obstacle_data, input
    f = open('cookie_data.txt', 'r')
    player_data = json.load(f)
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
    input = Input()


def exit():
    global cookie, background, pet, coin, obs, jelly, input
    del(cookie)
    del(background)
    del(pet)
    del(coin)
    del(jelly)
    del(obs)
    del(input)


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y, click, ranking_data
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
            if cookie.slideCnt == 1:
                cookie.slideCnt = 0
                cookie.y = 150
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
            if (background.finish == 1 and x >= 295 and x <= 495 and y >= 122 and y <= 180):
                background.result = 1
            else:
                background.result = 0
        elif ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
            if(background.finish == 1 and input.x <= x and x <= input.x + 250 and y >= input.y and y <= input.y + 250 and input.cnt < 3):
                if(x >= 25 and x < 75):
                    if (y >= 25 and y < 75):
                        input.myname.append((20))
                    elif (y >= 75 and y < 125):
                        input.myname.append((15))
                    elif (y >= 125 and y < 175):
                        input.myname.append((10))
                    elif (y >= 175 and y < 225):
                        input.myname.append((5))
                    elif (y >= 225 and y < 275):
                        input.myname.append((0))
                elif(x >= 75 and x < 125):
                    if (y >= 25 and y < 75):
                        input.myname.append((21))
                    elif (y >= 75 and y < 125):
                        input.myname.append((16))
                    elif (y >= 125 and y < 175):
                        input.myname.append((11))
                    elif (y >= 175 and y < 225):
                        input.myname.append((6))
                    elif (y >= 225 and y < 275):
                        input.myname.append((1))
                elif(x >= 125 and x < 175):
                    if (y >= 25 and y < 75):
                        input.myname.append((22))
                    elif (y >= 75 and y < 125):
                        input.myname.append((17))
                    elif (y >= 125 and y < 175):
                        input.myname.append((12))
                    elif (y >= 175 and y < 225):
                        input.myname.append((7))
                    elif (y >= 225 and y < 275):
                        input.myname.append((2))
                elif(x >= 175 and x < 225):
                    if (y >= 25 and y < 75):
                        input.myname.append((23))
                    elif (y >= 75 and y < 125):
                        input.myname.append((18))
                    elif (y >= 125 and y < 175):
                        input.myname.append((13))
                    elif (y >= 175 and y < 225):
                        input.myname.append((8))
                    elif (y >= 225 and y < 275):
                        input.myname.append((3))
                elif (x >= 225 and x < 275):
                    if (y >= 25 and y < 75):
                        input.myname.append((24))
                    elif (y >= 75 and y < 125):
                        input.myname.append((19))
                    elif (y >= 125 and y < 175):
                        input.myname.append((14))
                    elif (y >= 175 and y < 225):
                        input.myname.append((9))
                    elif (y >= 225 and y < 275):
                        input.myname.append((4))
                input.cnt += 1
            if (background.result == 1):
                f = open('ranking_data.txt', 'r')
                ranking_data = json.load(f)
                f.close()

                ranking_data.append({"Coin": coin.cnt, "Score": jelly.cnt, "Name1": input.myname[0], "Name2": input.myname[1], "Name3": input.myname[2]})

                f = open('ranking_data.txt', 'w')
                json.dump(ranking_data, f)
                f.close()

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
    else:
        input.draw()

    update_canvas()
