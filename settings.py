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
        #self.ship_speed_factor=2
        self.ship_limit=3
        #子弹设置
        #self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=10
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        #外星人设置
        #self.alien_speed_factor=3
        self.fleet_drop_speed=10
        #加速
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        #self.fleet_direction=1

    def initialize_dynamic_settings(self):
        #初始化游戏的变化设置
        self.ship_speed_factor=3
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1
        self.alien_points=10
    def increase_speed(self):
        #提高速度设置
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)