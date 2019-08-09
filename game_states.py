# -*- coding: utf-8 -*-
"""
@author: Liu Hongzhi

Email: Kimlau0811@gmail.com

Created on Fri Aug  9 08:48:13 2019
"""

from enum import Enum


class GameStates(Enum):
    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3