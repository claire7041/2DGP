import json

obstacle_data = [
    {"x": 500, "y": 650, "Type": 1, "Size_x": 80, "Size_y": 448, "Crash": True},
    {"x": 600, "y": 150, "Type": 2, "Size_x": 67, "Size_y": 241, "Crash": True},
    {"x": 700, "y": 150, "Type": 3, "Size_x": 50, "Size_y": 60, "Crash": True},
    {"x": 800, "y": 150, "Type": 4, "Size_x": 34, "Size_y": 50, "Crash": True},
    {"x": 900, "y": 150, "Type": 5, "Size_x": 42, "Size_y": 94, "Crash": True},
    {"x": 1000, "y": 150, "Type": 6, "Size_x": 30, "Size_y": 50, "Crash": True},
    {"x": 1100, "y": 150, "Type": 7, "Size_x": 42, "Size_y": 78, "Crash": True},
    {"x": 1200, "y": 150, "Type": 8, "Size_x": 50, "Size_y": 60, "Crash": True},
    {"x": 1300, "y": 150, "Type": 9, "Size_x": 50, "Size_y": 60, "Crash": True},
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