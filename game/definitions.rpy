# image i_duneN = im.MatrixColor("gfx/bg/dune.jpg",im.matrix.saturation(0.5)*im.matrix.tint(.75,.75,1.0)*im.matrix.brightness(-0.2))
# from: https://lemmasoft.renai.us/forums/viewtopic.php?t=10312

# Backgrounds - Color
image black = "#000000"
image white = "#ffffff"

#backgrounds - Old
image bg splash = "backgrounds/dim_splash.png"
image bg border = "backgrounds/borders.png"

#backgrounds - White Fence
image fence = "backgrounds/BG - Fence.png"

#MS silhouette
image vin0:
    "backgrounds/silhouette.png"
    alpha 0.7

#silhouette round
image vin1:
    "backgrounds/silhouette.png"
    alpha 0.7

#silhouette box
image vin2:
    "backgrounds/silhouette2.png"
    alpha 0.28

#Music
define audio.theme = "<loop 22.073>music/NDRV3 OST - Gallery Music.mp3"  #Main theme (title)
define audio.main = "<loop 22.073>music/NDRV3 OST - SAKE NO TUKAMIDORI.mp3"  #Dialogue Music
define audio.static = "music/noise.ogg"

# SFX
# define sound.t1 = "sfx/1.ogg"  #Main theme (title)

# Voice Lines - Character
# define voice.t1 = "voice/1.ogg"  #Main theme (title)
