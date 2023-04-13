from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):

        added_players = []

        for player in players:
            if player not in self.players:

                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):

        for supp in supplies:
            self.supplies.append(supp)

    def sustain(self, player_name, sustenance_type):

        is_player = list(filter(lambda p: p.name == player_name, self.players))

        if is_player and sustenance_type in ['Food', 'Drink']:

            player = is_player[0]

            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            for i in range(len(self.supplies)-1, -1, -1):

                supply = self.supplies[i]

                if supply.__class__.__name__ == sustenance_type:

                    if player.stamina + supply.energy > 100:
                        player.stamina = 100
                    else:
                        player.stamina += supply.energy

                    supply_name = supply.name
                    self.supplies.pop(i)
                    return f"{player_name} sustained successfully with {supply_name}."

            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def duel(self, first_player_name, second_player_name):

        player_one = next(filter(lambda p1: p1.name == first_player_name, self.players))
        player_two = next(filter(lambda p2: p2.name == second_player_name, self.players))

        result = []

        for plr in [player_one, player_two]:
            if plr.stamina == 0:
                result.append(f"Player {plr.name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

        first = min([player_one, player_two], key=lambda p: p.stamina)
        second = max([player_one, player_two], key=lambda p: p.stamina)

        #   FIRST PLAYER ATTACKS
        if second.stamina - (first.stamina / 2) <= 0:
            second.stamina = 0
            return f"Winner: {first.name}"
        else:
            second.stamina -= (first.stamina / 2)

        #   SECOND PLAYER ATTACKS
        if first.stamina - (second.stamina / 2) <= 0:
            first.stamina = 0
            return f"Winner: {second.name}"
        else:
            first.stamina -= (second.stamina / 2)

        winner = max([first, second], key=lambda p: p.stamina)
        return f"Winner: {winner.name}"

    def next_day(self):

        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

        for player in self.players:

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):

        result = []

        [result.append(str(player)) for player in self.players]
        [result.append(supply.details()) for supply in self.supplies]

        return '\n'.join(result)








