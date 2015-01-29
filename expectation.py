from __future__ import division
from math import ceil

class Expectation:
    '''
    Determines optimal play by computing the expected points per turn
    until next points are earned.
    '''
    def __init__(self):
        self.TURN_MAX = 5
        high = 10
        self.cards = tuple(range(1, high + 1))

    def play(self, info):
        # need to get current hand, deck, and available folds
        deck = tuple(info.deck)
        hand = tuple(self.player.stack)
        fold = info.bestFold()[0][1]

        ev_hit = _turn(hand, deck, 1)

    def _p_deal(self, c, deck):
        return deck.count(c) / deck.len()

    def _p_fold(self, c, deck):
        return self._p_deal(c, deck)

    def _hit(self, hand, trn):
        return sum([self._p_deal(c) * c for c in hand]) / (trn+1)

    def _fold(self, ev_hit, trn):
        prob = sum([self._p_fold(c) for c in cards if c < ev_hit])
        ev = 0
        if prob > 0:
            ev = sum([p_fold(c) * c for c in cards if c < ev_hit]) / prob / (trn+1)
        return (prob, ev)

    def _turn(self, hand, trn):
        ev_hit = hit(hand, trn)
        if trn < TURN_MAX:
            for c in cards:
                if c not in hand:
                    ev_hit += turn(hand + tuple([c]), trn+1) * self._p_deal(c)
        if trn == 1:
            return ev_hit
        f = self._fold(ev_hit, trn)
        p_fold = f[0]
        ev_fold = f[1]
        return p_fold * ev_fold + (1-p_fold) * ev_hit







