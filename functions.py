import sys,pygame
from bullet import Bullet
from alien import Alien
from time import sleep

#from pygame.sprite import Sprite
def check_keydown(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        #创建一颗子弹加入buttles
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings,screen,ship,bullets):
    #没限制就发射一颗子弹
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,play_button,ship,bullets,aliens):

    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True
        #重置计分
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #清空外星人列表和子列表
        aliens.empty()
        bullets.empty()
        #创建新的外星人
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #显示得分

    if not stats.game_active:
        play_button.draw_button()



    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
    check_buttle_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_buttle_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collections=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collections:
        for aliens in collections.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level+=1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
        print("ship hit!!!")
    #检查是否到达底端
    check_aliens_buttom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return  number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            for alien in aliens.sprites():
                alien.rect.y += ai_settings.fleet_drop_speed
            ai_settings.fleet_direction *= -1
            #change_fleet_direction(ai_settings,aliens)
            break

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #响应外星人撞船
    if stats.ships_left>0:
        stats.ships_left-=1
        #更新记分牌
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
         #暂停
        sleep(1)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def check_aliens_buttom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #检查外星人是否到达屏幕底端
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break
def check_high_score(stats,sb):
    #检查是否出现最高分
    if stats.score > stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()


# def change_fleet_direction (ai_settings,aliens):
#     for alien in aliens.sprites:
#         alien.rect.y += ai_settings.fleet_drop_speed
#     ai_settings.fleet_direction = -1*ai_settings.fleet_direction




