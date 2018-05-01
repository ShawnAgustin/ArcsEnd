label start:

    # variables
    $ healer_FP = 0
    $ tank_FP = 0
    $ dps_FP = 0
    $ bad_ending = 0

    #show screen fp_points
    call prologue from _call_prologue
    call main_story from _call_main_story
    call tank_preArc from _call_tank_preArc
    call tank_done from _call_tank_done


    #call dps_preArc


    # continue main arc


    return
