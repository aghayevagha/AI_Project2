def shapes():
    return [L_1, L_2, L_3, L_4, Full_block, Outer_block]

"""
Full_block - returns dictionary with 0s since there is no visible ones
Outer_block - returns a tile where boundaries are 0s
L shapes - 4 different L shapes, with 90 degree turned
"""

def Full_block(tile):
    return {1: 0, 2: 0, 3: 0, 4: 0}
def Outer_block( tile):
    res = {1: 0, 2: 0, 3: 0, 4: 0}
    res[1] = sum(row[1:3].count(1) for row in tile[1:3])
    res[2] = sum(row[1:3].count(2) for row in tile[1:3])
    res[3] = sum(row[1:3].count(3) for row in tile[1:3])
    res[4] = sum(row[1:3].count(4) for row in tile[1:3])
    return res
def L_1( tile):
    res = {1: 0, 2: 0, 3: 0, 4: 0}
    res[1] = sum(row[1:].count(1) for row in tile[:-1])
    res[2] = sum(row[1:].count(2) for row in tile[:-1])
    res[3] = sum(row[1:].count(3) for row in tile[:-1])
    res[4] = sum(row[1:].count(4) for row in tile[:-1])
    return res
def L_2( tile):
    res = {1: 0, 2: 0, 3: 0, 4: 0}
    res[1] = sum([row[1:].count(1) for row in tile[1:]])
    res[2] = sum([row[1:].count(2) for row in tile[1:]])
    res[3] = sum([row[1:].count(3) for row in tile[1:]])
    res[4] = sum([row[1:].count(4) for row in tile[1:]])
    return res
def L_3( tile):
    res = {1: 0, 2: 0, 3: 0, 4: 0}
    res[1] = sum(row[:-1].count(1) for row in tile[:-1])
    res[2] = sum(row[:-1].count(2) for row in tile[:-1])
    res[3] = sum(row[:-1].count(3) for row in tile[:-1])
    res[4] = sum(row[:-1].count(4) for row in tile[:-1])
    return res
def L_4( tile): 
    res = {1: 0, 2: 0, 3: 0, 4: 0}
    res[1] = sum(row[:-1].count(1) for row in tile[1:])
    res[2] = sum(row[:-1].count(2) for row in tile[1:])
    res[3] = sum(row[:-1].count(3) for row in tile[1:])
    res[4] = sum(row[:-1].count(4) for row in tile[1:])
    return res
