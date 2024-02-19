print(f'{'Paint needed to cover the wall.':*^50}')

width_wall = int(input('\nEnter the width of the wall: '))
height_wall = int(input('\nEnter the height of the wall: '))

area =  height_wall * width_wall
paint_required = area / 2

# a cada 2 metros quadrados, preciso de 1 litro de tinta
print(f'\nThe dimention wall is {width_wall}x{height_wall} \n The Total wall area is: {area}m² square meters.')
print(f'\nYou will need approximately {paint_required} liters of paint to cover the wall.')
