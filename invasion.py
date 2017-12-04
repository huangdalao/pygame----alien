import pygame
import settings
from ship import Ship
#import ship
import functions as gf
def run_game():
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen=pygame.display.set_mode((1200,800))
    #bg_color=(200,200,222)
    pygame.display.set_caption("alien invasion")
    ship=Ship(screen)
    #开始游戏的主循环
    while True:
        gf.check_events()
        #每次循环都重绘屏幕
        gf.update_events(ai_settings,screen,ship)

run_game()



