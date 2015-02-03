class FoldLowWithHigh:
    def __init__(self, fold, hand):
        ''' Strategy that folds when 'fold' is available if 'hand' or higher is in hand'''
        self.fold = fold
        self.hand = hand

    def play(self, info):
        # get best fold as tuple (playerIndex, card)
        best = info.bestFold()
        # get current hand
        stack = self.player.stack
        if best[1] <= self.fold and max(stack) >= self.hand:
            return best
        return "Hit"
