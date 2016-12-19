import game_framework
import main_state
import json
from pico2d import *

name = "InterfaceState"

image = None
imagestart = None
imagecookie = None
imagepet = None
cookie = None
pet = None
charChoice = None
petChoice = None
rank = None

class Ranking:
    def __init__(self):
        self.bgm = load_music('interface_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.x, self.y = 580, 550
        self.x2, self.y2 = 350, 480
        self.coin = ranking_data[0]['Coin']
        self.score = []
        self.myname1 = []
        self.myname2 = []
        self.myname3 = []
        self.myname1.append((ranking_data[0]['Name1']))
        self.myname1.append((ranking_data[0]['Name2']))
        self.myname1.append((ranking_data[0]['Name3']))
        self.myname2.append((ranking_data[1]['Name1']))
        self.myname2.append((ranking_data[1]['Name2']))
        self.myname2.append((ranking_data[1]['Name3']))
        self.myname3.append((ranking_data[2]['Name1']))
        self.myname3.append((ranking_data[2]['Name2']))
        self.myname3.append((ranking_data[2]['Name3']))

        for i in range(3):
            self.score.append((ranking_data[i]['Score']))

        self.frame1 = 0
        self.frame2 = 0
        self.frame3 = 0
        self.frame4 = 0
        self.scoreFrame = []
        for i in range(12):
            self.scoreFrame.append((0))
        self.srank = load_image('scoreRank.png')
        self.image = load_image('myCoin.png')
        self.Number = load_image('number.png')
        self.ResultNumber = load_image('resultnumber.png')
        self.name = load_image('English.png')

    def update(self):
        self.frame1 = self.coin % 10
        self.frame2 = self.coin // 10
        self.frame3 = self.coin // 100
        self.frame4 = self.coin // 1000

        self.scoreFrame[0] = self.score[0] % 10
        self.scoreFrame[1] = self.score[0] // 10
        self.scoreFrame[2] = self.score[0] // 100
        self.scoreFrame[3] = self.score[0] // 1000
        self.scoreFrame[4] = self.score[1] % 10
        self.scoreFrame[5] = self.score[1] // 10
        self.scoreFrame[6] = self.score[1] // 100
        self.scoreFrame[7] = self.score[1] // 1000
        self.scoreFrame[8] = self.score[2] % 10
        self.scoreFrame[9] = self.score[2] // 10
        self.scoreFrame[10] = self.score[2] // 100
        self.scoreFrame[11] = self.score[2] // 1000

    def draw(self):
        self.srank.clip_draw(0, 0, 289, 185, self.x2 - 100, self.y2 - 20)
        self.image.clip_draw(0, 0, 200, 70, self.x + 75, self.y)
        self.image.clip_draw(0, 0, 200, 70, self.x + 75, self.y)
        if (self.coin < 10):
            self.Number.clip_draw(self.frame1 * 40, 0, 40, 100, self.x + 120, self.y)
        elif (self.coin >= 10 and self.coin < 100):
            self.Number.clip_draw(self.frame1 * 40, 0, 40, 100, self.x + 120, self.y)
            self.Number.clip_draw(self.frame2 * 40, 0, 40, 100, self.x + 100, self.y)
        elif (self.coin >= 100 and self.coin < 1000):
            self.Number.clip_draw(self.frame1 * 40, 0, 40, 100, self.x + 120, self.y)
            self.Number.clip_draw(self.frame2 * 40, 0, 40, 100, self.x + 100, self.y)
            self.Number.clip_draw(self.frame3 * 40, 0, 40, 100, self.x + 80, self.y)
        else:
            self.Number.clip_draw(self.frame1 * 40, 0, 40, 100, self.x + 120, self.y)
            self.Number.clip_draw(self.frame2 * 40, 0, 40, 100, self.x + 100, self.y)
            self.Number.clip_draw(self.frame3 * 40, 0, 40, 100, self.x + 80, self.y)
            self.Number.clip_draw(self.frame4 * 40, 0, 40, 100, self.x + 60, self.y)

        for i in range(3):
            self.name.clip_draw(self.myname1[i] * 50, 0, 50, 50, self.x2 - (170 - (i * 30)), self.y2 + 10)
        for i in range(3):
            self.name.clip_draw(self.myname2[i] * 50, 0, 50, 50, self.x2 - (170 - (i * 30)), self.y2 - 35)
        for i in range(3):
            self.name.clip_draw(self.myname3[i] * 50, 0, 50, 50, self.x2 - (170 - (i * 30)), self.y2 - 80)

        for i in range(3):
            if (self.score[i] < 10):
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4] * 40, 0, 40, 70, self.x2, self.y2 - (i * 50))
            elif (self.score[i] >= 10 and self.score[i] < 100):
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4] * 40, 0, 40, 70, self.x2, self.y2 - (i * 50))
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4 + 1] * 40, 0, 40, 70, self.x2 - 30, self.y2 - (i * 50))
            elif (self.score[i] >= 100 and self.score[i] < 1000):
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4] * 40, 0, 40, 70, self.x2, self.y2 - (i * 50))
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4 + 1] * 40, 0, 40, 70, self.x2 - 30, self.y2 - (i * 50))
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4 + 2] * 40, 0, 40, 70, self.x2 - 60, self.y2 - (i * 50))
            else:
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4] * 40, 0, 40, 70, self.x2, self.y2 - (i * 50))
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4 + 1] * 40, 0, 40, 70, self.x2 - 30, self.y2 - (i * 50))
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4 + 2] * 40, 0, 40, 70, self.x2 - 60, self.y2 - (i * 50))
                self.ResultNumber.clip_draw(self.scoreFrame[i * 4 + 3] * 40, 0, 40, 70, self.x2 - 90, self.y2 - (i * 50))


