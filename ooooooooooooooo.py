#import sound library




def clearscreen():
    print("\n" * 100)
    
clearscreen()

array_2d = [['', '', ''], 
            ['', '', ''], 
            ['', '', '']]

#print array_2d as a grid





def drawing():

    for i in range(3):
        for j in range(3):
            if(array_2d[i][j] == '0'):
                print("|"+"0", end="")
            elif(array_2d[i][j] == 'X'):
                print("|"+"X", end="")
            else:
                print("|"+" ", end="")
        print("|")
                
                
                
r = int(input("Enter the row: "))
c = int(input("Enter the column: "))

array_2d[r][c] = 'X'
drawing()


r = int(input("Enter the row: "))
c = int(input("Enter the column: "))



if(array_2d[r][c] == '0'):
    print("You already chose that spot")
    
elif(array_2d[r][c] == 'X'):
    print("That spot is already selected")
else:
    array_2d[r][c] = '0'
    drawing()