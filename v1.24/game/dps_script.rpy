# Main Arc: Martin

label dps_preArc:
    play music "music/Katawa Shoujo OST - Raindrops and Puddles.mp3" 
    
    scene town square with dissolve
    m "I guess I'll go level up by grinding the Dungeon."
    
    scene black with fade
    "3 hours of grinding later..."
    
    scene dungeon with dissolve
    m "Damn, these ants are getting easier."
    m "I can even solo the Queen Ant now. I must be too high level."
    m "I'm just gonna finish this last mob and head back to town."
    
    # DPS entrance and KS
    show ant at right with dissolve
    show DPS at offscreenleft
    show DPS:
        linear 1.0 xalign 1.0
    show DPS smile
    dps "KyaaaAAAAAHHH!" with vpunch
    hide ant with vpunch
    
    m "What?!"
    dps "Hey there [m]! You look much stronger since the last time I've seen you."
    m "HEY!? You KS'd me!"
    dps "Let's call it kill secure! Ok? ;)"
    #show winkyfaceDPS
    m "Whatever."
    dps "Hey, you wanna party up instead? That way our exp is shared."
    m "Alright, I guess that sounds good. Let me just clear my inventory back in the town square."
    #play sound "party_up.mp4"
    
    scene loadscreen with dissolve
    #play "loadscreen.mp4"   
    pause 2
    
    call loadscreen from _call_loadscreen_1
    
    scene town square with dissolve
    dps "U set? ;:^)"
    m "Yep, let's go to the wasteland to grind higher level mobs."
    m "I'll focus on supporting, you can go on the offense."
    m "I need to level up my white magic anyways." 
    dps "Sounds good bby. <3 ;)"
    
    
    
return
label dps_mainArc: 