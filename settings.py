'''
设置类
'''
class Settings():

    def __init__(self):
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(233,233,235)
        #飞船移动速度
        self.ship_speed_factor=2
        #子弹设置
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=10
        self.bullet_color=60,60,60
        self.bullets_allowed=5
        #外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1


