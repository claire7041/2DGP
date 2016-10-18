import game_framework
import main_state
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

class PetChoice:
    def __init__(self):
        self.x, self.y = 90, 380
        self.choice = 0
        self.frame = 0
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
        self.x, self.y = 190, 280
        self.choice = 0
        self.frame = 0
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

def enter():
    global image, cookie, pet, charChoice, petChoice, imagepet, imagecookie, imagestart
    charChoice = load_image('charChoice.png')
    petChoice = load_image('petChoice.png')
    image = load_image('Interface.png')
    imagestart = load_image('Interface_start.png')
    imagecookie = load_image('Interface_cookie.png')
    imagepet = load_image('Interface_pet.png')
    cookie = CookieChoice()
    pet = PetChoice()

def exit():
    global image, cookie, pet, charChoice, petChoice, imagepet, imagecookie, imagestart
    del(charChoice)
    del(petChoice)
    del(image)
    del(cookie)
    del(imagepet)
    del (imagecookie)
    del (imagestart)


def handle_events():
    global x, y, click, choose
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
                        choose = 2
                    elif (x >= 630 and x <= 740 and y >= 180 and y <= 230):  # 펫 선택
                        choose = 3
                    elif (x >= 500 and x <= 760 and y >= 60 and y <= 140):  # 게임시작
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

            elif(event.type , event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if click == 0:
                    if(x >= 620 and x <= 750 and y >= 250 and y <= 300):        # 캐릭터 선택
                        click = 1
                    elif(x >= 630 and x <= 740 and y >= 180 and y <= 230):      # 펫 선택
                        click = 2
                    elif(x >= 500 and x <= 760 and y >= 60 and y <= 140):       # 게임시작
                        game_framework.change_state(main_state)
                else:
                    if(x >= 750 and x <= 780 and y >= 450 and y <= 480):        # 선택창 나가기
                        cookie.choice, pet.choice = 0, 0
                        click = 0
                    elif(x >= 300 and x <= 460 and y >= 170 and y <= 220):      # 캐릭터 바꾸기 (프레임 1, 2, 3)
                        if click == 1:
                            cookie.frame = 0
                        elif click == 2:
                            pet.frame = 0
                    elif(x > 460 and x <= 620 and y >= 170 and y <= 220):
                        if click == 1:
                            cookie.frame = 1
                        elif click == 2:
                            pet.frame = 1
                    elif (x > 620 and x <= 780 and y >= 170 and y <= 220):
                        if click == 1:
                            cookie.frame = 2
                        elif click == 2:
                            pet.frame = 2

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

    if (click == 1):
        charChoice.clip_draw(0, 0, 800, 600, 520, 300)
    elif (click == 2):
        petChoice.clip_draw(0, 0, 800, 600, 520, 300)
    cookie.draw()
    pet.draw()

    update_canvas()


def update():
    delay(0.001)
    game_framework.mypet = pet.frame
    game_framework.mychar = cookie.frame


def pause():
    pass


def resume():
    pass




