import sys
sys.path.append('C:/Users/Challis/Chris/Python/pairsTournament')
import pairsClasses as p
from fold_low_with_high import FoldLowWithHigh
from expectation import Expectation

losers = []
for i in range(100):
    d = p.Dealer()
    d.gameState.players[0].strategy = FoldLowWithHigh(3, 8)
    d.gameState.players[1].strategy = FoldLowWithHigh(4, 8)
    d.gameState.players[2].strategy = Expectation()
    losers.append(d.play())

for i in range(6):
    print(losers.count(i))
