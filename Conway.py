# Conway's game of life 
# 
# Creation time 11.25 hours, as of 02 Dec 2021

# step1: Create board.  

import os, time, sys, copy, string, random

try: # Main Game Loop
    os.system('clear')
    print('\n\n\n')
    gen = 1
    # Setting constants
    width = 29
    height = 6
    board = []
    speed = 1.5
    colin = ' '
    alpha = 0
    numeric = 1  

    # Generates board
    for column in range (height):
        rows = []
        for row in range(width):
            leftovers = alpha//26
            alphad = alpha%26
            rows.append(str('a'*leftovers+string.ascii_lowercase[alphad]+str(numeric)))
            alpha +=1
        board.append(rows)
        alpha = 0
        numeric += 1
        deep = copy.deepcopy(board)

    # Checks if copied cell is dead or alive    
    def check (ccell):
        if ccell == '#':
            return 1
        else:
            return 0 

    # Display board
    def display(*args):
        print('Generation',gen)

        for each in range (len(board)):
            print('\n'+'_'*6*column)
            for eachr in range(len(rows)):
                print('|', end="")
                print(board[each][eachr],end='')
                if colin == '§':
                    if board[each][eachr] != '#':
                        board[each][eachr] = ' '
            print('|', end='')
        print('\n'+'_'*6*column)

    # Unpacks board
    def unpack(deep,board):
        for column in range(len(board)): 

            for row in range(len(rows)):
                count = 0
                cell = board[column][row]
                countcheck = 0
                for c in range(-1,2):
                    for r in range(-1,2):
                        countcheck +=1
                        if column + c >=0:
                            if row + r >=0:
                                try:
                                    ccell =deep[(column+c)][(row+r)]
                                    count += check(ccell)
                                except:
                                    pass
                            else:
                                pass
                        else:    
                            pass

                if cell == '#':
                    if count == 3 or count == 4:
                        board[column][row] = '#'
                    else:
                        board[column][row] = ' '

                if cell != '#':
                    if count == 3:
                        board[column][row] = '#'
                    else:
                        board[column][row] = ' '
        return board

    # step2: Create while loop for user to input live cells. Double entry removes live cell. display board after each.

    while True:
        #os.system('clear')
        display()
        #try:
        colin = input('Input column number, r to generate random, or § to begin\n>> ')
        if colin =='§':
                time.sleep(0.25)
                break
        elif colin == 'r':
            reng = random.randint(2, int((width*height/10)))
            for i in range(reng):
                columnv = random.randint(1,height-1)
                rowv = random.randint(1,width-1)
                board[columnv][rowv] = '#'
        else:
            for column in range(len(board)):
                for row in range(len(rows)):
                    if board[column][row] == colin:
                        board[column][row] = '#'
                        continue
                    else:
                        if deep[column][row]==colin:
                            print('here')
                            board[column][row] = deep[column][row]

        #except:
            #print('Nope try again')
            #time.sleep(speed)
            continue

    # step3: Have program loop in a time delayed fashion.
    while True:
        deep = copy.deepcopy(board)
        board = unpack(deep,board)
        display()
        gen += 1
        time.sleep(speed)
        os.system('clear')

    #        Could include a pause, rewind and speed control. 
    print('\n\n\n')
except KeyboardInterrupt:
    os.system('clear')
    print('\n\n\n\n\n\nProgram ended, final display ')
    display()
    sys.exit()