# -*- coding: utf-8 -*-
"""
@author: Liu Hongzhi

Email: Kimlau0811@gmail.com

Created on Fri Aug  9 12:37:23 2019
"""

import tcod as libtcod

from game_states import GameStates
from render_functions import RenderOrder


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return 'You died!', GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = '{0} is dead!'.format(monster.name.capitalize())

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message