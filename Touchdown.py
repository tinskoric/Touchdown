# Tin Skoric
# CS 021

# Touchdown
# You can only move forwards and backwards (including diagonally). You can't move sideways!

def clear():
    # These are the lists containing information that is printed on the gameboard when the gameboard function is called.
    # The clear function resets all items. Each item is assigned either as being an open position ("+"), a closed position
    # ("-"), a human player position ("X"), or a computer player position ("O"). The values list organizes all these values
    # in the order that they are positioned on the gameboard. The value_index list is ordered identically but with strings each
    # labeled with the name of their index counterparts from the values list. This is so that a specific position can be called
    # by name and referenced to a specific value to see if it is open, closed, or held by a player.
    global values, value_index
    a1 = b1 = c1 = d1 = e1 = f1 = g1 = h1 = i1 = "O"
    a2 = i2 = "-"
    b2 = c2 = d2 = e2 = f2 = g2 = h2 ="+"
    a3 = b3 = d3 = f3 = h3 = i3 = "-"
    c3 = e3 = g3 = "+"
    a4 = c4 = e4 = g4 = i4 = "-"
    b4 = d4 = f4 = h4 = "+"
    a5 = b5 = c5 = d5 = e5 = f5 = g5 = h5 = i5 = "+"
    b6 = d6 = f6 = h6 = "+"
    a6 = c6 = e6 = g6 = i6 = "-"
    c7 = e7 = g7 = "+"
    a7 = b7 = d7 = f7 = h7 = i7 = "-"
    b8 = c8 = d8 = e8 = f8 = g8 = h8 ="+"
    a8 = i8 = "-"
    a9 = b9 = c9 = d9 = e9 = f9 = g9 = h9 = i9 = "X"

    value_index = [
    "a1","b1","c1","d1","e1","f1","g1","h1","i1",
    "a2","b2","c2","d2","e2","f2","g2","h2","i2",
    "a3","b3","c3","d3","e3","f3","g3","h3","i3",
    "a4","b4","c4","d4","e4","f4","g4","h4","i4",
    "a5","b5","c5","d5","e5","f5","g5","h5","i5",
    "a6","b6","c6","d6","e6","f6","g6","h6","i6",
    "a7","b7","c7","d7","e7","f7","g7","h7","i7",
    "a8","b8","c8","d8","e8","f8","g8","h8","i8",
    "a9","b9","c9","d9","e9","f9","g9","h9","i9",
    ]

    values = [
    a1,b1,c1,d1,e1,f1,g1,h1,i1,
    a2,b2,c2,d2,e2,f2,g2,h2,i2,
    a3,b3,c3,d3,e3,f3,g3,h3,i3,
    a4,b4,c4,d4,e4,f4,g4,h4,i4,
    a5,b5,c5,d5,e5,f5,g5,h5,i5,
    a6,b6,c6,d6,e6,f6,g6,h6,i6,
    a7,b7,c7,d7,e7,f7,g7,h7,i7,
    a8,b8,c8,d8,e8,f8,g8,h8,i8,
    a9,b9,c9,d9,e9,f9,g9,h9,i9,
    ]
    return values, value_index

gameloop = 1
turn_count = 0
x_win = 0
o_win = 0
time_condition = 0

import time, random

def end_condition():
    # If either player reaches the other side of the gameboard before the other and before time runs out, they win. 
    # If time runs out before either reaches the opposite side, the game ends in a draw.
    global gameloop, x_win, o_win, time_condition
    if "X" in values[0:8] and time_condition > 0:
        x_win = 1
        gameloop = 0
        return gameloop, x_win
    elif "O" in values[72:80] and time_condition > 0:
        o_win = 1
        gameloop = 0
        return gameloop, o_win
    elif time_condition <= 0:
        x_win = 0
        o_win = 0
        gameloop = 0
        return gameloop, x_win, o_win
    else:
        x_win = 0
        o_win = 0

