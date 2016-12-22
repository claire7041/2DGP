import json

def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if (data[i]['Score'] < data[j]['Score']):
                data[i], data[j] = data[j], data[i]

def sum(data):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            data[i]['Coin'] += data[j]['Coin']


ranking_data = [
    {"Coin": 0, "Score": 0}
]

f = open('ranking_data.txt', 'w')
json.dump(ranking_data, f)
f.close()

f = open('ranking_data.txt', 'r')
ranking_data = json.load(f)
f.close()

bubble_sort(ranking_data)
sum(ranking_data)
ranking_data = ranking_data[:10]

print('[cookie_run]')

for rank in ranking_data:
    print('Coin:%d, Score:%d' %
        (rank['Coin'],
         rank['Score']))