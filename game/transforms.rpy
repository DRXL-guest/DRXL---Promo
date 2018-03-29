#Taken from DDLC by Dan Salvato
#Transforms to place characters on the screen in proper positions based on whether there are 2, 3, or 4 characters in the scene.

transform tcommon(x=960, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
        #yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=960, z=0.80):
        xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform focus(x=960, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        #yanchor 0.527 ypos 0.5
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform sink(x=960, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=960, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform hopfocus(x=960, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

transform dip(x=960, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=960, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform leftin(x=960, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

#Used when hiding sprites with dissolve to mirror the show effect
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        #yanchor 0.510 ypos 0.5
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300


transform t41:
    tcommon(300)
transform t42:
    tcommon(740)
transform t43:
    tcommon(1179)
transform t44:
    tcommon(1620)
transform t31:
    tcommon(360)
transform t32:
    tcommon(1440)
transform t33:
    tcommon(1560)
transform t21:
    tcommon(600)
transform t22:
    tcommon(1320)
transform t11:
    tcommon(1440)

transform i41:
    tinstant(300)
transform i42:
    tinstant(740)
transform i43:
    tinstant(1179)
transform i44:
    tinstant(1620)
transform i31:
    tinstant(360)
transform i32:
    tinstant(1440)
transform i33:
    tinstant(1560)
transform i21:
    tinstant(600)
transform i22:
    tinstant(1320)
transform i11:
    tinstant(1440)

transform f41:
    focus(300)
transform f42:
    focus(740)
transform f43:
    focus(1179)
transform f44:
    focus(1620)
transform f31:
    focus(360)
transform f32:
    focus(1440)
transform f33:
    focus(1560)
transform f21:
    focus(600)
transform f22:
    focus(1320)
transform f11:
    focus(1440)

transform s41:
    sink(300)
transform s42:
    sink(740)
transform s43:
    sink(1179)
transform s44:
    sink(1620)
transform s31:
    sink(360)
transform s32:
    sink(1440)
transform s33:
    sink(1560)
transform s21:
    sink(600)
transform s22:
    sink(1320)
transform s11:
    sink(1440)

transform h41:
    hop(300)
transform h42:
    hop(740)
transform h43:
    hop(1179)
transform h44:
    hop(1620)
transform h31:
    hop(360)
transform h32:
    hop(1440)
transform h33:
    hop(1560)
transform h21:
    hop(600)
transform h22:
    hop(1320)
transform h11:
    hop(1440)

transform hf41:
    hopfocus(300)
transform hf42:
    hopfocus(740)
transform hf43:
    hopfocus(1179)
transform hf44:
    hopfocus(1620)
transform hf31:
    hopfocus(360)
transform hf32:
    hopfocus(1440)
transform hf33:
    hopfocus(1560)
transform hf21:
    hopfocus(600)
transform hf22:
    hopfocus(1320)
transform hf11:
    hopfocus(1440)

transform d41:
    dip(300)
transform d42:
    dip(740)
transform d43:
    dip(1179)
transform d44:
    dip(1620)
transform d31:
    dip(360)
transform d32:
    dip(1440)
transform d33:
    dip(1560)
transform d21:
    dip(600)
transform d22:
    dip(1320)
transform d11:
    dip(1440)

transform l41:
    leftin(300)
transform l42:
    leftin(740)
transform l43:
    leftin(1179)
transform l44:
    leftin(1620)
transform l31:
    leftin(360)
transform l32:
    leftin(1440)
transform l33:
    leftin(1560)
transform l21:
    leftin(600)
transform l22:
    leftin(1320)
transform l11:
    leftin(1440)
