from estacion_mejora import UpgradeStation
from player import Player
from player_stat import PlayerStat
from wand import Wand
from wand_stat import WandStat

def print_info(player1: Player, player2: Player):
    print("Stats del player1: \n")
    print("Vida: " + str(player1.stats.health) + "\n")
    print("Armadura: " + str(player1.stats.armor) + "\n")
    print("Velocidad: " + str(player1.stats.speed) + "\n")
    print("Varitas: \n")

    for i in player1.wands:
        i.toString()

    print("\nStats del player2: \n")
    print("Vida: " + str(player2.stats.health) + "\n")
    print("Armadura: " + str(player2.stats.armor) + "\n")
    print("Velocidad: " + str(player2.stats.speed) + "\n")
    print("Varitas: \n")

    for i in player2.wands:
        i.toString()


#estacion de mejora
upgrade_station = UpgradeStation()

#varitas
varita1_stats = WandStat(1.5, "hielo")
varita2_stats = WandStat(2.0, "fuego")
varita3_stats = WandStat(1.3, "aire")

varita1 = Wand(varita1_stats)
varita2 = Wand(varita2_stats)
varita3 = Wand(varita3_stats)

wandSet1 = [varita1, varita2]
wandSet2 = [varita2, varita3]

#jugador
player1_stats = PlayerStat(20.0, 15.0, 2.5)
player2_stats = PlayerStat(15.0, 10.5, 5.2)


player1 = Player(player1_stats, wandSet1)
player2 = Player(player2_stats, wandSet2)

print_info(player1, player2)

#mejorar
upgrade_station.upgradeHealth(player1)
upgrade_station.upgradeDamage(player1.wands[0])
upgrade_station.upgradeArmor(player1)

upgrade_station.upgradeDamage(player2.wands[0])
upgrade_station.upgradeDamage(player2.wands[1])
upgrade_station.upgradeSpeed(player2)
upgrade_station.upgradeHealth(player2)

print("#######################################################\n")

print_info(player1, player2)