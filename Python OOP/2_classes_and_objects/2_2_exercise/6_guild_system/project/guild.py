class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):

        if player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:

            player = next(filter(lambda p: p.name == player_name, self.players))
            player.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."

        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):

        result = [f"Guild: {self.name}"]
        [result.append(p.player_info()) for p in self.players]
        return '\n'.join(result)





