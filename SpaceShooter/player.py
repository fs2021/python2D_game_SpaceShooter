
from ship import Ship
import pygame
import os


dir = os.path.dirname(__file__)
yellow_space_ship = pygame.image.load(os.path.join(dir, 'assets', 'pixel_ship_yellow.png'))
yellow_laser = pygame.image.load(os.path.join(dir, 'assets', 'pixel_laser_yellow.png'))

class Player(Ship):
    def __init__(self, x, y, screen_h, health=100, ) -> None:
        super().__init__(x, y, screen_h, health)
        self.ship_image = yellow_space_ship
        self.laser_image = yellow_laser
        #mask for collision 
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health
        self.scr_h = screen_h


    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen():
                self.lasers.remove(laser)

            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= 10
                        objs.remove(obj)
                        self.lasers.remove(laser)


    def healthbar(self, window):
        health_index = self.get_width() * self.health/self.max_health
        #two lines under image
        pygame.draw.rect(window, (255, 0, 0), (self.x, (self.y + self.get_height() + 10), self.get_width(), 5))
        pygame.draw.rect(window, (0, 255, 0), (self.x, (self.y + self.get_height() + 10), health_index, 5))

#overwrite metod from ship
    def draw(self, window):
        self.healthbar(window)
        return super().draw(window)