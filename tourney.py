import sys
# this should be the path to pairsClasses.py
# not needed if all files are in the same folder
sys.path.append('C:/Users/Challis/Chris/Python/pairsTournament')
# import pairsClasses and all Strategies to be played
import pairsClasses as p
from fold_low_with_high import FoldLowWithHigh
from expectation import Expectation

losers = []
for i in range(100):
    # defaults to 5 players that always hit
    d = p.Dealer(4)
    # replace some strategies
    d.gameState.players[0].strategy = FoldLowWithHigh(3, 8)
    d.gameState.players[1].strategy = FoldLowWithHigh(4, 8)
    d.gameState.players[2].strategy = Expectation()
    # play a game and append the loser index
    losers.append(d.play())

for i in range(1, len(d.gameState.players)+1):
    print("Player " + str(i) + ": " + str(losers.count(i)))
