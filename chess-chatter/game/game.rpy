label game_mid:
    "And then, game begins."
    
    scene bg chess full at chess_static
    with fade
    
    show fade_background at invisble
    
    show susie normal at from_left
    show david normal at from_right
    
    pause 1.0
    
    "David and Susie seat in front of each other, taking sides of a weird ritual table."
    
    show susie at sit_left
    show david at sit_right
    show bg at bg_sit
    
    "In fact, it can hardly be called table."
    "It's looks like two massive boxes attached to each other and firmly secured to the arena floor."
    "But the most interesting part is it's surface."
    "Most of it is covered with thick green glass."
    "There are also few tiny metallic rods sticking out on one side outside of glass cover."
    "Unlike some of youngsters might think, this is not some usual cheap ritualizing stuff like what is used in other gambling houses."
    "It is much more ancient and authentic."
    "Even the oldest players which seen it couldn't say anything positive about it."
    "Some say it's one of the artifacts, but then why nobody could make use of it?"
    "Everybody know now that artifacts are not some kind of abstract magic."
    "Guns are made for destruction, to hurt and kill people or animals, and not to dance around and pray."
    "Conserve cans just contain some weird preserved food in them and not to be used as drums."
    "Not to mention lots of more obvious things."
    "But this \"table\" and especially it's \"screen\" (some use this name to refer to it's glassy surface), is different."
    "No one made reasonable explanation for it."
    "Maybe it's just broken. Or probably it is one of the actual ritual stuff bearing no reasonable meaning from the beginning."
    ".."
    
    "But no matter how interesting this table is, game is usually more interesting than what it is played on."
    "I briefly look at the board."
    
    show bg chess opening
    with dissolve
    
    "First few moves were nothing interesting."
    "Only confirmed opponents have some basic openings knowledge."
    "Which isn't really surprising in a town famous for it's chess gambling, but still, one could expect worse from such shabby players."
    
    ".."
    
    show bg at chess_left
    show fade_background at very_long_fadein
    show david at right_to_center
    show susie at left_to_nothing
    
    call ambient_low
    play music "vagabond" fadein 10 fadeout 10
    
    "Suddenly when i look at the faces of players, i see David speaking."
    dav "..at brings you here?"
    "I can't hear him in this noise, but long time ago i had lost my hearing and then learned to read lips."
    "Luckily, i sit in position where i can see both of their faces and quite close."
    dav "You don't need to tell if you don't want to, but won't it be more human to at least know your opponent?"
    menu:
        "More human?"
        "What's he talking about?! Being human in gambling? Really?":
            $ moral -= 1
            "Well, probably he's just trying to let Susie's guard down."
            "Or to soften her so that she would handle him better if he loses."
        "He may have a point here.":
            $ moral += 1
            "Even if it doesn't change the whole situation, remaining human is always important."
            "More to yourself than anybody else."
    ".."
    dav "And if you are in grief, it's better to speak it off to somebody."
    sus ".."
    "Susie still remains silent."
    dav "Ok, i'll start about talking myself first then."
    dav "As you might know, my name's David."
    dav "I was born in a small village far far north."
    dav "So far, that we when there was winter, we rarely saw sun at all."
    dav "It surely was cold as hell, but we all were used to it from childhood."
    dav "But even being born there, i couldn't get used to live nearly half of year in darkness."
    dav "Probably that's because i heard stories and read books about sunny southern lands."
    dav "Otherwise, how could child even imagine that there could be different places?.."
    "Despite talking, David is still playing."
    show bg chess two figures
    with dissolve
    "There is no strict time control in such games, except for when players demand it."
    "So it's completely fine that his thinking takes some time."
    "But maybe he's doing that to distract opponent?.."
    dav "..And then someday i decided to run away to those great lands of south i created in my imagination."
    dav "I was young and naive and couldn't understand the world isn't like those fancy stories."
    dav "So then my journey started."
    dav "I can call it a miracle that i survived first winter."
    dav "I met it in a city called Eshuima."
    dav "It was way souther than my nameless village, but it wasn't that warm fertile land i imagined."
    dav "Only summer was hot, but the winter was still cold and if i wouldn't find a place to live in, i would die for sure."
    dav "But that place was still hell."
    dav "Not freezing hell i was used to, but hot hell of everyday twelve-hour hard labour."
    dav "If you have never left this city, you probably never saw the great machinery of mid-north people."
    dav "It still comes to me in my nightmares."
    dav "Judging by rumors i heard there, they decided to rebuild empire of their ancestors."
    dav "No, they don't have it yet. They only have several cities and a bunch of villages around them."
    dav "But they are building power."
    dav "They restored a lot of knowledge from the past and keeping it in secret, use it for what they are calling \"industry\"."
    dav "I worked there. I know what it means."
    dav "It's not the path to world prosperity and happiness like some fools think it to be."
    dav "Just take one aspect."
    dav "Here, in this town of darkness and ignorance, you have some guns from ancient era."
    dav "They are being repaired and passed on from generation to generation."
    dav "Ammunition for them is either awful or hard to produce and extremely costly."
    dav "So you don't even use guns for hunting."
    dav "Only for defence except for rare types who.."
    "At this point, i wasn't able to see what he was saying."
    "Someone was in the way of my sight and i could only see big \"magnetic chess\" board, which reproduced the game for those who couldn't see original."
    
    show fade_background at fast_fadeout
    show david at char_fadeout
    call ambient_normal
    call music_fade
    call angry_crowd
    
    "This brought me back to reality for a moment."
    "I nearly completely ignored the sounds while i was watching David's speech and now wave of noise filled my ears."
    
    
    show bg chess eaten
    with dissolve
    
    #show bg at chess_zoom_board
    
    "And i even stopped to follow the game, which was slowly moving forward."
    "They played open game, getting rid of figures without any reluctance, and now each had only knight out of light figures."
    "And while she might not realize bad consequences of this, Susie is left with two pairs of doubled pawns."
    "One of my neighbours seem to be irritated by this, spreading irritation further."
    "Suddenly, i spot a vendor selling snaks among the rows."
    "I take a closer look."
    
    menu:
        "All of them look disgusting, but my stomach growls from the smell of meat."
        "Buy a fried rat":
            show o rat at take_item
            "Poor fucker, but it's a man-eat-rat world."
            "..."
            "That wasn't enough, but i at least feel a little less hungry now."
            hide o
            with dissolve
        "Buy a bag of crow eyes":
            show o crow at take_item
            "Mmm... Chewy.."
            "..."
            "That wasn't enough, but i at least feel a little less hungry now."
            hide o
            with dissolve
    
    #show bg at chess_zoom
    #pause 2
    #show bg at chess_left
    
    show fade_background at very_long_fadein
    show david normal at char_fadein
    call ambient_low
    call music_unfade
    call angry_crowd(0)
    
    "Finished with food, i glance back at playing table and is captured back into David's monologue."
    dav "..produce everything using conveyor technology, increasing production rate and decreasing price."
    dav "Price of shells is so low that you could hear gunfire all day long in several districts."
    dav "And these are not from armed thugs - no, security is good there because most of society is so maniac about their \"state\"."
    dav "These are from firing ranges where youngsters are trained to shoot."
    
    show bg chess black attack
    with dissolve
    
    "When he said \"shoot\", Susie looked at him and then moved queen to check his king."
    "He paused briefly, looking at board."
    "Then without much thinking, moved king away."
    dav "So, what was i speaking about?.."
    dav "Enough of this Eshuima talk."
    dav "When the spring came and nights became warm enough to not freeze to death near fire, i run away from there even with more resolution than i had leaving my home."
    dav "I was traveling with trading caravans, by myself, then with a gang of ruffians."
    "Suddenly he stopped. Susie was looking at him with mixed expression of interest and fear."
    dav "..Why.. yet again, because i was so naive."
    "He probably answered her question which i missed."
    dav "I read ancient legends about nice villains."
    dav "But these were different. They weren't some kind of violent blood-thirsty maniacs, no."
    dav "But they only cared about having fun: drinking and gambling while they had money and robbing (and thus occasionally killing) people when they run out of it."
    dav "Probably i was raised in completely different culture, but it seemed strange to me: they were so nice and friendly to me, complete stranger, just because i joined them."
    dav "And with the same easiness they killed or took away last means of living from other strangers who happened to be in their way."
    
    show bg chess loosing queen
    with dissolve
    
    "Then he abruptly stopped talking again, looking at the board."
    "His previous move was made without thinking and Susie used that."
    "Now he had only one possible move and that was losing queen without even taking weaker figure in exchange."
    "With a sad smile on his face, he made that move."
    "Susie looks more confident now."
    "Before, she looked so desperate that i couldn't see any glimmer of hope on her face."
    "Now she had that specific expression of people who see spider thread appearing of nowhere and leading them to salvation."
    "David stopped talking for a while, concentrating on thinking."
    
    show fade_background at fast_fadeout
    show david at char_fadeout
    call ambient_normal
    call angry_crowd
    
    "Public demanded action."
    "Some were in rage for this careless loss."
    "My neighbour mentioned above was happy and was yelling \"GIVE UP, GIVE UP\"."
    "Several fellows picked that up and for a brief moment noise became unbearingly loud."
    "Somehow, stuff managed to calm the crowd down."
    "In the corner of my view i see guards taking away one of the most stubborn hecklers."
    
    show fade_background at very_long_fadein
    show david at char_fadein
    call ambient_low
    call angry_crowd(0)
    
    "David's face remained mostly calm through this noise, only twitching once or twice."
    
    show bg at chess_center
    show david at center_to_right
    show susie scared at from_left
    
    "But Susie, not accustomed to such places, reacts more painfully, even though crowd is cheering her up."
    "For a moment, she covered her ears with hands and tried to concentrate on board."
    "Then David probably said something to her, because she started to look at him with listening expression and opened her ears."
    "Soon, they got back to game."
    "And after couple of moves, David resumed talking."
    "But he was mostly concentrating on chess now."
    dav "So.. i left them. And continued my journey alone.."
    dav "Probably there isn't much time left of it now."
    dav "..And not much time to tell all of it."
    "He paused, looking at Susie's face. Their gazes met."
    
    #show david tired
    stop music fadeout 3
    
    "His expression changed. That fire in his eyes i could see earlier, was gone."
    dav "I'm tired of this."
    "And it was visible. He probably was gathering all his strength up to this moment."
    "But now he was clearly one of those tramps sleeping in the open air and eating rubbish."
    "Susie said something to him and he shook his head, looking back at board."
    
    show bg chess preparing counter
    with dissolve
    
    "Judging by his moves, he doesn't want to give up yet."
    "David is clearly planning something, having placed rooks in one line."
    "Suddenly, Susie started to speak, not looking at him at all."
    
    show bg at chess_right
    show david at right_to_nothing
    show susie scared at left_to_center
    call ambient_low(0.5, 3)
    play music "sad-theme" fadein 5.0 fadeout 10.0
    
    sus "What brings me here?"
    sus "What can bring me here except for despair?"
    sus "I lost my husband."
    sus "I have nobody left, i'm all alone now."
    sus "All alone in this dog-eat-dog society"
    sus "I won't survive this winter without harvesting and i can't do that alone."
    sus "And there is nobody to help, even for price!"
    sus "In this town, nobody cares about others."
    sus "Only about money and i can't afford paying much before selling yield."
    sus "One man told me to go here when i asked for help."
    sus "He had this disgusting smile on his face when said that."
    sus "Probably just wanted to see this spectacle."
    
    show susie normal
    "She smiles weakly and somewhat spiteful."
    sus "He probably never thought i had studied chess when i was younger and just wanted to laugh at me."
    sus "Even though i never had any exceptional talent in it, playing chess with my grandfather is my best childhood memory."
    sus "He died when i was teenager and i never managed to become even close to his level.."
    sus "I never had any worthy opponent since then and i'm probably much worse now."
    sus "But still, i thought i may have a chance.."
    "She pauses, making another move, eating another pawn."
    "David is considering something, whether her words or game i can't tell."
    dav "Was he a good man?.."
    dav "Your husband."
    "He added after a short pause, realizing his phrase is not understandable in current context."
    "She hesitates to answer, but then speaks up."
    sus "..Yes, you can say so."
    sus "I never loved him like i was supposed to, but he was a good person."
    sus "He.. he wasn't open to me, but he cared in his own way. Maybe even loved me."
    sus "Sometimes he was.."
    "She bites her lips and stops."
    sus "We were a good family. And.. i can't live on myself anymore.."
    "I can barely understand what Susie is saying. She hardly opens her mouth."
    "David looks at her, but she only looks down."
    "I think he said something and she made a slight nod."
    "He looks to the board, probably deciding something important."
    
    show bg chess move knight
    with dissolve
    
    "Then, sighing, he moves knight with confidence of a man who has placed all his hope into single chance."
    "Atmosphere becomes more intense as he proceeds with attack preparations."
    "But Susie is either too depressed or feels too safe due to huge material advantage."
    "She doesn't seem to be very attentive."
    "She stopped talking, but probably is still thinking about her life."
    
    show bg at chess_center
    show david at from_right
    show susie scared at center_to_left
    show fade_background at fast_fadeout
    call ambient_normal
    stop music fadeout 2
    
    pause 2
    
    show bg chess check rooks
    with dissolve
    
    "Another turn and David checks by opening rooks."
    "Susie again thinks for a while. Then considering possible material loss, she moves king into the corner."
    "Subtle victory smile appears on her opponent's face."
    "He checks again, sacrificing one of rooks."
    "Now black are forced to accept sacrifice."
    
    show bg chess mate
    with dissolve
    
    "And next move, already foreseen by a few professional players among the audience, is mate with that same knight."
    ".."
    
    call angry_crowd
    "Now public roars without any previous hesitation."
    "Those who won and those who lost their bets. And those who were watching for fun."
    "Winner is praised and applaused, loser loses interest of most, while some notorious fellows already approach her to offer their dirty deals."
    
    return
