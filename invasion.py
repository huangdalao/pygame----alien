import pygame
import settings
from ship import Ship
from alien import Alien
from stats import GameStats
from button import Button
from scoreboard import Scoreboard
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
    play_button=Button(ai_settings,screen,"play")
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #存储子弹
    bullets=Group()
    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,bullets,aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        #每次循环都重绘屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()



