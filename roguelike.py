import libtcodpy as libtcod
 
#Window size
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

#Maximum framerate
LIMIT_FPS = 20  
 
class Object:
    #This is a generic object: the player, a monster, an item, the stairs, etc.
    #It's always represented by a character on screen
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
 
    def move(self, dx, dy):
        #move by the given amount
        self.x += dx
        self.y += dy
 
    def draw(self):
        #Sets the color and then draws the character that represents this object at its position
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
 
    def clear(self):
        #Erases the character that represents this object
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE) 


def handle_keys():
    #Allows for turn-based gameplay
    key = libtcod.console_wait_for_keypress(True)  
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    #Exits game
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  
 
    #Movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0,-1)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0,1)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1,0)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1,0)
 
 
#############################################
# Initialization & Main Loop                #
#############################################
 
libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Basic Tutorial Roguelike', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#The player object
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)

#NPC object
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, 'K', libtcod.yellow)

#List of objects
objects = [npc, player]

while not libtcod.console_is_window_closed():
 
    #draw all objects in the list
    for object in objects:
	    object.draw()

    #blit the contents of "con" to the root console
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()


    #Erases all objects at their old positions before they move
    for object in objects:
	    object.clear()
 
    #handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break



