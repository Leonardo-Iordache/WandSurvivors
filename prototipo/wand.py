from wand_stat import WandStat
class Wand():
    def __init__(self, stats: WandStat):
        self.stats = stats


    def toString(self):
        print("Daño: " + str(self.stats.damage) + "\nTipo: " + str(self.stats.type))
