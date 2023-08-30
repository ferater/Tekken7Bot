"""
A simple bot that presses buttons when emerging from block or hit stun.

"""

from Bot import Bot
from TekkenGameState import TekkenGameState
from BotData import BotBehaviors
from NotationParser import ParseMoveList


class BotFrameTrap(Bot):

    def __init__(self, botCommands):
        super().__init__(botCommands)

    def Update(self, gameState: TekkenGameState):
        BotBehaviors.Basic(gameState, self.botCommands)
        if self.botCommands.IsAvailable():
            BotBehaviors.DefendAllAttacks(gameState, self.botCommands)
            if gameState.IsBotBlocking() or gameState.IsBotGettingHit():
                pass
            else:
                pass