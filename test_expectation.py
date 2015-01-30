from expectation import Expectation

class Player:
    def __init__(self):
        pass

class Info:
    def __init__(self, card):
        self.deck = []
        for i in range(1, 11):
            self.deck += i * [i]
        print(self.deck)
    def bestFold():
        return 10


info = Info(10)
p = Player()
p.stack = [9]
exp = Expectation()
exp.player = p

print(exp.play(info))
