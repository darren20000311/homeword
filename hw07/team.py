from player import Player


class Team:
    """A class representing a dodgeball team"""
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

    def is_position_filled(self, position):
        for player in self.players:
            if player.position == position:
                return True
        return False

    def show_roster(self):
        roster = f"The lineup for {self.name} is :\n"
        for player in self.players:
            roster += f"{player.number}\t{player.name}\t{player.position}\n"
        return roster