def gamerules(move_entry, input_type, current_turn, move_input_restrictions):
    # This function checks if movement selections are valid by checking the value_index
    # list for a string input and then cross-referencing the index of that with the value
    # of it from the values list. If the correct player selects a valid place to move
    # from or move to then the function will return that the selection is valid.
    # Player_move_select,"select",current_turn,player_move_select
    # The last input for this function "move_imput_restrictions" isn't really 
    # used but it could be used to expand on the gamerules in the future.
    # Can't go in a non-open spot or spot that is far away.
    # Can't move sideways. Can only move forwards and backwards as defined by index values.
    if input_type == "select":
        if move_entry in value_index:
            index_number = value_index.index(move_entry)
            if values[index_number] == "X" and current_turn == "X":
                return True
            elif values[index_number] == "O" and current_turn == "O":
                return True
            else:
                return False
        else:
            return False
    elif input_type == "move":
        if move_entry in value_index:
            index_number = value_index.index(move_entry)
            index_number_select = value_index.index(move_input_restrictions)
            if values[index_number] == "+":
                if current_turn == "X":
                    if index_number_select + 8 <= index_number and index_number <= index_number_select + 10:                   
                        return True
                    if index_number_select - 10 <= index_number and index_number <= index_number_select - 8:                     
                        return True              
                elif current_turn == "O":
                    if index_number_select + 8 <= index_number and index_number <= index_number_select + 10:                   
                        return True
                    if index_number_select - 10 <= index_number and index_number <= index_number_select - 8:                     
                        return True
            else:
                return False
        else:
            return False 
    else:
        return False     

