def main():
    #the driver code
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],       #Initializing an example sudoku board.
        [0,0,0,6,0,1,0,7,8],       # Zeros represent empty spaces
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7],
    ]

    print_board(board)   #Printing the board before it is solved
    solve_sudoku(board)   #Calling function to solve the sudoku
    print("\n")
    print("The solved sudoku board is: \n")
    print_board(board)



def solve_sudoku(board):
    find = find_empty_spaces(board)
    if not find:
         #If there are no empty spaces in the board, then it has been completed and the function call ends
        return True        
    
    else:
        row, col = find
    
    for i in range(1,10):
        if(valid_position(board,i,(row,col))):
            #If the empty space found above can be filled in by number "i", then that spaces' value is set to i
            board[row][col] = i 

            if(solve_sudoku(board)):
                return True
            else:
                board[row][col] = 0
    
    return False 


def valid_position(board,num,position):
    for i in range(9):

        # Checking to see if there is any other cell in the same row with number 'num'. Which would make 'num' an invalid number for that position 
        if board[position[0]][i] == num and position[1]!=i :
            return False

    for i in range(9):
        # Checking to see if number 'num' is already present in the same column
        if(board[i][position[1]] == num and position[0]!=i):
            return False
    
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            # Checking to see if 'num' is already present in the square.
            
            if(board[i][j] == num and (i,j)!=position):
                return False
    
    return True


def print_board(bo):
    for i in range(len(bo)):
        if(i%3==0 and i!=0):
            print("\n")
        for j in range(len(bo[0])):
            if (j%3==0 and j!=0):
                print(" | ",end = "")
            if(j==8):
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")

def find_empty_spaces(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                return (i,j)

    return None

main()


    
