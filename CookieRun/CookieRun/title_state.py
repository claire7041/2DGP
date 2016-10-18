import game_framework
import interface_state
from pico2d import *


name = "TitleState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del(image)

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




