import libtcodpy as libtcod

#Size of window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

 
 
def handle_keys():
    global playerx, playery
 
    #key = libtcod.console_check_for_keypress()  #real-time
    key = libtcod.console_wait_for_keypress(True)  #turn-based
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
 
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1
 
 



libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.sys_set_fps(LIMIT_FPS)



while not libtcod.console_is_window_closed():
	libtcod.console_set_default_foreground(0, libtcod.white)

	libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)

	libtcod.console_flush()

