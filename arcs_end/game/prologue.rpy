label prologue:
    $ player_name = "???"

############################################################################
    scene classroom
    play music "music/Classroom.mp3"

    show reno with dissolve
    reno "Good job everyone. Don't forget to do your homework and enjoy your summer!"
    hide reno with dissolve
    "Classmate A" "Pssst! What are you doing over your summer break?"
    "Classmate B" "I'm going to get a copy of that new game that's coming out tonight!"
    "Classmate B" "Are you going to the midnight release?"
    "Classmate A" "I wish!! My mom won't let me go, she says its too late..."
    "Classmate B" "Aww man, that sucks..."

    "Sucks for them, good thing I already pre-ordered it."
    "Don't have to wait in those long ass lines."
    show reno at left with dissolve
    reno "Oh! Meiko before you go."
    show meiko surprised at right with dissolve
    meiko "Hmmm?"
    show reno superhappy with dissolve
    reno "Make sure to really focus on your homework. You don't want to get held back now! haha!"
    show meiko blush with dissolve
    meiko "..."
    meiko "Y-y-yeah, I will! Okay?"
    show meiko embarassed with hpunch:
        linear 0.5 xalign 2.0
    hide reno with dissolve

    "Man, it would suck to be called out like that in front of the class..."
    "Classmate A" "I heard that Professor Kim and and Meiko's dad are close friends."
    "Classmate B" "Ahh, so that's why he always picks on her like that."
    "Or the fact that she really never does her homework..."

    "Anyways, class is over! The game doesn't come out until midnight, so I have a couple of hours to myself."
    "Maybe I can use that time to go home and finally catch up on that anime that I was watching."
    "I forget the name, but I think it was called Your Truth in March..."
    "...or something like that."

    scene black with fade
    "{i}Your home is a walking distance away from campus.{/i}"
    "{i}The cool summer breeze touches your skin as you listen to the other students talk about their plans for the summer.{/i}"
    "{i}You walk home as you take a deep breath of relief.{/i}"
    m "That semester was stressful, but I'm glad it's all over now."
#door sound
    m "Mom! Bobo! I'm home!"
######################################################
    scene MC_room with fade
    play sound "music/bootup.mp3"
    "{i}You boot up your computer.{/i}"
    play sound "music/Keyboard Typing Sound Effect.mp3"

    scene black with dissolve
    show text "{i}A few hours later.{/i}" with dissolve
    pause 2
    hide text with dissolve
    scene MC_room with dissolve
    pause 2
    stop sound

    
    "You watch \"Your Truth in March\" to let time pass by."
    m "How is it only 6PM????"
    "I already finished watching the whole season..."
    "And I don't really have anything else to do right now."

    m "I guess I'll go check out the game's forums."
    "{i}You go to a gaming news site.{/i}"
    "{i}At the top of the screen you see read:{/i}"

    nv "{b}\"MMOHOTS FIRST LOOK AT ARC'S END\"{/b}"
    nv "{b}The most anticipated MMORPG of the year, Arc's End, is set to release at midnight!{/b}"
    nv "{b}Arc's End has reached a new record of 720,000 copies pre-ordered!{/b}"
    nv "{b}Save the Land of Ferrous from the corrupted god, Arc, and fight alongside allies.{/b}"
    "There are already a bunch of forum posts on the game's website."
    "Mainly about predictions on the classes they might have or the kind of monsters we might see."
    "One post catches my eye though. Apparently, he was a beta tester so he got to see the game early."
    "He made a list of all the things he expects to be in the final release."
    "He even posted screenshots of the menu screen when he still had access to the beta."
    m "Wow, this actually looks legit."
    "Even though I've been waiting for this game for a long time, there hasn't really been any leaked information up to this point."
    "Finding any kind of information on Arc's End, whether it's real or not, is pretty exciting."

    scene black with dissolve
    show text "{i}A few hours later.{/i}" with dissolve
    pause 2
    hide text with dissolve
    #play sound ticking clock

    scene MC_room with dissolve
    m "I can't believe there's so much to this game. I wish I could have been a beta tester."
    "Not like I could have played anyways..."
    "I was so busy with school. My mom would be on my ass anytime she saw me playing games on a school night..."
    "I don't blame her though. She wants me to go to a big university, since she wasn't able to afford it when she was my age."
    "But since it's summer, there's nothing she can do about it now."
    "I love my mom, but all the late nights I spent studying is driving me insane."
    "You can only read so much about \"The History of World Economics\" and \"Micro-Biology\" before your brain starts mixing the two together."
    "One time in class, the teacher asked me when the US Stock Market Crash happened."
    "and I answered with \"The mitochondria is the powerhouse of the cell.\""
    "Needless to say, that wasn't the right answer..."
    "This summer break is much needed."
    m "Oh, it's already almost time for the game to release. I should probably head over to the GameGo soon."
    m "I'll be back Bobo. Protect the house while I'm gone."
    bobo "Nyan~"

    scene black with dissolve

