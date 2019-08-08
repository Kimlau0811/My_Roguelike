# -*- coding: utf-8 -*-
"""
@author: Liu Hongzhi

Email: Kimlau0811@gmail.com

Created on Thu Aug  8 10:58:45 2019
"""

import tcod as libtcod
from fov_functions import initialize_fov, recompute_fov
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
    screen_full = False
    screen_title = 'My Roguelike'
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    fov_algorithm = 0 #默认为0
    fov_light_walls = True #是否照亮墙壁
    fov_radius = 10 #视野大小
    
    colors = {
            'dark_wall': libtcod.Color(0, 0, 100),
            'dark_ground': libtcod.Color(50, 50, 150),
            'light_wall': libtcod.Color(130, 110, 50),
            'light_ground': libtcod.Color(200, 180, 50)
            }
    
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, screen_title, screen_full) 
    
    con = libtcod.console_new(screen_width, screen_height)
    
    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    
    fov_recompute = True
    
    fov_map = initialize_fov(game_map)
    
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        #使用用户输入内容更新key和mouse
        
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
        
        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)
 
        fov_recompute = False
        
        libtcod.console_flush()
        #在屏幕上显示所有内容
        
        '''
        libtcod.console_put_char(con, player.x, player.y, ' ', libtcod.BKGND_NONE)
        libtcod.console_put_char(0, player.x, player.y, ' ', libtcod.BKGND_NONE) #消除原始位置
        '''
        
        clear_all(con, entities)
        
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
                
                fov_recompute = True
        
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()