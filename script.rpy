# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Miki", color = "#dae03b")
define pov = Character("[povname]")

image WinterMikiFrown:
    "wintermiki frown.png"
    zoom 0.25

image WinterMikiUnHappy:
    "wintermiki unhappy.png"
    zoom 0.25

image WinterMikiSmile:
    "wintermiki smile.png"
    zoom 0.25

# The game starts here.

label start:
    $ povname = renpy.input("What is your name?", length=32)
    $ povname.strip()
    if not povname:
        $ povname = "uname"
    
    scene bg apartmentnight
    "you, [povname] are a completely loser in the real life "
    "You got bad grade and no ones love you"
    "you live in your room and never go outside"
    "one day you decide to go to the convenient store and buy some drinks"
    "at the time you try to J walk, a truck just crushing on you"
    "you die"
    "but you go to the dream world immediately"
    "hooray, you just be reincarnated and mushoku tensei"
    "God" "try to be a winner and get rid of loser's life!!!"

label bgm:
    scene bg futonroom
    with fade

label sprites:
    show WinterMikiFrown
    e "Onichan are you ok?"
    e "Do you know UT have final exam at next week"
    

label character:
    show WinterMikiUnHappy with dissolve
    e "Hey are you listening?"
    e "you feeling unwell right now"
    menu:
        "Yes":
            e "ok I got it"
label choices:
    show WinterMikiFrown
    default learned = False
    e "Do you think learning data structure, run time correctness and complexity, also the regex and DFSA and NFSA is useful?"

menu:
    "Yes":
        show WinterMikiSmile with dissolve
        jump choices1_a
    
    "no":
        show WinterMikiUnHappy
        jump choices1_b

label choices1_a:
    e "Good"
    $ learned = True
    jump choices1_common

label choices1_b:
    e "you make me piss off jackass"
    jump choices1_common

label choices1_common:
    e "you have a fucking csc236 final exam on next week"
    e "stupid UT only love bookworm"
    e "you are not hard working enough"
    e "that's the reason why you don't get success"

label flags:
    if learned:
        e "you r a good student I love you onichan"
    else:
        e "you r not a good student, you should review your csc236 final exam and do great job before talking to me"







    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
