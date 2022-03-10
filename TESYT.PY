array_2D = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

def draw():
    for j in range(3):
        for i in range(3):
            if(array_2D[j][i]=='0'):
                print("|"+"0",end="")
            elif(array_2D[j][i]=='X'):
                print("|"+"X",end="")
            else:
                print("|"+" ",end="")
        print("|")


def input_x():
    print("Player (X)")
    r=int(input("row:"))
    c=int(input("column:"))
    if int(r)>2:
            print("Invalid input cant be higher than 2")
            return input_x()
    if int(c)>2:
            print("Invalid input cant be higher than 2")
            
            return input_x()
    
    array_2D[r][c]='X'
    draw()



#//////       
def input_0():
    print("Player (0)")
    t=True
    while t==True:
        r=int(input("row:"))
        c=int(input("column:"))
        
        if int(r)>2:
            print("Invalid input cant be higher than 2")
            continue
        if int(c)>2:
            print("Invalid input cant be higher than 2")
            continue
        
        if array_2D[r][c]==' ':
            array_2D[r][c]='0'
            t=False
        else:
            print ("the cell already inputed: Try again")
            continue
    draw()
    
#//////   
def check_win_horizontal_x():
    if array_2D[0][0]=='X' and array_2D[0][1]=='X' and array_2D[0][2]=='X':
        print( "X is Winner")
        return 'w'
    if array_2D[1][0]=='X' and array_2D[1][1]=='X' and array_2D[1][2]=='X':
        print( "X is Winner")
        return 'w'
    if array_2D[2][0]=='X' and array_2D[2][1]=='X' and array_2D[2][2]=='X':
        print( "X is Winner")
        return 'w'
def check_win_horizontal_0():
    if array_2D[0][0]=='0' and array_2D[0][1]=='0' and array_2D[0][2]=='0':
        print( "0 is Winner")
        return 'w'
    if array_2D[1][0]=='0' and array_2D[1][1]=='0' and array_2D[1][2]=='0':
        print( "0 is Winner")
        return 'w'
    if array_2D[2][0]=='0' and array_2D[2][1]=='0' and array_2D[2][2]=='0':
        print( "0 is Winner")
        return 'w'




#//////       
def check_win_vertical_x():
    if array_2D[0][0]=='X' and array_2D[1][0]=='X' and array_2D[2][0]=='X':
        print( "X is Winner")
        return 'w'
    if array_2D[0][1]=='X' and array_2D[1][1]=='X'and array_2D[1][2]=='X':
        print( "X is Winner")
        return 'w'
    if array_2D[0][2]=='X' and array_2D[1][2]=='X' and array_2D[2][2]=='X':
        print( "X is Winner")
        return 'w'
    
def check_win_vertical_0():

    if array_2D[0][0]=='0' and array_2D[1][0]=='0' and array_2D[2][0]=='0':
        print( "0 is Winner")
        return 'w'
    if array_2D[0][1]=='0' and array_2D[1][1]=='0'and array_2D[1][2]=='0':
        print( "0 is Winner")
        return 'w'
    if array_2D[0][2]=='0' and array_2D[1][2]=='0' and array_2D[2][2]=='0':
        print( "0 is Winner")
        return 'w'
#
#
#
def check_win_diag_primary_0():
    if array_2D[0][0]=='0' and array_2D[1][1]=='0' and array_2D[2][2]=='0':
        print( "0 is Winner")
        return 'w'
    
def check_win_diag_primary_x():
    if array_2D[0][0]=='X' and array_2D[1][1]=='X' and array_2D[2][2]=='X':
        print( "X is Winner")
        return 'w'
def check_win_diag_secondary_0():
    if array_2D[2][0]=='0' and array_2D[1][1]=='0' and array_2D[0][2]=='0':
        print( "0 is Winner")
        return 'w'
def check_win_diag_secondary_x():
    if array_2D[2][0]=='X' and array_2D[1][1]=='X' and array_2D[0][2]=='X':
        print( "0 is Winner")
        return 'w'
#///main///   
draw()
t=True
while t==True:
    input_x()
    if check_win_horizontal_x()=='w':
        print("game over")
        break
    elif check_win_horizontal_0()=='w':
        print("game over")
        break
    elif check_win_vertical_0()=='w':
        print("game over")
        break
    elif check_win_vertical_x()=='w':
        print("game over")
        break
    elif check_win_diag_secondary_0()=='w':
        print("game over")
        break
    elif check_win_diag_primary_0()=='w':
        print("game over")
        break
    elif check_win_diag_primary_x()=='W':
        print("game over")
        break
    elif check_win_diag_secondary_x()=='W':
        print("game over")
        break
        
    
    input_0()