define anon = Character('Announcer', what_color='#ffffff')
define dav = Character('David', what_color='#ffffff')
define sus = Character('Susie', what_color='#ffffff')
define me = Character('Me', what_color='#ffffff')

image fade_background = Solid('#000000')

label start:
    
    python:
        aff_dav = 0
        aff_sus = 0
        moral = 0
    
    call ambient_start
    
    call intro
    call game_mid
    call outro
    call credits
    
    return
