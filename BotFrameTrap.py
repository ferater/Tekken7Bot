"""
A simple bot that presses buttons when emerging from block or hit stun.

"""

from Bot import Bot
from TekkenGameState import TekkenGameState
from BotData import BotBehaviors
from NotationParser import ParseMoveList
from BotOptionsModule import BotOptions


class BotFrameTrap(Bot):

    def __init__(self, botCommands, botOptions=None):
        super().__init__(botCommands)
        if botOptions is None:
            botOptions = BotOptions()  # Varsayılan değerli bir BotOptions nesnesi oluşturuluyor
        self.botOptions = botOptions

    def Update(self, gameState: TekkenGameState):
        print("punish", self.botOptions.isPunishmentOn)
        print("ground", self.botOptions.stayOnTheGround)
        BotBehaviors.Basic(gameState, self.botCommands)
        if self.botCommands.IsAvailable():
            BotBehaviors.DefendAllAttacks(gameState, self.botCommands)
            if gameState.IsBotBlocking() or gameState.IsBotGettingHit():
                pass
            else:
                pass
