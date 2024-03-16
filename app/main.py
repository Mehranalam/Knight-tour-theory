CHESSBOARD_LONG = 8

'''
Each house must be traversed once by the chess knight. 
So this function checks whether this house is valid or not.

    - IS_VALID() - function
'''


def is_valid(i, j, checked):
    if (i >= 1 and i <= CHESSBOARD_LONG and j >= 1 and j <= CHESSBOARD_LONG):
        if (checked[i][j] == -1):
            return True
    return False


'''
The main function of the program receives 3 basic parameters, 
the first one is col or a set of arrays that play the role of chess house, 
and the second one is the starting point of movement in the i-axis, 

and the next parameter is the starting point of the movement of the chess horse in the j-axis, 
the fourth parameter is the number of steps and house Counts the moves of the chess horse. 
This number is 64 on an 8 x 8 page.

(1,1) (2,1) 


The next 2 parameters are the amount of movement of the chess horse in the axes, 
in a way, the most important part, which is the intelligence of the movement of the chess horse.

    - HORSEـMOVEMENT() - function
'''


def horseـmovement(sol, i, j, step_count, x_move, y_move):
    if (step_count == CHESSBOARD_LONG * CHESSBOARD_LONG):
        print("in if - step")
        return True
    for k in range(0, 8):
        next_i = i + x_move[k]
        next_j = j + y_move[k]

        '''
        In this part, the houses that have been passed by the horse are placed with step _count.
        
            - This number starts from 0
            
            - Sample logical output:
                [0, 59, 38, 33, 30, 17, 8, 63]
                [37, 34, 31, 60, 9, 62, 29, 16]
                [58, 1, 36, 39, 32, 27, 18, 7]
                [35, 48, 41, 26, 61, 10, 15, 28]
                [42, 57, 2, 49, 40, 23, 6, 19]
                [47, 50, 45, 54, 25, 20, 11, 14]
                [56, 43, 52, 3, 22, 13, 24, 5]
                [51, 46, 55, 44, 53, 4, 21, 12]
                
                If you look carefully, the numbers from 0 to 64 are placed exactly 
                like the movement of the horse in chess. The letter L
            
        '''

        if (is_valid(next_i, next_j, sol)):
            sol[next_i][next_j] = step_count
            if (horseـmovement(sol, next_i, next_j, step_count + 1, x_move, y_move)):
                return True
            sol[next_i][next_j] = -1

    return False


def start_knight_tour():
    sol = []

    for i in range(0, CHESSBOARD_LONG + 1):
        a = [0]+([-1] * CHESSBOARD_LONG)
        sol.append(a)

    '''
    These two lines are all the logic of horse movement in 360 degrees. 
    All the positions of the horse in the L movement that it can create.
    
        - (i+2,j+1) - (i+1,j+2) - (i-1,j+2) - (i-2,j+1) 
        - (i-2,j-1) - (i-1,j-2) - (i+1,j-2) - (i+2,j-1)
        
    '''
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    sol[1][1] = 0

    if (horseـmovement(sol, 1, 1, 1, x_move, y_move)):
        final_board = ""
        for i in range(1, CHESSBOARD_LONG+1):
            for i in sol[i][1::]:
                final_board = final_board + f"  {i}  "

            final_board = final_board + "\n"
        return final_board
    return "False - this way not go to sucsseful :("


print(start_knight_tour())
