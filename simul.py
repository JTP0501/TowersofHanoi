# Initializing the no. of disks and the rods
n: int = int(input("Enter the no. of disks: "))
rods: list[list[str]] = [[],[],[]] # 0, 1, 2 [rod 0, rod 1, rod 2]

def start_create_disks(n: int) -> list[str]:

    """ This function creates disks based on the n input """

    list_of_disks: list[str] = [] # ['ooooo','ooo','o'] to be placed in starting rod
    for i in range(1, n + 1):
        # width of each disk must be odd
        disk: str = 'o' * (2 * i - 1)
        list_of_disks.append(disk)
    list_of_disks.reverse()
    return list_of_disks

def make_move(rods: list[list[str]]) -> list[list[str]]: # Move format x y which means move top disk on rod x to rod y (e.g. 1 2 which means move top disk from rod 1 to rod 2)  
    
    """ This function asks the user for their move and executes if valid """

    while True:
        user_input: str = input("Enter your move (src dest): ")
        try: # Check if input is exactly two integers
            src, dest = map(int, user_input.split())
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
            continue
        
        if not (1 <= src <= 3 and 1 <= dest <= 3): # Check if src and rod within the valid range
            print("Invalid rod numbers! Please enter numbers between 1 and 3.")
            continue

        if src == dest: # Check if src and dest are the same
            print("Source and destination rods cannot be the same! Try again.")
            continue
        
        if not rods[src - 1]: # Check if src rod is empty
            print(f"Rod {src} is empty! Choose a different source rod.")
            continue

        if check_valid(src, dest, rods):
            return update_rods(src, dest, rods)        
        else:
            print(f"Rod {src} to Rod {dest} is not a valid move. Try again!")

def update_rods(src: int, dest: int, rods: list[list[str]]) -> list[list[str]]:

    """ This function updates the rods with the move made """
    disk: str = rods[src-1].pop(len(rods[src-1]) - 1) # Gets the src disk       
    rods[dest-1].append(disk) 
    return rods

def check_valid(src: int, dest: int, rods: list[list[str]]): # Have to improve this

    """ This function checks if the move is a valid move """

    if not rods[src - 1]:
        return False

    len_src_disk: int = len(rods[src-1][-1]) # Length of the top disk of the source rod

    if not (rods[dest - 1]) or len_src_disk < len(rods[dest - 1][-1]): # If dest rod is empty or the src disk is smaller than dest disk
        return True
    return False # Default

def towers_simul(n: int, rods: list[list[str]]):
    
    """ Main game loop """
    
    turn_count: int = 1

    def towers_print(n: int, rods: list[list[str]]):
        """ This function prints an instance of the game (visual representation)"""

        nonlocal turn_count

        print(f" Turn Count: {turn_count}")

        max_width: int = n * 2 - 1
        for i in range(n):
            for rod in rods:
                if len(rod) >= n - i:
                    disk = rod[n - i - 1]
                else:
                    disk = '!'
                print(disk.center(max_width), end='     ')
            print()  # New line after each level

    def check_win(rods: list[list[str]]) -> bool:

        """ This function checks if the player has won """

        if not rods[0] and not rods[1] and rods[2]: # If rod 1 and rod 2 are empty and rod 3 have stuff in it, then that must mean the game is complete
            return True
        else:
            return False

    rods.pop(0) # 'remove' first rod
    rods.insert(0, start_create_disks(n)) # Create n disks and place it in the first rod
    towers_print(n, rods) # first visual of towers of hanoi
    while not check_win(rods):
        rods = make_move(rods)
        turn_count += 1
        towers_print(n, rods) # print visual of towers of hanoi (after move)
    print(f"You completed Towers of Hanoi in {turn_count} moves!")

towers_simul(n, rods)

