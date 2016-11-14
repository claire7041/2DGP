import json

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

print('[cookie_run]')

for obstacle in obstacle_data:
    print('x:%d, y:%d, Type:%d, Size_x:%d, Size_y:%d' %
          (obstacle['x'],
           obstacle['y'],
           obstacle['Type'],
           obstacle['Size_x'],
           obstacle['Size_y']))