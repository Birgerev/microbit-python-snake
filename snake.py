####### BBC-MICROBIT SNAKE #######
# Feel free to use code in       #
# whatever way you seem fitting. #
# Do not claim the code to be    #
# yours, and in case of          #
# redistribution you are to give #
# credits.                       #
#                                #
# Copyright Birger Evansson 2019 #
##################################

from microbit import *
import random

#Position class, used to keep track of 2 dimensional positions0
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Snake properties
snake_earlier = []
snake_lenght = 2
snake_pos = Position(0, 3)
snake_direction = 1;    #The direction that the snake is facing
                        #  0 = Up  |  1 = Right  |  2 = Down  |  3 = Left
#Cherry properties
cherry_pos = Position(4, 3)
cherry_clock = 2

game_speed = 300        #how often game code gets looped, measured in milliseconds

while True:
    sleep(game_speed)
    
    #Input handling
    snake_direction += button_a.get_presses()
    snake_direction -= button_b.get_presses()
    
    snake_direction = snake_direction % 4
    
    #Snake movement
    if snake_direction == 0 :
        move_x = 0
        move_y = 1
    if snake_direction == 1 :
        move_x = 1
        move_y = 0
    if snake_direction == 2 :
        move_x = 0
        move_y = -1
    if snake_direction == 3 :
        move_x = -1
        move_y = 0
    
    snake_pos.x += move_x
    snake_pos.y += move_y
    
    
    #Loop around the screen
    snake_pos.x = snake_pos.x % 5
    snake_pos.y = snake_pos.y % 5
    
    #Death Check
    for i in range(len(snake_earlier), 1, -1) :
        posi = snake_earlier[i-1]
        if snake_pos.x == posi.x :
            if snake_pos.y == posi.y :
                if i >= len(snake_earlier) - snake_lenght :
                    display.scroll("dead", wait=True, loop=True)
    
    #Cherry Check
    if snake_pos.x == cherry_pos.x :
        if snake_pos.y == cherry_pos.y :
            cherry_pos = Position(random.randint(0,4), random.randint(0,4))
            snake_lenght += 1
    
    #Rendering
    display.clear()
    
    cherry_clock += 1
    display.set_pixel(cherry_pos.x, cherry_pos.y, cherry_clock % 5 + 4)
    
    #Save old locations
    snake_earlier.append(Position(snake_pos.x, snake_pos.y))
    
    previous_positions = len(snake_earlier)
    
    for pos in snake_earlier :
        if snake_earlier.index(pos) >= previous_positions - snake_lenght :
            display.set_pixel(pos.x, pos.y, 7)
    display.set_pixel(snake_pos.x, snake_pos.y, 9)
