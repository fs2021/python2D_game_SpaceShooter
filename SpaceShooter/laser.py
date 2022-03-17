import pygame



class Laser:
    def __init__(self, x, y, image, screen_h) -> None:
        self.x = x
        self.y = y
        self.img = image
        self.mask = pygame.mask.from_surface(self.img)
        self.scr_h = screen_h


    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


    def move(self, vel):
        self.y += vel

    def off_screen(self):
        return not(-20 <= self.y <= self.scr_h)

    def collision(self, obj):
        """ 
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        coll = self.mask.overlap(obj.mask, (offset_x, offset_y))
        return coll != None
 """

        return collide(self, obj)

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()   


    
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    coll = obj1.mask.overlap(obj2.mask, (offset_x, offset_y))
    return coll != None
    #return 
    
    #upper function returns coordinates, or None. So we have True if overlap, and False if None

