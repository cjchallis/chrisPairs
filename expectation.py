from __future__ import division
from math import ceil
from copy import copy

class Expectation:
    '''
    Determines optimal play by computing the expected points per turn
    until next points are earned.
    '''
    def __init__(self, tm = 5, high = 10):
        self.TURN_MAX = tm
        self.cards = tuple(range(1, high + 1))

    def play(self, info):
        # need to get current hand, deck, and available folds
        deck = info.deck
        hand = tuple(self.player.stack)
        fold = info.bestFold()
        ev_hit = self._turn(hand, deck, 1)
        print("Hand:")
        print(hand)
        print("Fold:")
        print(fold)
        print("EV hit / turn:")
        print(ev_hit)
        if fold[1] / 2 < ev_hit:
            print("I folded.")
            print("\n\n")
            return fold
        print("I hit.")
        print("\n\n")
        return ev_hit

    def _p_deal(self, c, deck):
        return deck.count(c) / len(deck)

    def _p_fold(self, c, deck):
        return self._p_deal(c, deck)

    def _hit(self, hand, deck, trn):
        return sum([self._p_deal(c, deck) * c for c in hand]) / (trn+1)

    def _fold(self, ev_hit, deck, trn):
        prob = sum([self._p_fold(c, deck) for c in self.cards if c < ev_hit])
        ev = 0
        if prob > 0:
            ev = sum([self._p_fold(c, deck) * c for c in self.cards if c < ev_hit]) / prob / (trn+1)
        return (prob, ev)

    def _turn(self, hand, d, trn):
        ev_hit = self._hit(hand, d, trn)
        if trn < self.TURN_MAX:
            for c in self.cards:
                if c not in hand:
                    deck = copy(d)
                    deck.remove(c)
                    ev_hit += self._turn(hand + tuple([c]), deck, trn+1) * self._p_deal(c, d)
        if trn == 1:
            return ev_hit            
        f = self._fold(ev_hit, d, trn)
        p_fold = f[0]
        ev_fold = f[1]
        return p_fold * ev_fold + (1-p_fold) * ev_hit







