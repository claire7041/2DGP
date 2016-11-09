import json

cookie_data = [
    {"Cookie": 2, "Pet": 3, "Hp": 200}
]

f = open('cookie_data.txt', 'w')
json.dump(cookie_data, f)
f.close()

f = open('cookie_data.txt', 'r')
cookie_data = json.load(f)
f.close()

print('[cookie_run]')

print('Cookie:%d, Pet:%d, Hp:%d' %
        (cookie_data[0]['Cookie'],
         cookie_data[0]['Pet'],
         cookie_data[0]['Hp']))