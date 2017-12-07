import pygame
import settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
#import ship
import functions as gf
def run_game():
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen=pygame.display.set_mode((1200,800))
    #bg_color=(200,200,222)
    pygame.display.set_caption("alien invasion")
    ship=Ship(ai_settings,screen)
    #存储子弹
    bullets=Group()
    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        #每次循环都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()



