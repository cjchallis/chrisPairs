import sys
sys.path.append('C:/Users/Challis/Chris/Python/pairsTournament')
import pairsClasses as p
from fold_low_with_high import FoldLowWithHigh

losers = []
for i in range(500):
    d = p.Dealer()
    d.gameState.players[0].strategy = FoldLowWithHigh(3, 8)
    d.gameState.players[1].strategy = FoldLowWithHigh(4, 8)
    losers.append(d.play())

for i in range(6):
    print(losers.count(i))
