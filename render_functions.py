# -*- coding: utf-8 -*-
"""
@author: Liu Hongzhi

Email: Kimlau0811@gmail.com

Created on Thu Aug  8 12:32:37 2019
"""

import tcod as libtcod
from enum import Enum

class RenderOrder(Enum): #显示顺序
   CORPSE = 1
   ITEM = 2
   ACTOR = 3

'''
在屏幕上进行清除和绘制
'''

def render_all(con, entities, player, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True

                elif game_map.tiles[x][y].explored:
            
                    if wall:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
    #循环遍历游戏地图中的每个图块，并检查它是否阻挡视线。如果确实如此，则将其绘制成墙，如果不是，则绘制地板    
    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)
    # Draw all entities in the list
    for entity in entities_in_render_order:
        draw_entity(con, entity, fov_map)
    libtcod.console_set_default_foreground(con, libtcod.white)
    libtcod.console_print_ex(con, 1, screen_height - 2, libtcod.BKGND_NONE, libtcod.LEFT,
                         'HP: {0:02}/{1:02}'.format(player.fighter.hp, player.fighter.max_hp))


    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    # erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)