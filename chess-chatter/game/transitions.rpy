transform walk_away_right(d=10):
    xanchor 0.5
    linear d xpos 1.9

# ZOOM
transform small:
    yanchor 1.0 ypos 1.0
    zoom 0.9

transform unsmall:
    yanchor 1.0 ypos 1.0
    zoom 1.0

transform zoom_in(d=2, v=1):
    yanchor 1.0 ypos 1.0
    ease d zoom v

transform zoom_in_b(d=2, v=1):
    yanchor 1.0 ypos 1.0
    easeout d zoom v

transform zoom_in_c(d=2, v=1):
    yanchor 1.0 ypos 1.0
    easein d zoom v

transform zoom_to_center(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    ease d zoom v xpos 0.5

transform zoom_to_center_b(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    easeout d zoom v xpos 0.5

transform zoom_to_center_c(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    easein d zoom v xpos 0.5

transform zoom_to_left(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    ease d zoom v xpos 0.2

transform zoom_to_left_b(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    easeout d zoom v xpos 0.2

transform zoom_to_left_c(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    easein d zoom v xpos 0.2

transform zoom_to_right(d=2, v=1):
    yanchor 1.0 ypos 1.0
    xanchor 0.5
    ease d zoom v xpos 0.8

# ...
transform to_left:
    xanchor 0.5
    ease 2.0 xpos 0.2

transform to_right:
    xanchor 0.5
    ease 2.0 xpos 0.8

transform to_right_center:
    xanchor 0.5
    ease 2.0 xpos 0.66

transform to_center:
    xanchor 0.5
    ease 2.0 xpos 0.5

# characters
transform from_left(d=2):
    xanchor 0.5 xpos -0.2
    ease d xpos 0.2

transform from_right(d=2):
    xanchor 0.5 xpos 1.2
    ease d xpos 0.8

transform from_right_b(d=2):
    xanchor 0.5 xpos 1.2
    easeout d xpos 0.8

transform from_right_c(d=2):
    xanchor 0.5 xpos 1.2
    easein d xpos 0.8

transform from_left_fast:
    xanchor 0.5 xpos 0
    ease 2.0 xpos 0.2

#transform from_far_right:
    #xanchor 0.5 xpos 1.4
    #ease 2.0 xpos 0.9

# SIT
transform sit_left:
    xanchor 0.5 xpos 0.2
    ease 1.0 ypos 0.07

transform sit_right:
    xanchor 0.5 xpos 0.8
    ease 1.0 ypos 0.07

transform bg_sit:
    #yanchor 1.0
    ease 1.0 ypos -0.06

#
transform left_to_center:
    xanchor 0.5 xpos 0.2
    ease 2.0 xpos 0.5

transform right_to_center:
    xanchor 0.5 xpos 0.8
    ease 2.0 xpos 0.5

transform center_to_left:
    xanchor 0.5 xpos 0.5
    ease 2.0 xpos 0.2

transform center_to_right:
    xanchor 0.5 xpos 0.5
    ease 2.0 xpos 0.8

transform left_to_nothing:
    xanchor 0.5 xpos 0.2
    ease 2.0 xpos -0.5

transform left_to_nothing_b:
    xanchor 0.5 xpos 0.2
    easeout 2.0 xpos -0.5

transform left_to_nothing_c:
    xanchor 0.5 xpos 0.2
    easein 2.0 xpos -0.5

transform right_to_nothing:
    xanchor 0.5 xpos 0.8
    ease 2.0 xpos 1.5

# bg
transform bg_center_to_right:
    xanchor 0.5 xpos 0.5
    ease 2.0 xpos 0.55

transform bg_center_to_right_b:
    xanchor 0.5 xpos 0.5
    easeout 2.0 xpos 0.55

transform bg_center_to_right_c:
    xanchor 0.5 xpos 0.5
    easein 2.0 xpos 0.55

transform bg_right_to_center:
    xanchor 0.5 xpos 0.55
    ease 2.0 xpos 0.5

transform bg_center_to_left:
    xanchor 0.5 xpos 0.5
    ease 2.0 xpos 0.45

transform bg_left_to_center:
    xanchor 0.5 xpos 0.45
    ease 2.0 xpos 0.5

transform bg_left_to_center_b:
    xanchor 0.5 xpos 0.45
    easeout 2.0 xpos 0.5

transform bg_left_to_center_c:
    xanchor 0.5 xpos 0.45
    easein 2.0 xpos 0.5

# fade
transform char_fadeout:
    alpha 1.0
    ease 1.5 alpha 0.0

transform char_fadein:
    alpha 0.0
    ease 1.5 alpha 1.0

transform invisble:
    alpha 0.0

transform very_long_fadein(d=12):
    alpha 0.0
    ease d alpha 0.4

transform fast_fadeout:
    alpha 0.4
    ease 3 alpha 0.0


#
transform chess_static:
    zoom 0.7
    xpos -0.38
    ypos 0

transform chess_zoom(d=2):
    ease d zoom 0.7

transform chess_zoom_board(d=2):
    ease d zoom 1.0 xpos -0.75

transform chess_center(d=2):
    ease d xpos -0.38

transform chess_right(d=2):
    ease d xpos -0.12

transform chess_left(d=2):
    ease d xpos -0.64



# 