def gamestate_cpu(current_turn):
    # At the beginning of each turn for the computer player, the time will be checked. The computer player will scan the 
    # gameboard, including its own currently held positions, and will select a 'strategy' accordingly. While all moves
    # are randomized, move *selection* is not, and the computer will narrow down selection options to areas near the 
    # human player if they are detected as being within close range. The defensive strategy will have the computer focus
    # on their end of the gameboard to select a position to move whereas the aggressive strategy will ignore their end of
    # the gameboard to select a position. The reason movements are randomized is to provide variety to play, with how the 
    # gaemboard is laid out, it is very possible for a completely random move to successfully block human player movement
    # provided that selections are narrowed down to being near the human player. At the end of selection, the computer
    # player will wait a random amount of time, then move its selection, check how much time has passed, and end its turn.
    global time_count, time_condition
    print(f"Player {current_turn} | Time Remaining: {time_condition // 60:.0f} Minutes {time_condition % 60:.0f} Seconds")
    cpu_open = []
    cpu_options = []
    cpu_open_options = []
    cpu_select = []
    cpu_select_refined = []
    cpu_detect = []
    cpu_danger = []
    cpu_detective_selection = []
    for i in range(len(values[0:27])):
        if values[i] == "X":
            cpu_danger.append(i)
    for i in range(len(values[27:53])):
        if values[i] == "X":
            cpu_detect.append(i)
    for i in range(len(values)):
        if values[i] == "O":
            cpu_select.append(i)
    cpu_select.sort()

    if len(cpu_danger) != 0:
        for i in cpu_select:
            if i < 18:
                cpu_select.remove(i)
        for i in range(len(cpu_danger)):
            index_detect = cpu_danger[i]
            for x in cpu_select_refined:
                if values[index_detect - 10] == "O" and values[index_detect - 9] == "O" and values[index_detect - 8] == "O":
                    cpu_select_refined.remove(x)
                elif x < index_detect - 10 or x > index_detect - 8:
                    cpu_select_refined.remove(x)
                    cpu_detective_selection.append(x)
        if len(cpu_detective_selection) != 0:
            cpu_random_select = random.choice(cpu_detective_selection)
            cpu_move_select = value_index[cpu_random_select]
        elif len(cpu_detective_selection) == 0:
            cpu_random_select = random.choice(cpu_select)
            cpu_move_select = value_index[cpu_random_select]
        # Defensive: 
        # Selected if human player holds any position near the starting position of 
        # computer player. Computer player will ignore all movement options that are
        # not near the region. Computer player will check if all movement options 
        # in front of specified human player position are blocked off. If that is 
        # the case, the computer will ignore those options, otherwise the computer
        # will ignore all other options.

    elif len(cpu_detect) != 0:
        for i in cpu_select:
            if i > 8:
                cpu_select.remove(i)
        for i in range(len(cpu_detect)):
            index_detect = cpu_detect[i]
            for x in cpu_select_refined:
                if x < index_detect - 20:
                    cpu_select_refined.remove(x)
                    cpu_detective_selection.append(x)
        if len(cpu_detective_selection) != 0:
            cpu_random_select = random.choice(cpu_detective_selection)
            cpu_move_select = value_index[cpu_random_select]
        elif len(cpu_detective_selection) == 0:
            cpu_random_select = random.choice(cpu_select)
            cpu_move_select = value_index[cpu_random_select]
        # Aggressive:
        # Selected if human player holds any position  halfway across the board, but 
        # not near the starting position of computer player. Computer player will ignore
        # movement options not near the region and will randomly move
        # around that position.

    elif cpu_select[-1] > 8 and len(cpu_detect) == 0:
        for i in cpu_select:
            if i > 8 or i == cpu_select[-2]:
                cpu_select_refined.append(i)
        cpu_random_select = random.choice(cpu_select_refined)
        cpu_move_select = value_index[cpu_random_select]

    elif cpu_select[-1] <= 8 and len(cpu_detect) == 0:
        cpu_random_select = random.choice(cpu_select)
        cpu_move_select = value_index[cpu_random_select]
        # Random:
        # Selected if human player still only holds positions around their own side
        # of the gameboard. The computer will randomly select and move from one of 
        # its positions.

    for i in range(len(values)):
        if values[i] == "+":
            cpu_open.append(i)
    if len(cpu_danger) >= 0:
        for i in range(len(cpu_open)):
            if i - 10 <= cpu_random_select <= i - 8:
                cpu_options.append(i)
    else:
        for i in range(len(cpu_open)):
            if i + 8 <= cpu_random_select <= i + 10:
                cpu_options.append(i)   
    for i in range(len(cpu_options)):
        index_value = cpu_options[i]
        if values[index_value] == "+":
            cpu_open_options.append(index_value)
    try:
        cpu_random_move = random.choice(cpu_open_options)
    except:
        try:
            for i in range(len(cpu_open)):
                index_value = cpu_open[i]
                if i - 8 == cpu_random_select or i - 9 == cpu_random_select or i - 10 == cpu_random_select:
                    cpu_open_options.append(index_value)
            cpu_random_move = random.choice(cpu_open_options)
        except:
            cpu_select = []
            for i in range(len(values)):
                if values[i] == "O":
                    cpu_select.append(i)
            cpu_select.sort()
            cpu_random_select = random.choice(cpu_select)
            cpu_move_select = value_index[cpu_random_select]
            for i in range(len(cpu_open)):
                index_value = cpu_open[i]
                if i - 8 == cpu_random_select or i - 9 == cpu_random_select or i - 10 == cpu_random_select:
                    cpu_open_options.append(index_value)
            cpu_random_move = random.choice(cpu_open_options)
    cpu_move_place = value_index[cpu_random_move]

    time.sleep(random.randint(0,0))
    values[value_index.index(cpu_move_place)] = current_turn
    values[value_index.index(cpu_move_select)] = "+"
    time_stop = time.time()
    time_count = time_stop - time_start
    time_condition = time_condition - time_count
    end_condition()
    # The part at the bottom with a bunch of exceptions works like this:
    # The computer player will find a list of open places to move and will then refine them according to the position that was selected from the earlier strategy.
    # If the computer doesn't find any suitable options according to slightly broader conditions. Finally, if the computer still cannot do this, a new, completely
    # random position will be selected to move from along with a random nearby open position to move to. "I don't know what I have to do but I have to move."
    # The "time.sleep" part is the amount of time the computer player waits before moving and ending its turn. The end_condition function is called to check
    # if the computer has won.

def gamestate_player(current_turn):
    # At the beginning of each turn for the human player, the time will be displayed and the user will be prompted to enter a position from which to move from.
    # The position will be checked using the gamerules function. If the input is invalid the user will be prompted to reenter, otherwise the user will be 
    # prompted to enter a position to move to, which will again be checked through the gamerules function. If the input is invalid the user will be prompted 
    # to reenter, otherwise the move will be entered and the turn will end.
    global time_count, time_condition
    player_turn = 0
    while player_turn != 1:
        print(f"Player {current_turn} | Time Remaining: {time_condition // 60:.0f} Minutes {time_condition % 60:.0f} Seconds")
        player_move_select = str(input("Enter the current position of your next move: "))
        if gamerules(player_move_select,"select",current_turn,player_move_select) == True:
            player_move_place = str(input("Enter where you would like to move your current selection: "))
            if gamerules(player_move_place,"move",current_turn,player_move_select) == True:
                values[value_index.index(player_move_place)] = current_turn
                values[value_index.index(player_move_select)] = "+"
                time_stop = time.time()
                time_count = time_stop - time_start
                time_condition = time_condition - time_count
                player_turn = 1
                end_condition()
            else:
                print('''
Invalid entry! You can only move to a position currently unoccupied, displayed as '+', and nearby the position you are moving from. 
Please remember to enter the position exactly as it appears (Ex: "a9" not "A9").
                ''')        
        else:
            print('''
Invalid entry! You can only select a position you currently occupy. Please remember to enter the position exactly as it appears 
(Ex: "a9" not "A9").
            ''')

