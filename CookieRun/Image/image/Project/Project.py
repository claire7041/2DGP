from pico2d import *

def keyborad_event():
    global running
    global Keyborad_Right
    global Keyborad_Left
    Move_events = get_events()
    for event in Move_events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                Keyborad_Right = True
            elif event.key == SDLK_LEFT:
                Keyborad_Left = True
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Keyborad_Right = False
            elif event.key == SDLK_LEFT:
                Keyborad_Left = False


open_canvas()
Cookie = load_image('cookie_run.png')
Cookie_jump = load_image('cookie_jump.png')
First_background = load_image('First_Background.png')
First_ground = load_image('First_ground-horz.png')

running = True
Cookie_x = 200
Cookie_y = 117
frame = 0
Keyborad_Right = False
Keyborad_Left = False
while(running):
    First_background.draw(400, 300)
    First_ground.draw(400, 25)
    if Keyborad_Right == True:
        Cookie_x += 10
    elif Keyborad_Left == True:
        Cookie_x -= 10
    Cookie.clip_draw(frame * 75, 0, 75, 87, Cookie_x, Cookie_y)
    update_canvas()
    frame = (frame + 1) % 3
    delay(0.08)
    keyborad_event()

close_canvas()