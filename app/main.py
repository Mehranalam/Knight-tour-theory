import random

def chessboard(Knight_place):
    # TODO
    counter = 0
    chess_board_index = []
    for init in range(1,65):
        if counter % 2 == 0:
            chess_board_index.append("■,")
        else:
            chess_board_index.append("■,")
        counter += 1
        if counter == 8:
            chess_board_index.append("\n")
            counter = 0
    
    if chess_board_index[Knight_place] == "\n":
        chess_board_index[Knight_place-1] = "♞,"
    else:
        chess_board_index[Knight_place] = ""
        chess_board_index[Knight_place] = "♞,"
    
            
    return chess_board_index

# chess unicode: U+2658 = ♞ --- □
chessboard_results = ""
for behavior in chessboard(random.randrange(1,64)):
    chessboard_results = chessboard_results + behavior

print(chessboard_results)

print("--------------------------------------------------")

def theory(chess_board):
    new_chessboard_generation = chess_board
    index_of_knight = new_chessboard_generation.index("♞,")
    
    important_row = []
    helper = 2
    for inity in range(1,9):
        important_row.append(inity)
        important_row.append(8 * helper)
        if helper == 2:
            for hidden in range((8 * (8 - 1)) + 1, (8 * 8) + 1):
                important_row.append(hidden)
                
            handle_loop = 1
            for sijal in range(1 ,8):
                handle_loop = handle_loop + 8
                important_row.append(handle_loop)
        helper += 1  
        
    important_row.sort()  

    calbacker = index_of_knight in important_row
    if calbacker:
        if 1 <= index_of_knight <= 8:
            jjk = (((index_of_knight + 8) + 8) + 8) + 1
            new_chessboard_generation[jjk] = "♞,"
        elif 56 <= index_of_knight <= 64:
            jjk = (((index_of_knight + 8) + 8) + 8) + 1
            new_chessboard_generation[jjk] = "♞,"
        
        chessboard_results = ""
        for behavior in new_chessboard_generation:
            chessboard_results = chessboard_results + behavior

        print(chessboard_results)
        
    
theory(chessboard(random.randrange(1,64)))


    
    
    
    
