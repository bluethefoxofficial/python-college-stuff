
import random
import arcade

def draw_pine_tree(x, y):

    arcade.draw_triangle_filled(x + 40, y,       
                                x, y - 100,    
                                x + 80, y - 100, 
                                arcade.color.DARK_GREEN)

    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


def guim():
    
    
    treenum = 0
    
    

    SCREEN_WIDTH = 1920 
    SCREEN_HEIGHT = 1080

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Exampl for game")

    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()




    for i in range(0, random.randint(1, 6)):
        x = random.randint(0, SCREEN_WIDTH - 60)
        y = random.randint(0, SCREEN_HEIGHT - 60)
    
        draw_pine_tree(x, y)
        treenum += 1
    





    arcade.finish_render()

    arcade.run()



def consolem():
    
    print("<Console mode>")
    
    
    
    
    
    
    
    
mode = input("mode 1 for gui 2 for console>")


if mode == "1":

    guim()

elif mode == "2":
    consolem()