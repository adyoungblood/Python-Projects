import pygame

import sys

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from ship import Ship

from alien import Alien

import game_functions as gf

def run_game():
    #Initialization of pygame, settings, and screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    

    #Make a group to store bullets in, a ship, and a group to store aliens in
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    print("Ships Left: " + str(stats.ships_left))
 
    #Main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)
        else:
            print("Game Over!!!")
            pygame.quit()
            sys.exit()
            break
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
