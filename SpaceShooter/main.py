
from tkinter import *
from tkinter import ttk

import pygame
import os
import time
import random
from enemy import Enemy
from laser import collide

from player import Player

pygame.font.init() #to print text

#constants
WIDTH = int(750)
HEIGHT = int(650)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#name of window
pygame.display.set_caption("Space Shooter")



#load images
#project dir, path to this main.py
dir = os.path.dirname(__file__)
#print(dir)

background_orig = pygame.image.load(os.path.join(dir, 'assets', 'background-black.png'))
#make it size of window
background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))

# /home/q/Documents/python/Space Shooter/assets/pixel_ship_red_small.png

def main_menu():

    def start_game():
        
        menu_window.destroy()
        main()

    menu_window = Tk()
    menu_window.title('Space Shooter')
    
    frm = ttk.Frame(menu_window, padding=10)
    frm.grid()
    ttk.Label(frm, text="Use").grid(column=1, row=0)
    ttk.Label(frm, text="\u2192 \u2193  \u2191 \u2190").grid(column=0, row=1, pady=10)
    ttk.Label(frm, text="To move your ship").grid(column=2, row=1)
    ttk.Label(frm, text="Enter").grid(column=0, row=2)
    ttk.Label(frm, text="To shoot laser").grid(column=2, row=2, pady=10)



    ttk.Button(frm, text="Start game", command=start_game).grid(column=0, row=3)

    ttk.Button(frm, text="Quit", command=menu_window.destroy).grid(column=2, row=3)
    
    menu_window.mainloop()



def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("arial", 30)
    lost_font = pygame.font.SysFont("comicsans", 60)
    player_velocity = 5
    laser_velocity = 4
    wave_length = 5
    enemy_vel = 1
    lost = False
    lost_count = 0

    enemies = []

    player = Player(300, 400, HEIGHT, health=100)
    
    

    def redraw_window():
        WINDOW.blit(background, (0,0))
        level_label = main_font.render(f"level: {level}", 1, (100, 150, 150))
        lives_label = main_font.render(f"lives: {lives}", 1, (100, 150, 150))
        WINDOW.blit(level_label, (10, 10))
        WINDOW.blit(lives_label, ((WIDTH - 10 - lives_label.get_width()), 10))

        #pygame.draw.rect(WINDOW, (255, 0, 0), (0, 0, 20, 10))
        

        
        for enemy in enemies:
            enemy.draw(WINDOW)
        player.draw(WINDOW)

        if lost:
            lost_label = lost_font.render("You lost!", 1, (150, 150, 150))
            WINDOW.blit(lost_label, ((WIDTH/2 - lost_label.get_width()/2), (HEIGHT/2)))

        pygame.display.update()
        

    def ship_touch(cur_ship):
        border_l = False
        border_r = False
        border_u = False
        border_d = False
        if cur_ship.x <= 0:
            border_l = True
        elif cur_ship.x >= (WIDTH - cur_ship.get_width()):
            border_r = True

        if cur_ship.y <= 0:
            border_u = True
        elif cur_ship.y >= (HEIGHT - cur_ship.get_height()):
            border_d = True

        return [border_l, border_r, border_u, border_d]


    def level_difficulty(lev):
        return 1/((2+lev)/lev)


    while run:
        clock.tick(fps)
        redraw_window()
        #clock makes loop run in constant time
        if len(enemies) == 0:
            level +=1
            wave_length += 3
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, (WIDTH-100)), random.randrange(-int(1000/level_difficulty(level)), -150), random.choice(["red", "green", "blue"]), HEIGHT)
                enemies.append(enemy)


        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count +=1  #it increases every frame
        
        if lost:
            if lost_count > fps*4:       #it is 4 seconds pause
                run = False
            else:
                continue  # do not run next code in loop, run from the start of loop
                 


        #check if events occured in this time frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed() #returns dictionary with all keys and if they are pressed
        if (keys[pygame.K_LEFT] and not ship_touch(player)[0]):  #left
            player.x -= player_velocity
        if (keys[pygame.K_RIGHT] and not ship_touch(player)[1]):   #right
            player.x += player_velocity
        if (keys[pygame.K_UP] and not ship_touch(player)[2]): #up
            player.y -= player_velocity
        if (keys[pygame.K_DOWN] and not ship_touch(player)[3]): #down
            player.y += player_velocity
        
        if (keys[pygame.K_KP_ENTER]):
            player.shoot()


        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_velocity, player)
            #random shooting 
            if (random.randrange(0, int(4*fps*level_difficulty(level))) == 1):
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
              
            elif enemy.y > HEIGHT: #enemy reach bottom
                lives -= 1
                enemies.remove(enemy)

            


        
        player.move_lasers(-laser_velocity, enemies)

        if run==False:
            main_menu()


main_menu()