class PetChoice:
    def __init__(self):
        self.x, self.y = 110, 280
        self.choice = 0
        self.frame = player_data[0]['Pet']
        self.speed = 15
        self.image = load_image('mypetChoice.png')
        self.blue = load_image('choose.png')
        self.exit = load_image('exit.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 130, self.x, self.y)
        if (self.choice == 1):
            self.blue.clip_draw(0, 0, 135, 40, 380, 195)
        elif (self.choice == 2):
            self.blue.clip_draw(0, 0, 135, 40, 540, 195)
        elif (self.choice == 3):
            self.blue.clip_draw(0, 0, 135, 40, 700, 195)
        elif (self.choice == 4):
            self.exit.clip_draw(0, 0, 50, 50, 763, 463)


class CookieChoice:
    def __init__(self):
        self.x, self.y = 210, 180
        self.choice = 0
        self.frame = player_data[0]['Cookie']
        self.Hp = player_data[0]['Hp']
        self.image = load_image('cookieChoice.png')
        self.blue = load_image('choose.png')
        self.exit = load_image('exit.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)
        if(self.choice == 1):
            self.blue.clip_draw(0, 0, 135, 40, 380, 195)
        elif (self.choice == 2):
            self.blue.clip_draw(0, 0, 135, 40, 540, 195)
        elif (self.choice == 3):
            self.blue.clip_draw(0, 0, 135, 40, 700, 195)
        elif (self.choice == 4):
            self.exit.clip_draw(0, 0, 50, 50, 763, 463)


def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if (data[i]['Score'] < data[j]['Score']):
                data[i], data[j] = data[j], data[i]

def sum(data):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            data[i]['Coin'] += data[j]['Coin']

def enter():
    global soundmotion, sound, soundchose, image, cookie, pet, charChoice, petChoice, imagepet, imagecookie, imagestart, rank, ranking_data, player_data
    sound = load_wav('ui_1.wav')
    sound.set_volume(64)
    soundmotion = load_wav('ui_2.wav')
    soundmotion.set_volume(32)
    soundchose = load_wav('ui_3.wav')
    soundchose.set_volume(64)
    f = open('cookie_data.txt', 'r')
    player_data = json.load(f)
    f.close()

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    bubble_sort(ranking_data)
    sum(ranking_data)

    charChoice = load_image('charChoice.png')
    petChoice = load_image('petChoice.png')
    image = load_image('Interface.png')
    imagestart = load_image('Interface_start.png')
    imagecookie = load_image('Interface_cookie.png')
    imagepet = load_image('Interface_pet.png')
    cookie = CookieChoice()
    pet = PetChoice()
    rank = Ranking()

def exit():
    global  soundmotion, sound, soundchose,image, cookie, pet, charChoice, petChoice, imagepet, imagecookie, imagestart, rank
    del(soundmotion)
    del(sound)
    del(soundchose)
    del(charChoice)
    del(petChoice)
    del(image)
    del(cookie)
    del(imagepet)
    del (imagecookie)
    del (imagestart)
    del (rank)


def handle_events():
    global soundmotion, sound, soundchose, x, y, click, choose, player_data
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 600 - event.y
                #if(event.type,  event.key) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if click == 0:
                    if (x >= 620 and x <= 750 and y >= 250 and y <= 300):  # 캐릭터 선택
                        soundmotion.play()
                        choose = 2
                    elif (x >= 630 and x <= 740 and y >= 180 and y <= 230):  # 펫 선택
                        soundmotion.play()
                        choose = 3
                    elif (x >= 500 and x <= 760 and y >= 60 and y <= 140):  # 게임시작
                        soundmotion.play()
                        choose = 1
                    else:
                        choose = 0
                if(click == 1 or click == 2):
                    if (x >= 300 and x <= 460 and y >= 170 and y <= 220):  # 캐릭터 바꾸기 (프레임 1, 2, 3)
                        cookie.choice, pet.choice = 1, 1
                    elif (x > 460 and x <= 620 and y >= 170 and y <= 220):
                        cookie.choice, pet.choice = 2, 2
                    elif (x > 620 and x <= 780 and y >= 170 and y <= 220):
                        cookie.choice, pet.choice = 3, 3
                    elif (x >= 750 and x <= 780 and y >= 450 and y <= 480):
                        cookie.choice, pet.choice = 4, 4
                    else:
                        cookie.choice, pet.choice = 0, 0

            elif(event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if click == 0:
                    if(x >= 620 and x <= 750 and y >= 250 and y <= 300):        # 캐릭터 선택
                        click = 1
                        soundchose.play()
                    elif(x >= 630 and x <= 740 and y >= 180 and y <= 230):      # 펫 선택
                        click = 2
                        soundchose.play()
                    elif(x >= 500 and x <= 760 and y >= 60 and y <= 140):       # 게임시작
                        soundchose.play()
                        player_data = [
                            {"Cookie": cookie.frame, "Pet": pet.frame, "Hp": cookie.Hp, "Speed": pet.speed}
                        ]

                        f = open('cookie_data.txt', 'w')
                        json.dump(player_data, f)
                        f.close()

                        game_framework.change_state(main_state)
                else:
                    if(x >= 750 and x <= 780 and y >= 450 and y <= 480):        # 선택창 나가기
                        sound.play()
                        cookie.choice, pet.choice = 0, 0
                        click = 0
                    elif(x >= 300 and x <= 460 and y >= 170 and y <= 220):      # 캐릭터 바꾸기 (프레임 1, 2, 3)
                        sound.play()
                        if click == 1:
                            cookie.frame = 0
                            cookie.Hp = 650
                        elif click == 2:
                            pet.frame = 0
                            pet.speed = 15
                    elif(x > 460 and x <= 620 and y >= 170 and y <= 220):
                        sound.play()
                        if click == 1:
                            cookie.frame = 1
                            cookie.Hp = 700
                        elif click == 2:
                            pet.frame = 1
                            pet.speed = 10
                    elif (x > 620 and x <= 780 and y >= 170 and y <= 220):
                        sound.play()
                        if click == 1:
                            cookie.frame = 2
                            cookie.Hp = 700
                        elif click == 2:
                            pet.frame = 2
                            pet.speed = 10



x, y, click, choose = 0, 0, 0, 0

def draw():
    clear_canvas()
    if(choose == 0):
        image.draw(400, 300)
    elif(choose == 1):
        imagestart.draw(400, 300)
    elif (choose == 2):
        imagecookie.draw(400, 300)
    elif (choose == 3):
        imagepet.draw(400, 300)
    rank.draw()

    if (click == 1):
        charChoice.clip_draw(0, 0, 800, 600, 520, 300)
    elif (click == 2):
        petChoice.clip_draw(0, 0, 800, 600, 520, 300)
    cookie.draw()
    pet.draw()

    update_canvas()


def update():
    delay(0.001)
    rank.update()


def pause():
    pass


def resume():
    pass




