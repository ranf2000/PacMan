import pygame as pg
from math import atan2, pi, sin, cos, radians
from vector import Vector
from copy import copy
from timer import Timer, TimerDict
from maze import Maze, GridPoint
from settings import Settings
from game_stats import GameStats
from time import sleep


class PowerPellet:
    def __init__(self, game, v, grid_pt, name='anonymous', scale=1.0, scale_factor=1):
        self.game = game
        self.v = v
        self.maze = game.maze
        self.settings = game.settings
        self.scale = scale
        self.scale_factor = scale_factor
        self.default_scale_factor = scale_factor
        self.screen, self.screen_rect = game.screen, game.screen.get_rect()
        self.name = name
        self.rect = None
        self.grid_pt = grid_pt
        self.grid_pt = game.maze.location(2, 6)
        #       self.update_next_prev()
        # self.choose_next()
        self.pt = copy(self.grid_pt.pt)
        self.location_displayed = False
