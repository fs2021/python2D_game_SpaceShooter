from laser import Laser



class Ship:
    COOLDOWN = 30
    #HEIGHT = 600
    def __init__(self, x, y, screen_h, health=100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
        self.scr_h = screen_h
        

    def draw(self, window):
        # pygame.draw.rect(window, (150, 100, 100), (self.x, self.y, 40, 60), 2)
        window.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()   

    def shoot(self):
        if self.cool_down_counter == 0:
            test_laser = Laser(-10, -100, self.laser_image, self.scr_h)

            las_x = self.x + (self.get_width()/2) - test_laser.get_width()/2

            laser = Laser(las_x, self.y, self.laser_image, self.scr_h)
            self.lasers.append(laser)
            self.cool_down_counter = 1


    #makes time pause after shooting. if 1, wait 30frames
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0: 
            self.cool_down_counter +=1 

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen():
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)