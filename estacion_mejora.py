from player import Player
from wand import Wand


class UpgradeStation():
    def __init__(self):
        pass

    def upgradeHealth(self, player: Player):
        player.stats.health *= 1.5

    def upgradeSpeed(self, player: Player):
        player.stats.speed *= 1.1

    def upgradeArmor(self, player: Player):
        player.stats.armor *= 1.1

    def upgradeDamage(self, wand: Wand):
        wand.stats.damage *= 1.2

        