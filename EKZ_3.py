class Tomato:

    # Стадии созревания помидора
    states = {0: 'ничего', 1: 'цветок', 2: 'зелёный_помидор', 3: 'красный_помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помидор {self._index} сейчас {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил')

    # Собираем урожай
    def harvest(self):
        print(f'Садовник {self.name} собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f'Cадовник {self.name} собрал урожай')
        else:
            print('Собирать урожай пока рано.')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Время сбора урожая наступает когда помидор полностью созрел(Красный).
        Стадии роста   помидора: Ничего,
                                 Цветок,
                                 Зелёный помидор,
                                 Красный помидор''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    print("Посадили помидоры")
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Хулио', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()