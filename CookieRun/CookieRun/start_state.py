import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
sound = None
logo_time = 0.0


def enter():
    global image, sound
    open_canvas()
    image = load_image('resource/image/kpu_credit.png')
    sound = load_wav('resource/sound/ut_loading.wav')
    sound.set_volume(64)
    sound.play()


def exit():
    global image
    del(image)
    close_canvas()


def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.1)
    logo_time += 0.1


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass



