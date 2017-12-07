import pygame
#from bullet import Bullet
class Ship():
    def __init__(self,ai_settings,screen):
        #初始化飞船
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将每艘飞船放在底部
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.rect.centerx=float(self.rect.centerx)
        #飞船移动
        self.moving_right=False
        self.moving_left=False
        self.bullet_shit=False
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
       # self.rect.centerx=self.center
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
