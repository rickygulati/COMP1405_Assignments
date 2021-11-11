# Student Number: 101146071
# Student Name: Ricky Gulati

white_pieces = ["k", "q", "b", "n", "r", "p", "-"]
black_pieces = ["K", "Q", "B", "N", "R", "P", "-"]
piece_points = [0.0, 10.0, 5.0, 3.5, 3.0, 1.0, 0.0]

# Function to enter a new current state of the chessboard
# @params   none
# @return   chessboard(list of lists)

def new_chessboard():
    chessboard = []
    for i in range(8):
        row = input("Enter the state of the row: ")
        while len(row) != 8:
            row = input("Incorrect number of characters!\nEnter exactly 8 characters:")
        flag = True
        while flag:
            
            for ch in row:
                if ch not in white_pieces and ch not in black_pieces:
                    flag = False
                    break
            if flag == False:
                row = input("Invalid character!\nRe-enter the row: ")
                flag = True
            else: 
                flag = False
        char_list = []
        for j in row:
            char_list.append(j)
        chessboard.append(char_list)
    return chessboard

# Function to display the chessboard
# @params   chessboard(list of lists)
# @return   none
def print_board(chessboard):
    for i in range(8):
        print("--------------------------------------------------")
        for j in range(8):
            print("| ",chessboard[i][j], " ", end = "")
        print("|")
    print("--------------------------------------------------")    

# Function to calculate score 
# @params   chessboard(list of lists)
# @return   none
def calc_score(chessboard):
    black_sum = 0.0
    white_sum = 0.0
    for i in range(8):
        for j in range(8):
            for k in range(7):
                if chessboard[i][j] == white_pieces[k]:
                    white_sum += piece_points[k]
                elif chessboard[i][j] == black_pieces[k]:
                    black_sum += piece_points[k]
    if black_sum > white_sum:
        print("Black is winning!")
    elif white_sum > black_sum:
        print("White is winning")
    else:
        print("The game is tied")

# Function to move a piece
# input coordinates are taken as integers between 1-8
# @params   chessboard(list of lists)
# @return   chessboard(list of lists)
def move_piece(chessboard):
    original_x = int(input("Enter the x coordinate of the piece you wish to move(1-8): "))
    original_y = int(input("Enter the y coordinate of the piece you wish to move(1-8): "))
    
    if chessboard[original_x][original_y] == "-":
        print("Empty space! No piece in this positon!")
        return chessboard
    else:
        final_x = int(input("Enter the x coordinate of the position at which you wish to move the piece(1-8): "))
        final_y = int(input("Enter the y coordinate of the position at which you wish to move the piece(1-8): "))
        temp = chessboard[original_x - 1][original_y - 1]
        chessboard[original_x - 1].pop(original_y - 1)
        chessboard[original_x - 1].insert(original_y - 1, "-")
        chessboard[final_x - 1].pop(final_y - 1)
        chessboard[final_x - 1].insert(final_y - 1, temp)
        return chessboard

# main function
# @params   none
# @return   none

def main():
    print("\t\t\tWelcome to the chess simulator\nUse this simulator to calculate which side(white or black) is winning\nTo use it:\n\t1. Enter the current state of the chessboard for which you wish to find the winning side.\n\t2. The side winning will be calculated and displayed now.\n\t3. You may also choose to move a piece by entering it's coordinates\nUse the following key to enter the chessboard:\nWhite pieces are in lowercase\nBlack pieces are in uppercase\nk: king\nq: queen\nr: rook\nn: knight\nb: bishop\np: pawn\n-: empty space")

    print("Entering chessboard now...")
    board = new_chessboard()
    print_board(board)
    calc_score(board)
    while True:    
        ch = int(input("Enter 1 to move a piece\nEnter 2 to quit: "))
        if ch == 1:
            move_piece(board)
            print_board(board)
        elif ch == 2:
            break
        else:
            ch = int(input("Invalid choice! Enter again"))

main()





        



        



