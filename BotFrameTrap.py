"""
A simple bot that presses buttons when emerging from block or hit stun.

"""

from Bot import Bot
from TekkenGameState import TekkenGameState
from TekkenEncyclopedia import TekkenEncyclopedia
from BotData import BotBehaviors
from CharacterData import *
# from NotationParser import ParseMoveList
from BotOptionsModule import BotOptions


class BotFrameTrap(Bot):

    def __init__(self, botCommands, botOptions=None):
        super().__init__(botCommands)
        if botOptions is None:
            botOptions = BotOptions()
        self.botOptions = botOptions
        self.gameplan = None
        self.enemyCyclopedia = TekkenEncyclopedia(False)

    def Update(self, gameState: TekkenGameState):
        print("aaaaaaaaaaa: ", self.botOptions.blockType)
        self.enemyCyclopedia.Update(gameState)
        if gameState.WasFightReset():
            self.botCommands.ClearCommands()
            self.gameplan = None
        if self.gameplan == None:
            char_id = gameState.GetBotCharId()
            if char_id != None:
                self.gameplan = GetGameplan(char_id)
# ======================================= #
        if self.gameplan != None:
            # BotBehaviors.Basic(gameState, self.botCommands)
            if self.botCommands.IsAvailable():
                if (self.botOptions.blockType == "Defend All"):
                    BotBehaviors.DefendAllAttacks(gameState, self.botCommands)
                elif (self.botOptions.blockType == "High and Mid Attacks"):
                    BotBehaviors.DefendHighMidAttacks(
                        gameState, self.botCommands)
                elif (self.botOptions.blockType == "Low Attacks"):
                    BotBehaviors.DefendLowAttacks(
                        gameState, self.botCommands)

                if (self.botOptions.escapeFromThrows):
                    BotBehaviors.TryBreakThrows(gameState, self.botCommands)
                if not self.botOptions.stayOnTheGround:
                    BotBehaviors.GetUp(gameState, self.botCommands)

                #     BotBehaviors.DefendAllAttacks(gameState, self.botCommands)

                # punishmet
                if (self.botOptions.isPunishmentOn):
                    frameAdvantage = None
                    if gameState.IsBotBlocking():
                        frameAdvantage = self.enemyCyclopedia.GetFrameAdvantage(
                            gameState.GetOppMoveId())
                    elif gameState.IsBotGettingHit():
                        frameAdvantage = self.enemyCyclopedia.GetFrameAdvantage(
                            gameState.GetOppMoveId(), isOnBlock=False)
                    # else:
                    #     BotBehaviors.TechThrows(gameState, self.botCommands)
                    try:
                        frameAdvantage = int(frameAdvantage) * -1
                    except:
                        frameAdvantage = None
                    if frameAdvantage != None:
                        if frameAdvantage >= 10:
                            if gameState.IsBotWhileStanding():
                                punish = self.gameplan.GetMoveByFrame(
                                    ResponseTypes.ws_punishes, frameAdvantage)
                            else:
                                punish = self.gameplan.GetMoveByFrame(
                                    ResponseTypes.st_punishes, frameAdvantage)
                        # if(self.botOptions.printPunishes):
                            if punish != None:
                                self.botCommands.AddCommand(punish)
