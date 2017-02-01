import math
import pdb
moves = 'R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3'



directions = ['North', 'East', 'South', 'West']
def getDirections(move, curr_dir):
    if move[0] == 'R':
        cd = clock(curr_dir)
    else:
        cd = counter(curr_dir)
    return cd


def pythag():
    current_direction = 'North'
    x = 0
    y = 0

    moves_array = moves.split(', ')
    for i in moves_array:
        current_direction = getDirections(i, current_direction)
        if current_direction == 'North':
            y += int(i[1:])
        elif current_direction == 'West':
            x -= int(i[1:])
        elif current_direction == 'East':
            x += int(i[1:])
        elif current_direction == 'South':
            y -= int(i[1:])
    hypot = x + y
    pdb.set_trace()
    return hypot



def clock(nd):
    new_direction = ''
    if nd == 'West':
         new_direction = 'North'
    else:
        new_index = directions.index(nd)+1
        new_direction = directions[new_index]

    return new_direction



def counter(nd):
    new_direction = ''
    if nd == 'North':
         new_direction = 'West'
    else:

        new_index = directions.index(nd)-1
        new_direction = directions[new_index]

    return new_direction


pythag()
pdb.set_trace()
