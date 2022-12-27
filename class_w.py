from random import choice, randint, randrange


class Workers:
    def __init__(self):
        self.name = choice(['Иван', 'Катя', 'Алексей', 'Роман', 'Эвелина', 'Артур', 'Анатолий'])
        self.age = randint(18, 65)
        self.salary = randrange(15000, 150000)
        self.experience = randint(1, 47)