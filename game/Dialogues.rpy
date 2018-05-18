label DR_01:
    show fence with dissolve
    show bg border
    show vin2
    with dissolve
    play music static fadein 2.0
    show h 11 at f22
    show k 11 at t21
    h "...Say, is this working?"
    show h 11 at t22
    show k 12 at f21
    k "Of course, you dummy, just start already!"
    show h 22 at f22
    show k 11 at t21
    h "Greetings to our lovely audience tuning in this evening. \nWe have a special treat just for you. "
    show h 12 at f22
    show k 11 at t21
    h "Our plans are still in development, but there's nothing \nwrong with giving you a small taste of what's to come. "
    show h 13 at t22
    show k 13 at f21
    k "And if there is, this was totally all your idea, \nso everything's your fault! "
    show h 13 at t22
    show k 14 at f21
    k "You lost at rock-paper-scissors, so it's your job \nto take responsibility!"
    show h 24 at f22
    show k 15 at t21
    h "...I suppose I can live with that."
    show h ms1 at f22
    show k 11 at t21
    h "Anyhow, do you like drama, horror, and \nsweet, sweet despair? "
    show h ms2 at f22
    show k 11 at t21
    h "The look on people's faces as the last wisps of life flee from their bodies is the most exquisite sight of all."
    show h ms3 at f22
    show k 11 at t21
    h "There is nothing more exhilarating than watching those detestable beings pass into the void right before you."
    show h ms4 at f22
    show k 11 at t21
    h "No trace of their existence shall haunt the earth evermore."
    show h ms5 at f22
    show k 11 at t21
    h "And yet people still insist on dwelling upon their fading memory like aimless spectres. "
    show h ms6 at f22
    show k 11 at t21
    h "What blind contrary foolishness, projecting \nsentiments onto dead. "
    hide k
    hide h
    with dissolve
    show black:
        alpha 0.5
    show h ms7:
        zoom 2.0
        xalign 0.5 yalign 0.25
        choice:
            ease 0.1 xalign 0.498 yalign 0.251
        choice:
            ease 0.2 xalign 0.505 yalign 0.249
        choice:
            ease 0.1 xalign 0.51 yalign 0.248
        choice:
            ease 0.25 xalign 0.498 yalign 0.25
        choice:
            ease 0.15 xalign 0.505 yalign 0.2505
        repeat
    with Fade(0.0, 0.2, 0.5)

    h "Spiritless, soulless automatons, weeping for empty shells they were programmed to mourn."
    hide h
    hide black
    with dissolve

    show h 13 at t22
    show k 22 at f21
    k "But you're not like those faceless, brainless \nfools, are you? "
    show h 13 at t22
    show k 12 at f21
    k "This kind of sick twisted reality is exactly what excites your nasty sadistic heart!"
    show h 15 at f22
    show k 11 at t21
    h "Come, join us in a phantasm of carnage and chaos!"
    show h 16 at f22
    show k 11 at t21
    h "A thousand untold horrors await your eyes! \nA fae land of cruelty where civility dares not cross."
    show h 17 at t22
    show k 16 at f21

    k "...Doesn't that just sound like f u n...?"
    hide h
    hide k
    hide bg border
    hide fence
    hide vin2
    with fade
    call start
    return

label DR_02:
    show fence with dissolve
    show bg border
    show vin2
    with dissolve
    play music static fadein 2.0
    show h 11 at f22
    show k 11 at t21
    h "...Say, is this working?"
    show h 11 at t22
    show k 12 at f21
    k "Of course, you dummy, just start already!"
    show h 22 at f22
    show k 11 at t21
    h "Greetings to our lovely audience tuning in this evening. \nWe have a special treat just for you. "

    hide h
    hide k
    hide bg border
    hide fence
    hide vin2
    with fade
    call start
    return

label DR_03:
    play music main fadein 2.0
    "This Video is not Avalible."
    with fade
    call start
    return
