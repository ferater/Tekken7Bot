class BotOptions:
    def __init__(self, isPunishmentOn=False, stayOnTheGround=False, escapeFromThrows=False, blockType=None):
        self.isPunishmentOn = isPunishmentOn
        self.stayOnTheGround = stayOnTheGround
        self.escapeFromThrows = escapeFromThrows
        self.blockType = blockType
