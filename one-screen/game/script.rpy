define anon = Character('Announcer', what_color='#ffffff')
define dav = Character('David', what_color='#ffffff')
define sus = Character('Susie', what_color='#ffffff')
define me = Character('Me', what_color='#ffffff')

image fade_background = Solid('#000000')

image bg chess empty = LiveComposite(
    (1280, 640),
    (-70, 0), "bg chess",
    (-70, 0), "board empty")

image bg chess random = LiveComposite(
    (1280, 640),
    (-70, 0), "bg chess",
    (-70, 0), "board random")

image bg chess full = LiveComposite(
    (1280, 640),
    (-70, 0), "bg chess",
    (-70, 0), "board full")

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
