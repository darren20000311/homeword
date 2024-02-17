class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        self.players_on_bench = []

    def send_to_bench(self, player_name):
        if player_name not in self.players_on_bench:
            self.players_on_bench.append(player_name)

    def get_from_bench(self):
        if self.players_on_bench:
            return self.players_on_bench.pop(0)
        else:
            return "The bench is empty."
        
    def show_bench(self):
        return "\n".join(self.players_on_bench)