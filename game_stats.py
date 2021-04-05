class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0
        self.power_dots = 99
        self.level = 1

    def reset_stats(self):
        self.lives_left = self.settings.lives_limit
        self.score = 0