##################################################

##CONTINUE HERE NEXT TIME
    scene gameGo with fade
    #play sound "busy.ogg" on loop
    "{i}As you walk towards the GameGo store, you see that the line is already a good two blocks away from the store.{/i}"
    m "Woah...I didn't expect the line to be that long. Good thing the pre-order line isn't as long."

    "{i}As your walking to the line you notice two girls pass by with distinct expressions.{/i}"
    "{i}One of them is wearing really large glasses with this weird smile on her face, while the other person she is walking with seems to be more calm, but excited at the same time.{/i}"

    show yui superhappy with dissolve:
        xpos 0.4
    show rikku with dissolve:
        xpos 0.6

    "Happy Girl" "Aaaaaaahhhhhh~~ I can't believe we finally got it!! I've been waiting so long for this!!!"
    "Normal Girl" "Hey, calm down. Aren't you getting a little too excited?"
    "Happy Girl" "Which race are you gonna make?"
    "Normal Girl" "You're not even listening to a word I'm saying, are you...?"
    "Happy Girl" "I think I'm gonna go with the Elf race!"
    "Normal Girl" "..."

    show yui superhappy:
        linear 3.0 xalign -1.0
    show rikku:
        linear 3.0 xalign -1.0

    m "It seems like the game is attracting all kinds of people."
    m "Wait... is that..."

    show meiko scared at left with dissolve
    m "...the girl who got called out in class earlier today?"
    m "Meiko, wasn't it?"
    m "What's with that face she has on right now..."
    meiko "WAAAAAAHHHHH!! The line is so long!" with vpunch
    meiko "I knew I should've gotten here earlier!" with hpunch

    show meiko cry with dissolve
    meiko "Mom's gonna kill me if I stay out too late!" with vpunch

    show meiko surprised with dissolve
    "Someone in line" "Hey! The lines back there!"
    show meiko blush with dissolve
    meiko "Oh, s-s-sorry mister I didn't realize!!"
    hide meiko with dissolve

    m "I guess she didn't pre-order the game."
    m "Weird she doesn't seem like the \"gamer\" type."
    m "She seems like the type who spends all day chasing a butterfly."
    m "Only to realize after catching it, that it was a bird the whole time."

    scene black with dissolve
    m "Hi, I'm here to pick up a copy of Arc's End."
    "Clerk" "Sir, may I see your ID?"
    $ player_name = renpy.input("Enter your name: ")
    if player_name == "":
        $ player_name = "Jun"
    "Clerk" "Okay! Here's your copy, [player_name]. Enjoy!"
    m "Thank you!"

    scene gamego with dissolve
    "Man, I finally got my copy."
    "{i}As you're walking out of GameGo, you still see Meiko in line. She looks to have calmed down from whatever happened when you first saw her.{/i}"
    "{i}But she is no where near close to getting her copy yet.{/i}"
    "She's probably gonna be there for a while..."

    "Oh well, that's not my problem, it's time to go home and play this game finally!"
    scene black with fade
    #play walking noise

    scene MC_house with fade
    m "I'm home Bobo!"
    bobo "Nya..."
    "Bobo seems to have been sleeping since I left. Some guard cat he is..."
    m "I should probably sleep, but I really want to get a headstart on this game."
    "{i}You insert your disc into your PC and boot up the game.{/i}"

return
