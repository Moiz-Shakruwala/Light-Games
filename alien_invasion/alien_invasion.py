import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #creates the display window which here would be our game window
    pygame.display.set_caption("Alien Invasion") # sets the title for the display window
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    # Load the background image
    bg_img = pygame.image.load('images/bg.jpg')

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens,ship)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets) 
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(bg_img, screen, ship, aliens, bullets)

    
run_game()