import json
from class_w import Workers


def load_to_json(filename):
    return json.load(open(filename))


def write_to_json(data, filename):
    json.dump(data, open(filename, 'w'), indent=4)


data = {"Workers": []}

for i in range(10):
    data['Workers'].append(Workers().__dict__)

write_to_json(data, 'worker.json')
new_read = load_to_json('worker.json')
print('Введите номер пользователя, информацию о котором необходимо вывести')
ex = int(input())
print(ex)
print(new_read['Workers'][ex]['name'],
      new_read['Workers'][ex]['age'],
      new_read['Workers'][ex]['salary'],
      new_read['Workers'][ex]['experience'])
print('Имя | Возраст | Зарплата | Рабочий стаж')
