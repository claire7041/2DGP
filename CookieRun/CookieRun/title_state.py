import game_framework
import interface_state
from pico2d import *


name = "TitleState"
image = None
sound = None
logo_time = 0.0

def enter():
    global image, sound
    image = load_image('resource/image/title.png')

    sound = load_music('resource/sound/bgm_lobby.mp3')
    sound.set_volume(32)
    sound.play()

def exit():
    global image, sound
    sound.stop()
    del(image)
    del(sound)

def handle_events():
    events = get_events()
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    global logo_time

    if (logo_time > 1.5):
        logo_time = 0
        game_framework.push_state(interface_state)
    delay(0.01)
    logo_time += 0.01


def pause():
    pass


def resume():
    pass




