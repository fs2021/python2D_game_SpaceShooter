from ship import Ship
import pygame
import os

#project dir, path to this main.py
dir = os.path.dirname(__file__)
#print(dir)

red_space_ship = pygame.image.load(os.path.join(dir, 'assets', 'pixel_ship_red_small.png'))
green_space_ship = pygame.image.load(os.path.join(dir, 'assets', 'pixel_ship_green_small.png'))
blue_space_ship = pygame.image.load(os.path.join(dir, 'assets', 'pixel_ship_blue_small.png'))


#lasers
red_laser = pygame.image.load(os.path.join(dir, 'assets', 'pixel_laser_red.png'))
green_laser = pygame.image.load(os.path.join(dir, 'assets', 'pixel_laser_green.png'))
blue_laser = pygame.image.load(os.path.join(dir,'assets', 'pixel_laser_blue.png'))

COLOR_MAP = {
            "red": (red_space_ship, red_laser),
            "green": (green_space_ship, green_laser),
            "blue": (blue_space_ship, blue_laser)

            }

class Enemy(Ship):
    def __init__(self, x, y, color, screen_h, health=100) -> None:
        super().__init__(x, y, screen_h, health) 
        self.ship_image, self.laser_image = COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, vel):
        self.y += vel
