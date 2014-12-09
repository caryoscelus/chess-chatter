label intro:
    call ambient_normal(1, 2)
    
    play music "circus-drum" fadein 5 fadeout 5 noloop
    
    scene bg lots:
        xpos 0.45
    
    show fade_background at invisble
    show announcer speech at from_left_fast
    show bg lots at bg_left_to_center
    
    pause 2.0
    
    anon "Welcome, welcome, welcome!"
    anon "Here goes the show of the day!"
    anon "Chess battles with high stakes!"
    anon "And, first pair in our program, let's see..."
    "Announcer makes a pause, trying to increase dramatism of the moment."
    
    stop music fadeout 2
    play sound "gunshot"
    show announcer with vpunch
    
    anon "..David and Susanna!"
    anon "Please come here!"
    "Two figures separate from the grey mass of players waiting for their turn and head towards arena entrance."
    
    show david mute at from_right, small
    show david at to_right_center
    show susie normal at from_right, small
    
    "When they finally appear near him, announcer continues."
    anon "..Now, do you solemnly swear to fulfill your deal and pay fully and in time if you loose?"
    
    "(yeah, like it's even {i}possible{/i} to not pay fully when you have already deposited your bet)"
    "Both players nod in agreement and say something."
    
    anon "Okay, now will you please take your lots?"
    anon "Who will play white and who will play black - that's the question!"
    anon "You'll have only one game, only one chance, so please choose carefully!"
    
    anon "And you, bettors, you have your last chance to reconsider your bets after lots are taken!"
    
    call ambient_normal(0.5, 2)
    
    "When announcement is over, his acting slips and for a brief moment i can see tired old man."
    "And public becomes somewhat silent in anticipation of fate choice."
    
    menu:
        "While they are taking their lots, i examine players."
        "Look at man":
            $ aff_dav += 1
            call man_then_woman
            #call show_two_guys((david, man_description), (susie, woman_description))
        "Look at woman":
            $ aff_sus += 1
            call woman_then_man
            #call show_two_guys((susie, woman_description), (david, man_description))
    
    jump after_choice_podium
    
label man_then_woman:
    show bg at bg_center_to_left, zoom_in(2, 1.08)
    show fade_background at very_long_fadein(2)
    show announcer at left_to_nothing
    show david at zoom_to_center(2)
    show susie at right_to_nothing
    
    call man_description
    
    show bg at bg_left_to_center, zoom_in(2)
    show david at zoom_to_left_b(2, 0.9)
    show susie at from_right_b
    pause 2
    show bg at bg_center_to_left, zoom_in(2, 1.08)
    show david at left_to_nothing_c
    show susie at zoom_to_center_c(2)
    
    "Then i switch my gaze at the second player."
    call woman_description
    
    show bg lots at bg_left_to_center, zoom_in(2)
    show susie at zoom_to_right(2, 0.9)
    show david at from_left
    show fade_background at fast_fadeout
    return

label woman_then_man:
    show bg at bg_center_to_left, zoom_in(2, 1.08)
    show fade_background at very_long_fadein(2)
    show announcer at left_to_nothing
    show susie at zoom_to_center(2)
    show david at right_to_nothing
    
    call woman_description
    
    show bg at bg_left_to_center, zoom_in(2)
    show susie at zoom_to_left_b(2, 0.9)
    show david at from_right_b
    pause 2
    show bg at bg_center_to_left, zoom_in(2, 1.08)
    show susie at left_to_nothing_c
    show david at zoom_to_center_c(2)
    
    "Then i switch my gaze at the second player."
    call man_description
    
    show bg lots at bg_left_to_center, zoom_in(2)
    show david at zoom_to_right(2, 0.9)
    show susie at from_left
    show fade_background at fast_fadeout
    return

label man_description:
    "This man, who was called David, has just arrived here in our town a few days ago."
    "His shabby look and thin figure suggest that he's one of those who have lost everything and trying their luck to make living."
    "Most of such fellows loose."
    "And less lucky of them who fall into temptation to play with The Red King, loose everything."
    "Everybody think they will be the first to win against him and get all the riches he offering."
    "But in the end, no one ever won in public game with King."
    "And after each winning he kills the looser and adds their skull to his private collection."
    "Something is definitely wrong with that man (as well as with those who agree to play with him, knowing his story)."
    "But luckily, today he is only watching. Probably there won't be any blood after games."
    ".."
    return

label woman_description:
    "When i look more at her more intently, i suddenly recognize her."
    "I knew her as Susie years ago and would never thought she would end up here."
    "She must be really desperate to come here, in the most violent gambling club."
    "Susie never was the type to play out of pure interest."
    "Probably, she lost everything, but doesn't won't to give up her hope."
    "Maybe doing this for her children or dying parents who need doctor and can't afford one.."
    "But then it's pretty stupid."
    "If she has no experience, chances to win are near zero unless she's lucky to get same level opponent."
    "That might be the case though."
    ".."
    return
    
label after_choice_podium:
    "While i was thinking about their lives, they took their lots."
    "Now they both look at them and like it happens all the time at such moments, suddenly gain the opposite expressions on their faces."
    
    show david smile
    show susie sad
    with dissolve
    
    "Winning smile appears on David's face, while Susie makes a sad sigh and her desperate look becomes even more so."
    
    show bg at bg_center_to_right
    show david at walk_away_right
    show susie at walk_away_right
    show announcer at from_left
    "They slowly walk to the playing table as the announcer starts to speak again and public starts to whisper."
    #"Some even talk aloud, not concerned with strict official rules no one actually tries to enforce."
    "Some change their bets or make them just now."
    "Like betting on white or black matters."
    "If you bet on white, you'll get less gain proportional to average winning rate anyway."
    "That rule may or may not apply to players themselves, however."
    "It won't this time, since David is betting his freedom on the game."
    "So he can either became slave or not. No middle options."
    "As for Susie, her stake is more countable, but all the same, she probably bets all her savings."
    "And that deal is as fair as you can get in this town."
    ".."
    
    return
