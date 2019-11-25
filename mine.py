#board
#9 elements
#print board
#checking after every entry 
#1,2,3|
#4,5,6|
#7,8,9|
#player X, player O
board = ['-','-','-',
         '-','-','-',
         '-','-','-']


def update_printboard():
    global board
    '''printing board'''
    print('| '+board[0]+' | '+board[1]+' | '+board[2]+' |\n'+
          '| '+board[3]+' | '+board[4]+' | '+board[5]+' |\n'+
          '| '+board[6]+' | '+board[7]+' | '+board[8]+' |')
    
    return None


def check_for_winner(board):
    '''checking the board for winner'''
    #global board
    win_patterns = [board[0]+board[1]+board[3],
                    board[0]+board[3]+board[6],
                    board[0]+board[4]+board[8],
                    board[3]+board[4]+board[5],
                    board[6]+board[7]+board[8],
                    board[6]+board[4]+board[2],
                    board[1]+board[4]+board[7],
                    board[2]+board[5]+board[8]]
    if 'XXX' in win_patterns or 'OOO' in win_patterns:
        return True
    else:
        return False
       
        
    
def X_turn():
    '''ask X player to enter'''
    X_choice = int(input("It's X-turn enter choice(1-9): " ))
    
    while X_choice not in range(1,10):
        X_choice = int(input('Enter valid choice: '))
    else:
        return X_update(X_choice)
    
    
def O_turn():
    '''ask O player to enter'''
    O_choice = int(input("It's O-turn enter choice(1-9): " ))
    
    while O_choice not in range(1,10):
        O_choice = int(input('Enter valid choice: '))
    else:
        return O_update(O_choice)
    
def X_update(index):
    '''bringing board address using global'''
    global board
    '''updating board'''
    while board[index-1] != '-':
        index = int(input("Thats pre-occupied, choose another one: "))        
    else:
        board[index-1] = 'X'      
        #X_update(index)
    
    update_printboard()
    count = board.count('-')
    status=check_for_winner(board)
    
    if status:
        print('X won')
        return None
    else:        
        if count >= 1:
            O_turn()
        if count == 0:
            print('Tie')
            return None
                
    
def O_update(index):
    global board
    '''updating board'''
    while board[index-1] != '-':
        index = int(input("Thats pre-occupied, choose another one: "))       
    else:
        board[index-1] = 'O'
    
    update_printboard()
    count = board.count('-')
    status=check_for_winner(board)
    
    if status:
        print('O won')
        return None   
    else:        
        if count >= 1:
            X_turn()
        if count == 0:
            print('Tie')
            return None
    
def play():
    print('Welcome this game require Two players in total:\n'
          'player X and player O\n\n')
    print('1 2 3\n4 5 6\n7 8 9\n\n')
    first = input("Who's going first (X/O): ")
    while first != 'X' and first != 'O':
        
        first = input('Please! Enter either (X/O): ')
    else:

        if first == 'X':
            X_turn()
        elif first == 'O':
            O_turn()
        
        
      ##EXECUTION## 
            
play()