def gamestate():
    # Keeps track of turns and starts time.
    # This function is not reset for a specific player to start the game after 
    # replaying, so each new game *without* restarting the program, a different 
    # player could make the first move.
    global turn_count, time_start
    time_start = time.time()
    turn = 1
    if turn_count % 2 != 0:
        turn = "O"
        gamestate_cpu(turn)
    if turn_count % 2 == 0:
        turn = "X"
        gamestate_player(turn)
    turn_count += 1

def gameboard():
    # This is the gameboard. It is printed each time a turn is ended and displays the order of positions at a given time.
    # The numbers and letters correspond to positions on the gameboard. As an example "a9" corresponds to whatever value
    # can be found at the index of 72 in the values list.
        print(f'''
    a b c d e f g h i
1 | {values[0]} {values[1]} {values[2]} {values[3]} {values[4]} {values[5]} {values[6]} {values[7]} {values[8]}
2 | {values[9]} {values[10]} {values[11]} {values[12]} {values[13]} {values[14]} {values[15]} {values[16]} {values[17]}
3 | {values[18]} {values[19]} {values[20]} {values[21]} {values[22]} {values[23]} {values[24]} {values[25]} {values[26]}
4 | {values[27]} {values[28]} {values[29]} {values[30]} {values[31]} {values[32]} {values[33]} {values[34]} {values[35]}
5 | {values[36]} {values[37]} {values[38]} {values[39]} {values[40]} {values[41]} {values[42]} {values[43]} {values[44]}
6 | {values[45]} {values[46]} {values[47]} {values[48]} {values[49]} {values[50]} {values[51]} {values[52]} {values[53]}
7 | {values[54]} {values[55]} {values[56]} {values[57]} {values[58]} {values[59]} {values[60]} {values[61]} {values[62]}
8 | {values[63]} {values[64]} {values[65]} {values[66]} {values[67]} {values[68]} {values[69]} {values[70]} {values[71]}
9 | {values[72]} {values[73]} {values[74]} {values[75]} {values[76]} {values[77]} {values[78]} {values[79]} {values[80]}
        ''')

# The main function controls everything and calls in other functions to continue the gameloop once the game has started. 
# It is also where the player can choose to play again or not to play at all. If a valid answer is not entered the user
# will be asked to reenter. Once the user has stated they want to play, they will be prompted to enter an amount of 
# time in minutes that they wish to play. This amount can be entered as a decimal float and will be converted to standard
# format when displayed during the game. Example: time_condition = 3.5 becomes "3 minutes 30 seconds." If a numeric value 
# is not entered correctly the user will be prompted to reenter.
def main():
    global time_condition, gameloop
    loop = 1
    start = "0"
    while loop == 1:
        while start.lower() == "0":
            start = str(input("Play? (y/n): "))
            if start.lower() == "n":
                start = "n"
                loop = 0
            elif start.lower() == "y":
                start = "y"
            else:
                print("Invalid entry! Please try again.")
                start = "0"
        while start.lower() == "y":
            time_condition = 0
            while time_condition < 1:
                try:
                    time_condition = float(input("How many minutes do you want to set the timer to? (Enter a number greater than 0): "))*60
                except:
                    print("Invalid entry! Please try again.")
            gameloop = 1
            clear()
            while gameloop == 1:
                gameboard()
                gamestate()
            if x_win == 1:
                gameboard()
                print("X wins!")
                start = "0"
            elif o_win == 1:
                gameboard()
                print ("O wins!")
                start = "0"
            elif time_condition <= 0:
                gameboard()
                print("Draw!")
                start = "0"
            while start.lower() == "0":
                start = str(input("Play again? (y/n): "))
                if start.lower() == "n":
                    start = "n"
                    loop = 0
                elif start.lower() == "y":
                    start = "y"
                else:
                    print("Invalid entry! Please try again.")
                    start = "0"

main()