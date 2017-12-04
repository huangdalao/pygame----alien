import sys,pygame
def check_events():
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def upate_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # screen.fill(bg_color)
    # 让最近绘制的屏幕可见
    pygame.display.flip()