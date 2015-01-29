class FoldLowWithHigh:
    def __init__(self, fold, hand):
        self.fold = fold
        self.hand = hand

    def play(self, info):
        best = info.bestFold()
        stack = self.player.stack
        if best[1] <= self.fold and max(stack) >= self.hand:
            return best
        return "Hit"
