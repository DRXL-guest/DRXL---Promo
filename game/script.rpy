# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define b = Character("{color=#0000ffff}B{/color}utt", color="#c8c8ff")
define h = Character("")
define k = Character("")

define config.rollback_enabled = False

label splashscreen:
    show bg splash with dissolve
    "This is a Demo Version: Intended for Promotional Use Only"
    "The Visuals used in this Demo are Not Representative of the Final Game."
    return

# The game starts here.
label start:
    window hide
    show white
    show vin1 with dissolve
    stop music fadeout 2.0
    menu:
        "DR_01 - Introductions":
            call DR_01
        "DR_02 - Interactions":
            call DR_02

        "Return to Menu":
            hide vin1 with dissolve
            with dissolve
            $ MainMenu(confirm=False)()
            stop music fadeout 2.0
