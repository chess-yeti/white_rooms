import random

def move_player(player_position:list[int,int], move:str):
    if move == "up":
        player_position[1] -= 3
    elif move == "down":
        player_position[1] += 3
    elif move == "left":
        player_position[0] -= 3
    elif move == "right":
        player_position[0] += 3
    elif move == "cheat":
        print("Glitch said 'No cheating in my place!' Glitch killed you.")
        exit()
    elif move == "call glitch":
        print("you died to Glitch he looks like a man but he is made out of void and has a purple aura. He will kill you on command")
    elif move == "pray":
        print("Have you made it or not? No one knows expect Glitch....")
        exit()
    elif move == "claymore's jitsu":
        print(" ):< Fine if you killed Catch's group then I will let you win but don't do it again or I'll tell Glitch!")
        exit()
    if move == "summon glitch":
        print("'BY THE POWER OF CLAYMORE I SUMMON MORE MONSTERS HAHAHA!'.")
        add_more_monsters(5)

# NUM_MONSTERS = 10

GRID_WIDTH = 10
GRID_HEIGHT = 10

# Define the number of monsters
NUM_MONSTERS = 4

# Define the player's starting position
player_position = [0, 0]

# Define the positions of the monsters
monsters = []

def game():
    # Define the dimensions of the grid

    add_more_monsters(NUM_MONSTERS)

    # Define the dimensions of the exit
    exit_position = [GRID_WIDTH - 1, GRID_HEIGHT - 1]

    # Define the grid
    grid = []
    for i in range(GRID_HEIGHT):
        grid.append(["."] * GRID_WIDTH)

    # Put the player on the grid
    grid[player_position[1]][player_position[1]] = "P"

    # Put the monsters on the grid
    for monster in monsters:
        grid[monster[1]][monster[0]] = "M"
    # Put the exit on the grid
    grid[exit_position[1]][exit_position[0]] = "X"

    # Print the grid
    for row in grid:
        print(" ".join(row))

    # Define the game loop
    keep_playing = True

    while keep_playing:
        # If the player is on the same square as a monster, exit the game
        for monster in monsters:
            if player_position == monster:
                print("you died to Catch they go in groups and try to pin you down. Avoid that!")
                return

        # Get the player's input
        move = input("Enter a move (up, down, left, right, call glitch, pray, summon glitch): ")

        # Move the player
        grid[player_position[1]][player_position[0]] = "."
        move_player(player_position, move)

        if move == "call glitch":
            print("You got killed by glitch he is a man but he is made of void with a purple aura. He will kill you on command. ")
            return



        # If the player is outside the grid, exit the game
        if player_position[0] < 0 or player_position[0] >= GRID_WIDTH or player_position[1] < 0 or player_position[1] >= GRID_HEIGHT:
            print("You fell off into space all the air get sucked out of your lungs and you burn to death from the heat!")
            return

        # If the player is on the same square as a monster, exit the game
        for monster in monsters:
            if player_position == monster:
                print("you died to Catch they go in groups and try to pin you down. Avoid that!")
                return

        # If the player is on the same square as the exit, exit the game
        if player_position == exit_position:
            print("You escaped the white rooms and the white distant grid explodes and catch has died! You made it!")
            return

        # Move the monsters
        for i in range(len(monsters)):
            grid[monsters[i][1]][monsters[i][0]] = "_"
            if monsters[i][0] < player_position[0]:
                monsters[i][0] += 2
            elif monsters[i][0] > player_position[0]:
                monsters[i][0] -= 2
            if monsters[i][1] < player_position[1]:
                monsters[i][1] += 1
            elif monsters[i][1] > player_position[1]:
                monsters[i][1] -= 1


        # Put the player on the grid
        grid[player_position[1]][player_position[0]] = "P"

        # Put the monsters on the grid
        for monster in monsters:
            grid[monster[1]][monster[0]] = "M" # Troll"
# 👹
        # Print the grid
        for row in grid:
            print(" ".join(row))

        print()


def add_more_monsters(how_many):
    for i in range(how_many):
        monsters.append([random.randint(3, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)])


game()
# import unittest
#
#
# class TestMovePlayer(unittest.TestCase):
#     def test_move_player_up(self):
#         # Set up the test by initializing the player's position
#         player_position = [0, 0]
#
#         # Call the move_player() function with "up" as the move
#         move_player(player_position, "up")
#
#         # Assert that the player's position has been updated correctly
#         self.assertEqual(player_position, [0, -1])
#
#     def test_move_player_down(self):
#         # Set up the test by initializing the player's position
#         player_position = [0, 0]
#
#         # Call the move_player() function with "down" as the move
#         move_player(player_position, "down")
#
#         # Assert that the player's position has been updated correctly
#         self.assertEqual(player_position, [0, 1])
#
#     def test_move_player_left(self):
#         # Set up the test by initializing the player's position
#         player_position = [0, 0]
#
#         # Call the move_player() function with "left" as the move
#         move_player(player_position, "left")
#
#         # Assert that the player's position has been updated correctly
#         self.assertEqual(player_position, [-1, 0])
#
#     def test_move_player_right(self):
#         # Set up the test by initializing the player's position
#         player_position = [0, 0]
#
#         # Call the move_player() function with "right" as the move
#         move_player(player_position, "right")
#
#         # Assert that the player's position has been updated correctly
#         self.assertEqual(player_position, [1, 0])
#
#
# # Run the unit tests
# if __name__ == '__main__':
#     unittest.main()
