# -*- coding: utf-8 -*-
"""
@author: Liu Hongzhi

Email: Kimlau0811@gmail.com

Created on Fri Aug  9 10:56:57 2019
"""

import tcod as libtcod

class BasicMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):

            if monster.distance_to(target) >= 2:
                monster.move_astar(target, entities, game_map)

            elif target.fighter.hp > 0:
                #print('The {0} insults you! Your ego is damaged!'.format(monster.name))
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)
 
        return results
                
                