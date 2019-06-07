import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

dungeon = [(x,y) for x in range(5) for y in range(5)]

def random_items():
    return(random.sample(dungeon,3))

def make_dungeon(player_position):
    print(" _ _ _ _ _")
    for cell in dungeon:
        y = cell[1]
        if y < 4:
            if cell == player_position:
                print("|X", end = "")
            else:
                print("|_", end = "")
        elif cell == player_position:
            print("|X|")
        else:
            print("|_|")

def move_player(position,m_input):
    x,y = position
    if m_input.upper() == "UP":
        x -= 1
    elif m_input.upper() == "LEFT":
        y -= 1
    elif m_input.upper() == "RIGHT":
        y += 1
    elif m_input.upper() == "DOWN":
        x += 1
    elif m_input.upper() == "QUIT":
        exit()
    return(x,y)

random_select = random_items()

def moves(position):
    x,y = position
    moves = ["UP","RIGHT","DOWN","LEFT"]
    if x == 0:
        moves.remove("UP")
    elif y == 4:
        moves.remove("RIGHT")
    elif x == 4:
        moves.remove("DOWN")
    elif y == 0:
        moves.remove("LEFT")
    return(moves)

def main():
    location = random_select[0]
    door = random_select[1]
    dragon = random_select[2]
    print("Welcome to the Dungeon!")
    input("Press 'Enter' on your keyboard to start the game!")
    make_dungeon(location)
    print("You are currently in room {}".format(location))
    while True:
        move_list = moves(location)
        print("You can move{}".format(move_list))
        print("Enter 'QUIT' to quit")
        main_input = input("\n").upper()
        if main_input == "QUIT":
            break
        elif main_input in move_list:
            location = move_player(location,main_input)
            clear_screen()
            make_dungeon(location)
            if location == dragon:
                print("You lost ! Dragon ate you")
                break
            elif location == door:
                print("Congratulations . you won !")
                break
            else:
                print("You are currently in room {}".format(location))
        else:
            clear_screen()
            make_dungeon(location)
            print("Walls are hard ! Don't run into them.")
main()
