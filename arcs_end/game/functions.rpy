label functions:
    # animations, etc.
    label loadscreen:
        scene black with dissolve
        with Pause(1)

        show text "Loading."
        with dissolve
        with Pause(1)
        hide text
        with dissolve

        show text "Loading.."
        with dissolve
        with Pause(1)
        hide text
        with dissolve

        show text "Loading..."
        with dissolve
        with Pause(1)
        hide text
        with dissolve

        #play "loadscreen.mp4"
        pause 2
        return

    label questaccept:
        show text "{b}QUEST ACCEPTED{/b}" with dissolve:
            ypos 0.2
        pause 1.5
        hide text with dissolve    
        return

    label questfinish:
        show text "{b}QUEST COMPLETED{/b}" with dissolve:
            ypos 0.2
        pause 1.5
        hide text with dissolve
        return
