import pygame as pg
import game_functions as gf
from settings import Settings
from maze import Maze, GridPoint
from character import Pacman, Blinky, Inky, Pinky, Clyde
from power_pill import PowerPellet
from button import Button
from game_stats import GameStats
from sound import Sound
from scoreboard import Scoreboard
from time import sleep
from vector import Vector


# ===================================================================================================
# class Game
# ===================================================================================================
class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("PacMan Portal")
        self.font = pg.font.SysFont(None, 48)

        self.maze = Maze(game=self)

        self.pacman = Pacman(game=self)
        self.ghosts = [Blinky(game=self), Pinky(game=self), Clyde(game=self), Inky(game=self)]
        for ghost in self.ghosts:
            ghost.set_ghosts(self.ghosts)
#        self.power_pellet = PowerPellet(game=self)
        self.finished = False
        self.sound = Sound(bg_music="sounds/PAC_MAN(Super Smash Bros Ultimate).wav")
        self.sound.play()
        self.sound.pause_bg()
        self.play_button = self.stats = self.sb = None
        self.hs = 0
        self.restart()
 #       self.newcopy = self.maze.grid[:][:]



    def restart(self):
        self.stats = GameStats(settings=self.settings)
        self.play_button = Button(settings=self.settings, screen=self.screen, msg="Play")
        self.sb = Scoreboard(game=self, sound=self.sound)
        self.stats.high_score = self.hs
        self.stats.game_active = False
        self.sb.prep_high_score()

    def _pacman_hit(self):
        if self.stats.lives_left > 0:
            self.stats.lives_left -= 1
            del self.pacman
            self.pacman = Pacman(game=self)

        else:
            self.stats.game_active = False
            self.restart()


    def to_grid(self, index):
        row = index // 11
        offset = index % 11
        ss = self.maze.location(row, offset)
        return ss

    def to_pixel(self, grid):
        pixels = []



    def play(self):
        while not self.finished:
            gf.check_events(game=self, stats=self.stats, play_button=self.play_button, sound=self.sound)
            # self.screen.fill(self.settings.bg_color)
            if self.stats.game_active:
                self.sound.unpause_bg()
                self.maze.update()
                for ghost in self.ghosts: ghost.update()
                self.pacman.update()
                self.sb.show_score()
            if not self.stats.game_active:
                self.play_button.draw()
                self.sound.pause_bg()
                self.sb.show_high_score()

            pg.display.flip()
            if pg.sprite.spritecollideany(self.pacman, self.ghosts):
                self._pacman_hit()
                print("lost a life")
      #      if pg.sprite.spritecollideany(self.pacman, self.maze.timer_normal):
      #          self._pacman_hit()

    def reset(self):
        self.hs = self.stats.high_score


def main():
    game = Game()
    game.play()


if __name__ == '__main__': main()
