import os

class Scoreboard:
    def __init__(self, filename='scoreboard.txt'):
        self.filename = filename
        self.scores = self._load_scores()

    def _load_scores(self):
        if not os.path.exists(self.filename):
            self._create_file()
            return {}

        scores = {}
        with open(self.filename, 'r') as file:
            for line in file:
                player, wins = line.strip().split(',')
                scores[player] = int(wins)
        return scores

    def _save_scores(self):
        with open(self.filename, 'w') as file:
            for player, wins in self.scores.items():
                file.write("{},{}\n".format(player, wins))
                
    def _create_file(self):
        with open(self.filename, 'w') as file:
            # Create an empty file if it doesn't exist
            pass

    def update_score(self, winner):
        if winner in self.scores:
            self.scores[winner] += 1
        else:
            self.scores[winner] = 1
        self._save_scores()
