import random


def make_grid():
    """function creates the empty list of lists that will be used as a grid"""
    grid = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]
    return grid


def print_grid(grid):
    """prints a grid in the terminal"""
    for y in grid:
        for x in y:
            print(x, end='')
        print()


def space_empty(grid, row, column):
    """checks to make sure a space is empty"""
    if grid[row-1][column-1] == '-':
        return True
    else:
        return False

def check_inputs(row, column):
    """Checks to make sure user inputs are valid"""
    good_inputs = ['1','2','3']
    if not row in good_inputs:
        print('Invalid input: must be a number between 1 and 3')
        return False
    elif not column in good_inputs:
        print('Invalid input: must be a number between 1 and 3')
        return False
    else:
        return True


def user_move(grid):
    """user gives number for column and row, and then it adds the X there and returns the grid"""
    columns = [3,1,2]
    rows = [3,1,2]
    print('Which row and column do you want to place your X in?')
    row = input('Row: ')
    column = input('Column: ')
    if check_inputs(row, column):
        row = int(row)
        column = int(column)
        if row in rows and column in columns:
            if space_empty(grid, row, column):
                grid[row-1][column-1] = 'X'
                print_grid(grid)
                return grid
            else:
                print('Invalid input: space is already full')
                user_move(grid)
    else:
        user_move(grid)


def someone_wins(grid):
    """checks all 8 win conditions. If someone wins, returns true. columns = y values, rows = x values"""
    columns = [0,1,2]
    rows = [0,1,2]
    for y in columns:
        value1 = None
        value2 = None
        value3 = None
        for x in rows:
            value = grid[y][x]
            value3 = value2
            value2 = value1
            value1 = value
            if value1 == value2 == value3 and value1 != '-':
                return True
    for y in columns:
        value1 = None
        value2 = None
        value3 = None
        for x in rows:
            value = grid[x][y]
            value3 = value2
            value2 = value1
            value1 = value
            if value1 == value2 == value3 and value1 != '-':
                return True
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '-':
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '-':
        return True
    else:
        return False


def is_tie(grid):
    """Checks to see if a tie has occurred"""
    columns = [0,1,2]
    rows = [0,1,2]
    for y in columns:
        for x in rows:
            if grid[y][x] == '-':
                return False
    return True



def computer_move(grid):
    """makes the computers move and adds an O to the grid"""
    while True:
        r_column = random.randint(0,2)
        r_row = random.randint(0,2)
        if space_empty(grid, r_row, r_column):
            grid[r_row][r_column] = 'O'
            print('Computer\'s move')
            print_grid(grid)
            return grid



def main():
    grid = make_grid()
    go_first = input('Would you like to go first? (Y/N)')
    print_grid(grid)
    if go_first == 'Y' or go_first == 'y':
        user_move(grid)
    else:
        computer_move(grid)
        user_move(grid)
    while True:
        if someone_wins(grid):
            print("player wins")
            break
        elif is_tie(grid):
            print('It is a tie')
            break
        else:
            computer_move(grid)

        if someone_wins(grid):
            print('Computer wins')
            break
        elif is_tie(grid):
            print('It is a tie')
            break
        else:
            user_move(grid)
    play_again = input('Would you like to play again? (Y?N)')
    if play_again == 'Y' or play_again == 'y':
        main()
    else:
        print('Thanks for playing :)')


if __name__ == '__main__':
    main()
