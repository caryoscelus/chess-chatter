label outro:
    scene bg lots:
        xanchor 0.5 xpos 0.45
    with fade
    
    show bg at bg_left_to_center
    show announcer speech at from_left
    play music "circus-drum" fadein 5 fadeout 5 noloop
    
    "Announcer tries to outvoice the crowd, but he barely manages."
    anon "32 turn game by two amateurs with nearly their lives at stake, is now over in a funny ending where pure material weight doesn't matter anymore!"
    
    call angry_crowd(0, 10)
    
    "His voice is somewhat formally happy like always when he can see the public was entertained and club gained a lot from bets."
    "It's his job to be happy at such moments, so all the sincerity has vanished long time ago."
    
    show announcer at left_to_nothing
    show bg at bg_center_to_left
    show david normal at from_right
    
    "On the other hand, David seems to be genuinely happy at first."
    "By hobo standards, he is rich now."
    "But then his face becomes tired and somewhat irritated as he tries to push throw the crowd and all the dealers offering him management"
    "(Which is basically robbing off player with nearly no guarantees; some say this tradition has been successfully carried from the ancient times, but who would believe that?)."
    dav "I just want some ramen and a bed to sleep on"
    "He says that to no one in particular."
    "But that immediately leads to a bunch of merchants importunately offering him their services."
    "I notice sheriff's secret agent (or rather errand boy) carefully watching if someone will rob the winner."
    "He doesn't do that out of love for justice, but just for profit: if the criminal is found, he will be sold into slavery."
    "And half of the price will go directly to sheriff. The other half will go to him indirectly."
    "Surely he'll share a little bit of it with this kid."
    "But David seems to be cautious: even if he's new to our town, he's certainly not new to this kind of clubs."
    
    menu:
        "Now, what should i do?"
        "Search for Susie":
            call outro_susie
        "Leave":
            call outro_leave
    jump outro_end
    
label outro_susie:
    show bg at bg_left_to_center
    show david at right_to_nothing
    
    "I have other plans at home, but.."
    "After spending all the game \"listening\" to their conversation, i just can't leave them alone without knowing how it all ends."
    
    "I switch my gaze to the crowd, searching for Susie."
    show bg at bg_center_to_right
    pause 2.0
    
    "After a few moments, i find her."
    
    show susie drinking at char_fadein
    
    "She stands near the bar, apparently waiting for barman to fulfill her order."
    "He doesn't try to be fast. She bears no interest for him in current state of looser."
    "He's not the type who now awaits her probable \"moral fall\", neither for his own pleasure, nor for profit."
    "When he finally gives her some drink in a dirty glass, she greedily swallows it in a few gulps."
    "By her reaction, i can see she never drank something stronger than ale."
    "But Susie doesn't seem to care about how she looks now."
    "She puts her head on counter and sobs silently."
    "I watch her like that, probably for a few minutes."
    "Then, decided there's no use to watch from such distance, push through the crowd to the bar."
    
    show bg
    show susie sad at from_left
    with fade
    
    "Susie sits there with her head on counter, faced towards me."
    "She doesn't sob anymore, just stares beyond the crowd into nothingness."
    "Passer-bys sometimes pause their glances on her and disapprovingly shaking their heads, move along."
    "The seat near her is empty, so i take it."
    "She doesn't react at first."
    show susie normal
    with dissolve
    "Then, her eyes twitch, acknowledging my presence."
    
    menu:
        "What should i do?"
        "Talk to her":
            pass
        "Nothing more interesting here":
            jump outro_leave
    me "Umm, hello. You might not remember me, but we have met long time ago."
    me "So.. Maybe i can help you with something?.."
    "I still wonder why i am even saying that."
    
    sus "Help?.."
    sus "Now?.."
    "She answers without much thought."
    
    sus "He said.. i can.."
    "I can't understand what she is mumbling now."
    sus "Why did?.. I should've agreed."
    sus "Ah, you can't understand."
    "She says that somewhat irritated, but sounding more sane now."
    sus "Just take me out of here, please."
    sus "I can hardly find my way in this stinking place.."
    
    "I help her to get up."
    "Then we slowly move out to the street."
    
    call ambient_normal(0, 1)
    scene black
    with fade
    
    "It is early evening. Freed from the noises of the crowd, we stay near the entrance of this gambling house."
    "A few minutes pass in silence."
    "Then Susie suddenly straightens up, having decided on something."
    sus "Thank you, stranger. I am fine now."
    sus "I will leave.. leave this place, this town altogether."
    sus "And if i die, please remember me."
    "(She probably isn't fully sober yet if she thinks i can detect her death far from here)"
    "Not adding another word, she leaves."
    
    scene bg road:
        #zoom 0.125
        zoom 0.5
    with fade
    
    show bg:
        yanchor 0.3 ypos 0.3
        xanchor 0.5 xpos 0.5
        #linear 80 zoom 0.375
        linear 50 zoom 2
    
    play music "vagabond" fadein 10 fadeout 10
    call music_unfade(0.5, 5)
    
    "This change in her happened so fast that i just stay there astonished and watch her walk."
    "When she is far out of my reach, i finally realize i haven't even said \"goodbye\"."
    ".."
    me "Goodbye, Susie. I hope you made right choice."
    "She can't hear me now, but for some reason i still say it."
    ".."
    "And then i just stand there, watching sunset even after loosing sight of her figure."
    
    return

label outro_leave:
    "There's nothing more to see here."
    "I leave."
    
    call ambient_normal(0, 1)
    scene black
    with fade
    "On my way home, i can't help but think about this game."
    "It's not like i never seen drama in gambling, but something about it felt different."
    "Maybe.. it's that \"being human\" David mentioned?"
    ".."
    "Probably i just should have a good dinner and stop thinking about stupid things."
    return

label outro_end:
    #scene black
    #with fade
    "END."
    
    return
