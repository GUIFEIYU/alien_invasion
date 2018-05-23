#!/usr/bin/python
# -*- coding: utf-8 -*-
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为 1 表示方向向右，为 -1 表示方向向左
        self.fleet_direction = 1