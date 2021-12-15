def credit():
    card_list = input('Введите номер кредитной карты: ').split()
    print(card_list)
    print('*' * 12, card_list[-1])


credit()

def palindrom():
    word = str(input())
    a = word[::-1]
    if word == a:
        print("yes, this is a palindrom")
    else:
        print("no, this is not a palindrom")

palindrom()


class Tomato:
    states = [1, 2, 3]

    def __init__(self, for_index):
        self._index = for_index
        self._state = Tomato.states[0]

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self._state == Tomato.states[-1]:
            print('is ripe')


class TomatoBush:
    def __init__(self, ammount):
        self.tomatoes = []
        for i in range(ammount):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self):
        for t in self.tomatoes:
            if not t.is_ripe():
                return False
        return True

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name):
        self.name = name

    def work(self, tbush: TomatoBush):
        tbush.grow_all()

    def harvest(self, tbush):
        if tbush.all_are_ripe():
            tbush.give_away_all()
            return True
        else:
            print('not all tomatoes are ripe')
            return False

    @staticmethod
    def knowledge_base():
        print('spravka')


Gardener.knowledge_base()
tom = Gardener('Tom')
bush = TomatoBush(3)
tom.work(bush)
tom.harvest(bush)
tom.work(bush)
tom.harvest(bush)

# while not tom.harvest(bush):
#     tom.work(bush)

