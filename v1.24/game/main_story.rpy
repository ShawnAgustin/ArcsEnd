label main_story:
    
    scene black with fade
    
    "Create your Character!"
    "{i}The screen is black, but you hear a voice of an old man speaking to you.{/i}"
    
    $ player_ign = renpy.input("What is your name, Adventurer?")
    if player_ign == "":
        $ player_ign = "imaJUNation" 
        
    "Old Man Voice" "What is your race, [player_ign]?"
    $ mc_race = ""
    
    menu race_pick:
        "Beast":
            "Old Man Voice" "The beasts are an agile race known for their aggressive behavior. Are you sure you want to choose this race?"
            jump beast_YN
        "Human":
            "Old Man Voice" "The humans are the dominating race, known as the Protectors of the Land of Ferrous. Are you sure you want to choose this race?"
            jump human_YN
        "Elf":
            "Old Man Voice" "The elves are mystical creatures with an expertise in the healing arts. Are you sure you want to choose this class?"
            jump elf_YN
        "Fairy":
            "Old Man Voice" "The fairies are magical beings that are known for their use of Dark Magic. Are you sure you want to choose this class?"
            jump fairy_YN
            
    label beast_YN:
        menu BYN:
            "Yes":
                $ dps_FP += 1
                $ mc_race = "Beast"
                "Character Created: [player_ign] the [mc_race]"
                jump race_done
            "No":
                jump race_pick
                
    label human_YN:
        menu HYN:
            "Yes":
                $ tank_FP += 1
                $ mc_race = "Human"
                "Character Created: [player_ign] the [mc_race]"
                jump race_done
            "No":
                jump race_pick
                
    label elf_YN:
        menu EYN:
            "Yes":
                $ healer_FP += 1
                $ mc_race = "Elf"
                "Character Created: [player_ign] the [mc_race]"
                jump race_done
            "No":
                jump race_pick
                
    label fairy_YN:
        menu FYN:
            "Yes":
                $ mc_race = "Fairy"
                "Character Created: [player_ign] the [mc_race]"
                jump race_done
            "No":
                jump race_pick
                
    label race_done:
    "Welcome to the Land of Ferrous, [mc_race]"
    call loadscreen from _call_loadscreen
    
##################################################

    play music "music/Town Square_Main Menu.mp3"
    scene town_square with fade
    
    show dale NPC with dissolve
    
    dale "Would you like to know the basics?"
    mg "I'm good. I've played multiple MMORPGs before."
    dale "Okay, now initiating tutorial stages."
    mg "Are you kidding me?"
    dale "You are playing an MMORPG which stands for..."
    mg "Seriously?! This is worse than Kingdom Kokoro 2's tutorial!"
    dale "The first MMORPG created was..."
    mg "Why did they even implement this in the game? *yawn*"
    scene black with dissolve
    show text "{i}45 minutes later{/i}" with dissolve
    pause 1.2
    hide text with dissolve
    dale "Congratulations! You've completed the tutorial."
    
    m "zzZzzZzZZz"
    
##################################################

    scene MC_room with fade
    bobo "Nyan?"
    m "zzZzzZzZZz"
    bobo "Nyaaaaaaaaaaaaaaaa!"
    "{i}Bobo jumps on your face.{/i}"
    m "WAHHHHHH! BOBO!" with hpunch
    m "Oh...I fell asleep."
    bobo "Nyan. -_-"
    m "At least I finished that stupid tutorial."
    m "How long was I out for?"
    "{i}You check the time and it reads 3PM.{/i}"
    m "SHIT! There goes my headstart!"
    m "Might as well start with what I can."
    "{b}[player_ign] is now online.{/b}"

##################################################

    scene town_square with fade
    m "I need to get started on finding some quests."
    "{i}You look around the Town Square, searching for available quests.{/i}"
    
    show dale NPC with dissolve
    "{i}You notice a large NPC with an exclamation point above his head.{/i}"
    dale "Did someone say quest? :^)"
    m "Wow, it's like they know what I'm saying in real life."
    dale "Yes, we do."
    m "What the hell?"
    dale "I need Slime Gels for my daughter's 20th birthday party."
    dale "Can you hunt and gather me 5 Slime Gels?"
    mg "Yes. Seems easy enough, but what kind of birthday party needs Slime Gels?"
    show dale NPC_smug with dissolve
    mg "Okaaay?"
    hide dale NPC with dissolve

##################################################
    scene black with dissolve
    #"{i}You head over to the grasslands.{/i}"
    show text "{i}A few minutes later.{/i}" with dissolve
    pause 1.2
    hide text with dissolve
    scene grasslands with dissolve
    m "This is pretty easy. I mean it IS the first quest."
    m "I just need 2 more slime gels."
    "{i}As you look for the last few slimes, you notice a girl having a difficult time dealing with two slimes.{/i}"

    show meiko IGN_angry with dissolve
    tank "Just die! Just dieeeee already!"
    "{i}You notice the girl attacking the slime with her fists.{/i}"
    mg "You know it'd be easier to kill it if you equip your weapon first."
    tank "I don't need your help! I can handle it just fine."
    mg "Alright. Good luck."
    "{i}Meiko notices she isn't doing any damage.{/i}"
    tank "This is gonna take me hours!"

    show meiko IGN_blush with dissolve
    tank "Uhh, wait! Could you at least show me how to equip my weapon before you go?"
    mg "Geez, did you even do the tutorial?"
    tank "I did, but I didn't really pay attention."
    mg "Well, we might as well just party up, so I can teach you the basics."
    tank "F-F-FFine, but only until I finish this quest!"
    menu tsundereYN:
        "That's fine.":
            $ tank_FP += 1
            show meiko IGN_superblush with dissolve
            tank "Thanks." 
        "Why are you making the condition?":
            show meiko IGN_blush with dissolve
            mg "I'm helping you!" 
            tank "Alright, I get it! Can you please help me?"
    #play sound "party.ogg"
    
    show meiko IGN with dissolve
    mg "Well, to start off, an MMORPG stands for ..."
    show meiko IGN_angry with dissolve
    tank "WHAT DOES THAT HAVE TO DO WITH EQUIPPING WEAPONS?!"
    scene black with fade
    show text "{i}11 minutes later{/i}" with dissolve
    pause 1.2
    hide text with dissolve
    
    scene grasslands with fade
    show meiko IGN with dissolve
    "It should've taken us 4 minutes, but I had to guide her through it."
    tank "Thanks again."
    mg "Let me add you."
    show meiko IGN_blush with dissolve
    tank "Oh okay, sure."
    scene black with fade
    
return

label tank_done:
return

label dps_done:
return

label healer_done:
return
