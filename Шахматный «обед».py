def can_eat(pos1, pos2):
    pos1_x, pos1_y = pos1
    pos2_x, pos2_y = pos2
    dx = abs(pos1_x - pos2_x)
    dy = abs(pos1_y - pos2_y)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

print(can_eat((2, 1), (4, 2)))  # должно быть True
print(can_eat((5, 5), (6, 6)))  # должно быть True
print(can_eat((1, 1), (3, 3)))  # должно быть False
