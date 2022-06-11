# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#define config.main_menu_music = "audio/main-menu-theme.ogg"


####################################################################################################################################################
####################################################################################################################################################
                                                                #DEFAULTS AND DEFINES
####################################################################################################################################################
####################################################################################################################################################

default show_quick_menu = False
define voicevoid = Character("Voice", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vvoice",ctc="ctc_anchored",ctc_position="fixed")
define kristik = Character("Kristik", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vkristik",ctc="ctc_anchored",ctc_position="fixed")
define kristikmind = Character("Kristik's Mind", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#ff0000") ], voice_tag="Vkristik",ctc="ctc_anchored",ctc_position="fixed")
define bill = Character("Bill", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vbill",ctc="ctc_anchored",ctc_position="fixed")
define kyle = Character("Kyle", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vkyle",ctc="ctc_anchored",ctc_position="fixed")
define kevin = Character("Kevin", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vkevin",ctc="ctc_anchored",ctc_position="fixed")
define jason = Character("Jason", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vjason",ctc="ctc_anchored",ctc_position="fixed")
define aaron = Character("Aaron", color="#ffffff", who_outlines=[ (3, "#910000") ], what_outlines=[ (2, "#910000") ], voice_tag="Vaaron",ctc="ctc_anchored",ctc_position="fixed")
define wesley = Character("Wesley", color="#ffffff", who_outlines=[ (3, "#913800") ], what_outlines=[ (2, "#913800") ], voice_tag="Vwesley",ctc="ctc_anchored",ctc_position="fixed")
define suou = Character("Suou", color="#ffffff", who_outlines=[ (3, "#6f3680") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#6f3680", voice_tag="Vsuou",ctc="ctc_anchored",ctc_position="fixed")
define mayuri = Character("Mayuri", color="#ffffff", who_outlines=[ (3, "#0076a8") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#0076a8", voice_tag="Vmayuri",ctc="ctc_anchored",ctc_position="fixed")
define yuzuriha = Character("Yuzuriha", color="#ffffff", who_outlines=[ (3, "#8a8a8a") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#8a8a8a", voice_tag="Vyuzuriha",ctc="ctc_anchored",ctc_position="fixed")
define rikka = Character("Rikka", color="#ffffff", who_outlines=[ (3, "#434391") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#434391", voice_tag="Vrikka",ctc="ctc_anchored",ctc_position="fixed")
define nerine = Character("Nerine", color="#ffffff", who_outlines=[ (3, "#c4b482") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#c4b482", voice_tag="Vichigo",ctc="ctc_anchored",ctc_position="fixed")
define ichigo = Character("Ichigo", color="#ffffff", who_outlines=[ (3, "#c783c9") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#c783c9", voice_tag="Vringo",ctc="ctc_anchored",ctc_position="fixed")
define ringo = Character("Ringo", color="#ffffff", who_outlines=[ (3, "#c783c9") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#c783c9", voice_tag="Vringo",ctc="ctc_anchored",ctc_position="fixed")
define chidori = Character("Chidori", color="#ffffff", who_outlines=[ (3, "#215722") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#215722", voice_tag="Vchidori",ctc="ctc_anchored",ctc_position="fixed")
define erika = Character("Erika", color="#ffffff", who_outlines=[ (3, "#02ab97") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#02ab97", voice_tag="Verika",ctc="ctc_anchored",ctc_position="fixed")
define nurse = Character("Nurse", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vnurse",ctc="ctc_anchored",ctc_position="fixed")
define daboys = Character("The Boys", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vtheboys",ctc="ctc_anchored",ctc_position="fixed")
define intercom = Character("Intercom", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vintercom",ctc="ctc_anchored",ctc_position="fixed")
define unknown = Character("???", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vunknown",ctc="ctc_anchored",ctc_position="fixed")
define narrator = Character("", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vunknown",ctc="ctc_anchored",ctc_position="fixed")
define mom = Character("Mom", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vmom",ctc="ctc_anchored",ctc_position="fixed")
define xijingping = Character("Xi Jingping Bot 9000", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vxijing",ctc="ctc_anchored",ctc_position="fixed")
define natsuhi = Character("Natsuhi", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vnatsuhi",ctc="ctc_anchored",ctc_position="fixed")
define ange = Character("Ange", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vange",ctc="ctc_anchored",ctc_position="fixed")
define rudolf = Character("Rudolf", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vrudolf",ctc="ctc_anchored",ctc_position="fixed")
define toshiro = Character("Toshiro", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vtoshiro",ctc="ctc_anchored",ctc_position="fixed")
define c00 = Character("Chiester 00", color="#ffffff", who_outlines=[ (3, "#a18903") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#a18903", voice_tag="V00",ctc="ctc_anchored",ctc_position="fixed")
define c410 = Character("Chiester 410", color="#ffffff", who_outlines=[ (3, "#2105a1") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#2105a1", voice_tag="V410",ctc="ctc_anchored",ctc_position="fixed")
define c45 = Character("Chiester 45", color="#ffffff", who_outlines=[ (3, "#ec03fc") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#ec03fc", voice_tag="V45",ctc="ctc_anchored",ctc_position="fixed")
define c556 = Character("Chiester 556", color="#ffffff", who_outlines=[ (3, "#40ad8b") ], what_outlines=[ (2, "#FFFFFF") ], what_color="#40ad8b", voice_tag="V556",ctc="ctc_anchored",ctc_position="fixed")
define everyone = Character("Everyone", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Veveryone",ctc="ctc_anchored",ctc_position="fixed")
define kaori = Character("Kaori", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vkaori",ctc="ctc_anchored",ctc_position="fixed")
define beatrice = Character("Beatrice", color="#ffffff", who_outlines=[ (3, "#a34d02") ], what_outlines=[ (2, "#a34d02") ], voice_tag="Vbeatrice",ctc="ctc_anchored",ctc_position="fixed")
define haruhi = Character("Haruhi", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vharuhi",ctc="ctc_anchored",ctc_position="fixed")
define judge = Character("Judge", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vjudge",ctc="ctc_anchored",ctc_position="fixed")
define assistant = Character("D.A. Assistant", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vassistant",ctc="ctc_anchored",ctc_position="fixed")
define mikuru = Character("Mikuru", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vmikuru",ctc="ctc_anchored",ctc_position="fixed")
define citizen = Character("Random Ass Citizen", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vcitizen",ctc="ctc_anchored",ctc_position="fixed")
define simyo = Character("Shim Young", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vsimyo",ctc="ctc_anchored",ctc_position="fixed")
define doctor = Character("Doctor", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vdoctor",ctc="ctc_anchored",ctc_position="fixed")
define scav = Character("Scav", color="#ffffff", who_outlines=[ (3, "#000000") ], what_outlines=[ (2, "#000000") ], voice_tag="Vscav",ctc="ctc_anchored",ctc_position="fixed")

style text_timer_ok:
    xpos 550
    size 122
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style text_timer_near:
    xpos 550
    size 122
    color "#F22"
    outlines [(2, "#000", 0, 0)]

style text_timer_ok2:
    xpos 550
    size 122
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style text_timer_near2:
    xpos 550
    size 122
    color "#F22"
    outlines [(2, "#000", 0, 0)]    

screen text_timer( **kwargs ):
    # @param: kwargs
    #
    # duration = 10.0, 
    # success_label = 'success_label',
    # fail_label = 'fail_label', 
    # screen = 'text_timer',
    # ok_style = 'text_timer_ok',
    # near_style = 'text_timer_near',
    # style_swap = 5.0,
    # text_format = "{minutes:02d}:{seconds:02d}:{micro_seconds[0]}"
    vbox:
        add DynamicDisplayable(text_countdown, **kwargs)
        #
        #
        # This would likely be in a different screen
        # Remember to alter the kwargs and move success_label there though
        # Yes
        #

        textbutton "Shoot here!":
            hover_sound "audio/gunload_Master.wav"
            xpos 600
            ypos 170
            text_style "shoot_button_text"
            action [ Function(renpy.hide_screen, 'text_timer'), Call(kwargs.get('success_label', 'success_label')) ]

screen text_timer2( **kwargs ):
    # @param: kwargs
    #
    # duration = 10.0, 
    # success_label = 'success_label',
    # fail_label = 'fail_label', 
    # screen = 'text_timer',
    # ok_style = 'text_timer_ok',
    # near_style = 'text_timer_near',
    # style_swap = 5.0,
    # text_format = "{minutes:02d}:{seconds:02d}:{micro_seconds[0]}"
    vbox:
        add DynamicDisplayable(text_countdown2, **kwargs)
        #
        #
        # This would likely be in a different screen
        # Remember to alter the kwargs and move success_label there though
        # Yes
        #

        textbutton "Shoot here!":
            hover_sound "audio/gunload_Master.wav"
            xpos 600
            ypos 170
            text_style "shoot_button_text"
            action [ Function(renpy.hide_screen, 'text_timer2'), Call(kwargs.get('success_label2', 'success_label2')) ]

screen text_timermath( **kwargs ):
    add DynamicDisplayable(text_countdownmath, **kwargs)    

####################################################################################################################################################
####################################################################################################################################################
                                                                #IMAGE DEFINITIONS
####################################################################################################################################################
####################################################################################################################################################

image teast1 = Movie(channel="movie_dp", play="movies/tarkoveast1.mpg")
image teast2 = Movie(channel="movie_dp", play="movies/tarkoveast2.mpg")
image twest1 = Movie(channel="movie_dp", play="movies/tarkovwest1.mpg")
image twest2 = Movie(channel="movie_dp", play="movies/tarkovwest2.mpg")
image tarkovdeath = Movie(channel="movie_dp", play="movies/tarkovdeath.mpg")
image intro = Movie(channel="movie_dp", play="movies/intro.mpg")
image bg_intro = "title.png"

image white_base:
    "transitions/white_base.png"
    zoom 0.67

image objection:
    "matta.png"

image next_base:
    "transitions/next_base.png"
    zoom 0.67

image transition1:
    "transitions/transition1.png"
    zoom 0.67

image transition2:
    "transitions/transition2.png"
    zoom 0.67

image transition3:
    "transitions/transition3.png"
    zoom 0.67

image transition4:
    "transitions/transition4.png"
    zoom 0.67

image transition5:
    "transitions/transition5.png"
    zoom 0.67

image transition6:
    "transitions/transition6.png"
    zoom 0.67

image transition7:
    "transitions/transition7.png"
    zoom 0.67

image transition8:
    "transitions/transition8.png"
    zoom 0.67


image hospital_bed:
    "backgrounds/hosp_room2.jpg"
    zoom 1.3
image hospital_room:
    "backgrounds/hosp_room.jpg"
    zoom 1.3
image parking_lot:
    "backgrounds/school_parkinglot.jpg"
    zoom 1.3
image road_one:
    "backgrounds/school_road.jpg"
    zoom 1.3
image airport:
    "backgrounds/airport.png"
image city_street2:
    "backgrounds/city_street2.jpg"
    zoom 1.3
image city_alley:
    "backgrounds/city_alley.jpg"
    zoom 1.3
image city_station:
    "backgrounds/city_station.jpg"
    zoom 1.3
image hok_road:
    "backgrounds/hok_road.jpg"
    zoom 1.3

image BG039n:
    "backgrounds/BG039n.png"

image BG080N:
    "backgrounds/BG080N.png"

image BG046Y:
    "backgrounds/BG046Y.png"

image nicehouse:
    "backgrounds/nicehouse.jpg"
    zoom 0.67

image BG008Y:
    "backgrounds/BG008Y.png"

image BG018Y:
    "backgrounds/BG018Y.png"

image BG033y:
    "backgrounds/BG033y.png"

image ctc_anchored:
    zoom 0.07
    "GUI/arrow.png"
    yalign 0.96
    xpos 950
    linear 1.00 alpha 1.0
    linear 1.00 alpha 0.0
    repeat 

image BG080:
    "backgrounds/BG080.png"

image BG043:
    "backgrounds/BG043.png"

image hentai:
    "backgrounds/hentai.jpg"
    zoom 0.67

image BG080B:
    "backgrounds/BG080B.png"

image BG048:
    "backgrounds/BG048.png"

image dungeon:
    "backgrounds/dungeon.jpg"
    zoom 0.67

image niceroom:
    "backgrounds/niceroom.jpg"
    zoom 0.67

image niceroom2:
    "backgrounds/niceroom2.jpg"
    zoom 0.67
    
image niceroom3:
    "backgrounds/niceroom3.jpg"
    zoom 0.67

image day1:
    "backgrounds/day1.png"
    zoom 0.67

image day2:
    "backgrounds/day2.png"
    zoom 0.67

image day3:
    "backgrounds/day3.png"
    zoom 0.67

image BG005:
    "backgrounds/BG005.png"

image BG017n1:
    "backgrounds/BG017n1.png"

image BG003c:
    "backgrounds/BG003c.png"

image girl:
    "backgrounds/girl.png"
    zoom 0.67

image BG049:
    "backgrounds/BG049.png"

image helicopter:
    "backgrounds/helicopter.jpg"
    zoom 0.67

image math:
    "backgrounds/math.png"
    zoom 0.67

image cockpit:
    "backgrounds/cockpit.jpg"
    zoom 0.67    

image BG033:
    "backgrounds/BG033.png"

image tarkovstill1:
    "backgrounds/tarkovstill1.png"
    zoom 0.67

image tarkovstill2:
    "backgrounds/tarkovstill2.png"
    zoom 0.67

image hideout:
    "backgrounds/hideout.jpg"
    zoom 0.67

image tarkovlbel:
    "backgrounds/tarkovlbel.png"
    zoom 0.625

image BG038:
    "backgrounds/BG038.png"

image customs1:
    "backgrounds/customs1.jpg"
    zoom 0.625

image customs2:
    "backgrounds/customs2.jpg"
    zoom 0.625

image customs3:
    "backgrounds/customs3.jpg"
    zoom 0.625

image simyoung1:
    "backgrounds/simyoung1.png"
    zoom 0.67

image simyoung2:
    "backgrounds/simyoung2.png"
    zoom 0.67

image simyoung3:
    "backgrounds/simyoung3.png"
    zoom 0.67

image simyoung4:
    "backgrounds/simyoung4.png"
    zoom 0.67

image simyoung5:
    "backgrounds/simyoung5.png"
    zoom 0.67

image simyoung6:
    "backgrounds/simyoung6.png"
    zoom 0.67

image simyoung7:
    "backgrounds/simyoung7.png"
    zoom 0.67

image simyoung8:
    "backgrounds/simyoung8.png"
    zoom 0.67

image simyoung9:
    "backgrounds/simyoung9.png"
    zoom 0.67

image simyoung9point1:
    "backgrounds/simyoung9point1.png"
    zoom 0.67

image simyoung10:
    "backgrounds/simyoung10.png"
    zoom 0.67

image simyoung11:
    "backgrounds/simyoung11.png"
    zoom 0.67

image simyoung12:
    "backgrounds/simyoung12.png"
    zoom 0.67

image simyoung13:
    "backgrounds/simyoung13.png"
    zoom 0.67

image simyoung14:
    "backgrounds/simyoung14.png"
    zoom 0.67

image simyoung15:
    "backgrounds/simyoung15.png"
    zoom 0.67

image simyoung16:
    "backgrounds/simyoung16.png"
    zoom 0.67

image simyoung17:
    "backgrounds/simyoung17.png"
    zoom 0.67

image kor1:
    "backgrounds/kor1.png"
    zoom 0.67

image kor2:
    "backgrounds/kor2.png"
    zoom 0.67

image kor3:
    "backgrounds/kor3.png"
    zoom 0.67

image kor4:
    "backgrounds/kor4.png"
    zoom 0.67

image kor5:
    "backgrounds/kor5.png"
    zoom 0.67

image kor6:
    "backgrounds/kor6.png"
    zoom 0.67

image kor7:
    "backgrounds/kor7.png"
    zoom 0.67

image kor8:
    "backgrounds/kor8.png"
    zoom 0.67

image kor9:
    "backgrounds/kor9.png"
    zoom 0.67

image kor10:
    "backgrounds/kor10.png"
    zoom 0.67

image kor11:
    "backgrounds/kor11.png"
    zoom 0.67

image hanok:
    "backgrounds/hanok.jpg"

image kor12:
    "backgrounds/kor12.png"
    zoom 0.67

image kor13:
    "backgrounds/kor13.png"
    zoom 0.67

image kor14:
    "backgrounds/kor14.png"
    zoom 0.67

image court1:
    "backgrounds/court1.png"
    ypos 900

image court2:
    "backgrounds/court2.png"
    ypos 700

image court3:
    "backgrounds/court3.png"
    ypos 700

image court4:
    "backgrounds/court4.png"
    ypos 700

image BG025:
    "backgrounds/BG025.png"

image BG025n:
    "backgrounds/BG025n.png"

image prison:
    "backgrounds/prison.png"

image jail:
    "backgrounds/jail.png"

image BG007:    
    "backgrounds/BG007.png"

image BG043:
    "backgrounds/BG043.png"

image BG012:
    "backgrounds/BG012.png"

image BG080Y:
    "backgrounds/BG080Y.png"

image BG027_o:
    "backgrounds/BG027_o.png"

image BG028c:
    "backgrounds/BG028c.png"

image BG036:
    "backgrounds/BG036.png"

image stockx:
    "backgrounds/stockx.png"

image nike:
    "backgrounds/nike.jpg"

image BG039:
    "backgrounds/BG039.png"

image BG011N:
    "backgrounds/BG011N.png"

image suburb_roadcenter:
    "backgrounds/suburb_roadcenter.jpg"
    zoom 1.3

image shizu_houseext:
    "backgrounds/shizu_houseext.jpg"
    zoom 1.3

image city_street3:
    "backgrounds/city_street3.jpg"
    zoom 1.3

image suburb_konbiniext:
    "backgrounds/suburb_konbiniext.jpg"
    zoom 1.3

image city_street3_ni:
    "backgrounds/city_street3_ni.jpg"
    zoom 1.3

image LA_Penthouse_Bedroom:
    "backgrounds/LA_Penthouse_Bedroom.jpg"
    zoom 0.7

image shizu_houseext_ni:
    "backgrounds/shizu_houseext_ni.jpg"
    zoom 1.3

image city_street4:
    "backgrounds/city_street4.jpg"
    zoom 1.3

image suburb_shanghaiint:
    "backgrounds/suburb_shanghaiint.jpg"
    zoom 1.3

image suburb_park:
    "backgrounds/suburb_park.jpg"
    zoom 1.3

image lilly_hilltop:
    "backgrounds/lilly_hilltop.jpg"
    zoom 1.3

image shizu_fishing:
    "backgrounds/shizu_fishing.jpg"
    zoom 1.3

image shizu_park:
    "backgrounds/shizu_park.jpg"
    zoom 1.3

image school_forest1:
    "backgrounds/school_forest1.jpg"
    zoom 1.3

image city_clubint:
    "backgrounds/city_clubint.jpg"
    zoom 1.3

image city_street4_ni:
    "backgrounds/city_street4_ni.jpg"
    zoom 1.3

image school_dormhisao_ni:
    "backgrounds/school_dormhisao_ni.jpg"
    zoom 1.3

image school_dormhisao_ss:
    "backgrounds/school_dormhisao_ss.jpg"
    zoom 1.3

image school_gardens:
    "backgrounds/school_gardens.jpg"
    zoom 1.3

image BG010:
    "backgrounds/BG010.png"

image BG001:
    "backgrounds/BG001.png"

image BG030n1:
    "backgrounds/BG030n1.png"

image BG124:
    "backgrounds/BG124.png"

image BG011:
    "backgrounds/BG011.png"

image BG021:
    "backgrounds/BG021.png"

image BG022:
    "backgrounds/BG022.png"

image BG004Y:
    "backgrounds/BG004Y.png"

image BG003Y:
    "backgrounds/BG003Y.png"

image school_dormhallground:
    "backgrounds/school_dormhallground.jpg"
    zoom 1.3

image school_girlsdormhall:
    "backgrounds/school_girlsdormhall.jpg"
    zoom 1.3

image BG022N1:
    "backgrounds/BG022N1.png"

image BG023N1_o:
    "backgrounds/BG023N1_o.png"

image BG042:
    "backgrounds/BG042.png"
####################################################################################################################################################
####################################################################################################################################################
                                                                #PYHTON INITIALIZATION
####################################################################################################################################################
####################################################################################################################################################

init python:

    def text_countdown( st, at, 
                            duration = 1.0, 
                            fail_label = 'fail_label', 
                            screen = 'text_timer',
                            ok_style = 'text_timer_ok',
                            near_style = 'text_timer_near',
                            style_swap = 5.0,
                            text_format = "{seconds:02d}:{micro_seconds[0]}" ):
            
            remaining = duration - st

            parts_dict = {
                'minutes' : int( remaining // 60 ),
                'seconds' : int( remaining % 60 ),
                'micro_seconds' : str(int( (remaining % 1) * 10000 )), # we use str() so we can define precision
            }

            if remaining <= 0.0:
                renpy.hide_screen(screen)
                renpy.call(fail_label)
            
            return Text( text_format.format(**parts_dict), 
                        style = ok_style if remaining > style_swap else near_style), .1

    def text_countdown2( st, at, 
                            duration = 1.0, 
                            fail_label2 = 'fail_label2', 
                            screen = 'text_timer2',
                            ok_style = 'text_timer_ok2',
                            near_style = 'text_timer_near2',
                            style_swap = 5.0,
                            text_format = "{seconds:02d}:{micro_seconds[0]}" ):
            
            remaining = duration - st

            parts_dict = {
                'minutes' : int( remaining // 60 ),
                'seconds' : int( remaining % 60 ),
                'micro_seconds' : str(int( (remaining % 1) * 10000 )), # we use str() so we can define precision
            }

            if remaining <= 0.0:
                renpy.hide_screen(screen)
                renpy.jump(fail_label2)
            
            return Text( text_format.format(**parts_dict), 
                        style = ok_style if remaining > style_swap else near_style), .1

    def text_countdownmath( st, at, 
                            duration = 120.0, 
                            fail_math = 'fail_math', 
                            screen = 'text_timermath',
                            ok_style = 'text_timer_ok2',
                            near_style = 'text_timer_near2',
                            style_swap = 5.0,
                            text_format = "{minutes:01d}:{seconds:02d}:{micro_seconds[0]}" ):
            
            remaining = duration - st

            parts_dict = {
                'minutes' : int( remaining // 60 ),
                'seconds' : int( remaining % 60 ),
                'micro_seconds' : str(int( (remaining % 1) * 10000 )), # we use str() so we can define precision
            }

            if remaining <= 0.01:
                renpy.hide_screen(screen)
                renpy.call(fail_math)

            return Text( text_format.format(**parts_dict), 
                        style = ok_style if remaining > style_swap else near_style), .1                        
    
    
    config.developer = False
    config.auto_voice = "voice/{id}.wav"

    warDeathEnding = 0

    persistent.endingFinished1 = 0
    persistent.endingFinished2 = 0
    persistent.endingFinished3 = 0
    persistent.endingFinished4 = 0
    persistent.endingFinished5 = 0
    persistent.endingFinished6 = 0
    persistent.endingFinished7 = 0
    persistent.endingFinished8 = 0
    persistent.endingFinished9 = 0
    persistent.endingFinished10 = 0
    persistent.endingFinished11 = 0
    persistent.endingFinished12 = 0
    persistent.endingFinished13 = 0
    persistent.endingFinished14 = 0
    persistent.endingFinished15 = 0
    persistent.endingFinished16 = 0
    persistent.endingFinished17 = 0
    persistent.endingFinished18 = 0
    persistent.endingFinished19 = 0
    persistent.endingFinished20 = 0
    persistent.endingFinished21 = 0

    EXPsuou = 0
    EXPmayuri = 0
    EXPyuzuriha = 0
    EXPrikka = 0
    EXPnerine = 0
    EXPringo = 0
    EXPchidori = 0
    EXPerika = 0
    EXPichigo = 0
    EXPc00 = 0
    EXPc410 = 0
    EXPc45 = 0
    EXPc556 = 0
    EXPbeatrice = 0
    EXPaaronwesley = 0

    #======================================================================================================
    # TODO: REMOVE COMMENT BELOW FOR REGULAR RELEASE
    #======================================================================================================

    config.rollback_enabled = False


    #=================================================================================================================================
    # ARCHIVAL OPTIONS
    #=================================================================================================================================

    build.classify("game/**.png", "archive")
    build.classify("game/**.jpg", "archive")
    build.classify("game/**.wav", "archive")
    build.classify("game/**.ttf", "archive")
    build.classify("game/**.ogg", "archive")
    build.classify("game/**.rpym", "archive")
    build.classify("game/**.rpymc", "archive")
    build.classify("game/**.mpg", "archive")
    build.classify("game/**.flp", "archive")
    build.classify("game/**.rpyb", "archive")
    build.classify("game/**.txt", "archive")
    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.mp3", "archive")
    build.classify("game/**.md", "archive")
    build.classify("game/**.enigma64", "archive")
    build.classify("game/**.xmp", "archive")
    build.classify("game/**.idx2", "archive")
    build.classify("game/**.ico", "archive")
    build.classify("game/**.webp", "archive")

    config.layers = [ 'master', 'master1', 'master2', 'master3', 'master4', 'misc', 'misc2', 'misc3', 'misc4', 'transient', 'screens', 'overlay', 'mcsprite' ]
###################################################################################################################################################
###################################################################################################################################################
                                                                #DEBUG ITEMS
###################################################################################################################################################
###################################################################################################################################################


screen Beta:
    text "BETA v0.2.2.0b! DO NOT REDISTRIBUTE!" xpos -1 ypos 0.00 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]


# screen Stats:
#     text "!!! DEBUGGING ENVIRONMENT CURRENTLY ACTIVE !!!" xpos 0.25 ypos 0.036  color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "!!! DO NOT USE FOR FINAL RELEASE BUILD !!!" xpos 0.285 ypos 0.070  color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

#     text "CURRENT STATS:" xpos 0.85 ypos 0.076 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Suou EXP: [EXPsuou]" xpos 0.87 ypos 0.106 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Mayuri EXP: [EXPmayuri]" xpos 0.87 ypos 0.138 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Yuzuriha EXP: [EXPyuzuriha]" xpos 0.87 ypos 0.168 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Rikka EXP: [EXPrikka]" xpos 0.87 ypos 0.198 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Nerine EXP: [EXPnerine]" xpos 0.87 ypos 0.228 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Ringo EXP: [EXPringo]" xpos 0.87 ypos 0.258 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Chidori EXP: [EXPchidori]" xpos 0.87 ypos 0.288 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Erika EXP: [EXPerika]" xpos 0.87 ypos 0.318 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Ichigo EXP: [EXPichigo]" xpos 0.87 ypos 0.348 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Beatrice EXP: [EXPbeatrice]" xpos 0.87 ypos 0.378 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

#     text "REQUIRED STATS:" xpos 0.02 ypos 0.076 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Suou EXP: 9" xpos 0.02 ypos 0.106 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Mayuri EXP: 9" xpos 0.02 ypos 0.138 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Yuzuriha EXP: 9" xpos 0.02 ypos 0.168 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Rikka EXP: 10" xpos 0.02 ypos 0.198 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Nerine EXP: 10" xpos 0.02 ypos 0.228 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Ringo EXP: 8" xpos 0.02 ypos 0.258 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Chidori EXP: 12" xpos 0.02 ypos 0.288 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Erika EXP: 14" xpos 0.02 ypos 0.318 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Ichigo EXP: 9" xpos 0.02 ypos 0.348 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
#     text "Aaron/Wesley EXP: N/A" xpos 0.02 ypos 0.378 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

#     text "SYSTEM INFORMATION: NVIDIA GeForce RTX 3080, 16GB DDR5X 5200MHz, i7-12700F 12 CORES 20 THREADS @ 4.2 GHz" xpos 0.02 ypos 0.00 color "#ff1100" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]



####################################################################################################################################################
####################################################################################################################################################
                                                                #GAME SPLASH AND ACTUAL GAME
####################################################################################################################################################
####################################################################################################################################################

label main_menu:
    $_dismiss_pause = False
    screen disable_Lmouse():
        key "mouseup_1" action NullAction()
        key "K_RETURN" action NullAction()
        key "K_SPACE" action NullAction()
        key "K_KP_ENTER" action NullAction()
        key "K_SELECT" action NullAction()
    image splash = "gui/splash.png"
    image warning = "gui/warning.png"
    image beta = "gui/beta.png"
    with None
    $ renpy.transition(dissolve)
    show splash
    $ renpy.pause(2, hard=True)
    $ renpy.transition(dissolve) 
    hide splash
    $ renpy.transition(dissolve)
    $ renpy.pause(2, hard=True)
    show warning
    $ renpy.transition(dissolve)
    $ renpy.pause(6)
    hide warning
    $ renpy.transition(dissolve)
    $ renpy.pause(2, hard=True)
    show beta
    $ renpy.transition(dissolve)
    $ renpy.pause(4, hard=True)
    hide beta
    $ renpy.transition(dissolve)
    $ renpy.pause(2, hard=True)
    play music "audio/main-menu-theme.ogg"
    show intro
    $ renpy.pause(1.45, hard=True)
    show bg_intro
    $ renpy.pause(0.20, hard=True)
    $ renpy.transition(dissolve)
    jump main_menu_screen
# The game starts here.

label start:


    #======================================================================================================
    ## TODO: REMOVE BELOW FOR RELEASE VERSION
    #======================================================================================================
    #show screen Stats

    #======================================================================================================
    ## TODO: REMOVE BELOW FOR RELEASE VERSION
    #======================================================================================================
    show screen Beta


    $ renpy.transition(dissolve)
    $ renpy.pause(5, hard=True)
    scene blackvoid
    $ renpy.transition(dissolve)
    $ show_quick_menu = True
    $ renpy.pause(2, hard=True)
    if (persistent.endingFinished1 == 1 and endingFinished2 == 1 and endingFinished3 == 1 and endingFinished4 == 1 and endingFinished5 == 1 and endingFinished6 == 1 and endingFinished7 == 1 and endingFinished8 == 1 and endingFinished9 == 1 and endingFinished10 == 1 and endingFinished11 == 1 and endingFinished12 == 1 and endingFinished13 == 1 and endingFinished14 == 1 and endingFinished15 == 1 and endingFinished16 == 1 and endingFinished17 == 1 and endingFinished18 == 1 and endingFinished19 == 1 and endingFinished20 == 1 and endingFinished21 == 1):
        jump secretEnding
    else:
        pass
    #======================================================================================================
    ## TODO: WHEN DIALOGUE IS COMPLETE RE-HASH AND RENAME VOICE LINE FILES
    #======================================================================================================

    voicevoid "Kristik..."

    voicevoid "We need you."

    voicevoid "Your presence is required."

    voicevoid "We will be transporting you back home."

    voicevoid "You'll know the mission."

    voicevoid "Good luck."
    $ renpy.transition(dissolve)
    $ show_quick_menu = False
    jump storypartone


label storypartone:
    scene blackvoid
    $ renpy.pause(2.00, hard=True)  
    $ renpy.transition(dissolve)    
    $ show_quick_menu = True       
    kristik "Ughhh...."
    kristikmind "{i}What happened?"
    kristikmind "{i}My body aches...."
    kristikmind "{i}I felt like a lot of time passed, but nothing feels different."    
    $ renpy.pause(1.00, hard=True)    
    $ renpy.transition(dissolve)    
    show hospital_bed   
    $ renpy.pause(1.00, hard=True)     
    play sound "audio/heartbeat_single_Master.wav" loop
    play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
    kristik "The hell?...."
    kristikmind "{i}Why am I in a hospital?"
    nurse "You're finally awake. Your vitals seem to be fine, but your heartrate is a little high on average."
    kristikmind "{i}WTF????"
    kristikmind "{i}WHO IS THIS???"     
    kristikmind "{i}WHY AM I IN A HOSPITAL???"
    kristik "Uhhh...."
    kristik "No hablo Japonesa... eh.... si."
    nurse "?"
    kristik "Annyeong ha se yo?"
    nurse "????"
    kristik "Watashi wa... No Nihongo.. desu?"
    nurse "!" 
    nurse "I see."
    nurse "I'll call a male doctor in then."

    #=======================================
    #show schi0101
    #with dissolve
    #======================================

    kristikmind "{i}Let's fuckin GOOOO my coochie grabbin skillz came in clutch right there"
    hide hospital_bed
    $ renpy.transition(dissolve)    
    show hospital_room
    stop sound
    show kevin (15):
        xpos 400
        zoom 0.6
    with dissolve
    stop music fadeout 2.0
    kristik "..."
    kristik "Ain't no fuckin way bro..."
    hide kevin (15)
    show kevin (16):
        xpos 400
        zoom 0.6   
    kevin "Kristik...?"
    kristik "THE FUCK YOU DOIN HERE??"
    hide kevin (15)
    show kevin (29):
        xpos 400
        zoom 0.6   
    play music "audio/Sanoba Witch OST Real Friend InstVer 128k.ogg"
    kevin "BRUH WTF U MEAN WHAT ARE YOU DOIN HERE??"
    kristik "BRO SINCE WHEN WERE YOU GON BE A DOCTOR?"
    kevin "BITCH I BE A DOCTOR SINCE HO CHI MINH WENT TO CHINA"
    hide kevin (29)
    show kevin (21):
        xpos 400
        zoom 0.6      
    kevin "I thought I got rid of you..."
    kristik "What??"
    kristikmind "{i} Tf he mean got rid of me? Tryna kill me or some shit?"
    hide kevin (21)
    show kevin (34):
        xpos 400
        zoom 0.6          
    kevin "CAUSE YOU WAS NUTTING WHEN I CAME IN YOUR ROOM REMEMBER? SHIT WAS BACK IN KRISTIK SAGA 2!!"
    kristik "Bruh WHY THE FUCK YOU STILL THINKING ABOUT THAT? IT WAS LITERALLY ONLY A COUPLE OF MONTHS AGO"
    hide kevin (34)
    show kevin (29):
        xpos 400
        zoom 0.6          
    kevin "COUPLE MONTHS?? THE FUCK YOU ON??? ITS NEARLY BEEN 10 YEARS!!"
    kristikmind "{i}Tf is this mf talking about 10 years?? It was literally only couple months ago."
    kristik "Bruh u da one on some lean or some shit cause you dont even know what day it is"
    hide kevin (29)
    show kevin (28):
        xpos 400
        zoom 0.6   
    kevin "u callin me stupid or some shit?"
    kevin "BITCH look at the calendar"
    hide kevin (28)
    with dissolve
    $ renpy.pause(2.00, hard=True)     
    kristik "Bruh aint no way you trolling me"
    kristik "Aint no fuckin way its 2050"
    show kevin (29):
        xpos 400
        zoom 0.6
    with dissolve
    kevin "Tf do you want me to tell you then? Its 10 years thats straight facts. Your logic be straight buns bruh"
    kevin "We aint even talking about good buns we talking about rye bread or some shit."
    kristik "bruh get this food analogy outta here it aint working"
    hide kevin (29)
    show kevin (24):
        xpos 400
        zoom 0.6    
    kevin "Yeh prolly cause you real fat lmaooo"
    hide kevin (24)
    show kevin (17):
        xpos 400
        zoom 0.6        
    kevin "You was prolly salivating at the thought of sum bread fatty"
    hide kevin (17)
    show kevin (31):
        xpos 400
        zoom 0.6     
    kristik "Shut the fuck up BITCH just get me outta this hospital im done with your twitter girl drama"
    kristik "The fuck was I even in here for???"
    hide kevin (31)
    show kevin (35):
        xpos 400
        zoom 0.6      
    kevin "You for some reason fell into a coma outside your house."
    hide kevin (35)
    show kevin (21):
        xpos 400
        zoom 0.6   
    kevin "Yo mama called the paramedics and we thought you was dead"
    hide kevin (21)
    show kevin (27):
        xpos 400
        zoom 0.6      
    kevin "but i guess you alive then..."
    kristikmind "{i} why this mf sound disappointed that im alive bruh"
    kristikmind "{i} im abouta clothsline this dude if one more piece of shit comes out this dudes mouth"
    hide kevin (27)
    show kevin (21):
        xpos 400
        zoom 0.6    
    kevin "anyways i gotta file a report that you alive"
    hide kevin (21)
    show kevin (23):
        xpos 400
        zoom 0.6       
    kevin "i never thought i would have to fill that paper out with your name on it..."
    kristik "Bro im literally this close to turning your face into a tunnel with the amount of wack ass shit you saying"
    hide kevin (23)
    show kevin (28):
        xpos 400
        zoom 0.6    
    kevin "GO AHEAD PUSSY"
    hide kevin (28)
    show kevin (29):
        xpos 400
        zoom 0.6
    kevin "YOUR PUNCHES PROLLY FEEL LIKE STYROFOAM ANAL BEADS AT MOST"    
    kristik "OH REALLY NOW??"
    kevin "YEH PUSSY TRY ME"
    hide kevin (29)
    show kevin (31):
        xpos 400
        zoom 0.6  
    jason "Alright ya'll you better calm down."
    hide kevin(31)
    with dissolve 
    hide hospital_room
    $ renpy.transition(dissolve)    
    show hospital_bed
    $ renpy.pause(1.45, hard=True)
    show jason (90):
        xpos 400
        ypos 20
        zoom 0.6
    with dissolve
    jason "Or both of ya'll about to get this work yknowwhatimsayin"
    $ renpy.pause(1.25, hard=True)
    kristik "Pfff... Kekekekekekek..."
    hide jason (90)
    show jason (83):
        xpos 400
        ypos 20
        zoom 0.6
    jason "tf is so funny BITCH?"
    kristik "BAHAAHAHAHAAHAHAHEHEAHEAHWEAEHAWHEAWEAWEAWEHAWEHAWEHAWEH!!!!!"
    kristik "JAJAAJAJAJAJAJAJAJAJ XDXDXDXDXD"
    hide jason (83)
    show jason (82):
        xpos 400
        ypos 20
        zoom 0.6    
    kristik "XAXAXAXAXAXAXAXAXAA"
    kristik "LOLOLOLOLOLOLOLOLOLOLOL"
    hide jason (82)
    show jason (7):
        xpos 400
        ypos 20
        zoom 0.6 
    $ renpy.music.set_pause(True, channel="music")
    jason "SHUT THE FUCK UP FATASS BITCH BEANBAG LOOKIN ASS BITCH MANTITTIES BIGGER THAN AMY SCHUMER LOOKIN ASS SHUT YO BITCH ASS UP BEFORE I TURN THAT STOMACH INSIDE OUT INTO A DIMENSIONAL PORTAL"
    kristik "...."
    $ renpy.music.set_pause(False, channel="music")
    hide jason (7)
    show jason (88):
        xpos 400
        ypos 20
        zoom 0.6
    jason "*ahem*"
    hide jason (88)
    show jason (69):
        xpos 400
        ypos 20
        zoom 0.6    
    jason "Anyways... you had been called here... right?"
    kristik "Tf does that mean?"
    hide jason (69)
    show jason (7):
        xpos 400
        ypos 20
        zoom 0.6    
    $ renpy.music.set_pause(True, channel="music")
    jason "IT MEANS EXACTLY WHAT I SAID BITCH NOW ANSWER MY QUESTION"
    hide jason (7)
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6   
    kristik "uhhh.. i guess?"
    kristik "you don gotta be some damn rude though holy shit"
    hide jason (9)
    show jason (88):
        xpos 400
        ypos 20
        zoom 0.6
    $ renpy.music.set_pause(False, channel="music")
    jason "yeah yeah whatever shut yo bitch ass up and listen to me" 
    kristik "..."
    hide jason (88)
    show jason (67):
        xpos 400
        ypos 20
        zoom 0.6  
    jason "Remember those two dudes? Aaron and Wesley?"
    kristik "yeah what about em?"
    hide jason (67)
    show jason (75):
        xpos 400
        ypos 20
        zoom 0.6    
    jason "yeah... them dumbass BITCHs stole our shit!!!!"
    kristik "WHAT??? MY TEKKEN WAIFU COLLECTION TOO??!?!??!"
    hide jason (75)
    show jason (7):
        xpos 400
        ypos 20
        zoom 0.6   
    jason "FUCK NO AINT NOBODY GIVE A SHIT ABOUT THAT YOUR TEKKEN WAIFUS BE WORTH LITERAL BUNS"
    hide jason(75)
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (20):
        xpos 0
        zoom 0.6
    with dissolve
    kevin "heheh... buns... fatty again..."
    kristik "shut the fuck up kevin aint nobody asked you to talk with that granpda ass lookin hair why don you turn your head into a mushroom and apply to be in BTS"
    hide kevin (20)
    show kevin (27):
        xpos 0
        zoom 0.6    
    kevin "not that funny but ok..."
    hide kevin(27)
    hide jason (9)
    show jason (10):
        xpos 400
        ypos 20
        zoom 0.6
    with dissolve    
    jason "aight thats enough anyways to get to the point"
    jason "we made a deal with the demon realm to pass through it"
    hide jason (10)
    show jason (8):
        xpos 400
        ypos 20
        zoom 0.6    
    jason "only problem is that we need you in order to actually get through it"
    hide jason (8)
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6    
    kristik "hold up..."
    kristik "you askin me, a person who built a whole ass terrorist task force, who hijacked a plane and crashed it into a government establishment, who literally came back from the dead and killed your friends..."
    kristik "to help you go through my home land??"
    hide jason (9)
    show jason (88):
        xpos 400
        ypos 20
        zoom 0.6   
    jason "yes... i know... but this is much more of a serious situation"
    kristik "how tf is me killing your friends not as serious??"
    hide jason (88)
    show jason (82):
        xpos 400
        ypos 20
        zoom 0.6   
    jason "stfu... just keep quiet and lets get going"
    kristik "wait... what the fuck we leaving now???" 
    hide jason (82)
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6  
    with dissolve
    $ renpy.pause(1.25, hard=True)  
    jason "you really starting to piss me off BITCH"
    jason "stop asking questions or do i have to pull out your miranda rights?"   
    kristik "..."
    kristikmind "{i}jesus bro these guys are toxic asf...."
    hide jason (11)
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    with dissolve    
    kevin "Where's bill?"
    hide jason (9)
    show jason (82):
        xpos 400
        ypos 20
        zoom 0.6    
    jason "he prolly out with his hoes again..."
    hide jason(82)
    show jason (80):
        xpos 401
        ypos 20
        zoom 0.6   
    with dissolve
    jason "i can get no hoes bro (cry)"
    hide kevin (16)
    show kevin (27):
        xpos 0
        zoom 0.6
    kevin "bruh this dude...."
    bill "You guys we're talking about me?"
    hide hospital_bed
    $ renpy.transition(dissolve)    
    show hospital_room
    hide kevin(16)
    hide jason (80)
    show bill (1):      
        xpos 400
        zoom 0.6
    $ renpy.pause(1.00, hard=True)
    bill "Why are you guys in that fatass BITCH's hospital roo-"
    hide bill(1)
    show bill (48):      
        xpos 400
        zoom 0.6   
    stop music fadeout 3.0
    kristik "..."    
    bill "Shit...."
    play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
    bill "Hey Kristik! Long time no see!"
    kristik "dafuq d'you just call me you cracker?"
    hide bill(48)    
    show bill (21):      
        xpos 400
        zoom 0.6
    bill "Uh... you see... I was just joking haha."
    kristik "BITCH dat shit is either the worst joke I ever heard in my life or you is just a bitch"
    hide bill(21)  
    show bill (153):
        xpos 400
        zoom 0.6    
    bill "Heh... Well I guess I would be very knowledgable of getting the bitches."
    kristik "shut the fuck up bro I swear"
    stop music fadeout 3.0
    play music "audio/Sanoba Witch OST - School Dayz-(128kbps).ogg" fadein 2.0
    hide bill (153)
    hide hospital_room
    $ renpy.transition(dissolve)    
    show hospital_bed
    $ renpy.pause(0.50, hard=True)
    show jason (88):
        xpos 400
        ypos 20
        zoom 0.6
    with dissolve    
    jason "We need to hurry..."   
    jason "Kyle is on his way..."
    hide jason (88)
    show jason (76):
        xpos 400
        ypos 20
        zoom 0.6    
    jason "We should let him know that Kristik is alive"
    hide jason (76)
    with dissolve
    $ renpy.pause(1, hard=True)    
    stop sound
    ##################################################################################################
    #TODO: PLAY RUNNING SOUNDS THEN DOOR BLASTING OPEN
    ##################################################################################################   
    play sound "audio/doorkick.mp3"
    show kyle (7):
        xpos 300
        ypos 20
        zoom 0.6
    kyle "YOOOOOOOOOOO YALL SAID KRABBY IS BACK?!!?"    
    hide kyle (7)
    show kyle (12):
        xpos 200
        ypos 20
        zoom 0.6
    kyle "HOLY SHIDDDD BRO SINCE WHEN WAS YOU ALIVE??"
    kristik "since.... well ive been alive since i was born duh"
    hide kyle (12)
    show kyle (27):
        xpos 300
        ypos 20
        zoom 0.6
    kyle "Dam u got an attitude problem but yknow what it dont really matter"
    kristikmind "{i}... bruh... I GOT THE ATTITUDE PROBLEM?? THE FUCK YOU CALL THE OTHER GUYS THEN???"
    hide kyle (27)    
    show kyle (2):
        xpos 400
        ypos 20
        zoom 0.6    
    kyle "Anyways so I should prolly fill you in on whats been going on these past 10 years"
    hide kyle (2)
    show kyle (36):
        xpos 380
        ypos 20
        zoom 0.6    
    kyle "Dem dudes... Aaron and Wesley stole our planes and bombs"
    kristikmind "{i}damn i guess that flightsim really be workin on stealing them planes"
    hide kyle (36)
    show kyle (39):
        xpos 380
        ypos 20
        zoom 0.6    
    kyle "Its kinda ass cuz now they gon try to blow up the demon realm"
    hide kyle (39)
    show kyle (36):
        xpos 380
        ypos 20
        zoom 0.6    
    kristik "wait.. why does that matter?"
    kristik "I'm the only one here who has devil powers, and plus I tried to kill ya'll"
    kristik "idk why you guys are trying to help me even though I tried to kill you "
    hide kyle (36)
    show kyle (2):
        xpos 400
        ypos 20
        zoom 0.6 
    kyle "It dont matter bro"
    kyle "we homies for life my guy"
    kyle "shits in the past, what can you do"
    kyle "no point in holding grudges, you forever our fat indian BITCH"
    kristikmind "{i} dam bro thats so inspirational, im gon put that on facebook"  
    hide kyle (2)
    show kyle (40):
        xpos 400
        ypos 20
        zoom 0.6 
    kyle "anyway, we better get goin"
    kyle "we gotta pass through the demon realm to get to our base of operations where we got most of our shit"
    kristik "Aight then"
    hide kyle (40)
    with dissolve
    $ renpy.pause(0.50, hard=True)    
    hide hospital_bed
    $ show_quick_menu = False    
    show parking_lot
    with blinds
    $ renpy.pause(1.50, hard=True)    
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (1):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (14):
        xpos 0
        zoom 0.6        
    $ show_quick_menu = True        
    with dissolve
    kristik "Aight we gon get to our car"
    ##################################################################################################
    #TODO: PLAY WALKING SOUNDS
    ##################################################################################################
    hide kyle (5)
    hide jason (1)
    hide kevin (14)
    with dissolve
    window hide
    $ show_quick_menu = False
    with dissolve
    $ renpy.pause(0.50, hard=True)
    stop music fadeout 2.0
    hide parking_lot
    with dissolve
    $ renpy.pause(2, hard=True)  
    play music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k intro.ogg" 
    queue music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k.ogg"
    show road_one
    with dissolve  
    window show
    $ show_quick_menu = True
    with dissolve
    kristik "Where tf is the car?"
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6        
    $ show_quick_menu = True        
    with dissolve   
    kevin "We got feet for a reason bro"
    jason "Yeh why dont you use em more often? maybe turn that beanbag build into an actual human being"
    kristik "ok... but then where tf is bill??"
    hide jason (11)
    hide kevin (16)
    show jason (52):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (28):
        xpos 0
        zoom 0.6   
    with dissolve        
    jason "He got on a private jet... wit his bitches... (boohooo)"
    kevin "yeh da dude literally left us for some bitches"
    kristik "hold up just how much bitches he got??"
    hide jason (52)
    hide kevin (16)
    show jason (89):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (22):
        xpos 0
        zoom 0.6
    with dissolve
    jason "idk... bill got something like 8 hoes??"
    kevin "yeh he got 8 exactly..."
    kristikmind "{i} shiddd bruh... 8 bitches??? tf?"
    kristikmind "{i} kinda wanna see em..."
    kristikmind "{i} nah bro i dont want sloppy seconds thats just kinda gay.."
    hide jason (89)
    hide kevin (22)
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (23):
        xpos 0
        zoom 0.6
    kyle "well we almost at the airport"        
    kristik "airport tf???"
    kyle "yeh we going to the airport"
    kyle "we gotta fly through aint no way we walking lmao"
    kristik "aight bet what airline we flyin? United First Class? Delta Premium Economy?"
    hide jason (9)
    hide kevin (23)
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    jason "BITCH do we look like bill? We dont got $20K easily bro"
    kevin "yeh bruh we not a part of rich indian Google CEO family lookin ass"
    kristik "Aight fine i get it whatever bruh smh"
    $ show_quick_menu = False    
    hide road_one
    hide kyle (5)
    hide jason (11)
    hide kevin (16)
    show airport
    with blinds
    $ renpy.pause(1.50, hard=True)
    with dissolve
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (1):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (14):
        xpos 0
        zoom 0.6             
    with dissolve
    $ show_quick_menu = True
    kyle "Aight we here"
    hide kevin (14)
    show kevin (18):
        xpos 0
        zoom 0.6  
    kevin "Lesss gooo holy shit i haven't flown a plane in years"
    jason "Me neither, last time I flew a plane was that honeymoon me and my ex wife took to Algeria"
    hide jason (1)
    show jason (87):
        xpos 400
        ypos 20
        zoom 0.6
    jason "she said that she didnt like it broooo (cry cry cry)"
    hide jason (87)
    show jason (1):
        xpos 400
        ypos 20
        zoom 0.6    
    kyle "Damn yall haven't flown in that long?"
    kristik "i havent flown in years either"
    hide jason (1)
    hide kevin (18)
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6 
    jason "Aint nobody asked for your opinion"
    kristikmind "{i} bruh this mf imma kill this dude soon"
    hide jason (11)
    hide kevin(16)
    hide kyle (5)
    show bill (2):
        xpos 400
        zoom 0.6
    with dissolve
    stop music fadeout 1.0
    bill "Yoooo whatsup guys"
    play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
    kristik "bill??? tf you doin here???? i thought you was wit your bitches!?!?"
    hide bill(2)
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    with dissolve
    kevin "YEH EXACTLY WHERE YO BTICHES AT??"
    jason "YOU HERE JUST TO RUB IT IN ON US??"
    hide kyle (5)
    hide jason (11)
    hide kevin (16)
    show bill (10):
        xpos 400
        zoom 0.6
    with dissolve
    bill "Yeah... about that...."
    hide bill (10)
    show bill (33):
        xpos 400
        zoom 0.6
    bill "Hnnnrngrgrhh..."
    hide bill (33)
    show bill (19):
        xpos 400
        zoom 0.6
    stop music
    play music "audio/Sanoba Witch OST - Real Friend (Quiet Ver.)-(128kbps).ogg"
    bill "I ACTUALLY GOT NO BITCHES BROOOO!!!! (sob sob sob sob)"
    hide bill(19)
    show kyle (3):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (34):
        xpos 0
        zoom 0.6
    with dissolve   
    daboys "Bruh...."
    kevin "Seriously...?"
    jason "What about the private jet??!"
    hide kyle (3)
    hide jason (9)
    hide kevin (34)
    show bill (33):
        xpos 400
        zoom 0.6
    with dissolve
    bill "DAT SHIT IS REEEEENTED WAAAAHHHH!!!!!"
    hide bill(33)
    show kyle (3):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (34):
        xpos 0
        zoom 0.6
    with dissolve
    daboys "Ain't no fuckin way bruh..."
    hide kyle (3)
    hide jason (9)
    hide kevin (34)
    show bill (19):
        xpos 400
        zoom 0.6
    with dissolve    
    bill "PLZZ BROOO!!!! GET ME ON YOUR GUYS' FLIGHT!!! IM BROKE LIKE A HOMELESS MF"
    hide bill(19)
    show kyle (24):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (60):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (23):
        xpos 0
        zoom 0.6
    with dissolve    
    kevin "Uhhh.. sure but... who got money?"
    kyle "Ayo i dont got no money, my mom cancelled my card after i bought LEGO Batman on Steam for $5"
    jason "I dont got no cash on me..."
    hide kyle (21)
    hide jason (9)
    hide kevin (23)
    show kyle (21):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    with dissolve    
    daboys "..."
    kristik "...? What?"
    kyle "You got money right?"
    kevin "Yeh why dont you pay for his ticket?"
    jason "yeah dont be a douchebag"
    kristikmind "{i} bruh istg these mfs want ME TO PAY FOR THIS BROKE ASS BITCHS TICKET???"
    kristik "...bro"
    kristik "why should i pay for this dumbass dudes ticket"
    hide kyle (21)
    hide jason (9)
    hide kevin (16)
    show bill (19):
        xpos 400
        zoom 0.6
    with dissolve
    bill "PLEASE BROOOO I SWEAR ILL DO ANYTHING!!!!!"
    kristik "anything... eh?"
    hide bill (19)
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    with dissolve
    stop music
    play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
    jason "oh hell naw bruh dudes gonna be asking for some sussy shit"
    kevin "bro just pay for him"
    hide kyle (5)
    hide jason (11)
    hide kevin (16)
    show bill (19):
        xpos 400
        zoom 0.6
    with dissolve    
    kristik "fine but istg bill u better pay for it when u get the money. im charging u 69 percent interest"
    hide bill (19)
    show bill (14):
        xpos 400
        zoom 0.6
    stop music fadeout 2.0
    play music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k intro.ogg"
    queue music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k.ogg"
    bill "THANK UU BROOO!!! NOW LETS GET GOING!!"
    kristikmind "{i} jesus bruh this mf"
    hide bill (14)
    show bill (5):
        xpos 400
        zoom 0.6    
    kristik "wait but hold up how do you lie about having 8 bitches and not getting caught by this point"
    hide bill (5)
    show bill (9):
        xpos 400
        zoom 0.6
    bill "they was not even my bitches, they just some friends of my cousin"
    kristikmind "{i} sheeeesh ok jonathan (bill's cousin) pullin in that coochie"
    kristik "Where are they right now??"
    bill "tbh idfk... i havent talked to them in a while. all i heard was that they were flyin to somwehere but idk where and idk when."
    kristikmind "{i} smfh bad wingman"
    hide bill (9)
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    with dissolve    
    jason "we need to get going bro, flight leaves in 10 mins"
    hide kyle (5)
    hide jason (9)
    hide kevin (16)
    with dissolve
    intercom "Spirit Airlines flight 3387 is departing in 5 minutes. Any passengers who have not checked in with the podium will not be admitted to the flight once the doors close."
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6  
    with dissolve
    kevin "fuck bro thats our flight, we gotta go"
    $ show_quick_menu = False
    window hide
    hide kyle (5)
    hide jason (11)
    hide kevin (16)
    hide airport
    with dissolve
    stop music fadeout 2.0


    show white_base
    with dissolve
    show next_base
    show transition1
    with blinds
    $ renpy.pause(5, hard=True)  
    hide white_base
    hide next_base
    hide transition1
    with blinds
    $ renpy.pause(1, hard=True) 

    play music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k intro.ogg"
    queue music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k.ogg"
    show city_street2
    with Pixellate(2,5)
    $ renpy.pause(1.50, hard=True)    
    $ show_quick_menu = False
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    $ show_quick_menu = True        
    with dissolve     

#####################################################################################
##TODO: IMPROVE TRANSITION BETWEEN THESE TWO; WAY TOO FAST- EITHER ADD A NEW SCENE OR CHANGE SOMETHING
#####################################################################################
    kevin "that was a p shitty flight"
    jason "yeh those plastic ass chairs couldnt even recline"
    kristik "i could barely even fit in the seats"
    hide kevin (16)
    show kevin (17):
        xpos 0
        zoom 0.6
    kevin "u a fatass thats why kekekeke"
    hide kyle (5)
    hide jason (9)
    hide kevin (16)
    with dissolve
    transform slide:
        xalign 01.1 yalign 0.0
        ease 0.5 xalign 03.0
    show ssuo0101:
        xalign 1.1
    with dissolve
    kristik "...?"
    hide ssuo0101
    show ssuo0123 at slide
    $ renpy.pause(0.7, hard=True)
    kristik "... who tf was that?"
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6
    hide ssuo0123        
    with dissolve 
    kevin "tf are u doin krib? we gotta go man"
    kristik "Umm.. Uhhh... ughuhgh..."
    hide kevin (16)
    hide jason (9)
    show kevin (34):
        xpos 0
        zoom 0.6
    show jason (7):
        xpos 400
        ypos 20
        zoom 0.6    
    kevin "AYO TF IS THAT? THAT SHIT IS A BONER BRUH!!!"
    jason "EWWWWWWWW BRUH U GOT HARD OFF OF US???"
    kristik "NOO BRUH I SWEAR  I UHH.... I WAS JUST UHH...."
    jason "IMMA BEAT YO FUCKIN ASS SINCE U THINK THAT BEING GAY AND SHIT IS SO COOL"
    hide kyle (5)
    show kyle (18):
        xpos 700
        ypos 20
        zoom 0.6    
    kyle "Now, now, boys you gotta chill"
    kevin "CHILL??? HOW TF AM I GON CHILL WHEN HE GETTING A HARD ONE FROM OUR DICK??"
    kyle "Its probably a misunderstanding"
    kristikmind "{i} Yess!!! He understands me!!!"
    hide kevin (34)
    hide jason (7)
    hide kyle (18)
    show kyle (37):
        xpos 700
        ypos 20
        zoom 0.6    
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (26):
        xpos 0
        zoom 0.6 
    kyle "Maybe he da one who wants to get pegged!!!"
    kristik "...."
    hide kyle (37)     
    hide kevin (16)
    hide jason (9)
    show kyle (38):
        xpos 700
        ypos 20
        zoom 0.6       
    show kevin (34):
        xpos 0
        zoom 0.6
    show jason (7):
        xpos 400
        ypos 20
        zoom 0.6      
    jason "Oh so you like it if we on top?"
    kevin "...weird ass mf BITCH gay ass bitch ass mantitties literal buns BITCH..."
    kristik "GUYS IM NOT INTO GAY SHIT"
    hide kevin (34)
    hide jason (7)
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (26):
        xpos 0
        zoom 0.6     
    jason "Oh really?"
    kristik "YES I LOVE COOCHIE JUST AS MUCH AS THE NEXT GUY!!! PLZZZ BELIEVE ME!!!"
    hide jason (11)
    hide kevin (26)
    hide kyle (37)
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (16):
        xpos 0
        zoom 0.6    
    kevin "Wait, where the hell did bill go?"
    hide kyle(5)
    hide jason (9)
    hide kevin (16)
    with dissolve
    $ renpy.pause(0.7, hard=True)    
    show bill (155):
        xpos 100
        zoom 0.6
    show schi0101:
        xpos 600    
        zoom 1.2
    with dissolve
    bill "Sooo... yeah I got like 7,000 mansions up in California, my dad is the CEO of Roblox so I can get u some free robux"
    hide bill (155)
    show bill (50):
        xpos 100
        zoom 0.6
    bill "or i can get some other things for u for free ;))))))))"
    hide schi0101
    show schi0106:
        xpos 600    
        zoom 1.2
    unknown "Get away from me you weirdo."   
    hide bill (155)
    show bill (153):
        xpos 100
        zoom 0.6
    hide schi0106
    show schi0105:
        xpos 600    
        zoom 1.2        
    bill "Playin hard to get huh?"
    hide bill (155)
    show bill (154):
        xpos 100
        zoom 0.6   
    bill "What about a pickup line?"
    hide bill (154)
    show bill (131):
        xpos 100
        zoom 0.6
    bill "R u a highway???"
    hide bill (131)
    show bill (50):
        xpos 100
        zoom 0.6
    bill "Cuz imma drive you all night long!!! LOLLLOLL!!!!"
    hide schi0105
    show schi0106:
        xpos 600    
        zoom 1.2
    unknown ".... Isn't that just a lyric from the song in the Cars movie?"
    hide schi0106
    show schi0105:
        xpos 600    
        zoom 1.2
    hide bill (50)
    show bill (153):
        xpos 100
        zoom 0.6    
    bill "Yeh you got it right!!! XDXDXD!"    
    hide schi0105
    show schi0106:
        xpos 600    
        zoom 1.2    
    unknown "Fuck off no pussy getting lookin ass hair looking like rambutan lookin ass 8th member of BTS lookin ass"
    hide bill (153)
    show bill (151):
        xpos 100
        zoom 0.6        
    unknown "I'm going home. Don't follow me or I'm getting the no coochie police on your ass."
    transform moveright:
        xpos 600 ypos 0
        ease 0.5 xpos 1300
    hide schi0106
    show schi0105 at moveright:
        zoom 1.2
    $ renpy.pause(0.7, hard=True)
    bill "bruh...."
    hide bill (151)
    show bill (119):
        xpos 100
        zoom 0.6   
    bill "I was so close...."
    hide bill (119)
    with dissolve
    kristikmind "{i}bruh... this mf be so down bad..."
    show schi0105:
        xpos 300
        zoom 1.2
    with dissolve
    unknown "Didn't I just tell you not to follow me?"
    kristik "yeh but im not that down bad piece of shit tryna get some coochie"
    kristik "he my friend but some days hes just weird"
    hide schi0105
    show schi0102:
        xpos 300
        zoom 1.2     
    unknown "The hell is wrong with your friend? he's gonna need some therapy"
    hide schi0102
    show schi0101:
        xpos 300
        zoom 1.2  
    kristik "Yeah he broke up with his girlfriend a while ago and I guess hes tryna bounce back from that"
    hide schi0101
    show schi0102:
        xpos 300
        zoom 1.2   
    unknown "I wouldn't blame that girl. He's a creep and a pussy"
    hide schi0102  
    show bill (32):
        xpos 300
        zoom 0.6  
    with dissolve       
    bill "I DID EVERYTHING RIGHT!!! WHY WAS IT SUCH A FAILURE???!"
    bill "WAAAAHH!HHHHH!H!!!"
    hide bill (32)
    show schi0101:
        xpos 300
        zoom 1.2
    with dissolve 
    kristik "yeh.. hes got some... issues I guess"
    hide schi0101
    show schi0102:
        xpos 300
        zoom 1.2      
    unknown "Well, whatever. I have to go somewhere. I guess I'll see you around."
    kristik "K then"
    hide schi0102
    with dissolve
    $ renpy.pause(0.7, hard=True)    
    kristikmind "{i}See me around?? How so??"
    show kyle (2):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (13):
        xpos 0
        zoom 0.6
    with dissolve 
    kevin "Holy shit..."
    kristik "...?"
    kevin "That's the longest conversation you've ever had with a girl"
    kristik "What???!?!? No it's not!!!"
    jason "Did she notice your boner? You still have a hard on"
    kristik "Fuck... maybe?"
    hide jason (9)
    show jason (82):
        xpos 400
        ypos 20
        zoom 0.6
    jason "Well, whatever it's not my business really."
    hide kevin (13)
    show kevin (27):
        xpos 0
        zoom 0.6
    kevin "I'm fuckin tired bro... can we go to a hotel?"
    jason "yeh im smashin bro i gotta get some rest too"
    kyle "I guess I'm in the minority, I feel fine and more energetic!!!"
    kristik "Same, I'm not that tired."
    hide kevin (27)
    hide jason (82)
    show kevin (21):
        xpos 0
        zoom 0.6
    show jason (55):
        xpos 400
        ypos 20
        zoom 0.6   
    jason "Well you two can do something then, me and kevin are outta here"
    kevin "yeah im hella tired bro... those seats were literal hemorrhoids"
    hide jason (55) 
    hide kevin (21)
    with dissolve
    transform moveleft:
        xpos 700 ypos 20
        linear 0.2 xpos 400
    hide kyle (2)
    show kyle (2) at moveleft:
        zoom 0.6
    kyle "Why don't we do something togther then?"
    kristik "uhhh... no thanks you kinda weird tbh... and a little... gay?"
    hide kyle (2)
    show kyle (36):
        xpos 400
        ypos 20
        zoom 0.6
    kyle "Hmmm..."
    hide kyle (36)
    show kyle (37):
        xpos 400
        ypos 20
        zoom 0.6
    kyle "I guess, I'm a little gay ;;;)))))"
    kristik "Fuck that then, I'm outtie on my own"
    kyle "Suit yourself then"
    hide kyle (37)
    with dissolve 
    $ show_quick_menu = False
    hide city_street2
    with dissolve
    stop music fadeout 2.0
    $ renpy.pause(3.0, hard=True) 
    play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg" fadein 1
    show city_alley
    with dissolve
    $ show_quick_menu = True
    with dissolve
    kristikmind "{i} Shiddd... I haven't been here since my training a while back... damn this place has changed a lot."
    play sound "audio/bushrustle.mp3"
    ######################################################################################################
    #TODO: PLAY RUSTLING SOUND EFFECTS HERE
    ######################################################################################################
    $ renpy.pause(2.0, hard=True) 
    kristik "..."
    kristikmind "{i} The fuck was that???"

    ######################################################################################################
    #TODO: PLAY RUSTLING SOUND EFFECTS AGAIN HERE
    ######################################################################################################
    play sound "audio/bushrustle.mp3"    
    $ renpy.pause(2.0, hard=True) 
    kristik "..."    
    kristik "{i} This shits weird..."
    show ssuo0101:
        xpos 900
    with dissolve
    kristikmind "{i} It's that person again!!!"
    transform slidetwo:
        xpos 900
        ease 0.5 xpos 1300
    hide ssuo0101
    show ssuo0124 at slidetwo:
    $ renpy.pause(0.7, hard=True)
    kristik "..."
    kristik "Is she stalking me or some shit?"
    show schi0101:
        xpos 300    
        zoom 1.2  
    with dissolve
    hide schi0101
    show schi0102:
        xpos 300    
        zoom 1.2
    stop music fadeout 2.0
    unknown "Hey."
    hide schi0102
    show schi0101:
        xpos 300    
        zoom 1.2  
    play music "audio/Sabona Witch OST - Chotto Ennui-128k.ogg"
    kristik "tf???"
    kristik "What are you doing here?"
    hide schi0101
    show schi0102:
        xpos 300    
        zoom 1.2
    unknown "I told you we're going to see each other again."
    hide schi0102
    show schi0101:
        xpos 300    
        zoom 1.2    
    kristik "that fast tho??"
    kristik "i mean.. it was literally only a couple of hours ago."
    hide schi0101
    show schi0102:
        xpos 300    
        zoom 1.2
    unknown "Yeah. Anyawys, come out Suou."
    hide schi0102
    show schi0101:
        xpos 300    
        zoom 1.2
    kristikmind "{i} Who tf is she talking about??"
    transform moveshileft:
        xpos 300
        ease 0.7 xpos 100
    transform movesuouleft:
        xpos 1280
        ease 0.7 xpos 600
    hide schi0101
    show schi0101 at moveshileft:
        zoom 1.2
    show ssuo0105 at movesuouleft:
        zoom 1.2
    $ renpy.pause(0.7, hard=True)
    stop music fadeout 2.0
    kristik "..."
    play music "audio/Sanoba Witch OST - What-(128kbps).ogg" fadein 2.0
    kristik "ITS YOU BRUH!!!!"
    hide ssuo0105
    show ssuo0103:
        xpos 600
        zoom 1.2
    unknown "Hi..."
    kristik "WHO DA HELL ARE YOU BRO???!?"
    hide ssuo0103
    show ssuo0104:
        xpos 600
        zoom 1.2
    suou "My name is Suou..."
    kristik "Ok... and is there something you need from me??!"
    kristik "and hold on.. who is the green haired girl???"
    hide schi0101
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "I'm Chidori."
    hide schi0102
    show schi0101:
        xpos 100
        zoom 1.2
    hide ssuo0104
    show ssuo0103:
        xpos 600
        zoom 1.2
    kristik "uhhh.. ok.. Suou and Chidori... the hell do you want from me?"
    hide schi0101
    show schi0302:
        xpos 100
        zoom 1.2
    chidori "Are you going to tell him?"
    hide schi0302
    show schi0301:
        xpos 100
        zoom 1.2
    hide ssuo0103
    show ssuo0206:
        xpos 500
        zoom 1.2
    suou "I don't know... I doubt he even remembers anything."
    kristikmind "{i} Tf are they even talking about??"
    hide schi0301
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "Hey."
    hide schi0102
    show schi0101:
        xpos 100
        zoom 1.2
    kristik "Uhhh.. yeah?"
    hide schi0101
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "Do you remember her? Like, at all?"
    hide ssuo0206
    show ssuo0101:
        xpos 600
        zoom 1.2
    hide schi0102
    show schi0101:
        zoom 1.2
        xpos 100
    kristik "uhhh.. yeah? i saw her couple hours ago..."
    hide schi0101
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "No, I mean. Before this point. Maybe in your past?"
    hide schi0102
    show schi0101:
        xpos 100
        zoom 1.2
    kristik "No. I've never seen her before this point. In fact, I probably remember more about the Declaration of Independence than that person LOLOLOL"
    hide schi0101
    hide ssuo0101
    show schi0301:
        xpos 100
        zoom 1.2
    hide ssuo0103
    show ssuo0206:
        xpos 500
        zoom 1.2
    suou "I told you! He doesn't remember me!"
    kristik "Uhhh... Am I supposed to remember you?"
    hide schi0301
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "Well... let's say that it would kinda be problamatic if you did forget her.."
    hide schi0102
    show schi0101:
        xpos 100
        zoom 1.2
    kristik "Did I do something to you??"
    kristikmind "{i}Im tryna remember if I ever even SEEN a person that looks like that, I don't remember jack tho!!!"
    kristik "I'm sorry, I have no idea who the hell you are. Maybe you was a side hoe?"
    hide ssuo0206
    show ssuo0101:
        xpos 600
        zoom 1.2
    suou "Wait..."
    hide ssuo0101
    show ssuo0121:
        xpos 600
        zoom 1.2
    suou "You had side girls while we were dating?!?!?!?!?"
    kristik "What?? Since when did we ever date?"
    hide ssuo0121
    show ssuo0103:
        xpos 600
        zoom 1.2
    hide schi0101
    show schi0302:
        xpos 100
        zoom 1.2
    chidori "He doesn't rememeber you!!"
    hide ssuo0103
    hide schi0302
    show schi0301:
        xpos 100
        zoom 1.2
    show ssuo0207:
        xpos 500
        zoom 1.2
    suou "Oh right... Uhhh..."
    kristik "Aight... uh... idk who tf yall are but uhh imma just link up with my homies so if yall need something..."
    hide schi0301
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "Could I have your phone number?"
    hide schi0102
    show schi0101:
        xpos 100
        zoom 1.2
    kristik "uhhh... what?"
    kristik "why do you need it?"
    hide schi0101
    show schi0102:
        xpos 100
        zoom 1.2
    chidori "Just give it to me."
    hide schi0102
    show schi0101:
        xpos 100
        zoom 1.2
    kristikmind "{i}Bruh... idk this girl... she could be a groupie or some shit..."
    $ show_quick_menu = False
    window hide    
    menu:
        "Give her your phone number":
            $ show_quick_menu = True
            window show        
            jump Number
        "Don't give her your phone number":
            $ show_quick_menu = True
            window show        
            jump noNumber
    label Number:
        $ EXPchidori += 1
        $ EXPsuou += 1
        kristik "Uhhh. okay then... here it is."
        kristikmind "{i}I better not get stupid ass phone calls or text messages from this girl..."
        hide schi0101
        show schi0102:
            xpos 100
            zoom 1.2
        chidori "Thanks. I'll get in touch with you when I need you."
        hide schi0102
        show schi0101:
            xpos 100
            zoom 1.2
        kristik "Uhhh... ok but you better not send me weird scams or some shit"
        hide schi0101
        show schi0102:
            xpos 100
            zoom 1.2
        chidori "I won't."
        chidori "We'll now be going."
        chidori "Bye."
        hide schi0102
        hide ssuo0207
        with dissolve
        kristikmind "{i} something about that felt very fishy, but I hope it was for something important..."
        $ renpy.pause(1.0, hard=True)
        window hide
        hide city_alley
        $ show_quick_menu = False
        with Dissolve(1)
        stop music fadeout 2.0
        $ renpy.pause(2.0, hard=True)

        show white_base
        with dissolve
        show next_base
        show transition3
        with blinds
        $ renpy.pause(5, hard=True)  
        hide white_base
        hide next_base
        hide transition3
        with blinds
        $ renpy.pause(1, hard=True) 
        jump parttwo        


    label noNumber:
        ################################################################
        ##                  SUOU ROUTE ENDS HERE!!!
        ################################################################

        kristik "Sorry. I have no idea who you are, and I don't really wanna give my phone number to some random bitch i dont know lolololol"
        hide schi0101
        show schi0303:
            xpos 100
            zoom 1.2
        chidori "He doesn't want to do it..."
        hide ssuo0207
        show ssuo0210:
            xpos 500
            zoom 1.2
        suou "Yeah..."
        kristik "..?"
        hide ssuo0210
        hide schi0303
        show schi0102:
            xpos 100
            zoom 1.2
        show ssuo0101:
            xpos 600
            zoom 1.2
        chidori "Ok. Sorry to bother. We'll get going then."
        hide ssuo0101
        hide schi0102
        with dissolve
        $ renpy.pause(1.2, hard=True)
        kristik "tf was that all about?"
        with dissolve
        $ renpy.pause(1.2, hard=True)        
        window hide
        hide city_alley
        $ show_quick_menu = False
        with Dissolve(1)
        stop music fadeout 2.0
        jump parttwo

label parttwo:
    $ renpy.pause(3.0, hard=True)
    show city_station
    $ show_quick_menu = True
    with Dissolve(1)
    window show
    play music "audio/Sanoba Witch OST - Asa no Youki-320k.ogg"
    kristik "Whew..."
    kristik "Ugh..."
    kristik "I'm really tired..."
    kristik "I guess I'll be going to the hotel as well..."
    show kyle (1):
        xpos 400
        zoom 0.6
    with dissolve
    kyle "Yo Kristik, going back already?"
    kristik "yeah bro im tired asf... idk how tf you have this energy"
    hide kyle (1)
    show kyle (2):
        xpos 400
        zoom 0.6
    kyle "i just drank alot of kool aid"
    kristik "uhhh... ok then...."
    if EXPchidori >= 1:
        #################################################################
        #PLAY PHONE RING SOUND
        #################################################################
        play sound "audio/notification.mp3"
        $ renpy.pause(1,hard=True)
        kristik "Hm..?"
        kristik "A text message?"
        hide kyle (2)
        with dissolve
        chidori "{i} Meet me on the road next to the park. We need to talk."
        kristikmind "{i} Talk?? tf she wanna talk about?"
        show kyle (2):
            xpos 400
            zoom 0.6
        with dissolve
        kristik "Hey kyle, i have to go actually"
        hide kyle (2)
        show kyle (1):
            xpos 400
            zoom 0.6
        kyle "Where are you going?"
        kristik "uhhhh..... somewhere i gotta go bye!!!"
        hide kyle (1)
        with dissolve

        #################################################################
        #PLAY RUNNING SOUND
        #################################################################

        $ renpy.pause(1.0, hard=True)        
        $ show_quick_menu = False
        hide city_station
        show hok_road
        with dissolve
        $ renpy.pause(1.0, hard=True)
        $ show_quick_menu = True
        kristik "... should be somewhere here..."
        show schi0101:
            xpos 300
            zoom 1.2
        with dissolve
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "Hey."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "Hey... uh what do you need to talk about??"
        kristikmind "{i} WAIT!!! maybe she tryna get freaky in the forest???!!!"
        kristikmind "{i} hold up i dont even have any condoms tho!!!"
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "This is regarding Suou."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2        
        kristikmind "{i}Awwww damnit... WAIT HOLD UP MAYBE SHE WANTS A THREESOME???!"
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "This has nothing to with sexual acts."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristikmind "{i} fuck..."
        hide schi0101
        show schi0311:
            xpos 300
            zoom 1.2
        chidori "At least not yet..."
        kristik "Wait.. what?"
        hide schi0311
        show schi0312:
            xpos 300
            zoom 1.2    
        chidori "I'm rushing this a bit too much..."
        hide schi0312
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "Anyways, you know Suou right?"
        hide schi0102
        show schi0302:
            xpos 300
            zoom 1.2
        chidori "This may be hard to believe, but before you woke up in that hospital bed... she used to be your girlfriend."
        hide schi0302
        show schi0312:
            xpos 300
            zoom 1.2
        chidori "That was until you had to leave..."
        kristikmind "{i} What??? I don't remember that shit..."
        hide schi0312
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "I know, it's very hard to believe."
        chidori "But your memory had been wiped when you woke up on the hospital bed."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "Wait.. how do you even know that I was on a hospital bed????!?"
        kristik "And how do you even know about if I got my memory wiped or not????"
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "I don't know."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "Wat?????"
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "She just told me all this information."
        chidori "I just trust her as a friend, so she's probably telling the truth."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "So wait... maybe that's why I had that 10 year gap..."
        chidori "..."
        kristik "Where is Suou right now?"
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "She is back at home. I'm telling this information to you without her knowing."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "bruh...."
        kristik "She doesn't know we're having this conversation?!?!?"
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "No."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "So straight forward..."
        kristik "I don't know, this is all very hard to believe so I don't know if I should take this information as fact or if you're just tryna troll me."
        hide schi0101
        show schi0102:
            xpos 300
            zoom 1.2
        chidori "I understand."
        chidori "You could always confront her with this now that you know."
        hide schi0102
        show schi0101:
            xpos 300
            zoom 1.2
        kristik "uhhhh..."
        kristikmind "{i} Should I even do that?"
        $ show_quick_menu = False
        window hide           
        menu:
            "Go to Suou and ask her about this":
                $ show_quick_menu = True
                window show
                jump confrontSuou
            "Ignore advice and go back to train station":
                $ show_quick_menu = True
                window show            
                jump goback
        label confrontSuou:
            $ EXPsuou += 1
            kristik "I might as well..."
            kristik "There isn't much point on holding this information without her knowing."
            kristik "Where does she live?"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "I will show you. Follow me."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            kristik "uhhh.. ok."
            hide schi0101
            with dissolve
            kristikmind "{i}She better not end up murdering me, there's still so much Hentai out there that I haven't fapped to!!!"
            stop music fadeout 2.0
            $ show_quick_menu = False
            hide hok_road
            window hide
            with dissolve
            $ renpy.pause(1, hard=True)
            show suburb_roadcenter
            window show
            $ show_quick_menu = True
            with dissolve
            play music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k intro.ogg"
            queue music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k.ogg"
            $ renpy.pause(0.5, hard=False)
            narrator "..."
            kristik "Yo... are we there yet???"
            kristik "We literally been walkin for... 2 hours already...."
            show schi0102:
                xpos 300
                zoom 1.2
            with dissolve
            chidori "We are almost there."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            kristik "That's what you fuckin said an hour ago!"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "Yes. But truthfully I only lied so that I can suppress your complaining."
            hide schi0102
            show schi0101:
                 xpos 300
                 zoom 1.2
            kristik "Cheeky bitch..."
            hide schi0101
            hide suburb_roadcenter
            show shizu_houseext
            with dissolve
            $ renpy.pause(0.5, hard=True)
            show schi0102:
                xpos 300
                zoom 1.2
            with dissolve
            chidori "We're here."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            kristik "(huff).... woah yea.... (puff)"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "Please pull yourself together. You don't want to look like a beanbag when you see Suou."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            kristik "yeah yeah yeah whatever... hold on let me... catch my breath..."

            play sound "audio/intercom_call.mp3"
            $ renpy.pause(2, hard=True)
            ####################################################################################################################################
            ## PLAY INTERCOM BEEP SOUND
            ####################################################################################################################################
            
            suou "Hello?"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "Hi Suou. It's me Chidori."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            suou "Chidori? What do you need?"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "I forgot something at your house."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2         
            suou "What is it? I may be able to find it and bring it out to you"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "It's too small to try to find by yourself. I'll try to find it with you."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            suou "Really? Okay hold on, let me open the gate."
            hide schi0101
            with dissolve

            play sound "audio/gate.mp3"
            $ renpy.pause(4, hard=True)
            ######################################################################################################################################  
            ## PLAY GATE OPENING SOUND
            ######################################################################################################################################

            show schi0101:
                xpos 100
                zoom 1.2
            show ssuo0101:
                xpos 600
                zoom 1.2
            with dissolve
            suou "Chidori?"
            hide schi0101
            show schi0102:
                xpos 100
                zoom 1.2
            chidori "I'm sorry. I didn't actually lose anything. But your former boyfriend is here with you."
            hide schi0102
            show schi0101:
                xpos 100
                zoom 1.2
            hide ssuo0101
            show ssuo0106:
                xpos 600
                zoom 1.2
            suou "Huh?"
            hide ssuo0106
            show ssuo0128:
                xpos 600
                zoom 1.2
            with dissolve
            suou "HUHH???"
            kristik "Sup. "
            kristik "uhhh...."
            hide ssuo0128
            show ssuo0121:
                xpos 600
                zoom 1.2
            suou "What are you even doing here???"
            hide schi0101
            show schi0102:
                xpos 100
                zoom 1.2
            chidori "He needs to seek validation that you and him were copulating in the past. He doesn't believe me, so you will have to tell him."
            suou "How did you even find out about that????!"
            kristik "Uhhh... uhm-"
            hide ssuo0121
            show ssuo0103:
                xpos 600
                zoom 1.2
            chidori "I told him myself."
            chidori "You were always going on about him knowing the truth."
            hide schi0102
            show schi0101:
                xpos 100
                zoom 1.2
            hide ssuo0103
            show ssuo0121:
                xpos 600
                zoom 1.2
            suou "Well.. yeah! But I didn't mean him that you should tell him NOW!!!"
            hide ssuo0121
            show ssuo0103:
                xpos 600
                zoom 1.2
            kristik "So uhh...."
            kristik "You tellin me, that a couple of years ago we was smashin?"
            hide ssuo0103
            show ssuo0105:
                xpos 600
                zoom 1.2
            suou "Uhh...."
            kristik "Wait... Don't tell me... WE DIDN'T USE A CONDOM!??!?"
            hide ssuo0105
            show ssuo0121:
                xpos 600
                zoom 1.2
            suou "Of course we-"
            hide ssuo0121
            show ssuo0105:
                xpos 600
                zoom 1.2           
            suou "Wait no..."
            kristik "Wait... so I'm still a virgin?"
            suou "Uhhh...."
            kristik "Fuck! I thought I woulda lost my vriginity at least!"
            hide schi0101
            show schi0102:
                xpos 100
                zoom 1.2
            chidori "Is that the only thing boys think about?"
            hide schi0102
            show schi0101:
                xpos 100
                zoom 1.2
            kristik "Actually, most guys don't really care about that."
            kristik "But I'm not like most guys ;)))"
            kristik "I'm a menace (rawr)"
            hide schi0101
            show schi0302:
                xpos 100
                zoom 1.2
            chidori "Watch out Suou, your boyfriend is kinda a perv..."
            hide schi0302
            show schi0301:
                xpos 100
                zoom 1.2
            suou "Well, I guess it's good to see that he hasn't change much since then...."
            kristik "So wait... let me get this straight."
            hide schi0301
            show schi0101:
                xpos 100
                zoom 1.2
            hide ssuo0105
            show ssuo0102:
                xpos 600
                zoom 1.2
            kristik "We were dating back then, and then my memory got wiped???"
            kristik "How tf does that shit even happen? Amnesia?"
            kristik "Nah wait amnesia is just a cliche Indian Drama technique..."
            suou "You were forced to return to America due to your friends requiring you to pass through the demon realm."
            kristik "What??? They just said that I had a coma! "
            kristik "Lying bastards, I swear they are in for a knuckle chicken tikka masala one day..."
            suou "Because of that hijacking incident with you and the IRS, they would've been able to bring you back to America but in order for you to remain anonymous..."
            suou "... they wiped your memory and most other people's memory about you during that time."
            suou "Just so that you don't get in trouble by the law due to your terrorist organization."
            kristik "Well, okay I guess I can get that."
            kristik "But then how the hell do you still remember me?"
            hide ssuo0102
            show ssuo0105:
                xpos 600
                zoom 1.2
            suou "Well...."
            hide schi0101
            show schi0102:
                xpos 100
                zoom 1.2
            chidori "There's this rumour that you can start to remember events that were forcefully removed from your brain by just-{p=1.5}{nw}"
            hide schi0102
            show schi0101:
                xpos 100
                zoom 1.2
            hide ssuo0105
            show ssuo0121:
                xpos 600
                zoom 1.2
            suou "AHHH!! DONT TELL HIM THAT!!"
            hide schi0101
            show schi0102:
                xpos 100
                zoom 1.2
            hide ssuo0105
            show ssuo0103:
                xpos 600
                zoom 1.2
            chidori "Why not, its good information that he could maybe use himself to remember you as well."
            chidori "Don't you think so too, Kristik?"
            hide schi0102
            show schi0101:
                xpos 100
                zoom 1.2
            kristik "Uhhh... yeah sure..."
            kristikmind "{i}Really? Is this shit even real? This shit sounds like some witchcraft shit bro"
            kristikmind "{i}I mean I guess she lookin kinda thicc..."
            kristikmind "{i}Her clothing really baggy though.... kinda hard to tell for sure..."
            kristikmind "{i}But busting a nut to reverse amnesia??? Tf???"
            hide ssuo0103
            show ssuo0121:
                xpos 600
                zoom 1.2
            suou "I know what you're thinking! And no, don't even think about trying it yourself!!!!"
            hide ssuo0121
            show ssuo0103:
                xpos 600
                zoom 1.2
            hide schi0101
            show schi0102:
                xpos 100
                zoom 1.2
            chidori "You should try it. Not here or right now of course."
            hide schi0102
            show schi0101:
                xpos 100
                zoom 1.2
            kristik "Yeah... I know when to nut bruh"
            hide ssuo0103
            show ssuo0121:
                xpos 600
                zoom 1.2
            suou "No!!! Its out of the question!!!"
            hide schi0101
            show schi0302:
                xpos 100
                zoom 1.2
            chidori "What?? You can't be a hypocrite Suou. Just let him be and do his nutting."
            hide schi0302
            show schi0301:
                xpos 100
                zoom 1.2
            kristik "Wait. Ok hold on I'm not gonna do it right now..."
            hide schi0301
            show schi0102:
                xpos 100
                zoom 1.2
            chidori "In fact, let's do it right now."
            kristik "WAIT. WHAT-{p=0.5}{nw}"
            transform bigger:
                xpos 100 ypos 0
                zoom 1.2
                ease 0.5 zoom 1.8 xpos -20 ypos 70
            hide schi0102
            show schi0101 at bigger            
            kristik "WAIT TF ARE YOU DOIN??"
            hide ssuo0121
            show ssuo0123:
                xpos 600
                zoom 1.2
            suou "WHAT ARE YOU DOING CHIDORI?!?!"
            play sound "audio/unzipping.mp3"
            $ renpy.pause(1,hard=True)
            ############################################################################################
            ## PLAY UNZIPPING NOISES
            #############################################################################################

            kristik "WAAHH!!! WAIT A MINUTE!!"
            hide schi0101
            show schi0102:
                xpos -20 ypos 70
                zoom 1.8
            chidori "This won't hurt."
            hide ssuo0123
            show ssuo0103:
                xpos 600
                zoom 1.2
            hide schi0102
            show schi0101:
                xpos -20 ypos 70
                zoom 1.8
            kristik "WAITWAITWAITWAIT YOURE GONNA JACK ME OFF???"
            hide schi0101
            show schi0102:
                xpos -20 ypos 70
                zoom 1.8
            chidori "Do you not want to me to?"
            hide schi0102
            show schi0101:
                xpos -20 ypos 70
                zoom 1.8       
            kristikmind "{i}WHAT KIND OF FUCKIN QUESTION IS THAT???"  
            $ show_quick_menu = False
            window hide                
            menu:
                "''Yes please!!! Jack me off mommy!!!''":
                    $ show_quick_menu = True
                    window show
                    $ EXPchidori += 2
                    jump yesJack
                "''The fuck??? No bro!!!!''":
                    $ show_quick_menu = True
                    window show
                    $ EXPsuou += 1
                    jump noJack
            label yesJack:
                kristik "YES JACK ME OFF MOMMY!!!!!!"
                stop music fadeout 2.0
                hide schi0101
                transform smaller:
                    xpos -20 ypos 70
                    zoom 1.8
                    ease 0.5 zoom 1.2 xpos 100 ypos 0
                show schi0115 at smaller
                hide ssuo0103
                show ssuo0121:
                    xpos 600
                    zoom 1.2
                narrator "..."
                suou "What did you just call Chidori??!?"
                chidori "..."
                kristik "uhhh.... um yknow..."
                hide schi0115
                show schi0111:
                    xpos 100
                    zoom 1.2
                chidori "......"
                hide schi0111
                show schi0311:
                    xpos 100
                    zoom 1.2
                chidori "Sorry... this is my fault..."
                hide schi0311
                show schi0111:
                    xpos 100
                    zoom 1.2
                chidori "I.. actually have to go to somewhere..."                
                transform full_left:
                    xpos 100
                    zoom 1.2
                    ease 0.5 xpos -800
                hide schi0111
                hide ssuo0121
                show ssuo0104:
                    xpos 600
                    zoom 1.2
                show schi0111 at full_left
                $ renpy.pause(2)
                kristik "ummm..."
                hide schi0111
                hide ssuo0104
                show ssuo0103:
                    xpos 600
                    zoom 1.2
                suou "I also have stuff to do... so uhh.."
                suou "I'll be going back now..."
                hide ssuo0103
                with dissolve
                $ renpy.pause(1,hard=True)
                kristik "ugh... fuck..."
                kristik "i guess I might as well be heading back to the station..."
                window hide                
                $ show_quick_menu = False
                hide shizu_houseext
                with dissolve
                $ renpy.pause(1,hard=True)  
                window show
                $ show_quick_menu = True
                show city_station
                with dissolve
                play music "audio/Sanoba Witch OST - School Dayz-(128kbps).ogg"
                $ renpy.pause(2, hard=True)
                kristik "Jesus christ... how did i walk that far???"     
                show kyle(1):
                    xpos 400
                    zoom 0.6
                with dissolve
                kyle "Hey man, where the hell did you go?"           
                kristik "Dude... why the fuck are you still here?"
                kristik "It's been at least 4 hours since I left"
                hide kyle (1)
                show kyle (2):
                    xpos 400
                    zoom 0.6
                kyle "...A BITCH never leave another BITCH by himself. That's just how it is."
                hide kyle (2)
                show kyle (1):
                    xpos 400
                    zoom 0.6                
                kristik "The fuck?? That's both really nice but also pretty gay..."
                kristik "Anyways, I'm just gon wait for the train bro..."
                kristik "Holy shit i'm so tired..."
                hide kyle (1)
                show kyle (2):
                    xpos 400
                    zoom 0.6
                kyle "Next train is set to arrive in 30 minutes."
                kristik "Aight whatever... (huff)... I'll just wait...."
                stop music fadeout 2.0
                $ show_quick_menu = False
                window hide
                hide kyle (2)
                hide city_station
                with dissolve
                $ renpy.pause(2,hard=True)

                show white_base
                with dissolve
                show next_base
                show transition4
                with blinds
                $ renpy.pause(5, hard=True)  
                hide white_base
                hide next_base
                hide transition4
                with blinds
                $ renpy.pause(1, hard=True) 

                jump chapterthree                
            label noJack:
                kristik "HELL NO BRO!!! PLZ NO!!!"
                hide schi0101
                transform smaller:
                    xpos -20 ypos 70
                    zoom 1.8
                    ease 0.5 zoom 1.2 xpos 100 ypos 0
                show schi0115 at smaller          
                chidori "Hm."
                hide schi0115
                show schi0302:
                    xpos 100
                    zoom 1.2
                chidori "I guess this'll be a bit harder for you Suou..."
                kristik "Tf is that supposed to mean?"
                hide schi0302
                show schi0102:
                    xpos 100
                    zoom 1.2
                chidori "To be honest, I thought you were going to give into your beastly desires."
                chidori "I suppose I was wrong."
                hide schi0102
                show schi0101:
                    xpos 100
                    zoom 1.2
                kristik "BOI put some more RESPECC on my name!"
                kristik "OFC i can hold my self composure!!!"
                hide schi0101
                show schi0115:
                    xpos 100
                    zoom 1.2
                chidori "Even though you got an erection after seeing Suou for the first time?"
                hide ssuo0103
                show ssuo0123:
                    xpos 600
                    zoom 1.2
                suou "WHAT??? IS THAT TRUE KRISTIK?!?"
                $ EXPsuou += 2
                hide ssuo0123
                show ssuo0121:
                    xpos 600
                    zoom 1.2
                suou "So THAT's what you were talking about to your friends huh??"
                hide ssuo0121
                show ssuo0103:
                    xpos 600
                    zoom 1.2
                kristik "ummm... fuck uh I just remembered.."
                kristik "that i have an appointment for the indian ah mimi atta putakilia takalia concert today"
                hide schi0115
                show schi0102:
                    xpos 100
                    zoom 1.2
                chidori "How do you get an appointment for a concert?"
                hide schi0102
                show schi0101:
                    xpos 100
                    zoom 1.2
                kristik "AIGHT WELL GTG BYE!!!"
                hide schi0101
                hide ssuo0103
                with dissolve
                $ renpy.pause(1,hard=True)
                stop music fadeout 2.0
                window hide                
                $ show_quick_menu = False
                hide shizu_houseext
                with dissolve
                $ renpy.pause(1,hard=True)  
                window show
                $ show_quick_menu = True
                show city_station
                with dissolve
                play music "audio/Sanoba Witch OST - School Dayz-(128kbps).ogg"
                $ renpy.pause(2, hard=True)
                kristik "ugh.... holy shit... (huff)"
                kristik "Bitch ass... kyle left me..."
                kristik "Gotta wait for the next train ffs..."
                stop music fadeout 2.0
                $ show_quick_menu = False
                window hide
                hide city_station
                with dissolve
                $ renpy.pause(2,hard=True)

                show white_base
                with dissolve
                show next_base
                show transition5
                with blinds
                $ renpy.pause(5, hard=True)  
                hide white_base
                hide next_base
                hide transition5
                with blinds
                $ renpy.pause(1, hard=True) 


                jump chapterthree  

        label goback:
            kristik "I don't really think that's appropriate..."
            kristik "I mean she didn't look very confident to even talk to me"
            kristik "How da hell do you expect her to even take that info, she'll prolly get 1 tapped in the brain like this is csgo ezfrags cheats"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "I understand."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            kristik "Do you really?"
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "No, of course not. That analogy is too retarded for me to understand."
            hide schi0102
            show schi0101:
                xpos 300
                zoom 1.2
            kristik "It's because... like- CSgo has a lot of cheaters- forget it."
            hide schi0101
            show schi0102:
                xpos 300
                zoom 1.2
            chidori "Well, whatever. I will see you later then."
            chidori "Bye."
            hide schi0102
            with dissolve
            $ renpy.pause(0.65, hard=True)
            kristik "Weird convo... but I guess I should go back to the station."
            $ show_quick_menu = False
            window hide
            hide hok_road
            with dissolve
            $ renpy.pause(1.0, hard=True)
            window show
            show city_station
            with dissolve
            $ renpy.pause(1, hard=True)
            show kyle (1):
                xpos 400
                zoom 0.6
            with dissolve
            kyle "Where'd you go?"
            kristik "It... doesn't really matter..."
            kyle "Really?"
            kristik "Yeah..."
    elif EXPchidori < 1:
        play sound "audio/train.ogg"
        #################################################################
        #PLAY TRAIN SOUND
        #################################################################
        kristik "Looks like the train is here..."
        kyle "Yeah. Let's get on."
        stop music fadeout 2.0
        $ show_quick_menu = False
        window hide
        hide kyle (2)
        hide city_station
        with dissolve
        $ renpy.pause(2,hard=True)
        jump chapterthree  
    
    kyle "Welp, let's get going then. We gotta get on board before they leave without us."
    stop music fadeout 2.0
    $ show_quick_menu = False
    window hide
    hide kyle (2)
    hide city_station
    with dissolve
    $ renpy.pause(2,hard=True)
    jump chapterthree  


label chapterthree:
    if EXPchidori >= 3:
        $show_quick_menu = True
        play music "audio/Sabona Witch OST - Yasashii Kaze-128k.ogg"

        show city_street3
        window show
        with dissolve
        kristik "Shit..."
        kristik "Chidori isn't responding to any of my texts..."
        kristik "{i}Hey Chidori! I didn't really mean to call you ''mommy''... It just kind of slipped out..."
        chidori "{i}It's fine. It really doesn't matter a whole lot."
        kristik "{i}Are you comfortable meeting me at the 7-eleven today?"
        kristik "{i}Hello?"
        chidori "{i}..."
        kristik "She stopped typing after that..."
        kristik "I'll go there in case.. Maybe she's there?"
        $ renpy.pause(1,hard=True)
        hide city_street3
        show suburb_konbiniext
        with dissolve
        $ renpy.pause(1,hard=True)
        kristik "..."
        kristik "I don't see her..."
        kristik "Well fuck... I messed up really hard calling her mommy bruh..."
        show schi0111:
            xpos 600
            zoom 1.2
        with dissolve

        chidori "..."
        hide schi0111
        show schi0208:
            xpos 600
            zoom 1.2
        kristik "OH..."
        kristik "hey...?"
        hide schi0208
        show schi0311:
            xpos 300
            zoom 1.2
        with dissolve
        chidori "Hi..."
        kristik "You came..."
        hide schi0311
        show schi0313:
            xpos 300
            zoom 1.2
        chidori "Yeah..."
        kristikmind "{i}Bro holy shit this is so hard..."
        kristikmind "{i}This is harder than trying to remotely deactivate a bomb with a deaf person..."       
        kristik "So about that mommy thing..."
        hide schi0313
        show schi0111:  
            xpos 300
            zoom 1.2
        chidori "..."
        kristik "Um... so like-"
        hide schi0111
        show schi0201:
            xpos 300
            zoom 1.2
        stop music fadeout 1.0
        unknown "Chidori!!!"
        kristik "???"
        transform moveleft2:
            xpos 300
            zoom 1.2
            ease 0.5 xpos -10
        hide schi0201
        show schi0201 at moveleft2
        transform movefromright1:
            xpos 1280
            zoom 1.2
            ease 0.5 xpos 300
        show syuz0101 at movefromright1
        transform movefromright2:
            xpos 1280
            zoom 1.2
            ease 0.5 xpos 700
        show sner0101 at movefromright2
        $ renpy.pause(1.0, hard=True)

        kristikmind "{i}Who tf are they??"
        hide syuz0101
        show syuz0102:
            xpos 300
            zoom 1.2
        play music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k intro.ogg" 
        queue music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k.ogg"
        unknown "Sorry we're late, the hot dog convention got too busy."
        hide syuz0102
        show syuz0101:
            xpos 300
            zoom 1.2
        kristikmind "{i}the what fuckin convention?????"
        kristik "I'm sorry, the what fuckin convention??!"
        hide syuz0101
        show syuz0114:
            xpos 300
            zoom 1.2
        unknown "Chidori, who's this fat indian kid?"
        hide schi0201
        show schi0302:
            xpos -10
            zoom 1.2
        chidori "Its the boyfriend I was talking about...."
        unknown "Really?? Him??"
        hide syuz0114
        show syuz0110:
            xpos 300
            zoom 1.2
        hide schi0302
        show schi0301:
            xpos -10
            zoom 1.2
        unknown "He looks like a dud to be honest..."
        kristikmind "{i}the fuck did this bitch just call me?"
        $ EXPyuzuriha += 1
        $ EXPchidori += 1
        $ EXPnerine += 1
        kristik "Madame, my name is Sir Krabby Krabbick McFrabbick Lingle Bartholomew the Third,"
        kristik "I would like to inform you that this misunderstanding is rather tragic."
        kristik "For, I am NOT a dud, rather a strong and capable monsieur, with the ability to last longer than 5 seconds."
        kristik "In effetti, posso parlare italiano con perfetta fluidità poiché l'eredità della mia famiglia è della nobile famiglia Lal."
        unknown "????"
        hide schi0301
        show schi0106:
            xpos -10
            zoom 1.2
        chidori "What are you doing????!!"
        hide schi0106
        show schi0105:
            xpos -10
            zoom 1.2
        kristik "Idk.. girl on the right looks Italian."
        hide sner0101
        show sner0204:
            xpos 700
            zoom 1.2
        unknown "Perchè si! Come potresti dirlo? Il tuo italiano è davvero molto buono nonostante il forte accento!"
        hide sner0204
        show sner0203:
            xpos 700
            zoom 1.2
        kristik "uhhh..."
        kristik "Signora.... uh io... io uh... non riuscivo... a capire?"
        hide sner0203
        show sner0102:
            xpos 700
            zoom 1.2
        unknown "Penso che sia davvero fantastico che tu abbia deciso di imparare l'italiano! Dove l'hai imparato? Da quanto tempo lo stai imparando?"
        hide sner0102
        show sner0101:
            xpos 700
            zoom 1.2
        kristik "No... capito?"
        hide sner0101
        show sner0212:
            xpos 700
            zoom 1.2
        unknown "È estremamente difficile trovare una persona che parli italiano in questa regione."
        hide sner0212
        show sner0203:
            xpos 700
            zoom 1.2
        kristik "UHHHHH.... "
        kristik "Lei..... parla english????"
        hide syuz0110
        show syuz0114:
            xpos 300
            zoom 1.2
        unknown "The hell is this conversation?"
        kristik "Chidori, who are these people?!"
        hide syuz0114
        show syuz0110:
            xpos 300
            zoom 1.2
        hide schi0105
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "Silver hair is Yuzuriha."
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        yuzuriha "..."
        hide schi0101
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "Blonde is Nerine."
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        hide sner0203
        show sner0102:
            xpos 700
            zoom 1.2
        nerine "Ciao! Come ti chiami?"
        hide sner0102
        show sner0101:
            xpos 700
            zoom 1.2
        kristik "Uhhh.... mi chiamo... mi chiamo... Kristik?"
        hide sner0101
        show sner0102:
            xpos 700
            zoom 1.2
        nerine "Da dove vieni e che etnia sei?"
        hide sner0102
        show sner0101:
            xpos 700
            zoom 1.2
        kristik "Can... u... speek... Engrish?"
        hide sner0101
        show sner0102:
            xpos 700
            zoom 1.2
        nerine "Yes. I can."
        hide sner0102
        show sner0101:
            xpos 700
            zoom 1.2
        kristikmind "{i}Holy shit thank god... my Italian came in clutch there but holy shit I haven't learned it in so long..."             
        hide syuz0110
        show syuz0102:
            xpos 300
            zoom 1.2
        yuzuriha "So, what did you need to talk about Chidori?"
        hide syuz0102
        show syuz0101:
            xpos 300
            zoom 1.2
        hide schi0101
        show schi0302:
            xpos -10
            zoom 1.2
        hide schi0101
        show schi0303:
            xpos -10
            zoom 1.2
        chidori "Well, as I've said before, this was Suou's boyfriend back then."
        hide syuz0101
        show syuz0108:
            xpos 300
            zoom 1.2
        hide schi0303
        show schi0301:
            xpos -10
            zoom 1.2                      
        yuzuriha "There's no way! He's too fat and pimple ridden to even get a prostitute!"              
        kristikmind "{i}Bruh this bitch really starting to piss me off..."
        hide syuz0108
        show syuz0107:
            xpos 300
            zoom 1.2
        yuzuriha "Do you even remember anything about Suou, Kristik?"
        hide syuz0107
        show syuz0101:
            xpos 300
            zoom 1.2
        kristik "uhhh... no. I don't."
        kristik "To be honest, I still don't really believe that I was her boyfriend."
        kristik "With my beanbag lifestyle it would have been unheard of for me to get a girlfriend."
        hide sner0101
        show sner0208:
            xpos 700
            zoom 1.2
        nerine "Awww... There's no reason to be so self depracating."
        hide sner0208
        show sner0104:
            xpos 700
            zoom 1.2
        nerine "After all, not EVERYTHING is bad about you."
        hide sner0104
        show sner0103:
            xpos 700
            zoom 1.2
        hide schi0303
        hide schi0302
        hide schi0301
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "Anyways. Kristik, these two are to accompany you."
        chidori "I know about your mission to bring down both the ASIANBOYZ faction."
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        kristikmind "{i}Wait...? What??? Accompany me? ASIANBOYZ??? Tf is that??"
        kristik "Wait... what is ''ASIANBOYZ''???"
        hide schi0101
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "They are the uprising faction. You know, the ones you're trying to bring down?"
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        kristik "What?? I never heard that name..."
        hide schi0101
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "They were former friends of you. Aaron and Wesley?"
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        kristik "Oohhhhhh....!"
        kristikmind "{i}They really called themselves the ''ASIANBOYZ''???"
        kristikmind "{i}That name is almost as gay as kyle..."
        hide schi0101
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "Anyways, they will be here to accompany you to bring them down. I already informed your other friends, Kyle, Jason and Kevin about this."
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        kristikmind "{i}Holy shit, she's on top of these things..."
        kristikmind "{i}i woulda still be on my hospital bed on my fat noob ass watching anime probably..."
        kristik "But if you're able to do all these things... why can't you just fight the ''ASIANBOYZ''??"
        hide schi0101
        show schi0102:
            xpos -10
            zoom 1.2
        chidori "Me and Suou are not demons. We cannot fight, nor do we have the ability to. Unlike you three."
        chidori "That and a couple of other people I know are demons..."
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2                
        kristik "Uhhh... ok then."
        hide schi0101
        show schi0102:
            xpos -10
            zoom 1.2     
        chidori "Now you all get going."
        hide schi0102
        show schi0101:
            xpos -10
            zoom 1.2
        hide syuz0101
        transform moveCompleteLeft:
            xpos 300
            zoom 1.2
            ease 0.5 xpos 1280
        show syuz0108:
            xpos 300
            zoom 1.2
        yuzuriha "Yeah! Okay then. Now let's goooooooo!! (dababy)"
        hide syuz0108
        show syuz0108 at moveCompleteLeft
        $ renpy.pause(1,hard=True)
        kristik "Looks like she's really excited about this..."
        hide syuz0108
        transform moveCompleteLeft2:
            xpos 700
            zoom 1.2
            ease 0.5 xpos 1280
        nerine "Well, I'll also get going. We will meet you later."
        kristik "K."
        stop music fadeout 2.0
        hide sner0103                
        show sner0103 at moveCompleteLeft2
        $renpy.pause(1,hard=True)
        hide sner0103
        transform moveFmLeft2Center:
            xpos -10
            zoom 1.2
            ease 0.5 xpos 300
        hide schi0101
        show schi0101 at moveFmLeft2Center
        play music "audio/Sabona Witch OST - Yasashii Kaze-128k.ogg"
        $renpy.pause(1,hard=True)
        kristik "..."
        $ show_quick_menu = False
        window hide           
        menu:
            "''I want you to come!''":
                $ show_quick_menu = True
                window show            
                $ EXPchidori += 1
                kristik "I want you to come!"
                hide schi0101
                show schi0102:
                    xpos 300
                    zoom 1.2
                chidori "Like I've said, I'm unable to fight anything."
                hide schi0102
                show schi0101:
                    xpos 300
                    zoom 1.2
                kristik "That doesn't matter."
                kristik "If anything, I'll just feel more alone without you."
                hide schi0101
                show schi0111:
                    xpos 300
                    zoom 1.2
                chidori "..."
                hide schi0111
                show schi0208:
                    xpos 300
                    zoom 1.2
                chidori "....."
                hide schi0208
                show schi0311:
                    xpos 300
                    zoom 1.2
                chidori "...is that true?"
                kristik "Yeah."
                hide schi0311
                show schi0312:
                    xpos 300
                    zoom 1.2
                chidori "........"
                hide schi0312
                show schi0104:
                    xpos 300
                    zoom 1.2
                chidori "Well.. that's good to hear..."
                hide schi0104 
                show schi0103:
                    xpos 300
                    zoom 1.2
                kristik "Yeah...."
                hide schi0103
                show schi0317:
                    xpos 300
                    zoom 1.2
                chidori "..."
                kristik "..."
                hide schi0317
                show schi0110:
                    xpos 300
                    zoom 1.2
                chidori "........"
                hide schi0110
                show schi0114:
                    xpos 300
                    zoom 1.2
                chidori "Well, I'm going to get going."
                chidori "Thanks."
                hide schi0114
                show schi0203:
                    xpos 300
                    zoom 1.2
                $ renpy.pause(1,hard=True)
                hide schi0203
                with dissolve
                kristik "..."
                kristik "Well, I should definitely start going..."
                stop music fadeout 2.0
                $ show_quick_menu = False
                window hide
                hide suburb_konbiniext
                with dissolve
                $ renpy.pause(2, hard=True)

                show white_base
                with dissolve
                show next_base
                show transition6
                with blinds
                $ renpy.pause(5, hard=True)  
                hide white_base
                hide next_base
                hide transition6
                with blinds
                $ renpy.pause(1, hard=True) 


                jump chapterfour                        
            "Leave the area and go to the hotel":
                $ show_quick_menu = True
                window show            
                kristik "Alright. Well I'll be going then too."
                hide schi0101
                show schi0102:
                    xpos 300
                    zoom 1.2
                chidori "Ok."
                hide schi0102
                show schi0101:
                    xpos 300
                    zoom 1.2
                $ renpy.pause(1,hard=True)
                hide schi0101
                with dissolve
                stop music fadeout 2.0
                $ show_quick_menu = False
                window hide
                hide suburb_konbiniext
                with dissolve
                $ renpy.pause(2, hard=True)

                show white_base
                with dissolve
                show next_base
                show transition7
                with blinds
                $ renpy.pause(5, hard=True)  
                hide white_base
                hide next_base
                hide transition7
                with blinds
                $ renpy.pause(1, hard=True) 

                jump chapterfour     

    elif EXPsuou >= 5:
        stop music 
        play music "audio/Sabona Witch OST - Chotto Ennui-128k.ogg"
        $show_quick_menu = True
        window show
        with dissolve 
        show city_street3_ni  
        with dissolve 
        kristik "Damn... it's fuckin cold...."
        kristik "Not only did fuckin Kyle leave me, he didn't even tell me what hotel we are even staying at..."
        kristik "Bastard bitch ass..."
        show ssuo0101c:
            xpos 400
            zoom 1.2
        with dissolve
        kristik "...?"
        suou "...."
        hide ssuo0101c
        show ssuo0124c:
            xpos 400
            zoom 1.2
        suou "Kristik??"
        hide ssuo0124c
        show ssuo0103c:
            xpos 400
            zoom 1.2
        suou "What are you doing here?"
        kristik "My fuckin friend left me and I have no idea where they are right now..."
        hide ssuo0103c
        show ssuo0105c:
            xpos 400
            zoom 1.2
        suou "Oh...."
        suou "Then how about you come to my place?"
        hide ssuo0105c
        show ssuo0103c:
            xpos 400
            zoom 1.2   
        kristik "WUTT????"
        kristik "RLLY??"
        hide ssuo0103c
        show ssuo0105c:
            xpos 400
            zoom 1.2
        suou "Yeah..."
        $ show_quick_menu = False
        window hide
        menu:
            "''HELL YEAH!!!! LESSS GOOOOO (dababy)''":
                $ show_quick_menu = True
                window show            
                $ EXPsuou += 1
                kristik "HELL YEAH!!!! LESSS GOOOOO (dababy)"
                kristik "Where yo crib at shawty?"
                hide ssuo0105c
                show ssuo0103c:
                    xpos 400
                    zoom 1.2
                suou "You already know where it is..."
                kristik "Oh yeah you right"
                kristik "thats word right there"
                suou "???"  
                hide ssuo0103c
                show ssuo0105c:
                    xpos 400
                    zoom 1.2            
                suou "Just follow me..."  
                kristik "YES MY QUEEN!!!"
                suou "..."
                hide ssuo0105c
                with dissolve
                $ renpy.pause(1, hard=True)
                hide city_street3_ni
                window hide
                stop music fadeout 2.0
                $ show_quick_menu = False
                with dissolve
                $ renpy.pause(2,hard=True)   
                jump yesHouse         
            "''I'm sorry madame, I cannot accept such an offer''":
                $ show_quick_menu = True
                window show
                kristik "I'm sorry madame, I cannot accept such an offer...."  
                suou "oh..."           
                hide ssuo0105c
                show ssuo0103c:
                    xpos 400
                    zoom 1.2
                suou "Are you sure...?"
                kristik "UHHHMMMM..."
                $ show_quick_menu = False
                window hide               
                menu:
                    "''NAH BRO NVM IM DIVIN IN!!!!!''":
                        $ show_quick_menu = True
                        window show                    
                        $ EXPsuou += 1
                        kristik "NAH BRO NVM IM DIVIN IN!!!!!"
                        kristik "WE GON GET IT LITTY TITTY TONIGHT!!!"
                        suou "???"  
                        hide ssuo0103c
                        show ssuo0105c:
                            xpos 400
                            zoom 1.2            
                        suou "Just follow me..."  
                        kristik "YES MY QUEEN!!!"
                        suou "..."
                        hide ssuo0105c
                        with dissolve
                        $ renpy.pause(1, hard=True)
                        hide city_street3_ni
                        window hide
                        $ show_quick_menu = False
                        stop music fadeout 2.0
                        with dissolve
                        $ renpy.pause(2,hard=True)   
                        jump yesHouse                           
                    "''Yes I'm sure. Thank you for the offer.''":
                        $ show_quick_menu = True
                        window show                    
                        kristik "Yes I'm sure. Thank you for the offer."
                        suou "..."
                        hide ssuo0103c
                        show ssuo0106c:
                            xpos 400
                            zoom 1.2
                        suou "Are you telling the truth?"
                        kristik "uhhhh..... yes?"
                        hide ssuo0106c
                        show ssuo0105c:
                            xpos 400
                            zoom 1.2 
                        suou "I see..."
                        hide ssuo0105c
                        show ssuo0103c:
                            xpos 400
                            zoom 1.2           
                        suou "Are you sure you're sure though?"
                        kristikmind "{i}Fuck bro don't tempt me like this..."
                        kristik "...Now I'm not so sure..."      
                        suou "Then just come with me."
                        $ EXPsuou += 1
                        kristik "Ok..."
                        hide ssuo0103c
                        with dissolve
                        $ renpy.pause(1, hard=True)
                        hide city_street3_ni
                        window hide
                        stop music fadeout 2.0
                        $ show_quick_menu = False
                        with dissolve
                        $ renpy.pause(2,hard=True)   
                        jump yesHouse   
        label yesHouse:
            play music "audio/Sabona Witch OST - Yasashii Kaze-128k.ogg" fadeout 2.0
            $show_quick_menu = True
            window show
            with dissolve 
            show house_interior1  
            with dissolve             
            show ssuo0103:
                xpos 400
                zoom 1.2       
            with dissolve     
            suou "We're here..." 
            kristikmind "{i}Sheeshhhhh.... not bad"
            kristikmind "{i}Could be a bit more minimalistic but way better than my clay village back in Fiji..."
            hide ssuo0103
            show ssuo0105:
                xpos 400
                zoom 1.2
            suou "Let me take a shower and get changed first..."
            kristik "uhh... ok.."
            hide ssuo0105
            with dissolve
            play sound "audio/shower.ogg" loop
            kristik "Nothing much to do...."
            kristik "I wonder if that thing that Chidori said about busting a nut is true..."
            kristik "Wait why am I think about busting a nut in a girl's house??!?"
            kristik "Damn wait a minute... she taking a shower rn???"
            kristik "Ahh wait cmon bro"
            kristik "Get them horni ass thoughts out your head"
            kristik "..."
            kristik "Fuck..."
            kristik "Do she got a big dumpy???"
            kristik "AHHHH!! FUCK NO!"
            kristik "Maybe she smell nice?"
            kristik "..."
            kristik "tf is wrong with me?"
            kristik "Why can't I just think about normal shit?"
            kristik "Ok... maybe... TEKKEN! YES!!"
            kristik "..."            
            kristik "Chun Li got a big ass..."
            kristik "...."
            kristik "AHHHH FUCK!!!!"
            kristik "Ok hold on... think about guys then..."
            kristik "gay shit is weird, so maybe if i think about guys then it'll stop..."
            kristik "..."
            stop sound fadeout 2.0
            kristik "how big is jason's dick...?"
            kristik "..."            
            kristik "FUUUUCK!!"
            kristik "HOW DID I MANAGE TO THINK ABOUT DICK?!?"
            show ssuo0610:
                xpos 400
                zoom 1.2
            with dissolve
            suou "..."
            kristik "0_0"
            kristik "HOLD UP..."
            hide ssuo0610
            show ssuo0609:
                xpos 400
                zoom 1.2
            ############################################
            #               PLAY NEXT EPISODE SAN HOLO REMIX
            ############################################
            kristik "(ring ding ding ding ding ding ding ding)"

            suou "????"
            kristik "Sorry, it just came out like that"
            suou "Let's go to my bedroom."
            kristik "Uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
            kristik "u serious?"
            suou "Yes."
            hide suou0609
            hide house_interior1
            show LA_Penthouse_Bedroom
            with dissolve
            $ renpy.pause(1, hard=True)
            kristik "Damn... nice bedroom too."
            show ssuo0608:
                xpos 400
                zoom 1.2
            with dissolve
            suou "Kristik..."
            kristik "(gulp)"
            kristikmind "{i} is this the moment? The time where we both pass through the gates of adulthood?????!!!!"
            suou "...hungry"
            kristik "Huh?"
            hide ssuo0608
            show ssuo0610:
                xpos 400
                zoom 1.2
            suou "I'm hungry...."
            kristik "ur..... hungry????"
            suou "Yes...."
            kristik "HOw bout u hop in the kitchen and make sum sandwiches"
            hide ssuo0610
            show ssuo0608:
                xpos 400
                zoom 1.2                    
            suou "???"
            kristik "idk... thought that woulda been more funny."
            hide ssuo0608
            show ssuo0618:
                xpos 400
                zoom 1.2
            with Dissolve(3)                
            suou "ZZzzzzzzz...."
            kristik "What?????"
            kristik "She asleep that fast???"
            kristik "I wanted some sandwiches damnit..."
            suou "ZzZzZzZzzzzzz...."

            ######################################################################################################################################################
            ## PUT DOOR RING SOUND
            ######################################################################################################################################################
            play sound "audio/ringdoorbell.ogg"
            $ renpy.pause(2,hard=True)
            kristik "Huh?"
            kristik "Who the hell is at the door at this hour?"
            hide LA_Penthouse_Bedroom
            show shizu_houseext_ni
            with dissolve
            $ renpy.pause(1, hard=True)
            kristik "Uhhh.. Hello?"
            stop music fadeout 2.0
            show srik0201c:
                xpos 100
                zoom 1.2
            show srin0106c:
                xpos 600
                zoom 1.2
            with dissolve
            unknown "...."
            kristik "...?"
            hide srik0201c
            show srik0207c:
                xpos 100
                zoom 1.2
            show srin0106c:
                xpos 600
                zoom 1.2
            unknown "Where is Suou?"
            hide srik0207c
            show srik0208c:
                xpos 100
                zoom 1.2
            kristik "uhhh.. who are you?"    
            $ EXPringo += 1
            $ EXPrikka += 1
            hide srik0208c
            show srik0711c:
                xpos 100
                zoom 1.2
            with dissolve
            $ renpy.pause(1,hard=True)
            hide srik0711c
            show srik0113c:
                xpos 100
                zoom 1.2
            with dissolve
            $ renpy.pause(1,hard=True)
            hide srik0113c
            show srik0201c:
                xpos 100
                zoom 1.2
            with dissolve
            play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg" fadein 2.0
            unknown "Look, I have no idea who YOU are but I know for a fact that Suou lives here."
            kristik "Well she's asleep..."
            hide srin0106c
            show srin0201c:
                xpos 600
                zoom 1.2
            unknown "I don't really believe you..."
            kristik "Well... then you can just come inside and look for yourself."
            hide srik0201c
            hide srin0201c
            hide shizu_houseext_ni
            show house_interior1
            with dissolve
            $ renpy.pause(2,hard=True)
            hide house_interior1
            show LA_Penthouse_Bedroom
            hide ssuo0618
            show ssuo0618:
                xpos 400
                zoom 1.2                      
            with dissolve                  
            $ renpy.pause(2,hard=True)
            suou "ZzzZZzzzz..."
            hide ssuo0618
            hide LA_Penthouse_Bedroom
            show house_interior1
            show srik0208:
                xpos 100
                zoom 1.2
            show srin0106:
                xpos 600
                zoom 1.2
            with dissolve
            kristik "See? I told you."
            kristik "I didn't do no funny bidness yknowwhatimsayin"
            hide srik0208
            show srik0207:
                xpos 100
                zoom 1.2
            unknown "It's hard to believe a person who looks like a beanbag!"
            kristikmind "{i}tf is up with people calling me a beanbag??"
            hide srin0106
            show srin0105:
                xpos 600
                zoom 1.2
            unknown "Yeah... and you have a boner right now too."
            kristik "!!!!"
            hide srik0207
            show srik0208:
                xpos 100
                zoom 1.2
            hide srin0105
            show srin0104:
                xpos 600
                zoom 1.2                    
            stop music fadeout 1.0
            kristikmind "{i}FUCK I FORGOT I GOT A BONER WHEN SUOU TOLD ME TO GO INTO THE BEDROOM!!"
            hide srik0208
            show srik0117:
                xpos 100
                zoom 1.2
            play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
            unknown "EEEWWWWWW!!!"
            hide srik0117
            show srik0108:
                xpos 100
                zoom 1.2
            unknown "SO YOU DID DO SOMETHING TO HER!!!"
            hide srik0108
            show srik0109:
                xpos 100
                zoom 1.2
            kristik "NONONOO!!!! ITS JUST UH...."
            hide srik0109
            show srik0207:
                xpos 100
                zoom 1.2
            unknown "Hey, Ringo we got a pervert on our hands too!"
            hide srin0104
            show srin0105:
                xpos 600
                zoom 1.2
            hide srik0207
            show srik0208:
                xpos 100
                zoom 1.2
            ringo "Yeah Rikka, this kid is both fat and weird..."
            hide srin0105
            show srin0104:
                xpos 600
                zoom 1.2
            kristikmind "{i}Bruh these guys do not mince their words..."
            hide srik0208
            show srik0207:
                xpos 100
                zoom 1.2
            rikka "Hey! If you did anything funny to Suou and she tells us later, you're in big trouble mister!"
            hide srik0207
            show srik0208:
                xpos 100
                zoom 1.2
            kristik "Like i said, I DIDNT DO JACK SHIT!!!"
            hide srik0208
            show srik0108:
                xpos 100
                zoom 1.2
            rikka "It doesn't matter now! Get out of here!"
            hide srik0108
            show srik0109:
                xpos 100
                zoom 1.2
            kristik "WAIT WHY??? LIKE I SAID I DIDNT DO ANYTHING!!!"
            hide srik0109
            show srik0108:
                xpos 100
                zoom 1.2
            rikka "You're lying! Just get out of here or I'm calling the police!"
            hide srik0108
            hide ssuo0608
            hide ssuo0609
            hide srin0104
            window hide
            hide house_interior1                
            $ show_quick_menu = False
            with dissolve
            $ renpy.pause(1,hard=True)
            show shizu_houseext_ni
            window show
            $ show_quick_menu = True
            with dissolve
            $ renpy.pause(2,hard=True)

            kristik "wtf???"
            kristik "Why the hell did I get kicked out??!!"

            rikka "{i}Suou!! Wake up!!"
            suou "{i}zzZZ.... H-huh??"
            ringo "{i}Yeah! This weird indian kid was in your house!"
            suou "{i}W... what??"
            rikka "{i}Yeah! We kicked him out though!"
            kristik "SIGH...."
            kristik "I'll just leave them be then..."
            stop music fadeout 2.0
            hide shizu_houseext_ni
            window hide
            $ show_quick_menu = False
            with dissolve
            $ renpy.pause(4,hard=True)

            show white_base
            with dissolve
            show next_base
            show transition8
            with blinds
            $ renpy.pause(5, hard=True)  
            hide white_base
            hide next_base
            hide transition8
            with blinds
            $ renpy.pause(1, hard=True) 

            jump chapterfour

    else:
        $show_quick_menu = True
        window show
        with dissolve 
        show suburb_park 
        with dissolve 
        play music "audio/Sanoba Witch OST - Asa no Youki-320k.ogg"
        kristik "..."
        kristik "Kevin and Jason were both getting annoyed about my horny thoughts..."
        kristik "they told me to touch some grass... so I guess i'll better be doing that..."
        show seri0202:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve
        unknown "..."
        kristikmind "{i}wheelchair girl???"
        $ EXPerika += 1
        hide seri0202
        show seri0211:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve
        $ renpy.pause(1.4,hard=True)
        kristikmind "{i}a bit tomboyish... but not bad i guess..."
        stop music fadeout 2.0
        $ renpy.pause(2,hard=True)
        hide seri0211
        show seri0119:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "I know you're staring at me."
        hide seri0119
        show seri0111:
            xpos 100
            ypos -60
            zoom 1.1
        play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
        kristikmind "{i}Fuck..."
        kristikmind "{i}I better make a cover-up story..."
        kristik "Huh...? Oh, I didn't see you there."
        hide seri0111
        show seri0119:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "I'm not stupid bro. I can tell you were probably ogling at me."
        hide seri0119
        show seri0109:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "I may be in a wheelchair.. but I can get freaky deaky too ;)))))"
        kristik "Hold up... actually?"
        hide seri0109
        show seri0108:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "Hahahahaha!"
        hide seri0108
        show seri0113:
            xpos 100
            ypos -60
            zoom 1.1
        stop music fadeout 1.0
        play music "audio/Sabona Witch OST - Yasashii Kaze-128k.ogg" fadein 1.0
        unknown "Of course not..."
        kristikmind "{i} OOOOOF"
        kristikmind "{i} If I were her I woulda ended it all by that point..."
        hide seri0113
        show seri0210:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "I myself am not very sociable..."
        hide seri0210
        show seri0211:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "Most people are overly sensitive around me... it doesn't even feel like they treat me like a normal person..."
        hide seri0211
        show seri0202:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "Well... I guess with the condition I have I wouldn't be considered a ''normal'' person anyways..."
        hide seri0202
        show seri0203:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "What condition do you even got?"
        hide seri0203
        show seri0120:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve
        $ renpy.pause(1,hard=True)
        unknown "..."
        hide seri0120
        show seri0112:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "I was originally diagnosed with Pneumonoultramicroscopicsilicovolcanoconiosis and the doctors administered Dimethylamidophenyldimethylpyrazolone and performed various Hepaticocholangiocholecystenterostomies"
        hide seri0112
        show seri0111:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "..."
        kristik "wtf..."
        hide seri0111
        show seri0112:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "They then did a Esophagogastroduodenoscopy procedure... but one of the senior doctors had Hippopomonstrosesquipedalophobia and broke his nose, so they had to roll him out and perform a Uvulopalatopharyngoplasty."
        hide seri0112
        show seri0113:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "One cousin of mine had Pseudopseudohypoparathyroidism, so they thought there could be a link."
        hide seri0113
        show seri0112:
            xpos 100
            ypos -60
            zoom 1.1        
        unknown "Luckily, I was never found to have that condition."
        hide seri0112
        show seri0111:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "umm...."
        kristik "None of that shit was made up?"
        hide seri0111
        show seri0210:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "I wish that was the case..."
        kristik "Damn..."
        kristik "Now I feel kinda bad thinking if you thicc or not after you told me about your daijidasjklrwsejtajkserikosgopdogsnin condition or whatever it was..."
        hide seri0210
        show seri0119:
            xpos 100
            ypos -60
            zoom 1.1
        stop music
        unknown "So you were thinking about that!"
        hide seri0119
        show seri0108:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "H-Huh?? Yeah...?"
        hide seri0108
        show seri0106:
            xpos 100
            ypos -60
            zoom 1.1
        play music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k intro.ogg"
        queue music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k.ogg"
        unknown "I just said all that so I could bait you!"
        hide seri0106
        show seri0110:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "So you were a pervert..."
        hide seri0110
        show seri0108:
            xpos 100
            ypos -60
            zoom 1.1
        kristikmind "{i}bruh fuck... I just be taking Ls this whole week..."
        hide seri0108
        show seri0104:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "Soooo is what you said about getting freaky the truth or...?"
        hide seri0104
        show seri0119:
            xpos 100
            ypos -60
            zoom 1.1
        unknown "You're really gonna ask me that kind of question?"
        hide seri0119
        show seri0116:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "Well... I mean you kinda brought it up yourself..."
        hide seri0116
        show seri0119:
            xpos 100
            ypos -60
            zoom 1.1 
        unknown "So now you're blaming me even though I'm disabled and a girl? SMFH men these days...."       
        hide seri0119
        show seri0116:
            xpos 100
            ypos -60
            zoom 1.1
        kristikmind "{i}dis bitch really acting entitled even doe she in a wheelchair??"
        $ show_quick_menu = False
        window hide
        menu:
            "''Listen here bitch IDGAF if u got syphilis you gotta treat me wit sum RESPECC like the MAN I AM'' (playa shit)":
                $ show_quick_menu = True
                window show            
                $ EXPerika += 1
                kristik "Listen here bitch IDGAF if u got syphilis you gotta treat me wit sum RESPECC like the MAN I AM"
                hide seri0116
                show seri0119:
                    xpos 100
                    ypos -60
                    zoom 1.1   
                unknown "Wow, so now you call girls names like that?"
                hide seri0116
                show seri0119:
                    xpos 100
                    ypos -60
                    zoom 1.1        
                kristik "Its cuz im a pimp, i be fly out here and i dont need no bitches like u"
                hide seri0119
                show seri0107:
                    xpos 100
                    ypos -60
                    zoom 1.1   
                with dissolve
                $ renpy.pause(1,hard=True)    
                unknown "Pfff...."
                kristik "?"
                hide seri0107
                show seri0108:
                    xpos 100
                    ypos -60
                    zoom 1.1  
                unknown "HAHAHAHAAHAHAHAHAHA"
                kristik "???"    
                hide seri0108
                show seri0106:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "If u such a pimp... what's the hardest drug u ever took?"
                hide seri0106
                show seri0110:
                    xpos 100
                    ypos -60
                    zoom 1.1
                kristik "MaaAAAAaaaan, u dont even wanna know"
                hide seri0110
                show seri0106:
                    xpos 100
                    ypos -60
                    zoom 1.1  
                unknown "Oh trust me, I'm soOoOOoOo interested... KEKEKEKEKE"
                hide seri0106
                show seri0110:
                    xpos 100
                    ypos -60
                    zoom 1.1
                kristik "Bro I took some hard flinstones vitamin gummies yesterday"
                kristik "i ate 3 of em... when they only recommend TWO!!!" 
                kristik "i was litty like a candle and fly like an ostrich broooo"
                hide seri0110
                show seri0112:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "Wow... I'm impressed."
                unknown "That shit goes super hard bro"
                hide seri0112
                show seri0111:
                    xpos 100
                    ypos -60
                    zoom 1.1
                kristik "Yeh... I know.. I'm basically Walter White at this point with the amount of gummies i be producing"
                unknown "Yeah... shit is super hard..."
                hide seri0111
                show seri0106:
                    xpos 100
                    ypos -60
                    zoom 1.1 
                unknown "HARD FOR A 4 YEAR OLD LOLOLLOLLOLOLLLOLOL!!!!"
                hide seri0106
                show seri0108:
                    xpos 100
                    ypos -60
                    zoom 1.1
                kristikmind "{i} is she rlly dissing my flinstones gummies??"
                kristikmind "{i}I wasn't lying when I said i took 3 instead of 2...."
                jump nextnext
                
            "''I'm very sorry that I hurt your feelings ma'dame, I promise I will do no such thing ever again'' (simp shit)":
                $ show_quick_menu = True
                window show            
                $ EXPerika += 2
                kristik "I'm very sorry that I hurt your feelings ma'dame, I promise I will do no such thing ever again"
                kristik "For I am a respectable man who shall do no harm to the opposite sex, and nullify all prejudices that may be present due to this gender equality."
                kristik "Please accept my apology."
                hide seri0116
                show seri0212:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "Wow..."
                hide seri0212
                show seri0209:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "You know how to use your words..."
                kristikmind "{i}Lessss GOOOO!!!! (dababy)"
                kristikmind "{i}My coochie grabbing skills is off the CHARTS!!!"
                hide seri0209
                show seri0114:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "You really do know how to sway a girl's mind..."
                hide seri0114
                show seri0119:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "...Is what you wished I said."
                hide seri0119
                show seri0111:
                    xpos 100
                    ypos -60
                    zoom 1.1
                kristik "wait... wut???"
                hide seri0111
                show seri0108:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "HAHAHAHAHAAHAHAHAH!!!"
                hide seri0108
                show seri0106:
                    xpos 100
                    ypos -60
                    zoom 1.1
                unknown "''Ma'dame''?? LOLOLLOLLLLOLO"
                unknown "What are you? A British man from 1736??? LMFAOAOAOOAOAOAOAO!!!!"
                hide seri0106
                show seri0108:
                    xpos 100
                    ypos -60
                    zoom 1.1                
                kristik "..."
                kristikmind "{i}this fuckin girl and her trolling..."
                jump nextnext
    label nextnext:
        transform moveleftfromcenter1:
            xpos 100
            ypos -60
            zoom 1.1
            ease 0.5 xpos -120 ypos -60 zoom 1.1
        hide seri0108
        show seri0104 at moveleftfromcenter1
        show schi0101:
            xpos 600
            zoom 1.2
        with dissolve
        hide schi0101
        show schi0102:
            xpos 600
            zoom 1.2
        chidori "Hey, Erika and Kristik."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "Uhhh... Chidori tf are you doin here?"
        kristik "And ur name is erika?"
        hide seri0104
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Yeah that's my name. You like it?"
        hide seri0106
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "Uhh... it's a good name ig..."
        kristik "But what are you doing here Chidori?"
        hide schi0101
        show schi0102:  
            xpos 600
            zoom 1.2
        chidori "This is actually a favorable situation. I was supposed to introduce her to you but it looks like you guys are already well acquainted."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "I wouldn't really say that though..."
        hide schi0101
        show schi0102:
            xpos 600
            zoom 1.2
        chidori "Much how like you area demon, Erika here is also a demon too."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "Seriously???"
        kristik "This girl in a wheelchair who probably can't even go up some set of stairs is a demon too?"
        hide seri0104
        show seri0119:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Wow. That was such a cheap shot."
        hide seri0119
        show seri0120:
            xpos -120
            ypos -60
            zoom 1.1
        erika "I'll have you know I'm probably more powerful than you could ever be!"
        hide seri0120
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "Damn bruh you off the charts with the amount of cap you told me today"
        hide schi0101
        show schi0102:
            xpos 600
            zoom 1.2
        chidori "It's not a lie."
        chidori "Erika graduated top of her class in the Navy Seals, and she's been involved in numerous secret raids on Al-Quaeda, and she has over 300 confirmed kills."
        chidori "She is trained in guerrilla warfare and is the top sniper in the entire US armed forces."
        chidori "You are nothing to her but just another target. She will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "Did u really just make a NAVY SEALs copypasta joke to me???"
        hide schi0101
        show schi0102:
            xpos 600
            zoom 1.2
        chidori "I thought it would have been funny due to your dry humour."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "To be fair it was kinda funny... but YOU'RE the one with a dry sense of humour"
        hide seri0104
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1
        erika "So what do you need Chidori?"
        erika "Is this in regards to what you talked about yesterday?"
        hide seri0106
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        hide schi0101
        show schi0102:  
            xpos 600
            zoom 1.2
        chidori "Yes."
        chidori "I've commissioned both of you to fight the ASIANBOYZ."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "The.. who now?"
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        chidori "Your former friends, Aaron and Wesley. The ones that decided to steal your military assets and form the ASIANBOYZ."
        kristikmind "{i}''ASIANBOYZ''??? That's such a gay ass name...."
        hide schi0101
        show schi0102:
            xpos 600
            zoom 1.2
        chidori "I've already informed your other friends that Erika will be joining you guys. There may be some others who join with you two later down the line."
        hide schi0102
        show schi0101:
            xpos 600
            zoom 1.2
        kristik "Damn... ok... I didn't expect you to be this involved."
        hide seri0104
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Well that's just Chidori for you."
        erika "She likes to stick her nose into things where they shouldn't be stuck into!"
        hide seri0106
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        hide schi0101
        show schi0106:
            xpos 600
            zoom 1.2
        chidori "What's that supposed to mean???"
        hide schi0106
        show schi0105:
            xpos 600
            zoom 1.2
        hide seri0104
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Well remember that time when you tried to find my tampons--"
        hide seri0106
        show seri0104:  
            xpos -120
            ypos -60
            zoom 1.1
        hide schi0105
        show schi0106:
            xpos 600
            zoom 1.2
        chidori "Nobody asked you to bring that up!"
        hide schi0106
        show schi0105:
            xpos 600
            zoom 1.2
        hide seri0104
        show seri0108:
            xpos -120
            ypos -60
            zoom 1.1
        kristikmind "{i} wut is a tampohn??? idk what that is but it sounds like some industrial machinery..."
        hide seri0108
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "Uhhh... what's this ''temp ohn?'' Is that like some kind of industrial equpiment?"
        hide seri0104
        show seri0103:
            xpos -120
            ypos -60
            zoom 1.1
        erika "You seriously don't know?!??!?!"
        hide seri0103
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "No... I've never heard of that thing before."
        hide seri0104
        show seri0108:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Stop the cap LMFAOOAOAOAOAOA there's no way you don't know what a tampon is"
        hide seri0108
        show seri0104:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "No I'm serious. I grew up in a conservative family so I was never taught anything outside of just studying and eating Indian food."
        hide seri0104
        show seri0112:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Wow... that's kinda sad."
        hide seri0112
        show seri0110:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Do you wanna see mine?"
        kristik "uhhhh.... i guess?"
        hide seri0110
        show seri0112:
            xpos -120
            ypos -60
            zoom 1.1
        erika "So you are telling the truth... I thought you were lying this whole time."
        hide seri0112
        show seri0111:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "HAHAHAHAHA STUPID BITCH OF COURSE I KNOW WHAT A TAMPON IS LOLOLOLOLOLO!!!!!"
        hide seri0111
        show seri0119:
            xpos -120
            ypos -60
            zoom 1.1
        with dissolve
        $ renpy.pause(1,hard=True)
        erika "...Do you really know what they are though?"
        hide seri0119
        show seri0111:
            xpos -120
            ypos -60
            zoom 1.1
        kristik "Ofc lmao, it's the thing that you put inside your peepee so that you don't get pregnant duh"
        erika "..."
        hide schi0105
        show schi0101:
            xpos 600
            zoom 1.2
        chidori "..."
        hide seri0111
        show seri0108:
            xpos -120
            ypos -60
            zoom 1.1
        erika "HAHAAHYAHAHAH LMFAOFOAOAO OA OLOOLOLLLL!!!!!"
        hide seri0108
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1
        erika "THAT'S CONTRACEPTION NOT A TAMPON LMAO!O!!!!!!!"
        hide seri0106
        show seri0108:
            xpos -120
            ypos -60
            zoom 1.1     
        kristikmind "{i}Fuck! I always get them confused!"
        kristikmind "{i}Damnit! My attempt to troll this wheelchair bitch failed so hard!!!"
        hide seri0108
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1
        erika "Well, you're kinda funny Krabby Patty Ling Ling Bartholomew the Third"
        hide seri0106
        show seri0107:
            xpos -120
            ypos -60
            zoom 1.1                
        kristikmind "{i}wtf did she just call me???"
        hide seri0107
        show seri0106:
            xpos -120
            ypos -60
            zoom 1.1   
        erika "Me and Chidori need to go right now, so I guess I'll see you later beanbag!"
        hide seri0106
        hide schi0101
        with dissolve
        $ renpy.pause(1,hard=True)
        kristikmind "{i}Did that bitch really just call me a beanbag???"           
        stop music fadeout 2.0  
        show kyle (5):
            xpos 700
            ypos 20
            zoom 0.6
        show jason (11):
            xpos 400
            ypos 20
            zoom 0.6
        show kevin (16):
            xpos 0
            zoom 0.6
        with dissolve
        $ renpy.pause(1,hard=True)
        kristik "Yoooo!! What's up guys!!!!!"
        hide jason (11)
        show jason (89):
            xpos 400
            ypos 20
            zoom 0.6
        play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
        jason "Kristik... were you just talking to some bitches right now??"
        kristik "Uhhh... ummm..."
        hide kevin (16)
        show kevin (52):
            xpos 0
            zoom 0.6
        kevin "And you prioritizing these bitches over the boys??!?!?!?!?"
        kristik "UUHUHHHHHMMMM...."
        hide jason (89)
        show jason (11):
            xpos 400
            ypos 20
            zoom 0.6
        jason "Y'know what happens to people who prioritize bitches over the boys..."

        kristik "Uhhhmmm... BYE GUYS!!!"
        hide jason (11)
        hide kevin (52)
        hide kyle (5)
        with dissolve
        jason "WHERE YOU GOIN BITCH?!?!?"
        kristik "I gotta scram!"
        stop music fadeout 2.0
        hide suburb_park
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(4,hard=True)
        jump chapterfour


label chapterfour:
    if EXPerika >= 3:
        play music "audio/Sanoba Witch OST - School Dayz-(128kbps).ogg"
        $show_quick_menu = True
        window show
        with dissolve 
        show lilly_hilltop 
        with dissolve 
        kristik "Wow..."
        kristik "I guess touching grass really was a good option for me."
        kristik "I can see the world in a whole new perspective..."
        kristik "A whole new... vision..."
        unknown "{i}...well I guess the next step for you is to get some bitches"
        kristik "Huh...?"
        kristik "Who said dat???"
        show seri0110:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve
        erika "Heya! Did you miss me?"
        kristik "Bruhh..."
        kristik "How the fuck did you even wheel on up here?? Sorry to say but you gon need some actual FEET for this place."
        hide seri0110
        show seri0121:
            xpos 100
            ypos -60
            zoom 1.1
        erika "Wow... so mean... (cry cry cry)"
        kristik "Wait wait wait... uhhh i was only joking!!!!!"
        hide seri0121
        show seri0106:
            xpos 100
            ypos -60
            zoom 1.1
        erika "Yeah and I was joking too LOLOLOOLOLOLOLOL"
        hide seri0106
        show seri0109:
            xpos 100
            ypos -60
            zoom 1.1
        kristikmind "{i}bruh this mf...."
        hide seri0109
        with dissolve
        #################################################################
        #PLAY PHONE RING SOUND
        #################################################################
        play sound "audio/notification.mp3"
        $ renpy.pause(2,hard=True)
        chidori "{i}Hey Kristik."
        chidori "{i}Erika should be with you right now."
        kristikmind "{i}How tf she know that???"
        chidori "{i}Please get her and come to this location."
        kristikmind "{i}Uhhh.... ok..."
        show seri0109:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve
        kristik "Hey Erika, I need to take you somewhere."
        hide seri0109
        show seri0103:
            xpos 100
            ypos -60
            zoom 1.1
        erika "Huhhhhh???"
        hide seri0103
        show seri0114:
            xpos 100
            ypos -60
            zoom 1.1
        erika "You want to do it already?? Even though we just met??"
        kristik "-_-"
        hide seri0114
        show seri0111:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "Look I know its funny to troll me but this is more serious"
        hide seri0111
        show seri0113:
            xpos 100
            ypos -60
            zoom 1.1
        erika "Sorry...."
        hide seri0113
        show seri0120:
            xpos 100
            ypos -60
            zoom 1.1
        kristik "Shit... that's kinda cute tbh..."
        hide seri0120
        show seri0119:
            xpos 100
            ypos -60
            zoom 1.1
        erika "You said this was serious! And now you're calling me cute?!?!"
        hide seri0119
        show seri0111:
            xpos 100 
            ypos -60
            zoom 1.1
        kristik "OKOKOOK whatever we just need to go!"
        stop music fadeout 2.0
        hide seri0111
        hide lilly_hilltop
        with dissolve
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(2,hard=True)
        $show_quick_menu = True
        window show
        with dissolve 
        show shizu_fishing
        with dissolve
        play music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k intro.ogg"
        queue music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k.ogg"
        kristik "..."
        show schi0102:
            xpos -20
            zoom 1.2
        show sich0101:
            xpos 300
            zoom 1.2
        show smay0102:
            xpos 700
            zoom 1.2
        with dissolve
        chidori "You're finally here."  
        hide schi0102      
        show schi0101:
            xpos -20
            zoom 1.2
        kristik "Yeah... but who are they?"
        hide sich0101
        hide smay0102
        hide schi0101
        show seri0102:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve
        erika "They are all friends of mine. Chidori, Ichigo, and Mayuri."
        hide seri0102
        show seri0103:
            xpos 100
            ypos -60
            zoom 1.1
        hide seri0103
        with dissolve
        show schi0102:
            xpos -20
            zoom 1.2
        show sich0101:
            xpos 300
            zoom 1.2
        show smay0102:
            xpos 700
            zoom 1.2
        with dissolve
        chidori "I brought you two here to introduce these girls to Kristik."       
        hide schi0102
        show schi0101:
            xpos -20
            zoom 1.2
        hide sich0101
        show sich0102:
            xpos 300
            zoom 1.2
        ichigo "Is this fat indian kid really going to defeat ASIANBOYZ?"
        hide sich0102
        show sich0101:
            xpos 300
            zoom 1.2
        kristik "Who you callin fat? And yeah I can destroy ASIANBOYZ in one second with my skillz"
        hide sich0101
        show sich0102:
            xpos 300
            zoom 1.2
        ichigo "Oh really? With what skills?"
        hide sich0102
        show sich0101:
            xpos 300
            zoom 1.2
        kristik "I uhhh... got my BIG DICK!!!"
        ichigo "...."
        chidori "......"
        mayuri "........"
        hide sich0101
        hide smay0102
        hide schi0101
        show seri0102:
            xpos 100
            ypos -60
            zoom 1.1
        with dissolve      
        erika "... that's major cap bro"
        hide seri0102
        show seri0108:
            xpos 100
            ypos -60
            zoom 1.1
        erika "you indian anyways so that automatically isnt true LOLOLLOLOLOLOLOOOL"
        hide seri0108
        show seri0107:  
            xpos 100
            ypos -60
            zoom 1.1        
        kristikmind "{i}why this bitch talkin so much smack when she da one in a wheelchair?"
        hide seri0107
        with dissolve
        show schi0102:
            xpos -20
            zoom 1.2
        show sich0101:
            xpos 300
            zoom 1.2
        show smay0102:
            xpos 700
            zoom 1.2
        with dissolve  
        chidori "These two will also help you for fighting against the ASIANBOYZ."
        hide schi0102
        show schi0101:
            xpos -20
            zoom 1.2
        kristik "Just how much people is required to fight Aaron and Wesley??"
        kristik "They aren't even that strong"
        hide sich0101
        show sich0111:
            xpos 300
            zoom 1.2
        ichigo "They're stronger than you might think."
        hide sich0111
        show sich0108:
            xpos 300
            zoom 1.2
        ichigo "I thought you would have known that..."
        hide sich0108
        show sich0109:
            xpos 300
            zoom 1.2          
        kristik "Well I haven't seem them in a very long time..."
        kristik "Now that I think about it, they're the least present in this whole story..."
        hide schi0101
        show schi0102:
            xpos -20
            zoom 1.2
        chidori "Well, it doesn't matter right now."
        chidori "They're getting closer to accomplishing their goal. They need to be stopped now."
        hide schi0102
        show schi0101:
            xpos -20
            zoom 1.2
        hide sich0109
        hide smay0102
        hide schi0101
        with dissolve    
        stop music fadeout 2.0
        hide shizu_fishing
        with dissolve
        $ show_quick_menu = False
        window hide
        with dissolve
        $ renpy.pause(1,hard=True)
        window show
        $ show_quick_menu = True
        with dissolve
        narrator "..."
        narrator "......."
        $ renpy.pause(2,hard=True)
        show office
        with dissolve        
        play music "audio/jazznoir.ogg"
        $ renpy.pause(2,hard=True)        
        aaron "Wesley."
        aaron "We're nearly there."
        show wesley_1s:
            xpos 850
            ypos 80
            zoom 0.7
        show aaron_3s:
            xpos -90
            ypos 175
            zoom 0.65
        with dissolve
        wesley "What about Kristik?"
        hide aaron_3s
        show aaron_8s:
            ypos 175
            zoom 0.6
        aaron "Kristik doesn't matter. He may have 9 different girlfriends, but he won't beat us."
        wesley "Aren't most of them demons?"
        aaron "They are. But they're all relatively easy to kill."
        aaron "Since we stole all those bombs, we should be able to kill them with only one of them, maybe two at most."
        wesley "When are we striking?"
        hide aaron_8s
        show aaron_3s2:
            xpos -90
            ypos 175
            zoom 0.65
        with dissolve   
        play sound "audio/lightingciggie.ogg"
        ####################################################################################################################################################################################
        ## PLAY CIGARETTE LIGHTER SOUNDS
        ####################################################################################################################################################################################

        $ renpy.pause (3,hard=True)
        hide aaron_3s2
        show aaron_2s:
            ypos 175
            zoom 0.57
        with dissolve
        aaron "This damn lighter is out of fuel..."       
        aaron "We'll strike whenever we can." 
        hide aaron_2s
        show aaron_5s:
            ypos 175
            zoom 0.57
        aaron "I'm not really in the mood right now."   
        hide aaron_5s
        show aaron_2s:
            ypos 175
            zoom 0.57       
        wesley "Understood."
        hide aaron_2s
        show aaron_10s:
            ypos 180
            zoom 0.57 
        with dissolve                     
        aaron "Don't worry. When the time comes, they'll all be dead."       
        hide aaron_10s
        hide wesley_1s
        hide office
        stop music fadeout 2.0
        with dissolve
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(2,hard=True)
        $ EXPaaronwesley += 1
        jump chapterfive

    elif EXPchidori >= 5:
        $show_quick_menu = True
        window show
        with dissolve 
        play music "audio/Sanoba Witch OST - Dekiru-Kana_-128k.ogg"
        show shizu_park
        with dissolve
        kristik "Chidori told me to meet her here..."
        kristik "But where is she?"
        kristik "I've been standing here for 30 minutes!!"
        kristik "Maybe she baited me??"
        show schi0101:
            xpos 350
            zoom 1.2
        with dissolve
        $ renpy.pause(1,hard=True)
        hide schi0101
        show schi0102:
            xpos 350
            zoom 1.2
        chidori "Hey."
        hide schi0102
        show schi0101:
            xpos 350
            zoom 1.2
        kristik "Hey. Is there someone that you're gonna introduce?"
        hide schi0101
        show schi0311:
            xpos 350
            zoom 1.2
        with dissolve
        chidori "No..."
        hide schi0311
        show schi0316:
            xpos 350
            zoom 1.2
        chidori "I just wanted to see you..."
        kristik "Uhhh.... really?"
        hide schi0316
        show schi0208:
            xpos 350
            zoom 1.2
        chidori "Why do you sound disappointed...?"
        kristik "Ummm... I'm not disappointed..."

        # To be honest, the part below was pretty cringe to type.
        $ EXPchidori += 2
        kristik "I'm actually pretty happy right now"
        hide schi0208
        show schi0114:
            xpos 350
            zoom 1.2
        chidori "...Really?"
        hide schi0114
        show schi0203:
            xpos 350
            zoom 1.2
        kristik "Yeah."
        hide schi0203
        show schi0110:
            xpos 350
            zoom 1.2
        chidori "..."
        hide schi0110
        show schi0311:
            xpos 350
            zoom 1.2
        chidori "Then... do you want to go to my house?"
        kristik "Uhhh... what???"
        kristikmind "{i}how did it go to ''im happy'' to ''do yo uwant to fuck''??"
        kristikmind "{i}Nah wait, lets not get ahead of ourselves. she never said if she wanted to fuck..."
        hide schi0311
        show schi0310:
            xpos 350
            zoom 1.2
        kristik "Uhhh.. sure why not."
        hide schi0310
        show schi0114:
            xpos 350
            zoom 1.2
        chidori "Really?"
        hide schi0114
        show schi0203:
            xpos 350
            zoom 1.2
        kristik "Yeah... sure..."
        hide schi0203
        show schi0114:
            xpos 350
            zoom 1.2        
        chidori "Alright! Follow me."
        stop music fadeout 2.0
        hide schi0114
        with dissolve
        hide shizu_park
        with dissolve
        $ show_quick_menu = False
        window hide
        with dissolve
        $ renpy.pause(1,hard=True)
        $ EXPaaronwesley += 1
        jump chapterfive

    elif EXPchidori == 4:
        $show_quick_menu = True
        window show
        with dissolve 
        play music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k intro.ogg"
        queue music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k.ogg"
        show city_street4 
        with dissolve
        show kyle (5):
            xpos 700
            ypos 20
            zoom 0.6
        show jason (9):
            xpos 400
            ypos 20
            zoom 0.6
        show kevin (16):
            xpos 0
            zoom 0.6
        with dissolve       
        kevin "So where are those two guys you want us to meet?"
        hide jason (9)
        show jason (10):
            xpos 400
            ypos 20
            zoom 0.6
        jason "Yeah, these guys are taking a while."
        hide jason (10)
        show jason (8): 
            xpos 400
            ypos 20
            zoom 0.6
        kristik "Um.. they're actually both girls..."
        kevin "..."
        hide jason (8)
        show jason (90):
            xpos 400
            ypos 20
            zoom 0.6
        jason "... really..?"
        jason "You mean to tell me..."
        hide jason (90)
        show jason (89):
            xpos 400
            ypos 20
            zoom 0.6        
        jason "You were gettin bitches before us??"
        kristik "HOW THE FUCK IS TALKING TO SOME GIRLS ''GETTIN BITCHES''??"
        hide jason(89)
        show jason (7):
            xpos 400
            ypos 20
            zoom 0.6
        $ renpy.music.set_pause(True, channel="music")
        jason "SHUT YO ASS UP HOW YOU GETTIN BITCHES THIS FAST??"
        $ renpy.music.set_pause(False, channel="music")
        yuzuriha "Hey~~!"
        kristikmind "{i} Shit..."
        hide jason (7)
        hide kyle (5)
        hide kevin (16)
        with dissolve
        show syuz0206:
            xpos 100
            zoom 1.2
        show sner0101:
            xpos 600
            zoom 1.2
        with dissolve
        yuzuriha "We're here! Sorry we're late."
        $ EXPyuzuriha += 1
        $ EXPnerine += 1
        hide syuz0206
        show syuz0102:
            xpos 100
            zoom 1.2
        yuzuriha "Are those your friends?"
        hide syuz0102
        show syuz0101:
            xpos 100
            zoom 1.2
        kristik "uhhh excuse me for a moment..."
        hide syuz0101
        hide sner0101
        with dissolve
        show kyle (5):
            xpos 700
            ypos 20
            zoom 0.6
        show jason (11):
            xpos 400
            ypos 20
            zoom 0.6
        show kevin (28):
            xpos 0
            zoom 0.6
        with dissolve    
        jason "Kristik... they don't look like no dudes"
        hide kevin (28)
        show kevin (52):
            xpos 0
            zoom 0.6
        kevin "YEH KRISTIK YOU PRIORITIZING COOCHIE OVER THE BOYS???"    
        kristik "Guys STFU!!!"
        kristik "Why yall actin so weird in front of them????"
        hide jason (11)
        show jason (90):
            xpos 400
            ypos 20
            zoom 0.6
        jason "Ohohoho.... so you're telling US to shut up?"
        hide jason (90)
        show jason (87):
            xpos 400
            ypos 20
            zoom 0.6
        jason "Kristik... you were like a brother to me..."
        hide jason (87)
        show jason (52):
            xpos 400
            ypos 20
            zoom 0.6
        jason "And now... you're backstabbing us with coochie?!?!?!?"
        hide kevin (52)
        show kevin (58):
            xpos 0
            zoom 0.6
        kevin "I always knew you were a simp..."
        yuzuriha "Uhhh.... Kristik?"
        hide kevin (58)
        hide jason (52)
        hide kyle (5)
        with dissolve
        show sner0107:
            xpos 600
            zoom 1.2
        show syuz0112:
            xpos 100
            zoom 1.2
        with dissolve
        yuzuriha "... the hell is wrong with those guys?"
        kristik "They're just uh... a little too... brotherly..."
        hide syuz0112
        hide sner0107
        with dissolve
        show jason (80):
            xpos 400
            ypos 20
            zoom 0.6
        show kevin (53):
            xpos 0
            zoom 0.6
        show kyle (5):
            xpos 700
            ypos 20
            zoom 0.6
        with dissolve
        jason "WHYYYYY KRISTIK?!?!! WHY DID YOU HAVE TO FALL BACK TO YOUR ANIMAL DESIRES?!?!?!?"
        kevin "this pain in my chest... it hurts...."
        kristik "bruh... tf is wrong with these guys..."
        kristik "Guys... first of all I'm not dating them."
        hide jason (80)
        show jason (83):
            xpos 400
            ypos 20
            zoom 0.6
        hide kevin (53)
        show kevin (16):
            xpos 0
            zoom 0.6
        kristik "And second of all, they are here to {i}HELP {/i} us not for them to fuck me or anything!!"
        kristik "Right guys???"
        hide kevin (16)
        hide jason (83)
        hide kyle (5)
        with dissolve
        show sner0207:
            xpos 600
            zoom 1.2
        show syuz0112:
            xpos 100
            zoom 1.2
        with dissolve 
        yuzuriha "Well, yeah you're right... but you didn't have to say it like that."
        hide sner0207
        show sner0104:
            xpos 600
            zoom 1.2
        nerine "Well... to hopefully dispel this confusion, let's introduce ourselves!"
        hide sner0104
        show sner0105:
            xpos 600
            zoom 1.2
        nerine "My name is Nerine. I'm half Japanese and half Italian. Nice to meet you!"
        hide sner0105
        show sner0103:
            xpos 600
            zoom 1.2
        hide syuz0112
        show syuz0102:
            xpos 100
            zoom 1.2
        yuzuriha "My name is Yuzuriha. I'm full japanese, I suppose."
        hide syuz0102
        show syuz0101:
            xpos 100
            zoom 1.2
        kristik "Yeah..."
        hide syuz0101
        hide sner0103
        with dissolve
        show jason (90):
            xpos 400
            ypos 20
            zoom 0.6
        show kevin (16):
            xpos 0
            zoom 0.6
        show kyle (5):
            xpos 700
            ypos 20
            zoom 0.6
        with dissolve        
        jason "Kristik..."
        kristik "Huh...?"
        jason "Where did you manage..."
        hide jason (90)
        show jason (7):
            xpos 400
            ypos 20
            zoom 0.6
        jason "TO SNAG THESE BEAUTIFUL WOMEN?!??"
        kristik "uhh......"
        hide jason (7)
        hide kevin (16)
        hide kyle (5)
        with dissolve
        show jason (12):
            xpos 100
            ypos 20
            zoom 0.6
        show syuz0101:
            xpos 600
            zoom 1.2
        with dissolve
        jason "Hey, madame."
        kristikmind "{i}Oh god...."
        hide jason (12)
        show jason (90):
            xpos 100
            ypos 20
            zoom 0.6
        jason "Are you perhaps, an exothermic reaction?"
        kristikmind "{i}wtf kind of pickup line is that???"
        hide jason (90)
        show jason (78):
            xpos 100
            ypos 20
            zoom 0.6
        jason "Cause according to the Second Law of Thermodynamics, you are supposed to share your hotness with me!!!"
        kristikmind "{i}that was so bad..."
        hide syuz0101
        show syuz0117:
            xpos 600
            zoom 1.2
        hide jason (78)
        show jason (79):
            xpos 100
            ypos 20
            zoom 0.6        
        yuzuriha "W-well... I..."
        kristikmind "{i}How the FUCK DID THAT WORK???"
        hide syuz0117
        show syuz0116:
            xpos 600
            zoom 1.2
        yuzuriha "Um... I..."
        hide jason (79)
        show jason (64):
            xpos 100
            ypos 20
            zoom 0.6  
        jason "No need to answer madame! For I already know the answer."
        hide syuz0116
        show syuz0109:
            xpos 600
            zoom 1.2
        yuzuriha "Hehehehe....."
        kristikmind "{i}What the fuck...."
        hide syuz0109
        hide jason (64)
        with dissolve
        show kevin (56):
            xpos 100
            zoom 0.6 
        show sner0101:
            xpos 600
            zoom 1.2
        with dissolve
        kyle "...And I made a game that earned 10,000 ROBUX! How crazy is that???!?!!"
        hide sner0101
        show sner0105:
            xpos 600
            zoom 1.2
        nerine "Wow! That's so cool!"
        hide sner0105
        show sner0103:
            xpos 600
            zoom 1.2
        hide kevin (56)
        show kevin (17):
            xpos 100
            zoom 0.6 
        kevin "heh... I know... I am considered a ''ROBLOX '' veteran after all."
        hide kevin (17)
        show kevin (20):
            xpos 100
            zoom 0.6
        kevin "Did you know... I've been on ROBLOX since the first Doomspire Brickbattle?!?!?!!"
        hide sner0103
        show sner0208:
            xpos 600
            zoom 1.2
        nerine "Wow...."
        hide sner0208
        hide kevin (20)
        with dissolve
        kristik "..."
        kristik "these guys are such fucking hypocrites..."
        kristik "calling me a simp when they doin this shit...."
        show kyle (1):
            xpos 400
            zoom 0.6
        with dissolve
        kyle "...Well it looks like we're the only ones left."
        kristik "oh hell no bro im not into gay shit like i said"
        hide kyle (1)
        show kyle (2):
            xpos 400
            zoom 0.6
        kyle "Do you know who is though?"
        kristik "I know what you're gonna say, oh you're probably the one who's-"
        kyle "Jason is gay."
        kristik "... wut???"
        hide kyle (2)
        show kyle (4):
            xpos 400
            zoom 0.6
        kyle "Yeah. He's secretly gay."
        kristik "What??? Really?? Him????"
        kyle "Those pickup lines are completely fake. He just wants to get dicked down."
        hide kyle (4)
        show kyle (2):
            xpos 400
            zoom 0.6 
        kristik "What the fuck... how do you even know that??"
        kyle "He has a secret diary."
        kyle "I won't spoil the fun, but let's say he's into some of the really kinky gay shit."
        kristik "...."
        kristik "uhhh OOOOOKAAAAAAY then... uhhh..."
        kristik "Good to know i guess?"      
        stop music fadeout 2.0 
        hide kyle (2)
        hide city_street4
        with dissolve
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(2,hard=True)
        $ EXPaaronwesley += 1
        $show_quick_menu = True
        window show
        with dissolve
        play music "audio/jazznoir.ogg"
        show office2
        with dissolve
        $ renpy.pause(2,hard=True)
        show aaron_9s:
            xpos -10
            ypos 200
            zoom 0.55
        show wesley_1s:
            xpos 800
            ypos 100
            zoom 0.8
        with dissolve
        aaron "Anything to report?"     
        hide wesley_1s
        show wesley_2s_w:
            xpos 800
            ypos 100
            zoom 0.6
        with dissolve
        wesley "They are mobilizing quickly."
        wesley "New recruits for Kristik and his gang are growing."
        hide aaron_9s
        show aaron_8s:
            xpos -10
            ypos 220
            zoom 0.55
        hide wesley_2s_w
        show wesley_1s:
            xpos 800
            ypos 100
            zoom 0.8
        with dissolve
        aaron "Well shit..."
        aaron "Who would've guessed that he'd encounter 4 girls in such a short time..."
        hide aaron_8s
        show aaron_10s:
            xpos -90
            ypos 200
            zoom 0.55
        with dissolve  
        aaron "This throws off some parts of our plan..."    
        hide aaron_10s
        show aaron_2s:
            xpos -90
            ypos 200
            zoom 0.55
        with dissolve
        aaron "Hmmm...."
        hide aaron_2s
        show aaron_5s:
            xpos -90
            ypos 200
            zoom 0.55
        with dissolve
        aaron "We're going to have to bring out the ''thing'' in that case."
        hide wesley_1s
        show wesley_2s_w:
            xpos 800
            ypos 100
            zoom 0.6
        with dissolve
        wesley "It's an untested prototype, and plus we don't know how effective it is."
        hide aaron_5s
        show aaron_8s:
            xpos -10
            ypos 220
            zoom 0.55
        with dissolve  
        aaron "True. But it's the only thing we have to stop their growth." 
        aaron "Roll out the prototype. Monitor it's behavior and see if it's able to stop Kristik."             
        hide wesley_2s_w
        show wesley_1s:
            xpos 800
            ypos 100
            zoom 0.8
        with dissolve
        wesley "Yes."
        hide aaron_8s
        show aaron_10s:
            xpos -90
            ypos 200
            zoom 0.55
        with dissolve 
        aaron "I won't let that bastard live another second."        
        hide aaron_10s
        show aaron_5s:
            xpos -90
            ypos 200
            zoom 0.55
        with dissolve
        aaron "Not until I'm dead."
        stop music fadeout 2.0
        hide aaron_5s
        hide wesley_1s
        hide office2
        with dissolve
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(2,hard=True)
        jump chapterfive


    elif EXPsuou >= 6:
        play music "audio/Sanoba Witch OST - Dekiru-Kana_-128k.ogg"
        $show_quick_menu = True
        window show
        with dissolve 
        show suburb_roadcenter
        with dissolve
        kristik "Ugh.."
        kristik "What a shitty misunderstanding..."
        kristik "it's not my fault that i got a boner!!!"
        kristik "wait... I guess it is my fault..."
        kristik "but i didnt FUCK HER!!!"
        kristik "I just hope that I can clear this misunderstanding"
        hide suburb_roadcenter
        with dissolve
        show shizu_houseext
        with dissolve
        $ renpy.pause(2,hard=True)
        kristik "Alright... hopefully this'll work."

        ####################################################################################################################################
        ## PLAY INTERCOM BEEP SOUND
        ####################################################################################################################################
        play sound "audio/intercom_call.mp3"
        $ renpy.pause(3,hard=True)

        rikka "Hello?"
        kristik "yeah.... hi this is kristik"
        rikka "Kristik? Whos's Kristik?"
        kristik "... shit this might be one of those ''friends''"
        rikka "Please state your identity."
        kristik "Uhh... it's the..."
        rikka "If you are not going to tell us who you are, then please get off the property."
        kristik "It's uhh.. the guy who got the boner yesterday..."
        rikka "..."

        ####################################################################################################################################
        ## PLAY INTERCOM BEEP SOUND AGAIN
        ####################################################################################################################################
        play sound "audio/intercom_call.mp3"
        $ renpy.pause(2,hard=True)        

        kristik "fuck... I knew that would happen... she just hung up on the intercom...."
        play sound "audio/gate.mp3"
        ####################################################################################################################################
        ## PLAY GATE OPEN SOUND
        ####################################################################################################################################
        show srik0208:
            xpos 400
            zoom 1.2
        with dissolve
        hide srik0208
        show srik0207:
            xpos 400
            zoom 1.2
        rikka "What do you want?"          
        hide srik0207
        show srik0208:
            xpos 400
            zoom 1.2
        kristik "uhhh... you see... the whole boner thing right?"
        hide srik0208
        show srik0207:
            xpos 400
            zoom 1.2
        rikka "I don't care what excuses you have, I'm not going to listen to them."
        rikka "You clearly don't have self control, so you have no reason to be here."
        hide srik0207
        show srik0208:
            xpos 400
            zoom 1.2
        kristik "Umm I..."
        hide srik0208
        show srik0207:
            xpos 400
            zoom 1.2
        rikka "You can go now."
        hide srik0207
        show srik0208:
            xpos 400
            zoom 1.2
        kristik "Wait!!! I uh... I have a medical condition!!!"
        hide srik0208
        show srik0209:
            xpos 400
            zoom 1.2
        rikka "Oh I'm sure you do... what excuse did you manage to conjure up this time?"
        kristik "I uhh... have a condition called... superinflammatorybonerprematuria!!!"
        hide srik0209
        show srik0211:
            xpos 400
            zoom 1.2
        rikka "..."
        hide srik0211
        show srik0207:
            xpos 400
            zoom 1.2 
        rikka "... Do you really expect me to believe something that stupid sounding?"
        hide srik0207
        show srik0208:
            xpos 400
            zoom 1.2
        kristik "Uhhh... yes?"
        hide srik0208
        show srik0207:
            xpos 400
            zoom 1.2
        rikka "Just get out of here, there's no point."
        hide srik0207
        show srik0209:
            xpos 400
            zoom 1.2
        suou "Wait!"
        rikka "???"     
        hide srik0209
        show srik0208:
            xpos 100
            zoom 1.2
        show ssuo0101:
            xpos 600
            zoom 1.2
        with dissolve
        suou "Kristik?"
        kristik "Yooooo whatzzzzupp!! Yeah, could you explain to this girl about-"
        hide ssuo0101
        show ssuo0121:
            xpos 600
            zoom 1.2
        suou "Is that really true?? Did what Rikka tell me actually happen!??!"
        hide ssuo0121
        show ssuo0103:
            xpos 600
            zoom 1.2
        kristik "fuck..."
        kristik "well... ok here is the thing..."
        kristik "Uhhmmm..."
        kristik "No.1, I did NOT rape you, because obviously I'm such a smart a nice guy I would never do anything like that to such a beautiful woman like you."
        hide srik0208
        show srik0209:
            xpos 100
            zoom 1.2
        rikka "That's a lie obviously..."
        hide srik0209
        show srik0208:
            xpos 100
            zoom 1.2        
        kristik "No.2, I DID in fact get a boner-"
        hide ssuo0103
        show ssuo0121:
            xpos 600
            zoom 1.2 
        suou "So you that did happen!!"
        hide ssuo0121
        show ssuo0103:
            xpos 600
            zoom 1.2
        kristik "NONONONO wait!"
        $ show_quick_menu = False
        window hide        
        menu:
            "''It was due to my condition, superinflammatorybonerprematuria!''":
                $ show_quick_menu = True
                window show            
                kristik "It was due to my condition, superinflammatorybonerprematuria!"  
                hide srik0208
                show srik0207:
                    xpos 100
                    zoom 1.2   
                rikka "That's clearly a fake name!"
                rikka "Who the hell would name a condition like that?"
                hide srik0207
                hide ssuo0103
                show srin0107:
                    xpos 350
                    zoom 1.2
                with dissolve           
                jump suouFinal
            "''It was because you were just kinda hot...''":
                $ show_quick_menu = True
                window show            
                $ EXPsuou += 2
                kristik "It was because you were just kinda hot..." 
                hide srik0208
                show srik0109:
                    xpos 100
                    zoom 1.2
                hide ssuo0103
                show ssuo0128:
                    xpos 600
                    zoom 1.2
                suou "Wha-??"
                hide ssuo0128
                show ssuo0104:
                    xpos 600
                    zoom 1.2
                hide srik0109
                show srik0108:
                    xpos 100
                    zoom 1.2
                rikka "I knew it!"
                rikka "So all that condition was bullshit!"
                hide srik0108
                show srik0109:
                    xpos 100
                    zoom 1.2
                kristik "Well yeah, but-"
                hide srik0109
                hide ssuo0104
                show srin0107:
                    xpos 350
                    zoom 1.2
                with dissolve
                jump suouFinal
        label suouFinal:
            ringo "Hey guys, what's with all the fuss?"
            hide srin0107
            show srin0104:
                xpos 350
                zoom 1.2
            with dissolve
            $ renpy.pause(0.6,hard=True)
            hide srin0104
            show srin0105:
                xpos 350
                zoom 1.2
            ringo "Oh... it's just you..."
            hide srin0105
            show srin0104:
                xpos 350
                zoom 1.2
            kristikmind "{i}Bruh this mf sound so disappointed..."
            hide srin0104
            show srin0105:
                xpos 350
                zoom 1.2
            ringo "Are you trying to clear up the situation from yesterday?"
            hide srin0104
            show srin0105:
                xpos 350
                zoom 1.2
            hide srin0105
            show srin0104:
                xpos 350
                zoom 1.2
            kristik "uhhh... well keyword is ''TRYING'' here.."
            hide srin0104
            show srin0105:
                xpos 350
                zoom 1.2
            ringo "Let me handle this."
            hide srin0105
            with dissolve
            kristik "???"
            narrator "{i}(whispering...)"
            suou "Really??"
            rikka "I didn't know..."
            kristikmind "{i}Tf is she telling them?"
            narrator "{i}(whispering...)"
            kristik "...?"
            show srin0101:
                xpos 320
                zoom 1.2
            show srik0201:
                zoom 1.2
                xpos -50
            show ssuo0101:
                xpos 750
                zoom 1.2
            with dissolve
            suou "I'm really sorry..."
            kristik "...What?"
            hide srik0201
            show srik0111:
                xpos -50
                zoom 1.2
            rikka "Me too..."
            kristikmind "{i}TF DID SHE TELL EM?? NOW IM REALLY CURIOUS!"
            hide srik0111
            show srik0112:
                xpos -50
                zoom 1.2
            rikka "I didn't realize that..."
            kristik "Um... wtf?"
            kristik "hold on a second..."
            hide ssuo0101
            hide srik0112
            with dissolve
            kristik "{i}Just what the hell did you tell them???!?"
            hide srin0101
            show srin0202:
                xpos 320
                zoom 1.2
            ringo "{i}I just told them that you had a severe mental issue."
            hide srin0202
            show srin0204:
                xpos 320
                zoom 1.2
            kristik "{i}WHAT??!?!"
            kristik "{i}WHY TF WOULD YOU DO THAT??!?!?!"
            hide srin0204
            show srin0202:
                xpos 320
                zoom 1.2
            ringo "{i}Trust me, it's an easy way to get out of the situation you were in. Otherwise, there would have been no other option."
            hide srin0202
            show srin0201:
                xpos 320
                zoom 1.2
            kristik "{i}So basically, they think im an autist now?!?!?!"
            hide srin0201
            show srin0202:
                xpos 320
                zoom 1.2
            ringo "Well, I guess you could say that."
            hide srin0202
            show srin0204:
                xpos 320
                zoom 1.2
            kristikmind "{i}This mf..."
            hide srin0204
            show srin0111:
                xpos 320
                zoom 1.2
            show srik0112:
                zoom 1.2
                xpos -50
            show ssuo0101:
                xpos 750
                zoom 1.2
            with dissolve   
            kristik "uhhh... guys..."            
            hide srin0111
            show srin0101:
                xpos 320
                zoom 1.2
            kristik "Just to clear the air, I'm actually NOT mentally disabled, and I am a functioning human of society." 
            hide srik0112
            show srik0214:
                xpos -50
                zoom 1.2
            rikka "Aww... there he goes again."
            kristik "NO IM SERIOUS!!! IM NOT AUTISTIC!!!"
            hide srik0214
            show srik0211:
                xpos -50
                zoom 1.2
            rikka "So sad..."
            kristik "ughh.... PLEASE LISTEN TO ME!!!"
            kristik "Nevermind actually..."
            hide srin0101
            show srin0107:
                xpos 320
                zoom 1.2
            ringo "Would you like to come in?"
            hide srin0107
            show srin0106:
                xpos 320
                zoom 1.2
            kristik "Yknow what... fine."
            hide srin0106
            show srin0107:
                xpos 320
                zoom 1.2   
            ringo "You two go in. I need to talk to him first."
            hide srin0107
            show srin0106:
                xpos 320
                zoom 1.2
            rikka "Ok."
            suou "Sure..."
            hide srik0211
            hide ssuo0101
            with dissolve
            kristik "how tf am i going to clear this whole situation up??"
            hide srin0106
            show srin0107:
                xpos 320
                zoom 1.2
            ringo "It's fine. I'll explain it away once the time is right. Now you do whatever you want."
            ringo "I'll be around, so if you need me to be your wing-woman, let me know!"    
            hide srin0107
            show srin0106:
                xpos 320
                zoom 1.2
            kristik "Cheeky... but I guess that's nice?"
            hide srin0106
            with dissolve                                                         
            hide shizu_houseext
            with dissolve
            show house_interior1
            with dissolve
            show srin0101:
                xpos 320
                zoom 1.2
            show srik0203:
                zoom 1.2
                xpos -50
            show ssuo0101:
                xpos 750
                zoom 1.2
            with dissolve
            $ renpy.pause(1,hard=True)
            hide srik0203
            show srik0204:
                xpos -50
                zoom 1.2
            rikka "Alright Krabby, anything you want to do?"
            hide srik0204
            show srik0203:
                xpos -50
                zoom 1.2
            kristikmind "{i}Why is she so nice all of a sudden after finding out i was '''''AUTISTIC'''''?!???"
            kristik "Ummm.. not particularly? I just wanted to clear up the situation from yesterday..."
            hide srik0203
            show srik0204:
                xpos -50
                zoom 1.2                
            rikka "Oh don't be like that, there must be something you want to do!"
            hide srik0204
            show srik0203:
                xpos -50
                zoom 1.2
            kristik "WEEEEeeeeeeeellll..... now that you mention it..."
            kristikmind "{i}Nah wait... I don't think I should take advantage of this if they think im fuckin '''''AUTISTIC'''''"     
            kristik "Actually... nevermind."
            hide srin0101
            show srin0202:
                xpos 320
                zoom 1.2
            ringo "What? Don't be like that! Just tell us what you were going to say!"
            hide srin0202
            show srin0204:
                xpos 320
                zoom 1.2
            kristikmind "{i}Fuck you ringo... making me say this shit..."
            $ show_quick_menu = False
            window hide
            menu:
                "''I just wanted to fuck the shit out of Rikka.''":
                    stop music fadeout 2.0
                    $ show_quick_menu = True
                    window show                
                    $ EXPrikka += 2
                    kristik "I just.... wanted to fuck the shit out of Rikka!!!"
                    play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
                    hide srin0204
                    show srin0117:
                        xpos 320
                        zoom 1.2
                    hide ssuo0101
                    show ssuo0128:
                        xpos 750
                        zoom 1.2
                    hide srik0203
                    show srik0117:
                        xpos -50
                        zoom 1.2
                    rikka "H-huhh....??!?!!!"
                    hide ssuo0128
                    show ssuo0103:
                        xpos 750
                        zoom 1.2
                    hide srin0117
                    show srin0101:
                        xpos 320
                        zoom 1.2
                    hide srik0117
                    show srik0216:
                        xpos -50
                        zoom 1.2
                    rikka "Ringo... isn't this... a little too weird for him to say???!"
                    hide srin0101
                    show srin0107:
                        xpos 320
                        zoom 1.2
                    ringo "Maybe not for him it isn't..."
                    hide srin0107
                    show srin0101:
                        xpos 320
                        zoom 1.2
                    hide ssuo0103
                    show ssuo0121:
                        xpos 750
                        zoom 1.2
                    suou "Is that really true?!!! You would do that right now??!!!"
                    hide ssuo0121
                    show ssuo0103:
                        xpos 750
                        zoom 1.2
                    kristik "well... uh... I mean... Um..."
                    hide srik0216
                    show srik0106:
                        xpos -50
                        zoom 1.2
                    rikka "Well... if it's with you, then I'm fine with it..."
                    kristikmind "{i}WUTTT????!!!!"
                    hide srik0106
                    show srik0107:
                        xpos -50
                        zoom 1.2
                    kristik "Really??"
                    rikka "Ehehehe...."
                    hide srik0107
                    show srik0108:
                        xpos -50
                        zoom 1.2
                    hide srin0101
                    show srin0117:
                        xpos 320
                        zoom 1.2
                    hide ssuo0103
                    show ssuo0122:
                        xpos 750
                        zoom 1.2
                    rikka "OF COURSE NOT!!!! WHY WOULD I LET YOU DO IT OUT OF ALL PEOPLE?!?!!!!" 
                    hide srik0108
                    show srik0109:
                        xpos -50
                        zoom 1.2
                    hide srin0117
                    show srin0102:
                        xpos 320
                        zoom 1.2
                    hide ssuo0122
                    show ssuo0101:
                        xpos 750
                        zoom 1.2
                    kristikmind "{i}!!!!?????"     
                    hide srik0109
                    show srik0108:
                        xpos -50
                        zoom 1.2  
                    rikka "I JUST CAN'T KEEP UP THIS ACT RINGO!!! THIS IS JUST TOO HARD!!"       
                    rikka "AS SOON AS HE SAID THAT MY EARS NEARLY EXPLODED!!!"           
                    rikka "UGGHHH!!! I CAN'T TAKE THIS ANYMORE!!! IM OUT OF HERE!!!"
                    hide srik0108
                    transform moveleftoffscreen1:
                        xpos -50
                        zoom 1.2
                        ease 0.5 xpos -800 zoom 1.2
                    show srik0109 at moveleftoffscreen1
                    $ renpy.pause(1,hard=True)
                    hide srik0109
                    transform moveRinfromMid:
                        xpos 320
                        zoom 1.2
                        ease 0.5 xpos 0 zoom 1.2
                    transform moveSuoufromRight:
                        xpos 750
                        zoom 1.2
                        ease 0.5 xpos 600 zoom 1.2
                    hide srin0102
                    hide ssuo0101
                    show srin0102 at moveRinfromMid
                    show ssuo0101 at moveSuoufromRight
                    kristik "uhhh...."
                    kristik "So... Suou you probably know that I'm not austistic right?"
                    hide ssuo0101
                    show ssuo0110:
                        xpos 600
                        zoom 1.2
                    suou "Yeah...."
                    hide srin0102
                    show srin0115:
                        xpos 0
                        zoom 1.2
                    ringo "I just never expected you to say something like that, especially not to Rikka."
                    hide srin0115
                    show srin0112:
                        xpos 0
                        zoom 1.2
                    ringo "But, well I guess you do have a type for her then."
                    hide ssuo0110
                    show ssuo0111:
                        xpos 600
                        zoom 1.2
                    suou "..."
                    kristik "I... uhh...."
                    hide ssuo0111
                    show ssuo0113:
                        xpos 600
                        zoom 1.2
                    suou "It's ok... No matter who it is you like, I'll support you anyways."
                    hide ssuo0113
                    show ssuo0118:
                        xpos 600
                        zoom 1.2
                    kristikmind "{i}shit... I feel really bad now... after all she was my former ''girlfriend''...."
                    hide srin0112
                    show srin0202:
                        xpos 0
                        zoom 1.2
                    ringo "Hey Kristik. I'd like to have some alone time with Suou, so do you mind?"
                    hide srin0202
                    show srin0201:
                        xpos 0
                        zoom 1.2
                    kristik "Yeah... I understand."
                    stop music fadeout 2.0
                    hide srin0201
                    hide ssuo0118
                    with dissolve
                    hide house_interior1
                    with dissolve
                    window hide
                    $ show_quick_menu = False
                    with dissolve
                    $ renpy.pause(4,hard=True)
                    jump chapterfive
                "''I just wanted to make out with Suou.''":
                    stop music fadeout 2.0
                    $ show_quick_menu = True
                    window show                
                    $ EXPsuou += 2
                    kristik "I just.... wanted to make out with Suou."
                    hide srin0204
                    show srin0117:
                        xpos 320
                        zoom 1.2
                    hide ssuo0101
                    show ssuo0128:
                        xpos 750
                        zoom 1.2
                    hide srik0203
                    show srik0117:
                        xpos -50
                        zoom 1.2
                    suou "What....??!?!!!"   
                    hide ssuo0128
                    show ssuo0105:
                        xpos 750
                        zoom 1.2
                    hide srin0117
                    show srin0101:
                        xpos 320
                        zoom 1.2
                    hide srik0117
                    show srik0209:
                        xpos -50
                        zoom 1.2
                    suou "Umm... uhhh....."
                    hide ssuo0105
                    show ssuo0103:
                        xpos 750
                        zoom 1.2
                    suou "Is that really... what you want to do?"
                    kristik "Ummm... I guess?"
                    hide srin0101
                    show srin0107:
                        xpos 320
                        zoom 1.2
                    hide srik0209
                    show srik0214:
                        xpos -50
                        zoom 1.2
                    ringo "Hey, Rikka. We should get going. I forgot we had a ''meeting'' later today."
                    hide srin0107
                    show srin0106:
                        xpos 320
                        zoom 1.2
                    hide srik0214
                    show srik0201:
                        xpos -50
                        zoom 1.2
                    rikka "Yeah.... you're right...."
                    transform moveRikkaLeft:
                        xpos -50
                        zoom 1.2
                        ease 0.5 xpos -800 zoom 1.2
                    transform moveRingoLeft:
                        xpos 320
                        zoom 1.2
                        ease 0.5 xpos -800 zoom 1.2                    
                    hide srik0201
                    hide srin0106
                    show srik0201 at moveRikkaLeft
                    show srin0106 at moveRingoLeft
                    $ renpy.pause (0.7,hard=True)
                    hide srin0106
                    hide srik0201
                    suou "..."
                    transform moveSuoutoMiddle:
                        xpos 750
                        zoom 1.2
                        ease 0.5 xpos 320 zoom 1.2
                    hide ssuo0103
                    show ssuo0105 at moveSuoutoMiddle
                    kristik "uhhh...."
                    hide ssuo0105
                    show ssuo0103:
                        xpos 320
                        zoom 1.2
                    suou "You said... you wanted... to kiss right?"
                    kristikmind "{i}Shiddd!!!! is this the time i actually get some FUK?!?!?!?!?"
                    hide ssuo0103
                    hide house_interior1
                    with dissolve
                    $ renpy.pause(2,hard=True)
                    narrator "You can imagine what happened after that."
                    narrator "I'm not going to type that nor will I subject any poor voice actor to voice that."
                    if EXPsuou >= 9:                 
                        "{b}Good ending 12/21"  
                        if (persistent.endingFinished12 < 1):
                            $ persistent.endingFinished12 += 1
                        elif (persistent.endingFinished12 >= 1):
                            pass
                        else:
                            narrator "PERSISTENT DATA FAILURE FOR SECTION 7299. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                            $ renpy.quit()
                        $ renpy.pause(2,hard=True)
                        $ MainMenu(confirm=False)()
                    else:
                        jump noHoesEnding
                        return

    else:
        $show_quick_menu = True
        window show
        with dissolve 
        show city_clubint
        with dissolve 
        show kyle (23):
            xpos 700
            ypos 20
            zoom 0.6
        show jason (78):
            xpos 400
            ypos 20
            zoom 0.6
        show kevin (17):
            xpos 0
            zoom 0.6
        with dissolve   
        jason "WOooooOoOoOohhhh yeAH!!!!!!"
        jason "I wUv dem BEERS!!!"
        kristikmind "{i}I decided to hang out with the boys after they found out I was hanging with ''bitches''..."
        kristikmind "{i}they thought I had a fetish for disabled people or some bullshit like that..."
        hide kevin (17)
        show kevin (18):
            xpos 0
            zoom 0.6
        kevin "Yo Kristik! Try out this 100 percent pure vodka."
        kristik "Uhh.... no."
        hide kevin (18)
        show kevin (16):
            xpos 0
            zoom 0.6
        kevin "Awww cmon you're being a pussy now?"
        kristik "Fine!"
        play sounmd "audio/ROBLOX _Bloxy Cola Drink_ Sound Effect-(128kbps).ogg"
        ############################################################################################################################################
        # INSERT ROBLOX BLOXY COLA DRINKING SOUND
        ############################################################################################################################################
        $ renpy.pause(4,hard=True)
        hide kevin (16)
        show kevin (18):
            xpos 0
            zoom 0.6
        kristik "ughh..."
        kristik "wooaoaHhhh..."
        hide kevin (18)
        hide jason (78)
        hide kyle (23)
        hide city_clubint
        with Pixellate(5,8)        
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(2,hard=True)
        show city_street4_ni
        with Pixellate(5,8)        
        window show
        $ show_quick_menu = True
        kristik "......"
        kristik "fuck...."
        kristik "owww..... my fuckin head.."
        kristik "Where the hell am i???"
        kristik "why the fuck am I out in the street?"
        show aaron_11_n:
            xpos 450
            ypos 30
            zoom 0.4
        with dissolve
        unknown "..."
        hide aaron_11_n
        show aaron_11_n_1:
            xpos 450
            ypos 30
            zoom 0.4
        unknown "hmm..."
        hide aaron_11_n_1
        show aaron_11_n_2:
            xpos 450
            ypos 30
            zoom 0.4
        unknown "It's you."
        unknown "I never thought I would have found you here, being drunk out in the street."
        hide aaron_11_n_2
        show aaron_11_n_3: 
            xpos 450
            ypos 30
            zoom 0.4
        unknown "Krabbick."
        hide aaron_11_n_3
        show aaron_11_n:
            xpos 450
            ypos 30
            zoom 0.4
        kristik "!!!!!!!!"
        kristikmind "{i}Wait!! He's...!!!"
        kristik "Aaron?"
        hide aaron_11_n
        show aaron_11_n_2:
            xpos 450
            ypos 30
            zoom 0.4
        aaron "Hm."
        aaron "I'll see you around. Krabby."
        aaron "Let your friends know I saw them after your hangover."
        $ EXPaaronwesley += 1
        hide aaron_11_n_2
        show aaron_11_n:
            xpos 450
            ypos 30
            zoom 0.4
        kristik "Wait!!!!"
        hide aaron_11_n
        with dissolve
        kristik "Ughh... fuck!!"
        hide city_street4_ni
        with Pixellate(5,8)        
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(2,hard=True)
        show school_dormhisao_ni
        with Pixellate(5,8)        
        window show
        $ show_quick_menu = True
        kristik "ugh..."
        kristik "fuck where the hell am I now?!!!"
        hide school_dormhisao_ni
        show school_dormhisao_ss
        $ renpy.pause(1,hard=True)
        show seri0104:
            xpos 150
            ypos -60
            zoom 1.1  
        with dissolve
        hide seri0104 
        show seri0106:  
            xpos 150
            ypos -60
            zoom 1.1  
        erika "Hey."
        hide seri0106
        show seri0104:
            xpos 150
            ypos -60
            zoom 1.1
        kristik "Tf???? Erika??? What are you doing here??!!"
        hide seri0104
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1
        erika "I should be asking you the questions! What were you doing out in the street?"
        hide seri0112
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1
        kristik "I was... out drinking... and then i saw him!"
        hide seri0111
        show seri0119:
            xpos 150
            ypos -60
            zoom 1.1   
        erika "Who did you see?"     
        hide seri0119
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1  
        kristik "It was... Aaron..."
        hide seri0111
        show seri0113:
            xpos 150
            ypos -60
            zoom 1.1   
        erika "Hm...."
        hide seri0113
        show seri0119:
            xpos 150
            ypos -60
            zoom 1.1  
        erika "What did he say to you?"
        hide seri0119
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1  
        kristik "Fuck... I think he just was surprised to find me out in the street... then he walked off."   
        hide seri0111
        show seri0113:
            xpos 150
            ypos -60
            zoom 1.1   
        erika "Hmm..."
        hide seri0113
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1  
        erika "Now I'm worried... he is indeed out for your blood."
        erika "I'm just surprised he didn't want to kill you on the spot."
        hide seri0112
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1 
        kristik "Well, I was out in the middle of a public street. I doubt he could make a clean murder or get it away with it if he killed me there."                                     
        hide seri0111
        show seri0119:
            xpos 150
            ypos -60
            zoom 1.1  
        erika "He still could have killed you!"
        erika "You were so vulnerable I was able to pull you into my dorm room!"
        hide seri0119
        show seri0115:
            xpos 150
            ypos -60
            zoom 1.1  
        kristik "Well... yeah I guess..."
        hide seri0115
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1  
        erika "By the way, where are your friends?"
        hide seri0112
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1  
        kristik "My friends...."
        hide seri0111
        show seri0103:
            xpos 150
            ypos -60
            zoom 1.1
        kristik "MY FUCKIN FRIENDS!!!!!"    
        hide seri0103
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1   
        kristik "THOSE BASTARDS!!! HOW COULD THEY MAKE ME DRINK A SUPER STRONG VODKA, LEAVE ME OUT IN THE STREET ONLY TO BE SPOTTED BY MY ENEMY THEN PICKED UP BY A GIRL?!?!?!?!"
        kristik "WHAT KIND OF FUCKING FRIENDS ARE THEY?!!!!"       
        hide seri0111
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1  
        erika "Kristik.... calm down."
        erika "Do you know where they are right now?"
        hide seri0112
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1 
        kristik "I have no fucking clue..."
        kristik "The only fucking thing I know is that they were a bunch of bastards that left me out in the street."
        kristik "What time is it?"
        hide seri0111
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1 
        erika "8 AM."
        hide seri0112
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1            
        kristik "Alright, then I think it's time I leave."
        hide seri0111
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1    
        erika "What about your headache?"
        hide seri0112
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1    
        kristik "I can walk it off... I'll be out of your hair anyways."   
        hide seri0111
        show seri0113:
            xpos 150
            ypos -60
            zoom 1.1
        erika "Well... you're not that much of a bother for me..."
        hide seri0113
        show seri0111:
            xpos 150
            ypos -60
            zoom 1.1   
        kristik "It's okay. I'll be going now."
        hide seri0111
        show seri0112:
            xpos 150
            ypos -60
            zoom 1.1  
        erika "Well, if you say so. Bye."
        hide seri0112
        with dissolve
        hide school_dormhisao_ss
        show school_gardens
        with dissolve
        kristik "Really nice day today..."
        kristik "Too bad I can't really enjoy it because my FUCKING HEAD HURTS!!!"
        kristik "That bastard bitch balls Kevin... made me drink some fentanyl laced vodka..."
        hide school_gardens
        with dissolve
        window hide
        $ show_quick_menu = False
        with dissolve
        jump noHoesEnding


label chapterfive:
    if EXPchidori >= 7:
        play music "audio/Sanoba Witch OST - Sweet Sweet Alice(InstVer.)-128k intro.ogg"
        queue music "audio/Sanoba Witch OST - Sweet Sweet Alice(InstVer.)-128k.ogg"
        show BG010
        with dissolve
        $ show_quick_menu = True
        window show
        with dissolve
        show schi0101:
            xpos 350
            zoom 1.2
        with dissolve
        hide schi0101
        show schi0102:
            xpos 350
            zoom 1.2
        chidori "This way."
        hide schi0102
        show schi0101:
            xpos 350
            zoom 1.2
        kristikmind "{i}OoooH!! HELL YES!!! FINALLY I MIGHT BE ABLE TO GET A GIRLFRIEND!!!"
        kristik "So... is there any particular reason you want me to come over?"
        hide schi0101
        show schi0310:
            xpos 350
            zoom 1.2
        chidori "... work"
        kristik "huh?"
        hide schi0310
        show schi0202:
            xpos 350
            zoom 1.2
        chidori "I need help with my math homework!"
        hide schi0202
        show schi0208:
            xpos 350
            zoom 1.2
        kristik "What??!"
        kristikmind "{i}FUCK! THAT'S WHY SHE ASKED ME TO COME OVER???!!!"
        kristik "ummm.. what specifically?"
        hide schi0208
        show schi0102:
            xpos 350
            zoom 1.2
        chidori "Linear algebra and multivariable calculus."
        hide schi0102
        show schi0101:
            xpos 350
            zoom 1.2
        kristik "What??!!!"
        kristikmind "{i}Fuck!! I don't remember how to do that shit!!"
        hide schi0101
        show schi0102:
            xpos 350
            zoom 1.2   
        chidori "So you are going to help me, right?"
        hide schi0102
        show schi0101:
            xpos 350
            zoom 1.2
        kristik "Uhh... umm..."
        kristik "Yeah I totally will. Yeah."
        hide schi0101
        show schi0102:
            xpos 350
            zoom 1.2  
        chidori "Great. Now let's go."
        hide schi0102
        with dissolve
        hide BG010
        show BG001
        with dissolve
        show schi0401:
            xpos 350
            zoom 1.2
        with dissolve
        hide schi0401
        show schi0402:
            xpos 350
            zoom 1.2
        chidori "Alright. Take a look at the first question."
        chidori "For this triple integral, can you evaluate 4x²y - z³{i}dzdydx{/i}, from when z is 2 to 3, when y is from -1 to 4, and when x is from 1 to 0?"
        hide schi0402
        show schi0401:
            xpos 350
            zoom 1.2
        kristik "ummm..."
        $ show_quick_menu = False
        window hide      
        menu:
            "''Integrate {i}dz, dy, and dx{/i} in the order given from the inside most and then work it outside. All of them are considered constants, just like in a double integration. Because the limits are already setup, it's fairly easy.''":
                $ show_quick_menu = True
                window show
                $ EXPchidori += 1
                kristik "Just integrate {i}dz, dy, and dx{/i} in the order given from the inside most and then work it outside. All of them are considered constants, just like in a double integration. Because the limits are already setup, it's fairly easy."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "That does make sense."
                chidori "... and I got negative 755 over 4. Let me check if that's correct."
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2  
                chidori "..."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "Yeah. That's right."
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2               
                kristikmind "{i} holy shit i completely forgot how to do that I just bullshitted!! LETS GO!!!"                              
            "''Using the Extreme Value Theorem, find the absolute minimum and maximum by graphing it on the real plane and then find the points that intersect along this closed interval.''":
                $ show_quick_menu = True
                window show            
                kristik "Using the Extreme Value Theorem, find the absolute minimum and maximum by graphing it on the real plane and then find the points that intersect along this closed interval."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "That makes no sense."  
                chidori "This is an integration problem, there's no interval given."
                chidori "I'll just check the answer sheet in the back and see what it says later."
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2
        hide schi0401
        show schi0402:
            xpos 350
            zoom 1.2    
        chidori "Now what about this one?"
        chidori "Determine the volume of a region with a elliptic paraboloid towards the top with a cone facing upwards into the cylinder, that is below \n {i}z = 8 - x² - y²{/i} above {i} z = -(4x² + 4y²)¹/² {/i} and inside {i} x² + y² = 4.{/i} "  
        hide schi0402
        show schi0401:
            xpos 350
            zoom 1.2          
        kristik "Shit... 3d shapes..."
        $ show_quick_menu = False
        window hide
        menu:
            "''With the triple integral for a given solid, use Rolle's theorem to find a stationary intersectionary point within the limit. Integrate the limit by deriving the reciprocal value from both {i} dz and dy {/i}. It's aggregate can then be substituted and dervied from when θ < dA < π. Use arbitrary substitution to take the aggregate and convert to it's real coordinates. In the new matrice, from a1 ··· a3 in all 3 dimensions, compute the volume with this theorem and get your answer.''":
                $ show_quick_menu = True
                window show
                kristik "With the triple integral for a given solid, use Rolle's theorem to find a stationary intersectionary point within the limit."
                kristik "Integrate the limit by deriving the reciprocal value from both {i} dz and dy {/i}. It's aggregate can then be substituted and dervied from when θ < dA < π. Use arbitrary substitution to take the aggregate and convert to it's real coordinates."
                kristik "In the new matrice, from a1 ··· a3 in all 3 dimensions, compute the volume with this theorem and get your answer."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "What are you talking about?"
                chidori "There isn't any need to overcomplicate this with matrices or theorems, we can just integrate this with the volume integral and set it's upper and lower limits."       
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2
                kristik "O..."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "Whatever, it's fine. We can move onto Linear Algebra."
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2
                kristikmind "{i}Fuck!! Linear algebra sucks ass!!!"                                          
            "''The volume of a solid is given by that triple integral, set the upper and lower limits for this integral to be the regions that the question specified it to be above and below. For {i}D{/i} we can determine that it's limits is \n {i}0 < θ < 2π.{/i} Setup the volume integral and integrate {i} Z {/i} from {i} dz{/i}. Convert the integral over to polar coordinates, then integrate {i} r {/i} since {i}dA = r dr dθ{/i}. Compute the integral and get your answser.''":
                $ show_quick_menu = True
                window show
                $ EXPchidori += 1
                kristik "The volume of a solid is given by that triple integral, set the upper and lower limits for this integral to be the regions that the question specified it to be above and below."
                kristik "For {i}D{/i} we can determine that it's limits is {i}0 < θ < 2π.{/i} Setup the volume integral and integrate {i} Z {/i} from {i} dz{/i}. Convert the integral over to polar coordinates, then integrate {i} r {/i} since {i}dA = r dr dθ{/i}. Compute the integral and get your answser."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "Wow. You are very smart Kristik."
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2
                kristikmind "{i}Hell yea I am!!!!"
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "We can move onto Linear Algebra."
                hide schi0402
                show schi0401:
                    xpos 350
                    zoom 1.2                                                    
                kristikmind "{i}Fuck.... Linear algebra is literal AIDs..."    
        hide schi0401
        show schi0402:
            xpos 350
            zoom 1.2        
        chidori "Here's an easy one."
        chidori "Let {b}{i}T: R^n -> R^m{/b}{/i} be a linear transformation. Suppose that the nullity of {b}{i}T{/b}{/i} is zero."    
        chidori "If {b}{i} {{x1,x2,...,xk} {/b}{/i} is a linearly independent subset of {b}{i}Rn{/b}{/i}, then show that {b}{i}{{T((x1),T((x2),...,T((xk)}{/b}{/i} is a linearly independent subset of {b}{i}Rm.{/b}{/i}"
        hide schi0402
        show schi0401:
            xpos 350
            zoom 1.2
        kristikmind "{i}What the fuck was that?"
        kristik "Uhh..."
        $ show_quick_menu = False
        window hide
        menu:
            "''Consider that the combination {b}{i}c1T(x1)+c2T(x2)+···+ckT(xk)=0m,{/b}{/i}. Where {b}{i}0m{/b}{/i} is the {b}{i}m{/b}{/i} dimensional zero vector in {b}{i}Rm{/b}{/i}. To show that the set {b}{i}{{T(x1),T(x2),···,T(xk){/b}{/i}} is linearly independent, we need to show that {b}{i}c1=c2=···=ck=0{/b}{/i}.''":
                $ show_quick_menu = True
                window show
                $ EXPchidori += 1
                kristik "Consider that the combination {b}{i}c1T(x1)+c2T(x2)+ ··· +ckT(xk)=0m,{/b}{/i}. Where {b}{i}0m{/b}{/i} is the {b}{i}m{/b}{/i} dimensional zero vector in {b}{i}Rm{/b}{/i}. To show that the set {b}{i}{{T(x1),T(x2),···,T(xk){/b}{/i}} is linearly independent, we need to show that {b}{i}c1=c2=···=ck=0{/b}{/i}."
                kristik "Using the linearity of {b}{i}T{/b}{/i}, we have {b}{i}T(c1x1+c2x2+···+ckxk)=0m{/b}{/i}."
                kristik "Then the vector {b}{i}c1x1+c2x2+···+ckxk{/b}{/i} is in the nullspace {b}{i}N(T){/b}{/i} of {b}{i}T{/b}{/i}. Since the nullity, which is the dimension of the nullspace, is zero, we have {b}{i}N(T)={{0n}{/b}{/i}. This yields {b}{i}c1x1+c2x2+···+ckxk=0n.{/b}{/i}"
                kristik "Since the vectors {b}{i}x1,x2,···,xk{/b}{/i} are linearly independent, we must have {b}{i}c1=c2=···=ck=0{/b}{/i} as required. Thus we conclude that {b}{i}{{T(x1),T(x2),···,T(xk)}{/b}{/i} is a linearly independent subset of {b}{i}Rm{/b}{/i}."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "Wow. Very smart."
                hide schi0402
                show schi0404:
                    xpos 350
                    zoom 1.2
                chidori "Thanks for the help as always."
                hide schi0404
                show schi0403:
                    xpos 350
                    zoom 1.2    
                kristikmind "{i}hehehehehe...."   
                hide schi0403                 
                jump nextpartTwo         
            "''For an {b}{i}m x n{/b}{/i} matrix {b}{i}A{/b}{/i}, the nullspace consists of vectors {b}{i}x{/b}{/i} such that {b}{i}Ax=0{/b}{/i}. Thus, such an {b}{i}x{/b}{/i} must be n-dimensional. Since the nullspace is a subspace in {b}{i}R3{/b}{/i}, we conclude that {b}{i}n=3{/b}{/i}. The range is spanned by a single vector v. Thus, {{v} is a basis for the range. Thus, the rank is 1.''":
                $ show_quick_menu = True
                window show
                kristik "For an {b}{i}m x n{/b}{/i} matrix {b}{i}A{/b}{/i}, the nullspace consists of vectors {b}{i}x{/b}{/i} such that {b}{i}Ax=0{/b}{/i}. Thus, such an {b}{i}x{/b}{/i} must be n-dimensional. Since the nullspace is a subspace in {b}{i}R3{/b}{/i}, we conclude that {b}{i}n=3{/b}{/i}. The range is spanned by a single vector v. Thus, {{v} is a basis for the range. Thus, the rank is 1."
                hide schi0401
                show schi0402:
                    xpos 350
                    zoom 1.2
                chidori "This is not matrix A, and plus we're trying to verify something not find it's rank."
                hide schi0402               
                jump nextpartTwo
        label nextpartTwo:
            hide schi0401
            show schi0409:
                xpos 350
                zoom 1.2
            stop music fadeout 2.0
            chidori "I'm sorry, Kristik."
            chidori "If I'm going to be completely honest, I didn't want you to come here for my math homework."
            hide schi0409
            show schi0411:
                xpos 350
                zoom 1.2           
            kristikmind "{i}Wait... is this....?"   
            hide schi0411
            show schi0409:
                xpos 350
                zoom 1.2 
            chidori "Just follow me."
            hide schi0409
            with dissolve
            kristikmind "{i}Follow her?!"
            hide BG001
            with dissolve
            $ renpy.pause(2,hard=True)
            play music "audio/waterdripping.ogg"
            show BG030n1
            with dissolve
            $ renpy.pause(1,hard=True)
            kristik "Ummmm.... Chidori, where the hell are we going?"
            show schi0402:
                xpos 350
                zoom 1.2  
            with dissolve 
            chidori "Just a little longer."    
            hide schi0402
            with dissolve
            kristikmind "{i}Jesus bro... why does she have a concrete cellar under her house?!?!!"
            kristikmind "{i}Is she into BDSM?!??!?!?!!!!!"  
            stop music fadeout 2.0
            hide BG030n1
            play music "audio/darkambience.ogg"
            show BG124
            with dissolve
            $ renpy.pause(1,hard=True)            
            kristik "Ummm... Chidori? The hell is this?"
            kristik "Hello??"
            kristik "...."
            kristik "Fuck bro... I'm about to shit my pants..."
            unknown "Hello."
            kristik "the fuck???"
            unknown "You're back. Krabby."
            kristik "Wait.... isn't that...?"
            kristik "Aaron????"
            aaron "Very fast thinker I see, well that won't really help you."
            kristik "What the hell is this about and where is Chidori??!!!"
            aaron "Hm. You don't seem to understand. I'll come down there to assist you."
            kristik "What..?"
            show aaron_7:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            aaron "Long time no see, Kriatrik."
            kristik "What the hell are you doing here??!!! And what do you want??!!!!"
            hide aaron_7
            show aaron_11_1:
                xpos 500
                ypos 60
                zoom 0.34
            with dissolve
            aaron "You're well aware of my intentions. Kribshit."      
            kristik "What did you just call me?!?!!!"
            kristik "And where the hell is Chidori?!!!!"
            aaron "Your ''girlfriend'' Chidori works for me. Yup, I just commited NTR on you just like in Kristik Saga 1."
            kristik "I got... Cucked???!!"    
            hide aaron_11_1
            show aaron_7:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            aaron "Find that out for yourself."
            hide aaron_7
            with dissolve
            show schi0411:
                xpos 350
                zoom 1.2
            with dissolve
            chidori "..."
            kristik "What are you doing?!!!?!! Was that whole thing about bringing them down a ruse??!!! Just for you to bait me?!!!"
            hide schi0411
            show schi0409:
                xpos 350
                zoom 1.2 
            chidori "I'm sorry!"
            chidori "I had to do this. For the safety of me and my friends!"
            hide schi0409
            show schi0411:
                xpos 350
                zoom 1.2
            kristik "What??!!!"  
            hide schi0411
            with dissolve
            show aaron_11_1:
                xpos 500
                ypos 60
                zoom 0.34
            with dissolve
            aaron "There's no point in fighting KrisLick."             
            hide aaron_11_1
            with dissolve
            kristik "Wait!!! The fuck are you gonna do to me?!!!"
            aaron "You'll find that out soon. Chidori, get the Cock and Ball torture-inator."
            kristik "WHATT?!!!!! NOO!!!!!!"
            aaron "I'm just kidding I'm not that insane. Get out Xi JingPing."
            kristik "Oh.. phew..."
            kristik "WAIT THAT SHIT STILL HURTS!!!"
            play music "audio/maozedongdrip.ogg"
            show xi:
                xpos 400
                ypos 120
                zoom 0.7
            with dissolve
            kristik "oh fuck..."
            xijingping "HEY! YOU!"
            kristik "Uhh.. yeah?"
            xijingping "DID U GET A+ IN THE LAST TEST?!!"
            kristik "Ummm... which one?"
            xijingping "DID YOU GET AP 6 IN AP LANG??!!!"
            kristik "...No...?"

            #======================================================================================================
            # PLAY GUN LOADING SOUNDS
            #======================================================================================================
            play sound "audio/gunload_Master.wav"
            show gun:
                xpos 700
                ypos 320 
                zoom 0.6
            $ renpy.pause(0.8,hard=True)                
            xijingping "THEN YOU ARE DISOWN AND DIE!!!"
            kristik "WAIT!!! NONONONONO!!!!!"
            xijingping "NO EXCUSES! I EXPECT NOTHING LESS THAN 101%% ON AP LANG AND 1700 ON SAT!!"
            kristik "NONONNONONO!!!!!"
           
            #======================================================================================================
            # PLAY GUN SHOOTING SOUNDS
            #======================================================================================================
            play sound "audio/awp.mp3"
            show white
            $ renpy.pause(0.001,hard=True)
            hide white
            with Dissolve(1)
            xijingping "DIEE!!!!!"
            hide gun 
            hide xi
            with dissolve
            play sound "audio/awp.mp3"
            show white
            $ renpy.pause(0.001,hard=True)
            hide white
            with Dissolve(1)
            kristik "FUUUCK!!!!"
            play sound "audio/awp.mp3"
            show white
            $ renpy.pause(0.001,hard=True)
            hide white
            with Dissolve(0.2)   
            play sound "audio/awp.mp3" 
            show white
            $ renpy.pause(0.001,hard=True)
            hide white
            with Dissolve(0.2)  
            play sound "audio/awp.mp3"
            show white
            $ renpy.pause(0.001,hard=True)
            hide white
            with Dissolve(0.2)  
            play sound "audio/awp.mp3"
            show white
            $ renpy.pause(0.001,hard=True)
            hide white
            with Dissolve(1)       
            kristik "WAAAH!!! I WANT MY MOMMY!!!"

            #======================================================================================================
            # PLAY PISSING SOUNDS
            #======================================================================================================

            kristik "(peeing)"
            xijingping "AUGH!!!"
            kristik "Huh???!!"
            stop music fadeout 1.0
            play music "audio/darkambience.ogg"
            hide BG124
            show xidead1
            with dissolve
            xijingping "Ugh... (beep boop)"
            kristik "What??!"
            xijingping "This piss... it's... corrosive... "
            kristik "Wait... did I get this power..."
            kristik "from Bill when I drank his piss in Kristik Saga 2??!!!"
            xijingping "My functions are being overwritten... due to the piss... (beep boop)"
            hide xidead1
            show xidead
            xijingping "(blegh)"
            aaron "You bastard."
            hide xidead
            show BG124
            show aaron_11_1:
                xpos 500
                ypos 60
                zoom 0.34
            with dissolve
            aaron "You killed my Xi Jingping bot..."
            hide aaron_11_1
            show aaron_7:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            aaron "Chidori! GET THAT COCK AND BALL TORTURE-INATOR!!!" 
            kristik "WAIT!!!"
            hide aaron_7
            show aaron_11_1:
                xpos 500
                ypos 60
                zoom 0.34
            aaron "There's no working with me anymore. You're going in the cock and ball torture-inator."     
            hide aaron_11_1
            show schi0408:
                xpos 350
                zoom 1.2
            with dissolve
            kristik "Chidori!!! Don't do this to me!!"   
            kristik "My cock and balls are very important to me!!!"
            if EXPchidori >= 10:
                hide schi0408
                show schi0411:
                    xpos 350
                    zoom 1.2

                #======================================================================================================
                # PLAY GUN LOADING SOUNDS
                #======================================================================================================
                play sound "audio/gunload_Master.wav"

                show gun:
                    xpos 600
                    ypos 320 
                    zoom 0.6
                $ renpy.pause(0.8,hard=True)                    
                chidori "..."
                kristik "WHAT??!?!?"
                hide schi0411
                hide BG124
                hide gun
                #======================================================================================================
                # PLAY GUN SHOOTING SOUNDS
                #======================================================================================================
                play sound "audio/awp.mp3"
                show white
                $ renpy.pause(0.001,hard=True)
                hide white
                with Dissolve(1) 
                $ renpy.pause(3.001,hard=True)   
                kristik "...?"    
                show BG124
                with dissolve
                $ renpy.pause(1,hard=True)  
                kristik "...what?"    
                show schi0408:
                    xpos 350
                    zoom 1.1
                with dissolve
                kristik "Chidori??!!"
                kristik "Why am I alive??!!"
                hide schi0408
                show schi0409:
                    xpos 350
                    zoom 1.1
                chidori "I killed Aaron."
                hide schi0409
                show schi0408:
                    xpos 350
                    zoom 1.1
                play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
                kristik "NANI?!?!!"
                kristik "Where is his body?!!"
                hide schi0408
                show schi0409:
                    xpos 350
                    zoom 1.1
                chidori "His body got vaporized."
                hide schi0409
                show schi0408:
                    xpos 350
                    zoom 1.1
                kristikmind "{i}What the fuck kind of gun is that??!!!"      
                kristik "Okokokok... hold up.."
                kristik "There's still so much shit that's happened and I need an explanation."
                hide schi0408
                show schi0409:
                    xpos 350
                    zoom 1.1
                chidori "Ok."  
                stop music fadeout 2.0
                show white
                with Dissolve(0.5)        
                hide schi0409
                hide BG124  
                $ renpy.pause(1,hard=True)
                hide white
                show office
                with dissolve        
                $ renpy.pause(1,hard=True)   
                play music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k intro.ogg"
                queue music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k.ogg"     
                show wesley_1s:
                    xpos 850
                    ypos 80
                    zoom 0.7
                show aaron_8s:
                    xpos -10
                    ypos 220
                    zoom 0.55
                with dissolve                
                show schi0401 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                with dissolve
                hide schi0401 onlayer mcsprite
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}About a week ago, your friends decided to try to get into contact with people you interacted with."
                chidori "{i}One of them, was me."
                hide schi0402 onlayer mcsprite
                aaron "Any news yet?"
                wesley "I was able to get into contact with one of the ''bitches'' that Kristik talked to."
                hide schi0402 onlayer mcsprite
                hide aaron_8s
                show aaron_9s:
                    ypos 195
                    zoom 0.55
                aaron "Well... how did it go?"
                wesley "She luckily, agreed."
                aaron "How'd you manage that?"
                hide wesley_1s
                show wesley_2s_w:
                    xpos 800
                    ypos 100
                    zoom 0.6
                with dissolve
                wesley "I said that her and her friends will be captured and taken to an NTR slave ring where they will spend the rest of their lives in Ghana."
                hide aaron_9s
                show aaron_4s:
                    ypos 195
                    zoom 0.55                
                aaron "What the fuck???!"
                kristik "{i}What the fuck??!!!! Did he really tell you that???"
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}Yeah, he did."     
                hide schi0402 onlayer mcsprite     
                aaron "Why the hell... would you ever say that??!!!"
                wesley "It worked. So why not, right?"
                hide aaron_4s
                show aaron_9s:
                    ypos 195
                    zoom 0.55   
                aaron "I don't even have the resources for an NTR slave ring in Ghana, hell I've never even been to Ghana! What the fuck makes you think I can afford to run some stupid shit like that?!?!"         
                aaron "How the hell did she even believe you in the first place, that shit sounds stupid as hell!"    
                wesley "I took gruesome photos from Reddit and said this is what it looks like."
                hide aaron_9s
                show aaron_4s:
                    ypos 195
                    zoom 0.55                
                aaron "Jesus christ..."
                kristik "{i}Jesus christ..." 
                hide wesley_2s_w
                hide aaron_4s
                hide office
                show white
                with dissolve
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}After that, they told me that they will be building an underground bunker to hold the Xi Jingping bot 9000 under my house."                                 
                hide schi0402 onlayer mcsprite
                show schi0401 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                kristik "{i}How the fuck would you ever let anybody build an underground bunker under your house?!?!!"
                hide schi0401 onlayer mcsprite
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}Like I said, I didn't want to get kidnapped! I had to do it!"  
                hide schi0402 onlayer mcsprite
                hide white
                with dissolve
                show BG001    
                show aaron_7:
                    xpos 500
                    ypos 60
                    zoom 0.4
                with dissolve      
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}After that, Aaron came to my house and started construction on the underground bunker."  
                hide schi0402 onlayer mcsprite
                aaron "So, we're going to need you to bait Kristik into being his GF."
                aaron "Then, I can kill him with the Xi Jingping Bot 9000."
                aaron "If it doesn't work, take these."
                chidori "What are these?"
                aaron "It's the cock and ball torture-inator."
                aaron "It will surely destroy his little balls."
                chidori "Then, after this, I won't be involved in any more... things?"
                hide aaron_7
                show aaron_11:
                    xpos 500
                    ypos 60
                    zoom 0.34     
                aaron "ugh... goddamnit."
                hide aaron_11
                show aaron_11_1:
                    xpos 500
                    ypos 60
                    zoom 0.34     
                aaron "Look, all that NTR Ghana Slave ring shit was completely fake, I seriously am not going to do that anyway, I don't have the money."
                chidori "Wait... so that was a lie?"
                hide aaron_11_1
                show aaron_7:
                    xpos 500
                    ypos 60
                    zoom 0.4
                aaron "Yup."       
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}To be honest, I was pretty pissed that he lied about that."
                hide schi0402 onlayer mcsprite
                show schi0401 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8                
                hide schi0401 onlayer mcsprite                  
                kristik "{i}Why the fuck would you be pissed about that???!!! Isn't good that it was a lie?!!"                                         
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}Yeah, but he made me worried for no reason in the first place!!!"
                hide schi0402 onlayer mcsprite
                chidori "So wait... what would you have done if I didn't let you build a secret underground bunker?"
                aaron "psshhhh tbh IDK. we probably woulda just asked someone else on shaadi.com or something"
                kristik "{i}Bruh... shaadi.com..."
                hide schi0401 onlayer mcsprite
                show schi0402 onlayer mcsprite:
                    xpos -50
                    ypos 500
                    zoom 0.8
                chidori "{i}I didn't know what that was, but I didn't care to ask."
                hide aaron_7
                hide BG001
                show white
                with dissolve
                chidori "{i}After that, I was told to bait you to my house and then he would activate the Xi Jingping bot."
                hide schi0402 onlayer mcsprite  
                stop music fadeout 2.0
                with dissolve
                hide white
                show BG124
                show schi0401:
                    xpos 350
                    zoom 1.2    
                with dissolve
                play music "audio/Sanoba Witch OST - Sweet Treasure(QuietVer.)-(128kbps).ogg"
                kristik "So... why did you decide to kill Aaron instead?"           
                hide schi0401
                show schi0411:
                    xpos 350
                    zoom 1.2
                chidori "Well... it's just because...."
                hide schi0411
                show schi0408:
                    xpos 350
                    zoom 1.2
                chidori "umm...."
                hide schi0408
                show schi0409:
                    xpos 350
                    zoom 1.2
                chidori "I just like you..."
                hide schi0409
                show schi0408:
                    xpos 350
                    zoom 1.2
                kristik "So... you just committed homicide with a deadly wepaon... cause you thought it was all UwU i like you type shit???????!!!"
                hide schi0408
                show schi0409:
                    xpos 350
                    zoom 1.2
                chidori "Yeah..."
                hide schi0409
                show schi0408:
                    xpos 350
                    zoom 1.2
                $ show_quick_menu = False
                window hide
                menu:
                    "''Bro. IM NOT HELPING YOU IN COURT IF YOU GON GET HIT WITH MURDER CHARGES''":
                        $ show_quick_menu = True
                        window show
                        kristik "Bro. IM NOT HELPING YOU IN COURT IF YOU GON GET HIT WITH MURDER CHARGES"
                        hide schi0408
                        #======================================================================================================
                        # PLAY GUN LOADING SOUNDS
                        #====================================================================================================== 
                        stop music
                        play sound "audio/gunload_Master.wav"                      
                        show schi0405:
                            xpos 350
                            zoom 1.2
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6  
                        $ renpy.pause(0.8,hard=True)                                                           
                        kristik "WAIT CHILL!!!!"
                        #======================================================================================================
                        # PLAY GUN SHOOTING SOUNDS
                        #======================================================================================================
                        play sound "audio/awp.mp3"
                        show white  
                        window hide 
                        $ show_quick_menu = False
                        with dissolve
                        $ renpy.pause(1,hard=True)
                        window show
                        with dissolve             
                        narrator "Kristik was killed due to a fatal shot in the chest."
                        narrator "His body disintegrated into the air."
                        narrator "{b}Bad ending 2/21{/b}"
                        if (persistent.endingFinished2 < 1):
                            $ persistent.endingFinished2 += 1
                        elif (persistent.endingFinished2 >= 1):
                            pass
                        else:
                            narrator "PERSISTENT DATA FAILURE FOR SECTION 8937. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                            $ renpy.quit()
                        window hide
                        with dissolve                
                        $ MainMenu(confirm=False)()
                    "''its ok bb. i still wuv u.''":
                        $ show_quick_menu = True
                        window show
                        $ EXPchidori += 2         
                        kristik "its ok bb. i still wuv u."  
                        hide schi0408
                        show schi0404:
                            xpos 350
                            zoom 1.2
                        chidori "Really??!!"   
                        hide schi0404
                        show schi0403:
                            xpos 350
                            zoom 1.2
                        kristik "Umm.. yeah... sure..."
                        kristikmind "{i}Dis bitch is cray-cray but whatever... it dont matter..."
                        kristikmind "{i}if anything it means she more freaky deaky >3>"
                        stop music fadeout 2.0
                        hide schi0403
                        hide BG124
                        with dissolve
                        window hide 
                        $ show_quick_menu = False
                        with dissolve
                        $ renpy.pause(2,hard=True)
                        "{b}Good ending 13/21" 
                        if (persistent.endingFinished13 < 1):
                            $ persistent.endingFinished13 += 1
                        elif (persistent.endingFinished13 >= 1):
                            pass
                        else:
                            narrator "PERSISTENT DATA FAILURE FOR SECTION 8972. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                            $ renpy.quit()
                        $ renpy.pause(2,hard=True) 
                        $ MainMenu(confirm=False)()
            else:
                hide schi0408
                show schi0409:
                    xpos 350
                    zoom 1.2
                chidori "I'm sorry Kristik..."  
                chidori "I need to do what I'm told." 
                hide schi0409
                show schi0408:
                    xpos 350
                    zoom 1.2  

                play sound "audio/femurscream1.ogg"
                #========================================================================================      
                # PLAY FEMUR BREAKER SOUNDS AND BONE BREAKING SOUNDS
                #========================================================================================    

                show white
                $ renpy.pause(0.001,hard=True)
                hide white
                with Dissolve(1)
                kristik "OWWW!!! MY LEFT BALLS!!!!"
                #========================================================================================      
                # PLAY FEMUR BREAKER SOUNDS AND BONE BREAKING SOUNDS
                #========================================================================================    
                stop music fadeout 2.0
                play sound "audio/femurscream2.ogg"
                show white
                window hide
                $ show_quick_menu = False
                with dissolve
                $ renpy.pause(3,hard=True)
                window show
                with dissolve                
                narrator "Kristik's cock and balls were destroyed."
                narrator "He died from shock due to his balls being destroyed."
                narrator "{b}Bad ending 1/21{/b}"
                if (persistent.endingFinished1 < 1):
                    $ persistent.endingFinished1 += 1
                elif (persistent.endingFinished1 >= 1):
                    pass
                else:
                    narrator "PERSISTENT DATA FAILURE FOR SECTION 9025. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                    $ renpy.quit()
                window hide
                with dissolve                
                $ renpy.pause(3,hard=True)
                $ MainMenu(confirm=False)()


    elif EXPyuzuriha and EXPnerine >= 2:
        play music "audio/Sanoba Witch OST Real Friend InstVer 128k.ogg"
        show BG011
        with dissolve
        $ show_quick_menu = True
        window show
        with dissolve
        show syuz0101:
            xpos 100
            zoom 1.2
        show sner0101:
            xpos 600
            zoom 1.2
        with dissolve
        hide syuz0101
        show syuz0102:
            xpos 100
            zoom 1.2
        yuzuriha "Hey~!"
        hide syuz0102
        show syuz0101:
            xpos 100
            zoom 1.2
        kristik "Hm...?"
        hide syuz0101
        show syuz0102:
            xpos 100
            zoom 1.2
        yuzuriha "Who was that super-hottie with the glasses?"
        hide syuz0102
        show syuz0101:
            xpos 100
            zoom 1.2
        kristik "Oh... you mean... Jason...?"
        hide syuz0101
        show syuz0106:
            xpos 100
            zoom 1.2
        yuzuriha "hehe... yeah that one."
        kristikmind "{i}fuck bro... its always JASON thats getting the bitches..."
        kristikmind "{i}he won in the bitches arms race of 2025..."
        kristikmind "{i}AND HES GAY!!! THAT SHIT MAKES IT EVEN WORSE!!"
        kristik "Um.. what about him?"
        hide syuz0106
        show syuz0102:
            xpos 100
            zoom 1.2
        yuzuriha "Could you maybe... introduce him to me?"
        hide syuz0102
        show syuz0113:
            xpos 100
            zoom 1.2
        kristik "What's the point? You already talked to him before."
        hide syuz0113
        show syuz0112:
            xpos 100
            zoom 1.2
        yuzuriha "Tch... party pooper."
        hide syuz0112
        show syuz0110:
            xpos 100
            zoom 1.2
        kristik "Doesn't really matter anyways, you know his name now."
        hide sner0101
        show sner0208:
            xpos 600
            zoom 1.2
        nerine "Kristik, are you sure you're okay?"
        nerine "To me, it sounds like... you're jealous."
        hide sner0208
        show sner0201:
            xpos 600
            zoom 1.2
        hide syuz0110
        show syuz0108:
            xpos 100
            zoom 1.2
        yuzuriha "HAHAHAHAH LOOLLLL"
        hide syuz0108
        show syuz0107:
            xpos 100
            zoom 1.2
        yuzuriha "REALLY??!!!"
        hide syuz0107
        show syuz0206:
            xpos 100
            zoom 1.2
        yuzuriha "Are you really jealous?"
        $ show_quick_menu = False
        window hide
        menu:
            "''Hell no I couldn't give 18 shits abt u BITCH''":
                $ show_quick_menu = True
                window show
                kristik "Hell no I couldn't give 18 shits abt u BITCH"
                hide syuz0206
                show syuz0112:
                    xpos 100
                    zoom 1.2
                hide sner0201
                show sner0210:
                    xpos 600
                    zoom 1.2
                yuzuriha "Wow... rude."
                hide sner0210
                show sner0208:
                    xpos 600
                    zoom 1.2
                nerine "No need to get so mad, it's quite alright; everybody is different."
                hide sner0208
                show sner0203:
                    xpos 600
                    zoom 1.2
                kristik "Well, I appreciate that Nerine, unlike SOMEBODY else here who isn't as considerate."
                hide syuz0112
                show syuz0113:
                    xpos 100
                    zoom 1.2
                yuzuriha "It's not my fault you got the figure of a beanbag..."
                kristikmind "{i}... this mf bitch..."
                hide sner0203
                show sner0101:
                    xpos 600
                    zoom 1.2
                hide syuz0113
                show syuz0101:
                    xpos 100
                    zoom 1.2
                jump nextpartThree
            "''N-no.... i-i-i-i-i-it's not like I'm jealous or anything... b-b-b-b-BAKA!!!!''":
                $ show_quick_menu = True
                window show
                $ EXPyuzuriha += 1
                $ EXPnerine += 1
                kristik "N-no.... i-i-i-i-i-it's not like I'm jealous or anything... b-b-b-b-BAKA!!!!"
                hide syuz0206
                show syuz0111:
                    xpos 100
                    zoom 1.2
                hide sner0201
                show sner0108:
                    xpos 600
                    zoom 1.2    
                yuzuriha "Huh...??"
                nerine "...?"
                hide sner0108
                show sner0105:
                    xpos 600
                    zoom 1.2
                hide syuz0111
                show syuz0108:
                    xpos 100
                    zoom 1.2
                yuzuriha "HAHAAHHAHAHAHA ALOLOLOLOLOLOLOLO"
                nerine "Hahahahaha!!"
                kristikmind "{i}i thought acting like a girl would help alleviate the situation..."
                hide sner0105
                show sner0101:
                    xpos 600
                    zoom 1.2
                hide syuz0108
                show syuz0107:
                    xpos 100
                    zoom 1.2
                yuzuriha "What was the point of that?!"
                hide syuz0107
                show syuz0109:
                    xpos 100
                    zoom 1.2
                kristik "I thought it would be more funny, no?"
                hide sner0101
                show sner0105:
                    xpos 600
                    zoom 1.2
                nerine "Don't worry! Yuzuriha likes that kind of cute personality anyways."
                hide sner0105
                show sner0101:
                    xpos 600
                    zoom 1.2
                hide syuz0109
                show syuz0101:
                    xpos 100
                    zoom 1.2
        label nextpartThree:
            kristik "Anyways, you wanted to see Jason?"
            hide syuz0101
            show syuz0102:
                xpos 100
                zoom 1.2
            yuzuriha "Yes!!!"
            hide syuz0102
            show syuz0101:
                xpos 100
                zoom 1.2
            kristik "Ok. Let me call him up."
            hide syuz0101
            hide sner0101
            with dissolve

            #========================================================================================================================================================================
            #PLAY PHONE DIALING SOUND
            #========================================================================================================================================================================
            play sound "audio/dialing.ogg"

            $ renpy.pause(10,hard=True)
            stop sound
            jason "Yo."
            kristik "Hey Jason."
            jason "The fuck you want kristik..?"
            kristik "You know that girl... silver hair?"
            jason "Oh yeah that hottie. What about her?"
            kristik "Well... first of all I KNOW you're gay. So you probably don't think she's hot."
            jason "..."
            jason "...how do you know that I am gay?"
            kristik "Kyle told me. He said he read it somewhere from your diary."
            jason "...THAT FUCKING BITCH!!!"
            jason "I KNEW HE WAS DOING SOMETHING WEIRD IN MY ROOM!!"
            jason "I WAS WONDERING WHO'S NUT WAS ON MY DESK!!"
            kristikmind "{i}tf???? kyle nutting to his diary????"
            kristikmind "{i}shit must be REALLY freaky deaky up in that diary...."
            kristik "anyways... Yuzuriha wants to meet you. She probably likes you."
            jason "Tell her I'm gay."
            kristik "What???? She's not gonna believe that."
            kristik "You just come here and say that yourself."
            jason "The fuck? Hell no I'm not coming out just to tell someone I'm gay. You just do it. Bye."
            #========================================================================================================================================================================
            #PLAY IPHONE DISCONNECT CALL SOUND
            #========================================================================================================================================================================

            play sound "audio/iphonehangup.ogg"
            $ renpy.pause(1,hard=True)     
            kristik "Goddamnit.... leaving me to the fucking dirty work you bitch..."
            show sner0101:
                xpos 600
                zoom 1.2
            show syuz0101:
                xpos 100
                zoom 1.2  
            with dissolve
            hide syuz0101
            show syuz0102:
                xpos 100
                zoom 1.2
            yuzuriha "Well....?"
            yuzuriha "When's he coming??!"   
            hide syuz0102
            show syuz0101:
                xpos 100
                zoom 1.2
            kristik "Ummm...."
            kristik "He's... uh..."
            hide syuz0101
            show syuz0111:
                xpos 100
                zoom 1.2
            yuzuriha "Well???!"
            kristik "Jason is gay...."
            kristik "He doesn't like girls..."
            hide syuz0111
            show syuz0112:
                xpos 100
                zoom 1.2
            yuzuriha "Oh..."
            hide syuz0112
            show syuz0111:
                xpos 100
                zoom 1.2
            yuzuriha "Well... I suppose it doesn't matter that much then."
            kristikmind "{i}What...?"
            hide syuz0111
            show syuz0106:
                xpos 100
                zoom 1.2
            yuzuriha "Never mind that, do you know what polygamy is?"
            kristik "umm... why are you asking me that?"
            hide syuz0106
            show syuz0110:
                xpos 100
                zoom 1.2
            yuzuriha "Answer the question."
            kristik "its like the thing where you marry more than one spouse right?"
            hide syuz0110
            show syuz0206:
                xpos 100
                zoom 1.2
            yuzuriha "How would you like to engage in some devious polygamy with us?"
            kristikmind "{i}WHAT???"
            kristikmind "{i}TF SHE MEAN BY ''DEVIOUS''???!!"
            hide sner0101
            show sner0106:
                xpos 600
                zoom 1.2
            nerine "A little bit strange, but I suppose it will work."
            hide sner0106
            show sner0103:
                xpos 600
                zoom 1.2
            kristikmind "{i}what??!??! what will work??!!! my indian brain is melting rn..."
            hide syuz0206
            show syuz0102:
                xpos 100
                zoom 1.2
            yuzuriha "Alright! It's settled."
            hide syuz0102
            show syuz0101:
                xpos 100
                zoom 1.2
            kristik "WHAT???!!! NONOONONONONONO"
            hide syuz0101
            show syuz0111:
                xpos 100
                zoom 1.2
            kristik "THIS SHIT IS WAY TOO FAST!!! WHY ARE YOU DOING THIS?!!"
            hide syuz0111
            show syuz0112:
                xpos 100
                zoom 1.2
            yuzuriha "Are you saying... that you wouldn't marry us?!"
            kristik "NONONONO... its just why thO??"
            hide syuz0112
            show syuz0108:
                xpos 100
                zoom 1.2
            yuzuriha "Alright it's settled!! We'll meet you at the Clerk Recorder's office so you can fill out the documents."
            kristik "WHAT?!!!!"
            yuzuriha "Bye!"
            hide syuz0108
            hide sner0103
            with dissolve
            kristik "What the fuck..."
            show jason (11):
                xpos 400
                ypos 20
                zoom 0.6
            with dissolve
            jason "What the fuck is this marriage shit about?"
            kristik "OH SHIT!!"
            kristik "WHAT ARE YOU DOING HERE??!! I THOUGHT YOU WERE TOO LAZY???"
            hide jason (11)
            show jason (90):
                xpos 400
                ypos 20
                zoom 0.6
            jason "I just decided to see what the hell you were on about."
            hide jason (90)
            show jason (89):
                xpos 400
                ypos 20
                zoom 0.6
            jason "Turns out you're getting married... to some BITCHES??!!"
            kristik "Wait... why do you care? You're gay."
            hide jason (89)
            show jason (7):
                xpos 400
                ypos 20
                zoom 0.6
            jason "IF YOU GET MARRIED IT MEANS THAT THERES ONE LESS DICK TO SUCK!!!"
            kristik "ew...."
            hide jason (7)
            show jason (10):
                xpos 400
                ypos 20
                zoom 0.6
            jason "More importantly... Aaron and Wesley are apparently in the city."
            jason "We've recieved intel that it is the Xi Jingping bot 9000; it's the bot that killed Obama in Kristik Saga 2."
            hide jason (10)
            show jason (9):
                xpos 400
                ypos 20
                zoom 0.6
            kristik "The fuck??? Obama died???"
            hide jason (9)
            show jason (10):
                xpos 400
                ypos 20
                zoom 0.6
            jason "This happened while you were passed out from drinking Bill's piss."
            jason "Xi jingping and the Chinese navy pulled up to a revolver duel against Obama. Obama lost and died later."
            jason "Apparently, that Xi Jingping was just a bot created by Aaron and Wesley to destroy our allies."
            jason "So if you find anything that looks like Winnie the Pooh or Xi Jingping, kill it immediately."
            hide jason (10)
            show jason (9):
                xpos 400
                ypos 20
                zoom 0.6
            kristik "Uhhh... sure..."
            hide jason (9)
            show jason (10):
                xpos 400
                ypos 20
                zoom 0.6
            jason "Alright im outta here."
            hide jason (10)
            show jason (11):
                xpos 400
                ypos 20
                zoom 0.6   
            jason "You better not have any fucking kids when we come back."        
            kristik "Chill bro... those girls like you anyways."
            hide jason (11)
            show jason (4): 
                xpos 400
                ypos 20
                zoom 0.6
            jason "Really??!! hawewehawehahwehehehehe....."
            hide jason (4)
            show jason (50):
                xpos 400
                ypos 20
                zoom 0.6
            jason "I wish I were a girl..."
            kristik "Sussy...."
            stop music fadeout 2.0
            hide jason (50)
            hide BG011
            with dissolve
            window hide 
            $ show_quick_menu = False
            with dissolve
            $ renpy.pause(3,hard=True)
            window show 
            $ show_quick_menu = True
            with dissolve          
            show BG021
            play music "audio/Sanoba Witch OST - Dekiru-Kana_-128k.ogg"
            with dissolve
            show syuz0101:
                xpos 100
                zoom 1.2
            show sner0101:
                xpos 600
                zoom 1.2
            with dissolve
            hide syuz0101
            show syuz0102:
                xpos 100
                zoom 1.2
            yuzuriha "Alright Kristik, remember they're going to ask you some questions. Just make up any of the answers, and then tell us what you said after you're done."
            yuzuriha "They take stuff here REALLY seriously, so make sure you answer SERIOUSLY. Good luck in there!"
            hide syuz0102
            show syuz0101:
                xpos 100
                zoom 1.2
            kristik "Ok. Thanks...?"
            hide syuz0101
            hide sner0101
            with dissolve
            hide BG021
            show BG022
            with dissolve
            show girl1 (1) onlayer master1:
                xpos -50
                ypos 40
                zoom 0.6
            show girl3 (28) onlayer master2:
                xpos 120
                zoom 0.6
            show guy1 (1) onlayer master3:
                xpos 550
                zoom 0.6
            show guy2 (28) onlayer master4:
                xpos 800
                zoom 0.6
            with dissolve
            hide guy2 (28) onlayer master4
            show guy2 (27) onlayer master4:
                xpos 800
                zoom 0.6
            toshiro "Welcome to our office!"
            hide guy2 (27) onlayer master4
            show guy2 (28) onlayer master4:
                xpos 800
                zoom 0.6
            kristikmind "{i}Holy shit... these guys are so posh..."
            hide guy1 (1) onlayer master3
            show guy1 (9) onlayer master3:
                xpos 550
                zoom 0.6
            rudolf "We're the agency that you signed up to get this marriage through, right?"
            hide guy1 (9) onlayer master3
            show guy1 (1) onlayer master3:
                xpos 550
                zoom 0.6
            kristik "Uhh... yeah..."
            hide girl3 (28) onlayer master2
            show girl3 (3) onlayer master2:
                xpos 120
                zoom 0.6
            ange "Who the hell is this kid and how did he manage to even get married in the first place?"
            hide guy2 (28) onlayer master4
            show guy2 (1) onlayer master4:
                xpos 800
                zoom 0.6                  
            hide guy1 (1) onlayer master3
            show guy1 (7) onlayer master3:
                xpos 550
                zoom 0.6 
            hide girl3 (3) onlayer master2
            show girl3 (19) onlayer master2:
                xpos 120
                zoom 0.6                             
            kristikmind "{i}Who the hell is that chick and why is she so annoyed?"
            hide girl1 (1) onlayer master1
            show girl1 (20) onlayer master1:
                xpos -50
                ypos 40
                zoom 0.6
            natsuhi "Ange, how many times have I told you to not roast the client?"  
            hide girl1 (20) onlayer master1
            show girl1 (9) onlayer master1:
                xpos -50
                ypos 40
                zoom 0.6
            hide girl3 (19) onlayer master2
            show girl3 (10) onlayer master2:
                xpos 120
                zoom 0.6
            ange "Yeah, but how the hell is THIS kid getting married? And it's a polygamy, no less!"      
            hide girl3 (10) onlayer master2
            show girl3 (11) onlayer master2:
                xpos 120
                zoom 0.6
            kristikmind "{i}this bitch is HELLA salty LOOLLOLLO"
            hide girl1 (9) onlayer master1
            show girl1 (44) onlayer master1:
                xpos -50
                ypos 40
                zoom 0.6
            natsuhi "This is why we can't get any clients..."
            hide guy2 (7) onlayer master4
            show guy2 (34) onlayer master4:
                xpos 800
                zoom 0.6
            toshiro "I apologize for that, let me explain how this process will go."
            hide guy1 (7) onlayer master3
            show guy1 (1) onlayer master3:
                xpos 550
                zoom 0.6
            hide girl1 (44) onlayer master1    
            show girl1 (1) onlayer master1:
                xpos -50
                ypos 40
                zoom 0.6
            hide girl3 (11) onlayer master2    
            show girl3 (28) onlayer master2:
                xpos 120
                zoom 0.6                
            toshiro "We will help you with every part of the paperwork here. I will help you with the basic forms, Rudolf will help you with the tax related stuff, Ange will ''help'' with Clerk-recorder stuff, and Natsuhi will be involved with finalizing the documents."
            toshiro "Let's start with filling out your paperwork."
            hide guy2 (34) onlayer master4
            show guy2 (28) onlayer master4:
                xpos 800
                zoom 0.6     
            kristik "Uhh... sure..."  
            hide guy1 (7) onlayer master3
            hide girl1 (1) onlayer master1    
            hide girl3 (28) onlayer master2 
            hide guy2 (28) onlayer master4  
            with dissolve
            hide BG022
            with dissolve
            show BG004Y
            show page1:
                xpos 650
                zoom 0.5
            with dissolve
            show guy2 (28):
                xpos 50
                zoom 0.6
            with dissolve
            hide guy2 (28)
            show guy2 (34):
                xpos 50
                zoom 0.6
            toshiro "Let's take a look at the document."
            hide guy2 (34)
            show guy2 (28):
                xpos 50
                zoom 0.6            
            show page1_square1:
                xpos 650
                zoom 0.5
            $ renpy.pause(0.01,hard=True)
            hide page1_square1
            with Dissolve(0.5)
            show page1_square1:
                xpos 650
                zoom 0.5
            $ renpy.pause(0.01,hard=True)
            hide page1_square1
            with Dissolve(0.5)
            hide guy2 (28)
            show guy2 (34):
                xpos 50
                zoom 0.6            
            toshiro "On the top of the document, we have some information about our government's laws regarding the marriage license."
            toshiro "Bigomy, or marrying while already married is illegal, however we can pull you through a loophole that will allow us to make this possible."
            hide guy2 (34)
            show guy2 (28):
                xpos 50
                zoom 0.6            
            show page1_square2:
                xpos 650
                zoom 0.5
            $ renpy.pause(0.01,hard=True)
            hide page1_square2
            with Dissolve(0.5)
            show page1_square2:
                xpos 650
                zoom 0.5
            $ renpy.pause(0.01,hard=True)
            hide page1_square2
            with Dissolve(0.5)
            hide guy2 (28)
            show guy2 (34):
                xpos 50
                zoom 0.6            
            toshiro "Below that section, is the type of marriage license that will be required. What kind of marriage license are you seeking for?"   
            hide guy2 (34)
            show guy2 (28):
                xpos 50
                zoom 0.6  
            kristik "ZzzZZZZzzzzz..."
            hide guy2 (28)
            show guy2 (30):
                xpos 50
                zoom 0.6 
            toshiro "Uhh.... sir?"
            hide guy2 (30)
            show guy2 (29):
                xpos 50
                zoom 0.6 
            kristik "Zzz..... h-huh??? Oh sorry, I just fell asleep, cause this shit was so boring already LOLOLL"
            kristik "ill uhh... do the normal one, the first one..."
            hide guy2 (29)
            show guy2 (30):
                xpos 50
                zoom 0.6 
            toshiro "Uhh... sure..."
            hide guy2 (30)
            hide page1
            with dissolve
            show page2:
                xpos 650
                zoom 0.5
            with dissolve
            show guy2 (28):
                xpos 50
                zoom 0.6
            with dissolve
            hide guy2 (28)
            show guy2 (34):
                xpos 50
                zoom 0.6 
            toshiro "Page 2 requires your personal information."      
            toshiro "What is your first and last name?"
            hide guy2 (34)
            show guy2 (28):
                xpos 50
                zoom 0.6   
            $ show_quick_menu = False
            window hide 
            menu:
                "''Quandale Dingle Bartholomew Wilson Wolfgang Binglewood the Third.''":
                    $ show_quick_menu = True
                    window show
                    kristik "Quandale Dingle Bartholomew Wilson Wolfgang Binglewood the Third."
                    hide guy2 (28)
                    show guy2 (30):
                        xpos 50
                        zoom 0.6 
                    toshiro "Uhh.... are you really sure that's your real name?"
                    kristik "Yes."
                    hide guy2 (30)
                    show guy2 (29):
                        xpos 50
                        zoom 0.6   
                    toshiro "If you say so...."                                                          
                "''Kristik Lal.''":
                    $ show_quick_menu = True
                    window show
                    kristik "Kristik Lal."
                    hide guy2 (28)
                    show guy2 (34):
                        xpos 50
                        zoom 0.6 
                    toshiro "Alright."   
                    $ EXPyuzuriha += 1
                    $ EXPnerine += 1
            hide guy2 (34)
            hide guy2 (29)                 
            show guy2 (34):
                xpos 50
                zoom 0.6
            toshiro "What is your date of birth and birthplace?"
            $ show_quick_menu = False
            window hide
            menu:
                "''March 17th, 2005. I was born in Suva, Fiji.''":
                    $ show_quick_menu = True
                    window show
                    kristik "March 17th, 2005. I was born in Suva, Fiji." 
                    hide guy2 (28)
                    show guy2 (34):
                        xpos 50
                        zoom 0.6 
                    toshiro "Ok. Got that down. Now..."  
                    $ EXPyuzuriha += 1
                    $ EXPnerine += 1                                         
                "''April 1st, 1837. I was born in the coal mines of Wyoming.''":
                    $ show_quick_menu = True
                    window show
                    kristik "April 1st, 1837. I was born in the coal mines of Wyoming."
                    hide guy2 (28)
                    show guy2 (30):
                        xpos 50
                        zoom 0.6 
                    toshiro "Look, you have to take this more seriously."
                    kristik "I am. It's the cold hard fax."
                    hide guy2 (30)
                    show guy2 (29):
                        xpos 50
                        zoom 0.6   
                    toshiro "Whatever..."  
            hide guy2 (34)
            hide guy2 (29)                 
            show guy2 (34):
                xpos 50
                zoom 0.6
            toshiro "Where do you currently live?"
            $ show_quick_menu = False
            window hide
            menu:
                "''1337 Ganja Street, State of Weed, Marsian Surface. ZIP: 42069''":
                    $ show_quick_menu = True
                    window show
                    kristik "1337 Ganja Street, State of Weed, Marsian Surface. ZIP: 42069"
                    hide guy2 (28)
                    show guy2 (29):
                        xpos 50
                        zoom 0.6   
                    toshiro "ugh... whatever... i dont give a shit about this..."
                    kristikmind "{i}I know they told me to make it serious, but IDGAF LOLOOLOLl"  
                    hide guy2 (28)
                    show guy2 (30):
                        xpos 50
                        zoom 0.6 
                    toshiro "Excuse me for a second."                                     
                "''223 E 30th St, Kearney, Nebraska. ZIP: 68847''":   
                    $ show_quick_menu = True
                    window show
                    kristik "223 E 30th St, Kearney, Nebraska. ZIP: 68847"
                    hide guy2 (28)
                    show guy2 (34):
                        xpos 50
                        zoom 0.6 
                    toshiro "Alright. This should be it, you don't have anything else to do."  
                    $ EXPyuzuriha += 1
                    $ EXPnerine += 1                        
            hide page2
            hide guy2 (34)
            hide guy2 (30) 
            hide BG004Y
            stop music fadeout 2.0
            with dissolve
            $ renpy.pause (1,hard=True)
            if (EXPyuzuriha <= 5):
                show BG022
                play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
                with dissolve
                show girl1 (1) onlayer master1:
                    xpos -50
                    ypos 40
                    zoom 0.6
                show girl3 (28) onlayer master2:
                    xpos 120
                    zoom 0.6
                show guy1 (1) onlayer master3:
                    xpos 550
                    zoom 0.6
                show guy2 (29) onlayer master4:
                    xpos 800
                    zoom 0.6
                with dissolve
                hide guy2 (29) onlayer master4
                show guy2 (30) onlayer master4:
                    xpos 800
                    zoom 0.6
                toshiro "It's one of those stupid clients again...."
                hide girl1 (1) onlayer master1
                show girl1 (44) onlayer master1:
                    xpos -50
                    ypos 40
                    zoom 0.6
                hide girl3 (28) onlayer master2
                show girl3 (12) onlayer master2:
                    xpos 120
                    zoom 0.6
                hide guy1 (1) onlayer master3
                show guy1 (4) onlayer master3:
                    xpos 550
                    zoom 0.6
                
                rudolf "Goddmanit... why do we always get those kinds of guys?"
                ange "I told you so guys... he's a nutcase."
                natsuhi "Ugh.... how about...."
                hide girl3 (12) onlayer master2
                show girl3 (18) onlayer master2:
                    xpos 120
                    zoom 0.6                
                hide girl1 (44) onlayer master1
                show girl1 (52) onlayer master1:
                    xpos -50
                    ypos 40
                    zoom 0.6     
                natsuhi "WE KILL HIM!"    
                hide girl1 (52) onlayer master1
                show girl1 (55) onlayer master1:
                    xpos -50
                    ypos 40
                    zoom 0.6 
                hide guy1 (4) onlayer master3
                show guy1 (52) onlayer master3:
                    xpos 460
                    zoom 0.6    
                rudolf "I second that decision!"
                hide girl3 (18) onlayer master2
                show girl3 (16) onlayer master2:
                    xpos 120
                    zoom 0.6  
                ange "Now you guys are thinking!"  
                hide guy2 (30) onlayer master4
                show guy2 (29) onlayer master4:
                    xpos 800
                    zoom 0.6
                toshiro "Ughh... I guess it had to come to this."
                hide guy2 (29) onlayer master4
                show guy2 (32) onlayer master4:
                    xpos 800
                    zoom 0.6
                toshiro "THACH FEDERATION!!!"  
                hide guy2 (32) onlayer master4
                hide guy1 (52) onlayer master3
                hide girl3 (16) onlayer master2
                hide girl1 (55) onlayer master1
                with dissolve
                show girl7 (5) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (9) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (2) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (3) onlayer master4:
                    xpos 900
                    zoom 0.6
                with dissolve
                unknown "YES SIR!!"
                hide girl4 (3) onlayer master4
                hide girl6 (2) onlayer master3
                hide girl5 (9) onlayer master2
                hide girl7 (5) onlayer master1                
                show guy2 (32) onlayer mcsprite:
                    xpos -70
                    ypos 520
                    zoom 0.5
                show girl7 (1) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (7) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (3) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (1) onlayer master4:
                    xpos 900
                    zoom 0.6                
                toshiro "I NEED YOU GUYS TO BARRICADE THE AREA AND GRAB YOUR WEAPONS! WE KILLING TONIGHT!"
                hide guy2 (32) onlayer mcsprite
                hide girl4 (1) onlayer master4
                hide girl6 (3) onlayer master3
                hide girl5 (7) onlayer master2
                hide girl7 (1) onlayer master1                
                show girl7 (5) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (9) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (2) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (3) onlayer master4:
                    xpos 900
                    zoom 0.6
                unknown "YES SIR!!! WILL DO SIR!!!"
                hide girl4 (3) onlayer master4
                hide girl6 (2) onlayer master3
                hide girl5 (9) onlayer master2
                hide girl7 (5) onlayer master1  
                with dissolve
                hide BG022
                with dissolve
                $ renpy.pause (1,hard=True)                   
                show BG004Y
                with dissolve
                kristik "Where the hell did he go...?"
                kristik "We didn't even fill out the taxes..." 
                show guy2 (33):
                    xpos 400
                    zoom 0.6
                with dissolve
                kristik "oh hey. youre finally back. What took you so long?"
                hide guy2 (33)
                show guy2 (30):
                    xpos 400
                    zoom 0.6        
                toshiro "Unfortunately, due to your reponses, we have decided to terminate this relationship."
                hide guy2 (30)
                show guy2 (29):
                    xpos 400
                    zoom 0.6  
                kristik "What??!! But I answered truthfully on ALL of the questions!"
                hide guy2 (33)
                show guy2 (30):
                    xpos 400
                    zoom 0.6        
                toshiro "There's no use in lying."
                hide guy2 (30)
                show guy2 (32):
                    xpos 400
                    zoom 0.6  
                stop music
                toshiro "KILL HIM!!!!"
                kristik "WHAT???!!!"
                hide guy2 (32)
                with dissolve
                show guy1 (72):
                    xpos 600
                    zoom 0.6
                show girl1 (119):
                    ypos 40
                    xpos 100
                    zoom 0.6
                with dissolve
                rudolf "Sorry kid, it's just company policy."
                kristik "WHAT THE FUCK KIND OF POLICY IS THAT?!?!?!"
                kristik "IM OUTTA HERE!!!"
                #===========================================================================================================================================================================
                # INSERT RUNNING SOUNDS
                #===========================================================================================================================================================================
                hide girl1 (119)
                hide guy1 (72)
                with dissolve
                play music "audio/Riddle Joker OST _ Invisibly Faster-(128kbps) intro.ogg"
                queue music "audio/Riddle Joker OST _ Invisibly Faster-(128kbps).ogg"
                show guy2 (32):
                    xpos 400
                    zoom 0.6  
                with dissolve
                toshiro "HE'S RUNNING!11!1!!!!! JUST SHOOT HIM!!!"
                hide BG004Y
                show BG003Y
                with dissolve
                #===========================================================================================================================================================================
                # INSERT RUNNING SOUNDS
                #===========================================================================================================================================================================
                $ renpy.pause(1,hard=True)
                kristik "(huff) HOLY SHIT (puff) WHAT THE FUCK IS GOING ON??!!!"
                show girl4 (13) onlayer master3:
                    xpos 600
                    zoom 0.6                
                with dissolve
                c45 "Stop right there criminal scum!"
                hide girl4 (13) onlayer master3
                show girl4 (8) onlayer master3:
                    xpos 600
                    zoom 0.6
                kristik "pfff... what the fuck? A bunny girl?"
                kristik "What are you going to do to me?"
                play sound "audio/appearsound_Master.wav"
                show girl7 (17) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (1) onlayer master2:
                    xpos 250
                    zoom 0.6
                show girl6 (5) onlayer master4:
                    xpos 900
                    zoom 0.6
                with Dissolve(2)
                $ renpy.pause(0.5,hard=True)
                kristik "PSshsHShshh.... what is 4 bunny girls gonna do to me?"

                #===========================================================================================================================================================================
                # INSERT GUN LOADING SOUNDS
                #===========================================================================================================================================================================
                play sound "audio/gunload_Master.wav"
                show gun onlayer misc:
                    xpos 750
                    ypos 400 
                    zoom 0.5   
                show gun onlayer misc2:
                    xpos 1100
                    ypos 400 
                    zoom 0.5          
                show gun onlayer misc3:
                    xpos 400
                    ypos 400 
                    zoom 0.5    
                show gun onlayer misc4:
                    xpos 100
                    ypos 400 
                    zoom 0.5  
                $ renpy.pause(0.8,hard=True)                                                                        
                kristik "fuck...."        
                #===========================================================================================================================================================================
                # INSERT GUN SHOOTING SOUNDS
                #===========================================================================================================================================================================
                play sound "audio/awp.mp3"
                stop music fadeout 2.0
                show white
                hide girl7 (17) onlayer master1
                hide girl5 (1) onlayer master2
                hide girl4 (8) onlayer master3            
                hide girl6 (5) onlayer master4              
                hide gun onlayer misc
                hide gun onlayer misc2
                hide gun onlayer misc3
                hide gun onlayer misc4
                $ renpy.pause(1,hard=True)     
                $ show_quick_menu = False
                window hide
                with dissolve
                $ renpy.pause(2,hard=True)  
                narrator "Kristik was fatally shot with 4 bullet wounds to his thorax, stomach, head, and left arm."
                narrator "He was instantly killed."
                narrator "{b}Bad ending 3/21{/b}"
                if (persistent.endingFinished3 < 1):
                    $ persistent.endingFinished3 += 1
                elif (persistent.endingFinished3 >= 1):
                    pass
                else:
                    narrator "PERSISTENT DATA FAILURE FOR SECTION 10070. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                    $ renpy.quit()
                window hide
                with dissolve
                $ renpy.pause(2,hard=True) 
                $ MainMenu(confirm=False)()
            else:
                show BG022
                with dissolve
                play music "audio/Riddle Joker Original Soundtrack OST Secret Lab Instrumental-(128kbps).ogg"
                show girl1 (1) onlayer master1:
                    xpos -50
                    ypos 40
                    zoom 0.6
                show girl3 (28) onlayer master2:
                    xpos 120
                    zoom 0.6
                show guy1 (1) onlayer master3:
                    xpos 550
                    zoom 0.6
                show guy2 (28) onlayer master4:
                    xpos 800
                    zoom 0.6
                with dissolve
                hide guy2 (28) onlayer master4
                show guy2 (34) onlayer master4:
                    xpos 800
                    zoom 0.6
                toshiro "That's all for today. Tax and other pertinent paperwork can be filled out by us."
                toshiro "We'll inform you when we get the papers settled."
                hide guy2 (34) onlayer master4
                show guy2 (32) onlayer master4:
                    xpos 800
                    zoom 0.6                
                toshiro "THACH FEDERATION!!!"  
                kristik "???!! Wtf is the thach federation??!!"
                hide guy2 (34) onlayer master4
                hide guy1 (1) onlayer master3
                hide girl3 (28) onlayer master2
                hide girl1 (1) onlayer master1
                with dissolve
                show girl7 (5) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (9) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (2) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (3) onlayer master4:
                    xpos 900
                    zoom 0.6
                with dissolve
                unknown "YES SIR!!"
                kristikmind "{i}WHO TF ARE THESE PEOPLE??!!! THE THACH FEDERATION!>!!??!?!?!"
                kristikmind "{i}well, i guess he always liked anime girls..."
                hide girl4 (3) onlayer master4
                hide girl6 (2) onlayer master3
                hide girl5 (9) onlayer master2
                hide girl7 (5) onlayer master1                
                show guy2 (32) onlayer mcsprite:
                    xpos -70
                    ypos 520
                    zoom 0.5
                show girl7 (1) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (7) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (3) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (1) onlayer master4:
                    xpos 900
                    zoom 0.6                
                toshiro "I NEED YOU GUYS TO ESCORT THIS MAN OUT TO THE FRONT ENTRANCE! PRONTO!"
                hide guy2 (32) onlayer mcsprite
                hide girl4 (1) onlayer master4
                hide girl6 (3) onlayer master3
                hide girl5 (7) onlayer master2
                hide girl7 (1) onlayer master1                
                show girl7 (5) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (9) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (2) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (3) onlayer master4:
                    xpos 900
                    zoom 0.6
                unknown "YES SIR!!! WILL DO SIR!!!"
                kristikmind "{i}ESCORT?!?!?"
                kristikmind "{i}No wait.... not that kind of escort..."
                hide girl4 (3) onlayer master4
                hide girl6 (2) onlayer master3
                hide girl5 (9) onlayer master2
                hide girl7 (5) onlayer master1  
                with dissolve
                hide BG022
                with dissolve                
                show BG021
                with dissolve
                show syuz0101:
                    xpos 100
                    zoom 1.2
                show sner0101:
                    xpos 600
                    zoom 1.2
                with dissolve
                hide syuz0101
                show syuz0102:
                    xpos 100
                    zoom 1.2
                yuzuriha "Hey Kristik! Back already?"
                hide syuz0102
                show syuz0110:
                    xpos 100
                    zoom 1.2
                yuzuriha "But... who the hell are they??!!"
                hide syuz0110
                hide sner0101
                with dissolve
                show girl7 (9) onlayer master1:
                    xpos -50
                    zoom 0.6
                show girl5 (16) onlayer master2:
                    xpos 300
                    zoom 0.6
                show girl6 (5) onlayer master3:
                    xpos 600
                    zoom 0.6
                show girl4 (8) onlayer master4:
                    xpos 900
                    zoom 0.6
                with dissolve
                kristik "Oh... uhhh... to be honest I have no idea who they are..."          
                kristik "Apparently, they're from the ''Thach federation''????? Whatever the hell that is..." 
                hide girl7 (9) onlayer master1
                hide girl5 (16) onlayer master2
                hide girl6 (5) onlayer master3
                hide girl4 (8) onlayer master4   
                with dissolve    
                show girl4 (8):
                    xpos 700
                    zoom 0.6 
                show sner0102:
                    zoom 1.2 
                with dissolve
                nerine "What's your name?"   
                hide sner0102
                show sner0101:
                    zoom 1.2
                hide girl4 (8)
                show girl4 (10):
                    xpos 700
                    zoom 0.6  
                c45 "Chiester 45! Reporting for duty!" 
                hide girl4 (10)
                show girl4 (11):
                    xpos 700
                    zoom 0.6 
                hide sner0102
                show sner0101:
                    zoom 1.2  
                nerine "Hey, Kristik who do you prefer?"
                kristik "What??? Why are you asking me that??!"             
                hide girl4 (11)
                show girl4 (15):
                    ypos 100
                    xpos 700
                    zoom 0.6 
                $ show_quick_menu = False
                window hide
                menu:
                    "''I like bunny girls.''":
                        $ show_quick_menu = True
                        window show
                        $ EXPc00 += 1
                        kristik "I like bunny girls."
                        hide girl4 (15)
                        show girl4 (18):
                            ypos 100
                            xpos 700
                            zoom 0.6 
                        hide sner0101
                        show sner0102:
                            zoom 1.2  
                        nerine "Really? I never thought you would've like bunnies."    
                        hide sner0102
                        show sner0210:
                            zoom 1.2
                        nerine "Who would've thought...?"
                        hide sner0210
                        with dissolve                              
                        c45 "...."
                        kristik "Uhh...."     
                        hide girl4 (18)
                        show girl4 (19):
                            xpos 450
                            ypos 100
                            zoom 0.6
                        c45 "WAAAAH!!!!!"
                        kristik "WTF??!!!"
                        hide girl4 (19)
                        show girl1 (46):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show girl4 (19):
                            xpos 700
                            ypos 100
                            zoom 0.6
                        with dissolve
                        natsuhi "What the hell is going on here??"
                        hide girl1 (46)
                        show girl1 (48):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        kristik "..."
                        hide girl1 (38)
                        show girl1 (76):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        natsuhi "YOU BASTARD!!"
                        hide girl1 (76)
                        show girl1 (79):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        kristik "WOAHWOAHWOAHAOWOAHA!!! CHILL!!!"
                        kristik "I DIDNT EVEN DO ANYTHING!!!"
                        hide girl4 (19) 
                        show girl4 (18):
                            xpos 700
                            ypos 100
                            zoom 0.6  
                        c45 "No one has ever said anything like that to me..."
                        hide girl1 (79)
                        show girl1 (112):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        natsuhi "Ugh... not this shit again..."
                        hide girl1 (112)
                        show girl1 (76):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        natsuhi "WHAT DID YOU SAY TO HER YOU PERVERT?!?!"
                        kristik "WHAT?!?!?!? NO I JUST SAID I LIKED BUNNY GIRLS!"
                        natsuhi "SO YOU'RE A WEIRDO?!"
                        kristik "WHAT!?!?!?!?!?!? I mean... I guess that's kinda sussy..."
                        hide girl4 (18)
                        show girl4 (17):
                            xpos 700
                            ypos 100
                            zoom 0.6
                        c45 "Natsuhi! Put the gun down!"
                        hide girl4 (17)
                        show girl4 (20):
                            xpos 700
                            ypos 100
                            zoom 0.6
                        c45 "He didn't do anything!!!"
                        hide girl4 (20)
                        show girl4 (18):
                            xpos 700
                            ypos 100
                            zoom 0.6                        
                        hide girl1 (76)
                        show girl1 (112):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        natsuhi "Hahh.... whatever." 
                        hide girl1 (112)
                        show girl1 (107):
                            xpos 100
                            ypos 40
                            zoom 0.6    
                        natsuhi "Listen up kid, if you do anything weird in this building, I'm popping a cap in your ass!"       
                        hide girl1 (107)
                        hide girl4 (18)
                        with dissolve
                        kristik "Ok then..."
                        show girl7 (17) onlayer master1:
                            zoom 0.6
                        show girl5 (10) onlayer master2:
                            xpos 500
                            zoom 0.6
                        show girl6 (3) onlayer master3:
                            xpos 900
                            zoom 0.6   
                        with dissolve
                        unknown "Hey."  
                        hide girl5 (10) onlayer master2
                        show girl5 (13) onlayer master2:
                            xpos 500
                            zoom 0.6
                        unknown "We heard you like bunny girls."
                        kristikmind "{i}She looks scary af..."  
                        hide girl7 (17) onlayer master1 
                        hide girl5 (13) onlayer master2 
                        hide girl6 (3) onlayer master3
                        with dissolve
                        show guy2 (7):
                            xpos 350
                            ypos 40
                            zoom 0.6
                        with dissolve
                        toshiro "Alright guys, that's enough."
                        hide guy2 (7)
                        show guy2 (12):
                            xpos 350
                            ypos 40
                            zoom 0.6
                        toshiro "When I said escort, I didn't mean that..."
                        hide guy2 (12)
                        show guy2 (27):
                            xpos 350
                            ypos 40
                            zoom 0.6
                        toshiro "I apologize for the inconvience, you can come back here tomorrow to finalize everything else."
                        hide guy2 (27)
                        show guy2 (27):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show girl4 (3):
                            xpos 700
                            ypos 100
                            zoom 0.6  
                        with dissolve                            
                        c45 "Sir!!"
                        hide guy2 (27)
                        show guy2 (30):
                            xpos 100
                            ypos 40
                            zoom 0.6   
                        toshiro "What is it...?"          
                        hide girl4 (3)
                        show girl4 (3):
                            xpos 700
                            ypos 100
                            zoom 0.6     
                        hide girl4 (3)
                        show girl4 (1):
                            xpos 700
                            ypos 100
                            zoom 0.6        
                        stop music fadeout 2.0                                                    
                        c45 "An enemy is infiltrating our base!"
                        toshiro "Who??"
                        hide girl4 (1)
                        show girl4 (7):
                            xpos 700
                            ypos 100
                            zoom 0.6
                        c45 "Codenamed AWKC!"
                        hide guy2 (30)
                        show guy2 (32):
                            xpos 100
                            ypos 40
                            zoom 0.6   
                        play music "audio/Riddle Joker OST _ Invisibly Faster-(128kbps) intro.ogg"
                        queue music "audio/Riddle Joker OST _ Invisibly Faster-(128kbps).ogg"
                        toshiro "WHAT?!?!!! GET THE OTHERS AND BARRICADE THE FRONT!!!"
                        kristik "What the fuck is going on...?"
                        c45 "YESSIR!!!"
                        hide guy2 (32)
                        hide girl4 (7)
                        with dissolve
                        show guy2 (33):
                            xpos 350
                            ypos 40
                            zoom 0.6
                        with dissolve
                        toshiro "I'm sorry, it's currently too dangerous to leave this building."
                        kristik "What?!?!! Why?!?!! Who the hell is attacking this building?!?!"
                        hide guy2 (33)
                        show guy2 (29):
                            xpos 350
                            ypos 40
                            zoom 0.6
                        toshiro "A couple of these high profile criminals have been bugging us recently... these guys in particular stole our oil barrels in a ship port..."
                        kristik "The fuckk??? Why does a marriage office have barrells of oil??? And you said their name is ''''AWKC''''???"
                        hide guy2 (29)
                        show guy2 (33):
                            xpos 350
                            ypos 40
                            zoom 0.6                        
                        toshiro "It's a codename for their initials. We don't know their full names, but we do know their first names."
                        kristik "What are they??"
                        toshiro "Aaron and Wesley."
                        kristikmind "{i}WTF?!??!?!?!"
                        hide guy2 (33)
                        show guy2 (33):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show girl4 (3):
                            xpos 700
                            ypos 100
                            zoom 0.6  
                        with dissolve    
                        c45 "Sir!! We're ready!!"
                        hide girl4 (3)
                        show girl4 (3):
                            xpos 700
                            ypos 100
                            zoom 0.6     
                        hide girl4 (3)
                        show girl4 (1):
                            xpos 700
                            ypos 100
                            zoom 0.6     
                        hide guy2 (33)
                        show guy2 (32):
                            xpos 100
                            ypos 40
                            zoom 0.6                                             
                        toshiro "Then let's kill them bitches!!!"
                        kristik "What the fuck...!!!"
                        hide guy2 (32)
                        hide girl4 (1)
                        with dissolve
                        hide BG021
                        with dissolve
                        show BG011
                        with dissolve
                        show guy1 (72):
                            xpos 600
                            zoom 0.6
                        show girl1 (80):
                            ypos 40
                            xpos 100
                            zoom 0.6
                        with dissolve    
                        hide girl1 (119)
                        show girl1 (95):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        natsuhi "Get away from here! We gon pop a cap in your ass!"        
                        hide girl1 (95)
                        hide guy1 (72)
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        with dissolve
                        aaron "Hah.... I'm not even here for you guys."
                        aaron "Just looking out for an old friend."                                   
                        hide aaron_11_1
                        show girl1 (96):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show guy1 (72):
                            xpos 600
                            zoom 0.6 
                        with dissolve
                        natsuhi "As if! We never trusted you ever since you stole our oil!"                       
                        hide girl1 (96)
                        hide guy1 (72)
                        show aaron_11:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        with dissolve
                        aaron "Tch... Thach and his stupid anime girl federation...."
                        hide aaron_11
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        aaron "If that's how you want to do business, then that's not a problem."                        
                        hide aaron_11_1
                        show girl1 (96):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show guy1 (72):
                            xpos 600
                            zoom 0.6 
                        with dissolve
                        stop music fadeout 2.0
                        natsuhi "What the hell is he going to do next...?"
                        hide girl1 (96)
                        hide guy1 (72)
                        show aaron_7:
                            xpos 450
                            ypos 30
                            zoom 0.47
                        with dissolve 
                        aaron "Xi Jingping bot 9000! Get these sons of bitches!"
                        hide aaron_7
                        show xi:
                            xpos 400
                            ypos 120
                            zoom 0.7 
                        play music "audio/maozedongdrip.ogg"
                        xijingping "YOU THERE!"
                        hide xi
                        show girl1 (93):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show guy1 (72):
                            xpos 600
                            zoom 0.6 
                        with dissolve
                        natsuhi "SHIT! IT'S THE XI JINGPING BOT 9000!" 
                        hide girl1 (93)
                        hide guy1 (72)
                        show xi:
                            xpos 400
                            ypos 120
                            zoom 0.7 
                        with dissolve 
                        xijingping "YOU DO NOT HAVE HUSBAND!??!!! THIS IS WHAT HAPPEN WHEN YOU NO GO TO COLLEGE! YOU GET NO HUSBAND AND NO KID MEANS YOU ARE FAILURE!"
                        hide xi
                        show girl1 (83):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show guy1 (72):
                            xpos 600
                            zoom 0.6 
                        with dissolve   
                        natsuhi "It's true...."
                        hide girl1 (83)
                        show girl1 (84):
                            xpos 100
                            ypos 40
                            zoom 0.6    
                        natsuhi "I don't have a husband at the age of 33..."
                        hide girl1 (84)
                        show girl1 (61):
                            xpos 100
                            ypos 40
                            zoom 0.6  
                        natsuhi "I KNEW I SHOULD HAVE BEEN A BIOCHEMIST INSTEAD WAHAHAHAHHAHHHH!!!!!"
                        hide girl1 (61)
                        hide guy1 (72)
                        show xi:
                            xpos 400
                            ypos 120
                            zoom 0.7 
                        with dissolve 
                        xijingping "AND YOU! YOU HAVE NO WIFE??!! ITS BECAUSE YOU ARE TOO MUCH PUSSY! YOU WERE SCARED TO ATTEND SPELLING BEE IN MIDDLE SCHOOL! NOW LOOK AT YOU! YOU ARE FAILURE!"
                        hide xi
                        show girl1 (59):
                            xpos 100
                            ypos 40
                            zoom 0.6
                        show guy1 (62):
                            xpos 600
                            zoom 0.6 
                        with dissolve 
                        rudolf "It's true..."
                        hide guy1 (62)
                        show guy1 (61):
                            xpos 600
                            zoom 0.6 
                        rudolf "I intentionally spelled the words wrong on the placement test so I didn't have to go to the spelling bee.... BOOOHOOHohohohohooo"  
                        hide guy1 (61)
                        hide girl1 (59)
                        with dissolve
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        with dissolve
                        aaron "Heh... the one weakness of the Thach federation..."
                        aaron "The cold truth."
                        hide aaron_11_1
                        show aaron_11:
                            xpos 450
                            ypos 30
                            zoom 0.4                        
                        aaron "They couldn't handle any of this even if it came from their own mother..."  
                        aaron "Time to infiltrate the building."
                        stop music fadeout 2.0
                        hide aaron_11
                        hide BG011
                        with dissolve
                        play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
                        show BG021
                        with dissolve
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4   
                        with dissolve                     
                        aaron "Hm... where is Kristik?"      
                        hide aaron_11_1
                        with dissolve
                        show girl7 (9) onlayer master1:
                            xpos -50
                            zoom 0.6
                        show girl5 (16) onlayer master2:
                            xpos 300
                            zoom 0.6
                        show girl6 (5) onlayer master3:
                            xpos 600
                            zoom 0.6
                        show girl4 (8) onlayer master4:
                            xpos 900
                            zoom 0.6
                        with dissolve  
                        hide girl4 (8) onlayer master4    
                        show girl4 (13) onlayer master4:
                            xpos 900
                            zoom 0.6                               
                        c45 "Stop!"         
                        hide girl7 (9) onlayer master1
                        hide girl5 (16) onlayer master2
                        hide girl6 (5) onlayer master3
                        hide girl4 (8) onlayer master4 
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4   
                        with dissolve                     
                        aaron "Tch.. Thach's guards..."  
                        hide aaron_11_1                                                 
                        show girl7 (9) onlayer master1:
                            xpos -50
                            zoom 0.6
                        show girl5 (16) onlayer master2:
                            xpos 300
                            zoom 0.6
                        show girl6 (5) onlayer master3:
                            xpos 600
                            zoom 0.6
                        show girl4 (8) onlayer master4:
                            xpos 900
                            zoom 0.6
                        with dissolve 
                        hide girl4 (8) onlayer master4    
                        show girl4 (13) onlayer master4:
                            xpos 900
                            zoom 0.6                         
                        c45 "You won't fool us this time!"
                        hide girl7 (9) onlayer master1
                        hide girl5 (16) onlayer master2
                        hide girl6 (5) onlayer master3
                        hide girl4 (8) onlayer master4 
                        show aaron_11:
                            xpos 450
                            ypos 30
                            zoom 0.4   
                        with dissolve                     
                        aaron "Hmm...."
                        hide aaron_11
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        aaron "Look! Free Robux generator working 2022!!!! OMG!!!"
                        hide aaron_11_1                                                 
                        show girl7 (7) onlayer master1:
                            xpos -50
                            zoom 0.6
                        show girl5 (18) onlayer master2:
                            xpos 300
                            zoom 0.6
                        show girl6 (9) onlayer master3:
                            xpos 600
                            zoom 0.6
                        show girl4 (14) onlayer master4:
                            xpos 900
                            zoom 0.6
                        with dissolve 
                        everyone "WHERE?!?!!"
                        hide girl7 (7) onlayer master1
                        hide girl5 (18) onlayer master2
                        hide girl6 (9) onlayer master3
                        hide girl4 (14) onlayer master4  
                        with dissolve
                        stop music fadeout 1.0
                        narrator "..."
                        show girl7 (11) onlayer master1:
                            xpos -50
                            zoom 0.6
                        show girl5 (16) onlayer master2:
                            xpos 300
                            zoom 0.6
                        show girl6 (5) onlayer master3:
                            xpos 600
                            zoom 0.6
                        show girl4 (12) onlayer master4:
                            xpos 900
                            zoom 0.6
                        with dissolve   
                        play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
                        everyone "Fuck! He got away!"    
                        hide girl7 (11) onlayer master1
                        hide girl5 (16) onlayer master2
                        hide girl6 (5) onlayer master3
                        hide girl4 (12) onlayer master4  
                        with dissolve 
                        stop music fadeout 1.0
                        hide BG021
                        show BG004Y
                        with dissolve
                        play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
                        show guy2 (33):
                            xpos 350
                            zoom 0.6
                        with dissolve
                        toshiro "We should be safe here... the guards should have already gotten him by now."
                        kristik "What the fuck is going on???!"
                        hide guy2 (33)
                        show guy2 (29):
                            xpos 350
                            zoom 0.6
                        toshiro "I'm sorry that you had to get involved in this... it is our personal business after all."
                        kristik "You mentioned Aaron, right?!"
                        kristik "He was a friend of mine, but apparently he's gone AWOL and is trying to kill me!"
                        hide guy2 (29)
                        show guy2 (33):
                            xpos 350
                            zoom 0.6
                        stop music fadeout 2.0
                        toshiro "He was... your friend..?"
                        kristik "Oh shit..."                        
                        hide guy2 (33)
                        show guy2 (32):
                            xpos 350
                            zoom 0.6
                        play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
                        toshiro "HOW WOULD I KNOW IF YOU'RE A SPY FOR HIM THEN?!?!?!"
                        toshiro "THIS WAS ALL A PART OF YOUR PLAN HUH?!??! TO INFILTRATE THE OFFICE AND STEAL OUR OIL AGAIN!"
                        hide guy2 (32)
                        show guy2 (33):
                            xpos 350
                            zoom 0.6                        
                        kristik "WHY THE FUCK DO YOU GUYS EVEN HAVE OIL IN A {b}MARRIAGE COUNSELING OFFICE?!?!?!?!?!!"
                        kristik "I'M NOT A SPY FOR HIM ANYWAYS!!! HONEST TO SHIVA!!!"
                        hide guy2 (33)
                        show guy2 (32):
                            xpos 350
                            zoom 0.6
                        toshiro "STOP THE CAP!!!!"
                        hide guy2 (32)
                        show guy2 (33):
                            xpos 350
                            zoom 0.6    
                        #======================================================================================================
                        # PLAY GUN LOADING SOUNDS
                        #======================================================================================================
                        play sound "audio/gunload_Master.wav"
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6 
                        $ renpy.pause(0.8,hard=True)
                        hide gun
                        hide guy2 (33)
                        show guy2 (32):
                            xpos 350
                            zoom 0.6   
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6                                                      
                        toshiro "YOU WON'T FOOL ME!!"  
                        hide gun
                        hide guy2 (32)
                        show guy2 (33):
                            xpos 350
                            zoom 0.6      
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6                                                          
                        #======================================================================================================
                        # PLAY DOOR OPENING SOUNDS
                        #======================================================================================================   
                        $ renpy.pause(2,hard=True)    
                        hide gun 
                        hide guy2 (32)                                         
                        with dissolve
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        with dissolve
                        aaron "Oh..."
                        aaron "Looks like my job was already done."                                                                                       
                        hide aaron_11_1
                        show guy2 (33):
                            xpos 350
                            zoom 0.6  
                        with dissolve
                        toshiro "You..."                        
                        hide guy2 (33)
                        show guy2 (32):
                            xpos 350
                            zoom 0.6 
                        toshiro "HOW DID YOU GET HERE?!??!!!"
                        hide guy2 (32)                                         
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        with dissolve
                        aaron "If you expected me to be stopped by some bunny girls and sad members of society, then you sorely underestimated me."
                        play sound "audio/gunload_Master.wav"
                        show gun:
                            xpos 630
                            ypos 360 
                            zoom 0.5 
                        $ renpy.pause(0.8,hard=True)
                        aaron "You'll be the one who's dead."                        
                        hide aaron_11_1
                        show guy2 (32):
                            xpos 350
                            zoom 0.6
                        hide gun
                        toshiro "NOT IF I GET TO YOU FIRST!"
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6     
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.8,hard=True)                        
                        hide guy2 (32)
                        show guy2 (33):
                            xpos 350
                            zoom 0.6    
                        hide gun 
                        hide guy2 (32) 
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        show gun:
                            xpos 630
                            ypos 360 
                            zoom 0.5     
                        aaron "Oh you really think so?"
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.8,hard=True)
                        aaron "I played Escape From Tarkov for 500 hours, I clearly know how to shoot a gun."    
                        hide gun 
                        hide aaron_11_1
                        show guy2 (32):
                            xpos 350
                            zoom 0.6
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6 
                        toshiro "I PLAYED VALORANT FOR 2,000 HOURS!"    
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.8,hard=True)  
                        toshiro "I'M WAY BETTER!"           
                        kristikmind "{i}how many times are they gonna load that fuckin gun???"              
                        hide gun 
                        hide guy2 (32) 
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        show gun:
                            xpos 630
                            ypos 360 
                            zoom 0.5     
                        aaron "Really? Valorant?"
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.2,hard=True)
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.2,hard=True)
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.2,hard=True)
                        aaron "I was in the marines for 23 years." 
                        hide gun 
                        hide aaron_11_1
                        show guy2 (32):
                            xpos 350
                            zoom 0.6
                        show gun:
                            xpos 600
                            ypos 320 
                            zoom 0.6 
                        toshiro "MARINES??!!!"    
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)  
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)   
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)  
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)    
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)  
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)   
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)  
                        play sound "audio/gunload_Master.wav"
                        $ renpy.pause(0.15,hard=True)                                                 
                        toshiro "MARINES IS NOTHING!"  
                        kristik "Ok.. what the fuck is going on..."   
                        toshiro "I SERVED 20230219407 YEARS IN THE ARMY OF REDDIT AND HAVE OVER 90237458923675723485682346527846 CONFIRMED KILLS IN VIETNAM!!"
                        toshiro "I AM LEVEL 99999999999 IN PHANTOM FORCES AND I COULD KILL ANYONE IN A PHEMTOSECOND WITH MY BARE HANDS HELL EVEN WITH MY TOES!!!{p=0.1}{nw}" 
                        play sound "audio/awp.mp3" 
                        show white
                        hide gun
                        hide guy2
                        $ renpy.pause(0.001,hard=True)
                        hide white
                        with Dissolve(2)
                        kristik "WTF??!?!?!"
                        aaron "Jeez... that guy's talking was starting to hurt my brain."
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        show gun:
                            xpos 630
                            ypos 360 
                            zoom 0.5    
                        with dissolve
                        aaron "Now... where was I?"   
                        hide aaron_11_1
                        hide gun
                        show aaron_11:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        show gun:
                            xpos 630
                            ypos 360
                            zoom 0.5
                        aaron "Oh right..."
                        kristik "Pwease!!!! Onegai!!! No kill me!!"
                        #======================================================================================================
                        # PLAY GUN LOADING SOUNDS
                        #======================================================================================================
                        play sound "audio/gunload_Master_reverse.wav"
                        hide gun
                        with dissolve
                        $ renpy.pause(0.8,hard=True)
                        kristik "?????"
                        hide aaron_11
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4 
                        aaron "Kristik."
                        aaron "Why don't we have a bit of a chat?"
                        kristik "y-y-y-y-y-yesh!!!"
                        stop music fadeout 2.0
                        hide aaron_11_1
                        hide BG004Y
                        with dissolve
                        $ renpy.pause(1,hard=True)
                        show BG022N1
                        play music "audio/Sanoba Witch OST - Midday Star(InstVer.)-(128kbps).ogg"
                        with dissolve
                        play sound "audio/lightingciggie.ogg"
                        show aaron_3:
                            xpos -90
                            ypos 175
                            zoom 0.65     
                        with dissolve
                        kristik "..."    
                        hide aaron_3
                        show aaron_8:
                            xpos -10
                            ypos 220
                            zoom 0.55
                        with dissolve       
                        aaron "Did you ever wonder why I was trying to kill you?"  
                        kristik "Ummm.... "
                        kristik "To be hoenst I didn't really know..."     
                        show BG023N1_o
                        show d8:
                            xpos 800
                            ypos 100
                            zoom 0.7
                        with dissolve
                        unknown "Daaaddd.... I'm hungrrryyyy"
                        kristik "Who tf... is that?"
                        hide aaron_8
                        show aaron_4:
                            ypos 195
                            zoom 0.55  
                        aaron "Ugh... goddamnit... she followed me again...."
                        hide aaron_4
                        show aaron_9:
                            ypos 175
                            zoom 0.57
                        aaron "Didn't mommy tell you to go to bed?"
                        hide d8
                        show d9:
                            xpos 805
                            ypos 100
                            zoom 0.7
                        unknown "I want McDonald's!!"
                        aaron "Look Kaori, I'm going to call mommy and she'll pick you up."
                        hide d9
                        show d8:
                            xpos 800
                            ypos 100
                            zoom 0.7  
                        unknown "I want McDonald's!!!!!!"
                        kristik "Uhh.... Aaron who the hell is that?"
                        hide aaron_9
                        show aaron_10:
                            ypos 180
                            zoom 0.57 
                        aaron "It's my daughter... Kaori. She has the tendency to follow me every time I leave the house..."          
                        kristik "How the fuck did this little 6 year old leave the house??!?!?!"
                        hide aaron_10
                        show aaron_5:
                            ypos 180
                            zoom 0.57 
                        aaron "I don't really know... but it looks like I gotta go."  
                        hide aaron_5
                        hide BG023N1_o
                        hide d8
                        hide BG021
                        with dissolve
                        show BG011N
                        with dissolve     
                        show aaron_11_n:
                            xpos 120
                            zoom 0.4
                        show d5_n:
                            xpos 720
                            ypos 300
                            zoom 0.6
                        with dissolve
                        aaron "Sorry kristik... My daughter keeps pestering us."
                        hide d5_n
                        show d1_n:
                            xpos 720
                            ypos 300
                            zoom 0.6
                        kaori "It wouldn't have mattered if you didn't leave the house so much!!"
                        hide d1_n
                        show d4_n:
                            xpos 720
                            ypos 300
                            zoom 0.6
                        hide aaron_11_n
                        show aaron_7_n:
                            xpos 120
                            zoom 0.5
                        aaron "I gotta go to McDonald's... she wants a Happy Meal..."
                        hide d4_n
                        show d6_n:
                            xpos 730
                            ypos 300
                            zoom 0.6
                        kaori "Yayyyy!!"
                        hide aaron_7_n 
                        show aaron_11_n:
                            xpos 120
                            zoom 0.4
                        kristik "I suppose we can talk another time."
                        aaron "Yes. I will see you later. Let's go Kaori."
                        stop music fadeout 2.0
                        hide aaron_11_n
                        hide d6_n
                        with dissolve
                        kristik "..."         
                        hide BG011N
                        hide BG022N1
                        stop music fadeout 2.0
                        with dissolve  
                        window hide
                        $ show_quick_menu = False
                        with dissolve
                        $ renpy.pause(1,hard=True)
                        jump finalPart                   

                    "''I like you.''":     
                        $ show_quick_menu = True
                        window show
                        $ EXPnerine += 1
                        $ EXPyuzuriha += 1
                        kristik "I like you."
                        hide sner0101
                        show sner0208:
                            zoom 1.2
                        nerine "Very straightforward..."
                        hide girl4 (15) 
                        show girl4 (18):
                            xpos 700
                            ypos 100
                            zoom 0.6                          
                        hide sner0208
                        show sner0209:
                            zoom 1.2
                        kristikmind "{i}Man... why do I feel kinda... disappointed by that reaction?"
                        hide sner0209
                        hide girl4 (18)
                        with dissolve
                        show syuz0101:
                            xpos 100
                            zoom 1.2
                        show sner0209:
                            xpos 600
                            zoom 1.2
                        with dissolve   
                        hide syuz0101
                        show syuz0102:
                            xpos 100
                            zoom 1.2
                        yuzuriha "Well we better get going, oop look at the time it's nearly time to go!"
                        hide syuz0102
                        hide sner0209
                        with dissolve
                        hide BG021
                        with dissolve
                        show BG011
                        with dissolve
                        show syuz0111:
                            xpos 100
                            zoom 1.2
                        show sner0209:
                            xpos 600
                            zoom 1.2
                        with dissolve
                        yuzuriha "Kristik do you want to explain who all those people were??!"
                        kristik "Umm... they were all workers for the office."
                        hide syuz0111
                        show syuz0113:
                            xpos 100
                            zoom 1.2
                        yuzuriha "Well then who were those 4 other people??"
                        kristik "Like I said! I have no idea!"
                        kristik "I just heard that they were a part of the Thach Federation! I have no idea who Thach is though..."
                        hide syuz0113
                        show syuz0112:
                            xpos 100
                            zoom 1.2
                        yuzuriha "Thach huh...."
                        yuzuriha "I haven't heard that name in years..."
                        hide sner0209
                        show sner0108:
                            xpos 600
                            zoom 1.2
                        nerine "Thach? I do remember that name, but I don't remember him being involved with this situation."
                        hide syuz0112
                        show syuz0114:
                            xpos 100
                            zoom 1.2
                        yuzuriha "Well.. honestly, I can't be bothered right now. We got the documents filed but now I have a headache."
                        nerine "Erika has some pills to help with that at her house."
                        kristik "Erika?"
                        nerine "Yeah, she's another friend of ours."
                        yuzuriha "Well, then let's go. I can't stand around here forever!"
                        stop music fadeout 2.0
                        hide syuz0114
                        hide sner0108
                        with dissolve
                        $ renpy.pause(2,hard=True)
                        show aaron_11_1:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        with dissolve
                        aaron "Hm...."
                        play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
                        aaron "I was going to attack..."
                        hide aaron_11_1
                        show aaron_11:
                            xpos 450
                            ypos 30
                            zoom 0.4
                        aaron "But the Thach federation is getting involved now...?"
                        hide aaron_11
                        show aaron_7:
                            xpos 450
                            ypos 30
                            zoom 0.47
                        aaron "What a pain in the ass..."
                        hide aaron_7
                        with dissolve
                        play sound "audio/dialing.ogg"
                        $ renpy.pause(5,hard=True)
                        #========================================================================================================================================================================
                        #PLAY PHONE DIALING SOUND
                        #========================================================================================================================================================================
                        stop sound
                        wesley "{i}Hello?"
                        aaron "{i}Wesley. We got a problem."
                        wesley "{i}What happened?"
                        aaron "{i}The Thach federation is getting involved. Remember those bunny girls?"
                        wesley "{i}Shit.... those things were ruthless when we were stealing their oil barrels from the Oakland port!"
                        aaron "{i}Yeah... and they're here out of all places."
                        wesley "{i}Shit.... did you spot the members?"
                        aaron "{i}No I didn't. I'm thinking that they're in one of these buildings."
                        show girl7 (9):
                            xpos 450
                            zoom 0.6
                        with dissolve
                        c00 "The hell is all that murmuring?"
                        aaron "{i}Shit!!! It's Chiester 00!"
                        wesley "{i}The blonde one?!?!?!"
                        wesley "{i}You're fucked bro!! Get outta there!"
                        hide girl7 (9)
                        show girl7 (16):
                            xpos 450
                            zoom 0.6
                        c00 "I can see you clearly. I'm not stupid."
                        hide girl7 (16)
                        show girl7 (11):
                            xpos 450
                            zoom 0.6
                        aaron "{i}Shit!!! She's talking to herself!! She's weird!!"
                        wesley "{i}What>???? No way!"
                        hide girl7 (11)
                        show girl7 (16):
                            xpos 450
                            zoom 0.6 
                        play sound "audio/gunload_Master.wav"
                        show gun onlayer misc:
                            xpos 370
                            ypos 300
                            zoom 0.4
                        c00 "You're dead kid."
                        aaron "Who the fuck you callin a kid?"
                        hide girl7 (16)
                        show girl7 (11):
                            xpos 450
                            zoom 0.6
                        c00 "You asked for this!"                        


                        #===========================================================================================================================================================================
                        # INSERT GUN SHOOTING SOUNDS
                        #===========================================================================================================================================================================
                        stop music fadeout 2.0
                        play sound "audio/awp.mp3" 
                        hide gun onlayer misc
                        show white
                        $ renpy.pause(1,hard=True)
                        window hide
                        $ show_quick_menu = False
                        with dissolve
                        $ renpy.pause(2,hard=True)
                        hide white 
                        hide girl7 (11)
                        hide BG011
                        show school_gardens
                        with dissolve
                        play music "audio/Sanoba Witch OST - Midday Star(InstVer.)-(128kbps).ogg"    
                        window show
                        $ show_quick_menu = True
                        with dissolve       
                        show syuz0101:
                            xpos 100
                            zoom 1.2
                        show sner0101:
                            xpos 600
                            zoom 1.2
                        with dissolve
                        hide syuz0101
                        show syuz0102:
                            xpos 100
                            zoom 1.2
                        yuzuriha "We're nearly there." 
                        hide syuz0102
                        show syuz0101:
                            xpos 100
                            zoom 1.2
                        kristik "(huff) holy shit.... (puff) that was... super long..."
                        hide syuz0101
                        show syuz0114:
                            xpos 100
                            zoom 1.2
                        yuzuriha "Somebody needs to go out more..."
                        hide sner0101
                        show sner0204:
                            xpos 600
                            zoom 1.2
                        nerine "I think you might be more in need of a rest than Yuzuriha..."
                        hide sner0204
                        hide syuz0114
                        hide school_gardens
                        show school_dormhallground
                        with dissolve
                        show syuz0101:
                            xpos 100
                            zoom 1.2
                        show sner0101:
                            xpos 600
                            zoom 1.2
                        with dissolve
                        hide syuz0101
                        show syuz0102:
                            xpos 100
                            zoom 1.2                        
                        yuzuriha "I'll be back, I just need to get something from Erika. It won't be long."
                        hide syuz0102
                        hide sner0101
                        show sner0101:
                            xpos 350
                            zoom 1.2
                        with dissolve
                        stop music fadeout 3.0
                        kristik "..."
                        hide sner0101
                        show sner0209:
                            xpos 350
                            zoom 1.2
                        nerine "..."
                        kristik "So... uh..."
                        play music "audio/Sanoba Witch OST - Sweet Treasure(QuietVer.)-(128kbps).ogg"
                        kristik "How's life... and stuff?"
                        nerine "It's been alright..."
                        kristik "...."
                        hide sner0209
                        show sner0207:
                            xpos 350
                            zoom 1.2
                        nerine "...."
                        hide sner0207
                        show sner0212:
                            xpos 350
                            zoom 1.2
                        with dissolve
                        $ renpy.pause(1,hard=True)
                        hide sner0212
                        show sner0111:
                            xpos 350
                            zoom 1.2
                        with dissolve
                        nerine "I suppose it's a good time to bring this up..."
                        nerine "That polygamy fiasco Yuzuriha was talking about was... completely fake."
                        kristik "Wait... what???"
                        nerine "Ever wondered why they didn't ask for information regarding the spouse at the office?"
                        kristik "Uhh....."
                        hide sner0111
                        show sner0209:
                            xpos 350
                            zoom 1.2
                        nerine "It's because they're just waiting on one of us to get selected..."
                        kristik "Selected?"
                        hide sner0209
                        show sner0109:
                            xpos 350
                            zoom 1.2
                        nerine "Yeah. Selected from you to be their spouse."
                        hide sner0109
                        show sner0208:
                            xpos 350
                            zoom 1.2
                        nerine "So I guess, the question I wanted to ask is."
                        hide sner0208
                        show sner0111:
                            xpos 350
                            zoom 1.2
                        nerine "Who would you like to marry?"

                        #################To be honest, shits kinda cringe here LOlolololoo
                        #### im not very good at the romance stuff, so its pretty basic shit...
                        $ show_quick_menu = False
                        window hide
                        menu:
                            "''I would like to marry you, Nerine.''":
                                $ show_quick_menu = True
                                window show
                                $ EXPnerine += 3
                                kristik "I would like to marry you, Nerine."
                                hide sner0111
                                show sner0108:
                                    xpos 350
                                    zoom 1.2
                                nerine "H-huh...?"
                                hide sner0108
                                show sner0106:
                                    xpos 350
                                    zoom 1.2
                                nerine "There's no need to joke around, you can just tell me what you really think."
                                hide sner0106
                                show sner0108:
                                    xpos 350
                                    zoom 1.2 
                                kristik "I'm not joking Nerine."
                                kristik "I love you." #<------- shits a bit cringe ngl  
                                hide sner0108
                                show sner0103:
                                    xpos 350
                                    zoom 1.2 
                                nerine "..."
                                hide sner0103
                                show sner0106:
                                    xpos 350
                                    zoom 1.2 
                                nerine "Me too. I love you too."
                                show white 
                                stop music fadeout 5.0
                                with Dissolve(5)   
                                $ renpy.pause(3,hard=True)  
                                window hide
                                $ show_quick_menu = False
                                with dissolve
                                $ renpy.pause(1,hard=True)  
                                hide sner0106
                                hide school_dormhallground
                                hide white
                                with dissolve
                                "{b}Good ending 10/21" 
                                if (persistent.endingFinished10 < 1):
                                    $ persistent.endingFinished10 += 1
                                elif (persistent.endingFinished10 >= 1):
                                    pass
                                else:
                                    narrator "PERSISTENT DATA FAILURE FOR SECTION 11500. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                                    $ renpy.quit()
                                $ renpy.pause(2,hard=True) 
                                $ MainMenu(confirm=False)()                                                                    
                            "''I would like to marry Yuzuriha.''":
                                $ show_quick_menu = True
                                window show
                                $ EXPyuzuriha += 2
                                kristik "I would like to marry Yuzuriha."
                                hide sner0111
                                show sner0103:
                                    xpos 350
                                    zoom 1.2
                                nerine "..."
                                hide sner0103
                                show sner0102:
                                    xpos 350
                                    zoom 1.2
                                nerine "Why don't you let her know? She's down the hall to the right."
                                kristik "... you don't... feel bad?"
                                hide sner0102
                                show sner0201:
                                    xpos 350
                                    zoom 1.2
                                nerine "Aww c'mon, you're really going to ask me that kind of question?"
                                kristik "ooops... uhhh I guess I'll be going then..."
                                hide sner0201
                                show sner0102:
                                    xpos 350
                                    zoom 1.2
                                nerine "There's nothing to be afraid about! I know she'll love your answer anyways."
                                kristik "Thanks."
                                hide sner0102
                                with dissolve
                                hide school_dormhallground
                                show school_girlsdormhall
                                with dissolve
                                $ renpy.pause(1,hard=True)
                                kristik "I know she said not to be nervous, but goddamn this is the most my balls have been sweaty."
                                show syuz0108:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2
                                show seri0104:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1
                                with dissolve
                                yuzuriha "....hahaha! Yeah and then-"
                                kristik "Hey."
                                hide syuz0108
                                show syuz0102:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2
                                yuzuriha "Oh! What are you doing here? I was just about to leave."
                                yuzuriha "This is Erika."
                                hide syuz0102
                                show syuz0101:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2
                                hide seri0104
                                show seri0106:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1  
                                erika "Hey."
                                hide seri0106
                                show seri0104:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1                                  
                                kristik "Hi. Uhhh, Yuzuriha, there's something I need to say."
                                hide syuz0101
                                show syuz0102:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2
                                yuzuriha "...What is it?"
                                hide syuz0102
                                show syuz0101:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2
                                kristik "i..."
                                kristik "I WUV U!!!"
                                hide seri0104
                                show seri0112:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1 
                                hide syuz0101
                                show syuz0111:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2  
                                erika "Huh???"
                                hide seri0112
                                show seri0111:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1                                 
                                yuzuriha "...huh?" 
                                kristik "...shit. I said it wrong..."
                                hide seri0111
                                show seri0108:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1         
                                hide syuz0111
                                show syuz0108:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2     
                                erika "HAAHAHAHAHAAHA!!!"       
                                yuzuriha "HAHAAHASAHHAHA HA LAMOAOAOAO JKOASDJOASIFHBSEJKL T!!"   
                                hide syuz0108
                                show syuz0107:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2  
                                hide seri0108
                                show seri0107:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1                                                                                                                 
                                yuzuriha "What was that? ''I wuv u''???"
                                hide seri0107
                                show seri0101:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1 
                                hide syuz0107
                                show syuz0111:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2                                                                    
                                kristik "I JUST LOVE YOU OK!!?!?!??!? ASJKFHJKAHLFJADSFHKLH!!!"
                                erika "hm...."
                                kristikmind "{i}shit... they don't look too happy about that.."
                                hide syuz0111
                                show syuz0112:
                                    xpos 100
                                    ypos 60
                                    zoom 1.2
                                yuzuriha "Umm... just a sec Erika.."
                                hide seri0101
                                show seri0112:
                                    xpos 400
                                    ypos -60
                                    zoom 1.1   
                                erika "Uhh.... sure..."
                                hide seri0112
                                hide syuz0112
                                with dissolve
                                show syuz0113:
                                    xpos 350
                                    zoom 1.2 
                                with dissolve
                                yuzuriha "Kristik."
                                kristik "Y-Yesh??!!!"
                                hide syuz0113
                                show syuz0117:
                                    xpos 350
                                    zoom 1.2
                                yuzuriha "Is what you said really true?"
                                hide syuz0117
                                show syuz0118:
                                    xpos 350
                                    zoom 1.2   
                                yuzuriha "You... you wuv me?!"
                                kristik "Ok... it was a MISTAKE OK!!!"
                                hide syuz0118
                                show syuz0108:
                                    xpos 350
                                    zoom 1.2    
                                yuzuriha "JAJAJAJAJAJAAA its just too funny XD!!!"
                                hide syuz0108
                                show syuz0111:
                                    xpos 350
                                    zoom 1.2                                    
                                kristik "But, yes. I do."
                                hide syuz0111
                                show syuz0118:
                                    xpos 350
                                    zoom 1.2   
                                yuzuriha "Really..? What about me specifically?" 
                                kristik "umnmnmm..... you're... nice?"
                                hide syuz0118
                                show syuz0111:
                                    xpos 350
                                    zoom 1.2   
                                yuzuriha "Really?? That's it????"
                                kristik "Well, what do you want me to say! I love you, and it doesn't really matter what I like about you."
                                hide syuz0111
                                show syuz0118:
                                    xpos 350
                                    zoom 1.2   
                                yuzuriha "Final question...."
                                yuzuriha "Do you play Rogue Lineage on Roblox??"
                                $ show_quick_menu = False
                                window hide
                                menu:
                                    "''Yes. I'm a Pilgrim Knight.''":
                                        $ show_quick_menu = True
                                        window show
                                        kristik "Yes. I'm a Pilgrim Knight."
                                        hide syuz0118
                                        show syuz0115:
                                            xpos 350
                                            zoom 1.2       
                                        yuzuriha "Really...?!!"
                                        kristik "I'm not capping."
                                        hide syuz0115
                                        show syuz0116:
                                            xpos 350
                                            zoom 1.2       
                                        yuzuriha "You really are the one for me."
                                        kristik "I love you."
                                        yuzuriha "Me too."
                                        show white 
                                        stop music fadeout 5.0
                                        with Dissolve(5)   
                                        $ renpy.pause(3,hard=True)  
                                        window hide
                                        $ show_quick_menu = False
                                        with dissolve
                                        $ renpy.pause(1,hard=True)  
                                        hide syuz0116
                                        hide school_girlsdormhall
                                        hide white
                                        with dissolve
                                        "{b}Good ending 11/21"  
                                        if (persistent.endingFinished11 < 1):
                                            $ persistent.endingFinished11 += 1
                                        elif (persistent.endingFinished11 >= 1):
                                            pass
                                        else:
                                            narrator "PERSISTENT DATA FAILURE FOR SECTION 11738. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                                            $ renpy.quit()
                                        $ renpy.pause(2,hard=True)
                                        $ MainMenu(confirm=False)()
                                    "''No. It sounds gay.''":
                                        $ show_quick_menu = True
                                        window show
                                        kristik "No. It sounds gay."
                                        hide syuz0118
                                        show syuz0111:
                                            xpos 350
                                            zoom 1.2 
                                        #======================================================================================================
                                        # PLAY GUN LOADING SOUNDS
                                        #======================================================================================================    
                                        stop music 
                                        play sound "audio/gunload_Master.wav"
                                        show gun onlayer misc:
                                            xpos 600
                                            ypos 320 
                                            zoom 0.6  
                                        $ renpy.pause(0.8,hard=True)                                            
                                        yuzuriha "ROGUE LINEAGE IS NOT GAY!!!"
                                        kristik "WAIT WAITIWAWITWIATI!!!"                                                                                
                                        #======================================================================================================
                                        # PLAY GUN SHOOTING SOUNDS
                                        #======================================================================================================
                                        play sound "audio/awp.mp3"                                        
                                        show white 
                                        hide gun onlayer misc 
                                        window hide 
                                        $ show_quick_menu = False
                                        with dissolve
                                        $ renpy.pause(1,hard=True)
                                        window show
                                        with dissolve             
                                        narrator "Kristik was killed from a firearm wound to the frontal lobe."
                                        narrator "Paramedics' attempts at bringing back his consciousness were unsuccessful."
                                        narrator "{b}Bad ending 4/21{/b}"
                                        if (persistent.endingFinished4 < 1):
                                            $ persistent.endingFinished4 += 1
                                        elif (persistent.endingFinished4 >= 1):
                                            pass
                                        else:
                                            narrator "PERSISTENT DATA FAILURE FOR SECTION 11781. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                                            $ renpy.quit()
                                        window hide
                                        with dissolve                
                                        $ MainMenu(confirm=False)()


    elif EXPrikka >= 3:
        play music "audio/Sanoba Witch OST - School Dayz-(128kbps).ogg"
        show BG039
        with dissolve
        $ show_quick_menu = True
        window show
        with dissolve
        kristik "Goddamn..."
        kristik "I said some weird ass shit yesterday..."
        kristik "I have no idea what was up with me, but I guess I was pretty freaky deaky..."
        show aaron_11:
            xpos 450
            ypos 30
            zoom 0.3
        with dissolve
        unknown "..."
        hide aaron_11
        show aaron_11_1:
            xpos 450
            ypos 30
            zoom 0.3   
        unknown "...?"     
        unknown "Kribshit..."
        kristik "What...?"
        kristik "Who are you?"
        hide aaron_11_1
        show aaron_11:
            xpos 450
            ypos 30
            zoom 0.3   
        unknown "You don't know... Like like like?"
        kristik "Wut...?"
        hide aaron_11
        show aaron_11_1:
            xpos 450
            ypos 30
            zoom 0.3          
        unknown "Or... beatboxing time?"
        kristik "Wait..."
        kristik "Aaron?!?!?"
        kristik "Are you here to kill me!?!?!?!?"
        hide aaron_11_1
        show aaron_7:
            xpos 450
            ypos 30
            zoom 0.35
        aaron "What...? No."      
        aaron "It's probably that stupid rumor that Kyle and Jason told you about..."
        hide aaron_7
        show aaron_7:
            xpos 250
            ypos 30
            zoom 0.35  
        show dd7:
            xpos 720
            ypos 300
            zoom 0.55    
        with dissolve  
        unknown "Hurry up dad you're taking too long!" 
        kristik "DAD??!?!"
        hide dd7
        show dd8:
            xpos 720
            ypos 300
            zoom 0.55   
        unknown "Dad, who the heck is this guy?"
        hide aaron_7
        show aaron_11:
            xpos 250
            ypos 30
            zoom 0.3         
        aaron "It's uhhh friend of mine...."
        hide dd8
        show dd11:
            xpos 720
            ypos 300
            zoom 0.55  
        unknown "Well, you're taking too long. I'll just wait at the entrance."
        hide dd11
        hide aaron_11
        show aaron_11:
            xpos 450
            ypos 30
            zoom 0.3  
        with dissolve
        kristik "I didn't know you had a kid bro...."
        hide aaron_11
        show aaron_7:
            xpos 450
            ypos 30
            zoom 0.35
        aaron "Yeah it's a pain in the ass sometimes... I really wanted a son but... oh well..."    
        aaron "Kaori wanted to go shopping... so I might as well have gone."
        kristik "I don't got much to do either, can I come?"
        hide aaron_7
        show aaron_11:
            xpos 450
            ypos 30
            zoom 0.3  
        aaron "Sure I don't really care... she just wanted some new shoes."
        kristik "SHOES?!?!??!?"
        kristik "Aight bet imma buy her some fire shiddd!!"
        hide aaron_11
        show aaron_11_1:
            xpos 450
            ypos 30
            zoom 0.3          
        aaron "it better not be some dumb basketball shoes."    
        kristik "W-what?? No of course not! (cough cough)"    
        aaron "Right..."
        hide aaron_11_1
        with dissolve
        hide BG039
        show BG042
        with dissolve
        show aaron_11_1:
            xpos 250
            ypos 30
            zoom 0.3 
        show dd1:
            xpos 720
            ypos 300
            zoom 0.55             
        with dissolve   
        kaori "Yay the mall!!!"
        kristik "She really likes shopping huh?"
        hide aaron_11_1
        show aaron_11:
            xpos 250
            ypos 30
            zoom 0.3          
        aaron "She got it from her mother..."        
        hide aaron_11
        show aaron_7:
            xpos 250
            ypos 30
            zoom 0.35  
        aaron "Alright Kaori, well daddy is going to take a look at the GameStop, so uhh you and Kristik can look for some shoes or something..."
        kristik "WAT???"
        hide dd1
        show dd2:
            xpos 720
            ypos 300
            zoom 0.55  
        kaori "Okay!"
        kristikmind "{i}WAIT!! maybe i can buy some JORDANS!!!"
        kristikmind "{i}shit... i dont have money though..."
        hide aaron_7
        show aaron_11_1:
            xpos 250
            ypos 30
            zoom 0.3          
        aaron "Take my card and buy her some shoes."
        aaron "They better be actual good shoes; I don't want to see her with balenciagas." 
        kristik "Suuuurreee...."
        aaron "..."
        hide aaron_11_1
        hide dd2
        show dd1:
            xpos 400
            ypos 300
            zoom 0.55  
        with dissolve
        kaori "Where do you go first?"
        kristik "Hm...."
        hide dd1
        show dd2:
            xpos 400
            ypos 300
            zoom 0.55  
        kristik "Let's go to the Nike store."
        hide dd2
        show dd11:
            xpos 400
            ypos 300
            zoom 0.55  
        kaori "Ewwww! Nike is for boys!"     
        kristik "What??? WDYM!?!?!?"
        kristik "They have girl shoes too!"             
        hide dd11
        show dd7:
            xpos 400
            ypos 300
            zoom 0.55 
        kaori "Daddy let's me buy shoes from Gucci!"
        kristik "GUCCI???!!"
        kristik "Why da hell does a 6 year old need Gucci??!!"
        hide dd7
        show dd9:
            xpos 400
            ypos 300
            zoom 0.55 
        kaori "You look like you need some Gucci! You don't have anything expensive on you!"
        kristik "Cmon bro... let's get you some JORDANS!"
        hide dd9
        show dd11:
            xpos 400
            ypos 300
            zoom 0.55 
        kaori "Mommy says Jordans are ugly."
        kristik "WHAT?!?!?!?"
        kristik "Jordans are NOT UGLY THEY BE FIRE !!!"
        hide dd11
        show dd7:
            xpos 400
            ypos 300
            zoom 0.55 
        kaori "The only thing that's on fire right now is your pants because you're lying!"
        kristikmind "{i}why aaron's kid talking SO MUCH FUCKIN SMACK??!"
        hide dd7
        show dd11:
            xpos 400
            ypos 300
            zoom 0.55 
        kaori "Fine! i'll go to your ugly Nike store!"
        kristik "PShshsh.... It ain't ugly and YOU'LL SEE!!"
        hide dd11
        hide BG042
        with dissolve
        show nike
        with dissolve
        kristik "Wow..."
        kristik "Look at it... it's so BEAUTIFUL!! (cry cry)"
        show dd9:
            xpos 720
            ypos 300
            zoom 0.55 
        with dissolve
        kaori "More like ugly!!"   
        kristik "Pshh... it seems as though you haven't learned what REAL drip is..."
        hide dd9
        hide nike
        with dissolve
        show nike2
        with dissolve
        kristik "Hmm...."
        kristikmind "{i}Let's see..."
        kristikmind "{i}The bottom left and top left are trash-tier... lookin like construction boots and some sketchers type shit..."
        kristikmind "{i}middle and bottom right are aight..."
        kristikmind "{i}i think the left middle or top right would be a lot better..."
        $ show_quick_menu = False
        window hide
        menu:
            "Buy Jordan 6 Electric Green":
                $ show_quick_menu = True
                window show
                kristikmind "{i}I think imma buy some Jordan 6 Electric Green"
                jump partTwoTwoTwo
            "Buy Jordan 1 Mid SE Purple":
                $ show_quick_menu = True
                window show
                kristikmind "{i}Imma get her some of that Jordan 1 Mid SE Purple"
                jump partTwoTwoTwo
            "Buy shoes from StockX":
                $ show_quick_menu = True
                window show
                kristikmind "{i}all these shoes be kinda mid.... imma go online and buy some other shoes..."
                hide nike2
                show stockx
                with dissolve
                kristikmind "{i}Sheeeessh!!!!"
                kristikmind "{i}Shit lookin FIRE!!!"
                kristikmind "{i} goddamn these prices..."
                kristikmind "{i} doesn't really matter, i'm using Aaron's card anyways."
                hide stockx
                show nike2
                with dissolve
                kristikmind "{i}aight EZZZZ bought dem shoes!!"
                kristikmind "{i} boughta arrive via PUBG airdrop"
                show dd9:
                    xpos 400
                    ypos 300
                    zoom 0.55 
                with dissolve
                kaori "Are you going to get a shoe or what??!!"     
                kristik "Yeah yeah I already did they gon be airdropped ARMA 3 style"
                hide dd9
                show dd11:
                    xpos 400
                    ypos 300
                    zoom 0.55    
                kaori "Whatever! They better be cute!"
                hide dd11
                hide nike2
                with dissolve
                show BG042
                with dissolve
                kristik "The airdrop should be in by now...."
                transform fall:
                    xpos 300
                    ypos -1500
                    zoom 0.5
                    linear 0.3 ypos 800
                show shoes at fall
                $ renpy.pause(0.3,hard=True)
                play sound "audio/splat.ogg"
                kristik "Shit!!"       
                kristik "I caught em!!"
                show dd4:
                    xpos 400
                    ypos 300
                    zoom 0.55   
                with dissolve
                kaori "What is that?"
                kristik "hehehehe...."
                hide dd4
                hide shoes
                show shoes:
                    xpos 200
                    ypos 100
                    zoom 0.5         
                play sound "audio/tada.ogg"       
                kristik "BEHOLD! THE JORDAN 1 RETRO HIGH BRED BANNED (2016)!!!!"
                hide dd4
                show dd9:
                    xpos 720
                    ypos 300
                    zoom 0.55   
                kaori "Ewww... they look so ugly..."
                kristik "WHAT??! WDYM!!!"
                hide dd9
                show dd11:
                    xpos 720
                    ypos 300
                    zoom 0.55 
                kaori "I want Gucci!"   
                show aaron_7:
                    xpos 150
                    ypos 30
                    zoom 0.35          
                with dissolve
                aaron "Kristik... what the hell is that?"
                aaron "Why the hell did you buy my daughter Jordans?"
                aaron "That looks like size 70. How the hell is she going to wear that?!"
                hide dd11
                show dd7:
                    xpos 720
                    ypos 300
                    zoom 0.55
                kaori "Daddy he wouldn't listen to me! He bought me ugly shoes instead!!!"
                kristik "THEY AINT UGLY DOE!!!"
                hide dd7
                show dd4:
                    xpos 720
                    ypos 300
                    zoom 0.55
                hide aaron_7
                show aaron_11:
                    xpos 150
                    ypos 30
                    zoom 0.3                      
                aaron "It's ok Kaori... daddy will buy you some Louis Vitton later..."
                hide dd4
                show dd1:
                    xpos 720
                    ypos 300
                    zoom 0.55
                kaori "Yayyy!!"
                hide aaron_11
                show aaron_11_1:
                    xpos 150
                    ypos 30
                    zoom 0.3    
                aaron "As for you kristik..."
                aaron "How much did that thing even cost?"
                kristik "Something like.... $50,000???"
                hide aaron_11_1
                show aaron_11:
                    xpos 150
                    ypos 30
                    zoom 0.3     
                aaron "You're telling me... that you spent a whole Tesla on a size 70 shoe????!!!"
                kristik "Uhh... yeah?"
                hide aaron_11
                show aaron_11_1:
                    xpos 150
                    ypos 30
                    zoom 0.3   
                stop music
                play sound "audio/gunload_Master.wav"
                show gun:
                    xpos 200
                    ypos 320 
                    zoom 0.6
                $ renpy.pause(0.8,hard=True)       
                aaron "You're never getting my card again."  
                kristik "WOAHAOWHAOHO!!! IN FRONT OF YOUR DAUGHTER???!!"
                hide dd1
                show dd7:
                    xpos 720
                    ypos 300
                    zoom 0.55
                kaori "Psh. This doesn't matter, I've seen this happen hundreds of times with daddy."
                kristik "WTF???"
                aaron "Cya Kris."                                          
                #======================================================================================================
                # PLAY GUN SHOOTING SOUNDS
                #======================================================================================================
                play sound "audio/awp.mp3"                                        
                show white 
                hide gun onlayer misc 
                window hide 
                $ show_quick_menu = False
                with dissolve
                $ renpy.pause(1,hard=True)
                window show
                with dissolve             
                narrator "Kristik was sent to the afterlife after being penetrated by a 9mm bullet."
                narrator "His Jordans would forever be a reminder of why you shouldn't trust other people with your money."
                narrator "{b}Bad ending 5/21{/b}"
                if (persistent.endingFinished5 < 1):
                    $ persistent.endingFinished5 += 1
                elif (persistent.endingFinished5 >= 1):
                    pass
                else:
                    narrator "PERSISTENT DATA FAILURE FOR SECTION 12199. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                    $ renpy.quit()
                window hide
                with dissolve                
                $ MainMenu(confirm=False)()
        label partTwoTwoTwo:
            $ EXPrikka += 1
            show srik0202:
                xpos 400
                zoom 1.2
            with dissolve
            kristik "Oh..?"
            hide srik0202
            show srik0208:
                xpos 400
                zoom 1.2
            rikka "Tch."
            hide srik0208
            show srik0207:
                xpos 400
                zoom 1.2
            rikka "What are you doing here?"
            hide srik0207
            show srik0208:
                xpos 100
                zoom 1.2
            show dd9:
                xpos 720
                ypos 300
                zoom 0.55  
            with dissolve  
            kaori "What are you doing?! Hurry up and buy it already!"   
            hide dd9
            show dd6:
                xpos 720
                ypos 300
                zoom 0.55  
            hide srik0208
            show srik0201:
                xpos 100
                zoom 1.2
            rikka "Kristik..? Who is that?"
            hide dd6
            show dd1:
                xpos 720
                ypos 300
                zoom 0.55 
            kaori "Kaori. My name is Kaori!"
            kristik "It's one of my friend's daughter... we're looking for some shoes."
            hide dd1
            show dd8:
                xpos 720
                ypos 300
                zoom 0.55 
            hide srik0201
            show srik0108:
                xpos 100
                zoom 1.2
            rikka "Shoes?!!! Why would you buy this girl Nike's??!!!"
            hide srik0108
            show srik0109:
                xpos 100
                zoom 1.2
            hide dd8
            show dd7:
                xpos 720
                ypos 300
                zoom 0.55
            kaori "That's what I was telling him!"
            hide srik0109
            show srik0201:
                xpos 100
                zoom 1.2
            hide dd7
            show dd6:
                xpos 720
                ypos 300
                zoom 0.55            
            rikka "C'mon Kaori, let's leave this plebian and get some Gucci."
            hide dd6
            show dd1:
                xpos 720
                ypos 300
                zoom 0.55  
            kaori "Yay!!!"
            hide dd1
            hide srik0201
            with dissolve
            kristik "ugh... but JORDANS ARE FIRE!!!!!!!!!!"     
            hide nike2
            show BG042
            with dissolve
            show aaron_11_1:
                xpos 450
                ypos 30
                zoom 0.35                   
            with dissolve
            aaron "Where's Kaori?"
            kristik "She's with my friend... to buy Gucci..."
            aaron "Who's this friend?"
            kristik "Um... well uh it's a friend that's a girl I guess...?"
            aaron "Huh..."
            hide aaron_11_1
            show aaron_7:
                xpos 450
                ypos 30
                zoom 0.40
            aaron "I didn't know you managed to snag yourself a wife..."
            kristik "She isn't my wife!!"
            hide aaron_7
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.35  
            aaron "Yeah yeah whatever... cut the tsundere crap already."
            hide aaron_11
            show aaron_11_1:
                xpos 450
                ypos 30
                zoom 0.35              
            aaron "I already know of you and Kyle, Jason and Kevin."
            aaron "Seriously... what the hell kind of name is ''ASIANBOYZ''???"
            kristik "Wait... how do you know that?"
            hide aaron_11_1
            show aaron_7:
                xpos 450
                ypos 30
                zoom 0.40  
            aaron "I've got various intelligence sources...."
            hide aaron_7
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.35 
            aaron "By that I mean that I just look at your guys' Discord server."  
            kristikmind "{i}So much for ''intelligence''..."
            hide aaron_11
            show aaron_11_1:
                xpos 10
                ypos 30
                zoom 0.35                                
            show srik0201:
                xpos 800
                ypos 30
                zoom 1.1
            show dd1:
                xpos 450
                ypos 300
                zoom 0.55  
            with dissolve
            kaori "Daddy!!!"   
            hide dd1
            show dd5:
                xpos 450
                ypos 300
                zoom 0.55 
            kaori "Aunty Rikka bought me some Gucci!!!"
            aaron "That's cool I guess..."
            aaron "Anyways. Kristik, I will be seeing you later. We need to go. Her mom wants us home right now."
            kristik "Uhhh.. sure..."   
            hide dd5
            hide aaron_11_1
            with dissolve
            hide srik0201
            show srik0208:
                xpos 400
                zoom 1.1
            with dissolve
            hide srik0208
            show srik0207:
                xpos 400
                zoom 1.1
            rikka "What are you doing here?"
            hide srik0207
            show srik0208:
                xpos 400
                zoom 1.1        
            kristik "Ummm... I was just... kinda bored."
            kristik "So I want to the mall..."
            hide srik0208
            show srik0207:
                xpos 400
                zoom 1.1
            rikka "Are you sure that you aren't just following me??"
            hide srik0207
            show srik0208:
                xpos 400
                zoom 1.1        
            kristik "What?? No!"                 
            kristik "I ain't no pervert bro!"
            hide srik0208
            show srik0207:
                xpos 400
                zoom 1.1
            rikka "I'm not your ''bro''."
            rikka "I'm going home. There's noething else for me to do here."
            hide srik0207
            with dissolve
            kristik "But I just wanted... to apologize..."
            kristik "Though I guess if I were a girl and I said something like that to myself an apology probably wouldn't cut it..."
            kristik "Whatever... I suppose I'll get something to eat..."
            stop music fadeout 2.0
            hide BG042
            with dissolve
            $ renpy.pause(2,hard=True)
            play music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k intro.ogg"
            queue music "audio/Sanoba Witch OST - Kino-au Nakama-tachi-128k.ogg"
            show BG028c      
            with dissolve      
            kristik "Wow... I've never seen an Indian restaurant being this fancy before...."
            kristik "Now, I wonder... what should I even order?"
            kristik "Tandoori chicken?? Mmmmmm...."
            show BG027_o
            show srik0210:
                xpos 700
                zoom 1.1
            with dissolve
            play sound "audio/shopbell.ogg"
            rikka "I could really go for some Indian food..."
            kristik "WTF?!?!?!?!W!?W>?!>@?!>@>!@!@!#@"
            hide srik0210
            show srik0115:
                xpos 700
                zoom 1.1
            rikka "I love Indian people after all..."
            hide srik0115
            show srik0112:
                xpos 700
                zoom 1.1
            rikka "If only I could tell him..."
            kristikmind "{i}Tell who...?"
            kristikmind "{i}AND HOL UP SHE LOVE INDIAN PEPOEPLE!?!WE?E?>!?>?#>@?>#?@>?#$?$>?#??@?#>$??@#?$?@#?$?@>#?$>"
            hide BG027_o
            hide srik0112
            with dissolve
            show srik0113:
                xpos 400
                zoom 1.1
            with dissolve
            rikka "Hahh...."
            hide srik0113
            show srik0201:
                xpos 400
                zoom 1.1
            rikka "...?"
            hide srik0201
            show srik0117:
                xpos 400
                zoom 1.1
            with dissolve
            rikka "HUH???!!!"
            kristik "Oh... hi...?"
            hide srik0117
            show srik0108:
                xpos 400
                zoom 1.1
            rikka "I'M TOTALLY CONVINCED! YOU ARE FOLLOWING ME!"
            hide srik0108
            show srik0109:
                xpos 400
                zoom 1.1
            kristik "NO!!! IT'S TOTALLY A COINCIDENCE!!!"
            kristik "I'M NOT A CREEP I SWEAR!!!!"
            hide srik0109
            show srik0108:
                xpos 400
                zoom 1.1
            rikka "JUST LEAVE ME ALONE THEN YOU WEIRDO!!"
            hide srik0108
            show srik0207:
                xpos 400
                zoom 1.1
            rikka "I'm out of here!"
            hide srik0207
            with dissolve
            kristik "Bro... it's NOT MY FAULT THAT YOU LIKE INDIAN FOOD!!!"    
            kristik "Man... I just wanted to eat some tandoori chicken...."
            stop music fadeout 2.0
            hide BG028c
            with dissolve
            $ renpy.pause(1,hard=True)
            show BG036
            with dissolve
            $ renpy.pause(0.5,hard=True)
            kristik "Wow... nice day today."
            kristik "If only I didn't fuck up hard..."
            hide BG036
            show BG080Y
            with dissolve
            $ renpy.pause(0.5,hard=True)
            play music "audio/Sabona Witch OST - Yasashii Kaze-128k.ogg"
            kristik "Ugh.... Shiva...."
            kristik "The indian gods... what should I do?"
            narrator "...."
            voicevoid "Kristik..."
            kristik "?!!!!"
            voicevoid "League of Legends..."
            kristik "What...?"
            voicevoid "Gamer girl...."
            kristik "Gamer... girl?"
            voicevoid "Tekken."
            kristik "!!!!"
            kristik "I understand the mission."
            voicevoid "Yes..."
            kristik "Rikka is a gamer girl secretly."
            kristik "She loves League of Legends and Tekken."
            kristik "I know how to win her heart."
            kristik "I will show off my epic litty LOL Tekken 7 skillz."
            stop music fadeout 2.0
            hide BG080Y
            with dissolve
            $ show_quick_menu = False
            window hide
            with dissolve
            $ renpy.pause(2,hard=True)
            show BG012
            play music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps) intro.ogg"
            queue music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps).ogg"
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve
            $ renpy.pause(0.5,hard=True)
            kristik "I was able to convince Ringo to give Rikka's address...."
            kristik "I just need to keep in mind of what Shiva told me yesterday..."
            kristik "Remember... talk about League of Legends..."
            kristik "..."
            kristik "I just realized that I don't even play League of Legends..."
            kristik "Fuck... this might be harder than I thought."
            kristik "Well, I'll just try to think of something that is League related..."
            kristik "Anyways... I'd better start going..."
            $ renpy.pause(0.5,hard=True)
            show sho21a_952:
                xpos 350
                ypos 30
                zoom 0.8
            with dissolve
            stop music fadeout 2.0
            unknown "..."
            play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
            unknown "So this is the creep she was talking about..."
            hide sho21a_952
            show sho21a_921:
                xpos 350
                ypos 30
                zoom 0.8
            unknown "He does look really weird and mysterious..."
            hide sho21a_921
            show sho21a_952:
                xpos 350
                ypos 30
                zoom 0.8 
            unknown "I'll charge him in the court of law... no matter what it takes."
            hide sho21a_952
            hide BG012
            with dissolve
            $ renpy.pause(0.5,hard=True)
            show BG007
            with dissolve
            kristik "Where tf am I???"
            kristik "Is this really where she lives...?"
            show sho21a_202:
                xpos 600
                ypos 30
                zoom 0.8 
            show srik0108:
                xpos 0
                zoom 1.2
            with dissolve
            rikka "There he is! The closet weirdo!"
            hide srik0108
            show srik0109:
                xpos 0
                zoom 1.2
            kristik "Uhhh...whaT?!??!"
            kristik "Who tf is that??!!"
            hide sho21a_202
            show sho21a_201:
                xpos 600
                ypos 30
                zoom 0.8
            unknown "You're under arrest for stalking and perversion without a license!"
            hide sho21a_201
            show sho21a_202:
                xpos 600
                ypos 30
                zoom 0.8
            kristik "WHAT?!?!"
            kristik "wait... there's a license for that?"
            hide sho21a_202
            show sho21a_503:
                xpos 600
                ypos 30
                zoom 0.8
            unknown "Unfortunately, to qualify for such license you must be have less than 75%% body fat composition!"
            hide sho21a_503
            show sho21a_504:    
                xpos 600
                ypos 30
                zoom 0.8
            kristik "aww shit..."
            hide sho21a_504
            show sho21a_202:
                xpos 600
                ypos 30
                zoom 0.8
            play sound "audio/gunload_Master.wav"
            show gun onlayer misc:
                xpos 600
                ypos 320 
                zoom 0.6
            $ renpy.pause(0.8,hard=True)  
            hide sho21a_202
            show sho21a_201:
                xpos 600
                ypos 30
                zoom 0.8            
            unknown "Hold still!"
            hide sho21a_201
            show sho21a_202:
                xpos 600
                ypos 30
                zoom 0.8            
            kristik "WOAHWOAHWOAH WHY ARE YOU PULLING OUT A GUN???? IS IT BECAUSE IM BLACK?!?!?!"
            stop music fadeout 2.0
            play sound "audio/awp.mp3"                                        
            show white 
            hide gun onlayer misc
            hide sho21a_202
            hide srik0109
            hide BG007
            $ show_quick_menu = False
            window hide
            with dissolve
            $ renpy.pause(3,hard=True)
            hide white
            with dissolve
            $ renpy.pause(3,hard=True)
            $ show_quick_menu = True
            window show
            with dissolve            
            show jail
            with dissolve
            kristik "...."
            play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
            kristik "Owww.... where the fuck am I???"
            kristik "WHY AM I IN PRISON?!!!!"
            kristik "Goddamnit... I just wanted to GO TO HER HOUSE!!@!@!@!@!@!@!@"
            kristik "Ouch!"
            kristik "Fuck... is this a bullet wound in my arm??!!!"
            unknown "{i}Cell manager 2A, open cell 212B please."
            unknown "{i}Opening cell 212B."
            kristik "Cell 212B..? Am I that cell?"
            play sound "audio/jailopen.ogg"
            #====================================================================================================================================================================================
            ###PLAY CELL HONK AND DOOR OPENING SOUND
            #====================================================================================================================================================================================
            $ renpy.pause(2,hard=True)
            hide jail
            show prison
            with dissolve
            $ renpy.pause(0.5,hard=True)
                        
            show sho21a_202:
                xpos 250
                ypos 30
                zoom 1
            with dissolve
            hide sho21a_202
            show sho21a_201:
                xpos 250
                ypos 30
                zoom 1
            unknown "Hey."
            hide sho21a_201
            show sho21a_402:
                xpos 250
                ypos 30
                zoom 1
            kristik "YOU!!! YOU SHOT ME!!!"
            kristik "WHY??!!!!"
            kristik "IS IT BECAUSE YALL ON THAT RACISM SHIT?!?!!"
            hide sho21a_402
            show sho21a_503:
                xpos 250
                ypos 30
                zoom 1
            unknown "Look, in my defense I didn't see that I pulled a gun out."
            hide sho21a_503
            show sho21a_202:
                xpos 250
                ypos 30
                zoom 1
            kristik "HOW DO YOU NOT NOTICE A GUN POINTING AT ME?!?!?!!!"
            unknown "Alright guys, that's enough."
            hide sho21a_202
            show sho21a_501:
                xpos -100
                ypos 30
                zoom 1
            show haruhi07:
                xpos 500
                zoom 0.8
            with dissolve
            unknown "You guys are really loud."
            kristik "WHO ARE YOU?!!! ARE YOU HER BOSS?!!! I NEED TO FILE A COMPLAINT!!"
            hide haruhi07
            show haruhi09:
                xpos 500
                zoom 0.8   
            unknown "No, I'm your attorney, Haruhi Suzumiya."      
            unknown "I'm representing you in this case."
            kristik "CASE????!! IM GETTING SUED?!!!"
            unknown "You're not getting sued."
            kristik "Oh... phew..."
            hide haruhi09
            show haruhi07:
                xpos 500
                zoom 0.8  
            unknown "You're accused of stalking."
            kristik "WHAT>!?!?!?!??!@!@!@"   
            hide haruhi07
            show haruhi09:
                xpos 500
                zoom 0.8   
            kristik "I NEVER STALKED ANYBODY IN MY LIFE!! PROMISE!!!"
            unknown "We'll discuss details later but not now. Hurry up, let's go."
            hide haruhi09
            hide sho21a_501
            hide prison 
            with dissolve                              
            window hide
            $ show_quick_menu = False
            with dissolve
            $ renpy.pause(1,hard=True)
            show BG025
            with dissolve
            window show
            $ show_quick_menu = True
            $ renpy.pause(1,hard=True)
            with dissolve
            show haruhi11:
                xpos 200
                zoom 0.8 
            with dissolve
            kristik "Super fancy place..."
            hide haruhi11
            show haruhi07:
                xpos 200
                zoom 0.8
            haruhi "Alright, let's review this case."
            haruhi "uh..... defendant was spotted outside the complex area.... previous history of breaking and entering.... hm..."
            hide haruhi07
            show haruhi09:
                xpos 200
                zoom 0.8 
            haruhi "This is gonna be really hard."
            haruhi "EXTREMELY hard."
            kristik "Sheesh...."          
            hide haruhi09
            show haruhi12:
                xpos 200
                zoom 0.8
            haruhi "The district attorney... Beatrice Blaine Wolfeschlegelsteinhausenbergerdorff..."
            kristik "Who???!!"
            haruhi "The girl that shot you."
            kristik "HER??!!! SHES THE D.A.??!!!"
            haruhi "Yeah, she's really good at her job. Her conviction rate is 99%%."
            hide haruhi12
            show haruhi09:
                xpos 200
                zoom 0.8 
            haruhi "She's only ever had one case where she wasn't able to win. And it was her very first case."
            kristik "Fuck..."   
            hide haruhi09
            show haruhi12:
                xpos 200
                zoom 0.8
            haruhi "We've got some work cut out for ourselves, so make sure that you do EVERYTHING that I say. Hearing is tomorrow."
            kristik "TOMORROW?!!!"
            kristik "Wait... can't I mention that the D.A. shot me?!!! Maybe that's assault with a deadly weapon??!!!"
            hide haruhi12
            show haruhi09:
                xpos 200
                zoom 0.8 
            haruhi "It's not ''AWD''. She had a loaded firearm, which is not covered under AWD. It's a more serious charge."
            haruhi "You could mention it; however it probably won't help with your stalking charges but you might be able to get back at the D.A."  
            kristik "Yeah! LET'S GET BACK AT THE BITCH!"
            hide haruhi09
            show haruhi12:
                xpos 200
                zoom 0.8
            haruhi "If you say so."
            stop music fadeout 2.0
            hide haruhi12
            hide BG025
            with dissolve
            window hide
            $ show_quick_menu = False
            with dissolve
            $ renpy.pause(1,hard=True)
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8               
            with dissolve
            play music "audio/Phoenix Wright Ace Attorney OST - Trial-(128kbps).ogg"
            window show
            $ show_quick_menu = True
            $ renpy.pause(1,hard=True)
            with dissolve         
            judge "This court is now in session."  
            kristik "why tf is the judge a maid?"
            show haruhi09 onlayer mcsprite:
                xpos -200
                ypos 450
                zoom 0.55
            haruhi "Don't question it."
            hide haruhi09 onlayer mcsprite
            judge "Would the plaintiff like to start their opening statement?"
            assistant "Yes."
            hide mori2
            hide court1
            show court4
            show seitokaichou2:
                xpos 400
                zoom 0.73                  
            with dissolve
            kristik "Is that the D.A.'s assistant?"
            show haruhi09 onlayer mcsprite:
                xpos -200
                ypos 450
                zoom 0.55
            haruhi "Yeah. The D.A. will not be present. It will just be him."
            hide haruhi09 onlayer mcsprite
            hide seitokaichou2
            show seitokaichou6:
                xpos 400
                zoom 0.73    
            assistant "Ladies and gentlemen of the jury, I want to propose this situation to you."
            assistant "Imagine if you were doing your daily routine: waking up, showering, brushing your teeth, maybe dress up to go to work or go to school."
            assistant "But just imagine for a second that with every step you take, or with every cup of coffee you drink..."
            hide seitokaichou6
            show seitokaichou1:
                xpos 400
                zoom 0.73
            assistant "A FAT INDIAN MAN IS WATCHING YOU!!!"
            kristik "wtf...?"     
            hide seitokaichou1
            show seitokaichou5:
                xpos 400
                zoom 0.73
            assistant "Fat indian man... much like the defendant." 
            kristik "Bruh..."
            stop music 
            play sound "audio/objection.ogg"
            show white onlayer misc4
            show objection onlayer misc3:
                zoom 0.7
            $ renpy.pause(0.01,hard=True)
            hide white onlayer misc4
            with dissolve
            haruhi "OBJECTION!!!"   
            hide objection onlayer misc3
            hide court4
            show court2 
            hide seitokaichou5
            hide haruhi03
            show haruhi04:
                xpos 300
                ypos 29
                zoom 0.73 
            play music "audio/Phoenix Wright Ace Attorney OST - Questioning _ Moderato 2001-(128kbps).ogg"
            haruhi "According to his health reports... the defendant is only 40 pounds overweight!!!"
            hide court2
            hide haruhi04
            show court4
            show seitokaichou1:
                xpos 400
                zoom 0.73                  
            assistant "Tch."
            hide seitokaichou1
            show seitokaichou6:
                xpos 400
                zoom 0.73  
            assistant "No matter, it still doesn't change the fact that he's a stalker."             
            hide court4
            hide seitokaichou6
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "Does the defense have any more objections?"
            hide court1
            hide mori2 
            show court2 
            show haruhi02:
                xpos 300
                ypos 29
                zoom 0.73    
            haruhi "We have no objections."  
            hide court2
            hide haruhi02
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "Very well. The defense may give their opening statement."          
            hide court1
            hide mori2 
            show court2 
            show haruhi05:
                xpos 300
                ypos 29
                zoom 0.73    
            haruhi "Uhhh....."  
            hide haruhi05
            show haruhi15:
                xpos 300
                ypos 29
                zoom 0.73   
            stop music 
            play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
            haruhi "I got nothing lol.." 
            kristikmind "{i}WTF kind of lwayer did i get...?!!!"  
            hide haruhi15
            show haruhi02:
                xpos 300
                ypos 29
                zoom 0.73  
            stop music fadeout 1.0
            play music "audio/Phoenix Wright Ace Attorney OST - Trial-(128kbps).ogg" fadein 1.0

            haruhi "However, we're so good we don't need an opening statement."
            kristikmind "{i}i got a bad feeling about this..."
            hide court2
            hide haruhi02
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "If that's what the defense wishes, we can proceed as usual."   
            judge "The accusing party may start with their deliberation." 
            hide mori2
            hide court1
            show court4
            show seitokaichou2:
                xpos 400
                zoom 0.73 
            assistant "Judge. The prosecution calls Mikuru to the stand!!"
            kristikmind "{i}WHO TF IS MIKURU?!!!!"
            hide court4
            hide seitokaichou2
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "Mikuru. If you would please present yourself to the podium." 
            hide mori2
            hide court1 
            show court3
            with dissolve
            show mikuru4:
                xpos 240
                ypos -32
                zoom 0.8  
            with dissolve
            mikuru "Umm... Hi..."
            kristikmind "{i}IVE NEVER SEEN THAT PERSON IN MY LIFE!!! WHY IS SHE EVEN HERE?!!"
            show seitokaichou6 onlayer mcsprite:
                xpos -200
                ypos 500
                zoom 0.6 
            assistant "Mikuru, if you could explain to the court, what exactly were you doing at approximately 10 AM yesterday?" 
            hide seitokaichou6 onlayer mcsprite       
            hide mikuru4
            show mikuru1:
                xpos 240
                ypos -32
                zoom 0.8 
            mikuru "Umm.. I was being stalked by that man..."
            kristikmind "{i}WHAT THE FUCK?!!!! IVE NEVER EVEN STALKED THAT PERSON!!!!" 
            stop music
            play sound "audio/objection.ogg"
            show white onlayer misc4
            show objection onlayer misc3:
                zoom 0.7
            $ renpy.pause(0.01,hard=True)
            hide white onlayer misc4
            with dissolve
            haruhi "OBJECTION!!!!"   
            hide objection onlayer misc3
            hide mikuru1
            hide court3
            show court2 
            show haruhi03:
                xpos 300
                ypos 79
                zoom 0.73 
            with dissolve   
            play music "audio/Phoenix Wright Ace Attorney OST - Questioning _ Moderato 2001-(128kbps).ogg"
            haruhi "My client has never even seen that person! What evidence does she have that would prove her being stalked?"
            hide court2
            hide haruhi03
            show court4
            show seitokaichou6:
                xpos 400
                zoom 0.73                  
            assistant "If you're so inclined to ask, then let's ask the same question to her."
            hide court4
            hide seitokaichou6
            show court3
            show mikuru4:
                xpos 240
                ypos -32
                zoom 0.8  
            with dissolve
            show seitokaichou2 onlayer mcsprite:
                xpos -200
                ypos 500
                zoom 0.6 
            with dissolve
            assistant "Mikuru, what evidence do you have?"     
            hide seitokaichou2 onlayer mcsprite             
            mikuru "Umm... I uhh... saw him..."
            kristikmind "{i}WTF KIND OF BULLSHIT EVIDENCE IS THAT?!!!"    
            stop music
            play sound "audio/objection.ogg"
            show white onlayer misc4
            show objection onlayer misc3:
                zoom 0.7
            $ renpy.pause(0.01,hard=True)
            hide white onlayer misc4
            with dissolve
            haruhi "OBJECTION!!!!"   
            hide objection onlayer misc3
            hide mikuru4
            hide court3
            show court2 
            show haruhi03:
                xpos 300
                ypos 79
                zoom 0.73 
            with dissolve   
            haruhi "That's some shite evidence!"                                                              
            hide court2
            hide haruhi03
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "Watch your language."
            hide court1
            hide mori2 
            show court2 
            show haruhi15:
                xpos 300
                ypos 29
                zoom 0.73    
            haruhi "Woops lol..."     
            hide court2
            hide haruhi15
            show court3
            show mikuru4:
                xpos 240
                ypos -32
                zoom 0.8  
            with dissolve
            show seitokaichou2 onlayer mcsprite:
                xpos -200
                ypos 500
                zoom 0.6 
            with dissolve
            play music "audio/Phoenix Wright Ace Attorney OST - Questioning _ Moderato 2001-(128kbps).ogg"
            assistant "Mikuru, are you telling the truth?"
            hide seitokaichou2 onlayer mcsprite
            hide mikuru4
            show mikuru1:
                xpos 240
                ypos -32
                zoom 0.8  
            mikuru "Ummm uhh....."
            hide court3
            hide mikuru1
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "Remember, you are under oath. You will be imprisoned if you are found lying."
            hide court1
            hide mori2
            show court3
            show mikuru1:
                xpos 240
                ypos -32
                zoom 0.8  
            mikuru "UmmMMMm...."
            hide mikuru1
            show mikuru3:
                xpos 240
                ypos -32
                zoom 0.8 
            stop music
            play sound "audio/question.ogg"
            mikuru "I have no evidence! I was just paid by the D.A. to say this!"
            kristikmind "{i}N-NANI?!?!!"
            hide court3
            hide mikuru3
            show court1
            show mori1:
                xpos 400
                ypos -40
                zoom 0.8  
            play music "audio/Phoenix Wright Ace Attorney OST - Pressing Pursuit Cornered-(128kbps).ogg" 
            judge "Wow."
            hide mori1
            show mori3:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "Mikuru, you were lying just now?"
            hide court1
            hide mori3
            show court3            
            show mikuru3:
                xpos 240
                ypos -32
                zoom 0.8 
            mikuru "Please! I don't want to go to prison!"            
            hide court3
            hide mikuru3
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "You won't go to prison. You will have a scheduled execution on the 9th, and -1,000,000 social credit for your whole family."
            hide court1
            hide mori2
            show court3            
            show mikuru3:
                xpos 240
                ypos -32
                zoom 0.8 
            mikuru "What?!!! Noooo!!!!"
            hide mikuru3
            hide court3
            show court2 
            show haruhi02:
                xpos 300
                ypos 29
                zoom 0.73    
            haruhi "Heh... So much for evidence, DA."    
            hide court2
            hide haruhi02
            show court4
            show seitokaichou1:
                xpos 400
                zoom 0.73
            assistant "Tch."
            hide court4
            hide seitokaichou1
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            judge "I've made my decision. The defendant Kristik Lal, is not guilty on charges of stalking."
            kristikmind "{i}LETS GOOOOO!!!!"
            hide court1
            hide mori2
            show court4
            show seitokaichou1:
                xpos 400
                zoom 0.73
            assistant "What???!!! We didn't even do any cross examination!"                      
            hide court4
            hide seitokaichou1
            show court1
            show mori2:
                xpos 400
                ypos -40
                zoom 0.8   
            play sound "audio/question.ogg"
            judge "How about you cross examinate deez nuts?"
            judge "This court is adjourned. Go home."
            kristikmind "{i}LETS GOOOOO LOOOOOLL!!!!"
            hide court1
            hide mori2
            show court4
            show seitokaichou1:
                xpos 400
                zoom 0.73
            assistant "Tch..! Don't worry, Kristik! I will put you in prison!"
            hide court4
            hide seitokaichou1
            show court2 
            show haruhi02:
                xpos 300
                ypos 29
                zoom 0.73    
            haruhi "Another resounding success... thanks to me."  
            stop music fadeout 2.0 
            hide haruhi02
            hide court2
            with dissolve
            window hide
            $ show_quick_menu = False
            with dissolve
            $ renpy.pause(1,hard=True)
            show BG025
            with dissolve
            window show
            $ show_quick_menu = True
            $ renpy.pause(1,hard=True)
            with dissolve
            play music "audio/Riddle Joker Original Soundtrack OST Secret Lab Instrumental-(128kbps).ogg"
            show haruhi08:
                xpos 200
                zoom 0.8 
            with dissolve
            kristik "Let's GOOO!!!!"
            kristik "P100 LAW FIRM!!!"
            haruhi "Yeah!!! That was super easy!!!"
            hide haruhi08
            show haruhi06:
                xpos 200
                zoom 0.8 
            haruhi "That was honestly way too easy! I thought that the D.A. would be way smarter! They are totally so dumb!"
            hide haruhi06
            show haruhi07:
                xpos 200
                zoom 0.8             
            play sound "audio/Door knocking sound effect-(128kbps).ogg"
            #========================================================================================================================================================
            #       PLAY DOOR KNOCKING SOUNDS
            #========================================================================================================================================================      
            $ renpy.pause(2,hard=True)
            haruhi "Who's knocking at the door at this hour?"
            hide haruhi07
            with dissolve
            play sound "audio/Door Opening - Sound Effect _ ProSounds-(128kbps).ogg"
            #========================================================================================================================================================
            #       PLAY DOOR OPENING SOUNDS
            #========================================================================================================================================================      
            $ renpy.pause(2,hard=True)                              
            show haruhi07:
                xpos 200
                zoom 0.8  
            with dissolve        
            kristik "There was just a note outside the door..."
            haruhi "What??? A note??? Let me see it!"
            stop music fadeout 2.0
            hide haruhi07
            show note
            with dissolve
            kristik "..."
            kristik "This is kinda creepy..."
            hide note
            show haruhi07:
                xpos 200
                zoom 0.8  
            with dissolve 
            play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg" fadein 1.0
            haruhi "What?? What does this even mean?"
            kristik "Are they going to kill me?!"
            hide haruhi07
            show haruhi12:
                xpos 200
                zoom 0.8 
            haruhi "I heard rumours of the D.A. assassinating defendants who won against them..." 
            haruhi "That explains the 99%% conviction rate..."
            kristik "WHAT?!?!?!! SO I AM GOING TO DIE THEN?!!!!"
            hide haruhi12            
            show haruhi08:
                xpos 200
                zoom 0.8   
            haruhi "Probably not! They are just trying to scare you most likely." 
            haruhi "welp. I'm off! I gotta hit the hay!"
            hide haruhi08
            with dissolve
            kristik "WAIT DON'T JUST LEAVE ME!!!"
            play sound "audio/Door Opening - Sound Effect _ ProSounds-(128kbps).ogg"
            #========================================================================================================================================================
            #       PLAY DOOR CLOSING SOUNDS
            #========================================================================================================================================================      
            $ renpy.pause(2,hard=True)    
            kristik "Shit...."
            kristik "The D.A.... coming to kill me???"
            kristik "Fuck bro I gotta buy some guns!!"
            hide BG025
            show BG025n
            play sound "audio/Light Switch Sound Effect-(128kbps).ogg"
            stop music fadeout 1.0
            #========================================================================================================================================================
            #       PLAY LIGHT SWITCH SOUND
            #========================================================================================================================================================  
            $ renpy.pause(0.5,hard=True)          
            kristik "AHHH!!! WTF?!!! WHAT HAPPENED TO THE LIGHTS?!?!?!"    
            show sho21a_504_b:
                xpos 250
                ypos 30
                zoom 1
            with dissolve
            kristik "WHOS THERE?!?!!! DONT EAT ME!!! IM 99%% FAT ANYWAYS!!!"
            hide BG025n
            show BG025
            show sho21a_504:
                xpos 250
                ypos 30
                zoom 1      
            play sound "audio/Light Switch Sound Effect-(128kbps).ogg"
            #========================================================================================================================================================
            #       PLAY LIGHT SWITCH SOUND
            #========================================================================================================================================================      
            kristik "AHHH!!!!!!!!!!!!!!!!!!!!!!! (pissing)"  
            hide sho21a_504
            show sho21a_401:
                xpos 250
                ypos 30
                zoom 1  
            play music "audio/Sanoba Witch OST Real Friend InstVer 128k.ogg"
            beatrice "What are you doing??!!! Stop peeing!!"  
            kristik "WAAHHH!H!!!!!!!"
            hide sho21a_401
            show sho21a_402:
                xpos 250
                ypos 30
            beatrice "..."
            hide sho21a_402
            show sho21a_201:
                xpos 250
                ypos 30
            beatrice "Look, can you just stop peeing?"
            hide sho21a_201
            show sho21a_202:
                xpos 250
                ypos 30            
            kristik "WAAHHH!!!!--- oh... it's just you."
            hide sho21a_202
            show sho21a_201:
                xpos 250
                ypos 30
            beatrice "What do you mean it's just me??!!"
            hide sho21a_201            
            show sho21a_005:
                xpos 250
                ypos 30
            kristik "Idk... you just a lame L<OLOOOPO"
            hide sho21a_005
            show sho21a_504:
                xpos 250
                ypos 30
            beatrice "Oh really? Do you really want me to go through with what I wrote on that note?"
            kristik "No. I'm sorry my precious queen, your heiness."
            hide sho21a_504
            show sho21a_801:
                xpos 250
                ypos 30
            beatrice "Good boy."
            hide sho21a_801
            show sho21a_004:
                xpos 250
                ypos 30
            beatrice "Anyways... I came here because because I wanted to make a deal."
            hide sho21a_004
            show sho21a_005:
                xpos 250
                ypos 30   
            kristik "A deal...?"
            hide sho21a_005
            show sho21a_503:
                xpos 250
                ypos 30 
            beatrice "Yes. Well, if you're up with it."
            hide sho21a_503
            show sho21a_004:
                xpos 250
                ypos 30
            beatrice "I can drop all charges on you, if you become a subordinate for me."
            hide sho21a_004
            show sho21a_005:
                xpos 250
                ypos 30   
            kristik "Subordinate...?"
            kristik "Why would I work for you?"
            kristik "YOU FUCKIN SHOT ME!!"
            hide sho21a_005
            show sho21a_503:
                xpos 250
                ypos 30 
            beatrice "Well, it's your choice. Your case is wack anyways, so it'll be dropped no matter the situation."
            hide sho21a_503
            show sho21a_504:
                xpos 250
                ypos 30   
            kristik "ummm...."
            kristikmind "{i}If I work with her, I would abandoning all my friends and Rikka too..."
            $ show_quick_menu = False
            window hide
            menu:
                "''Sure why not, I might as well work with someone as cute as you.''":
                    $ show_quick_menu = True
                    window show
                    $ EXPbeatrice += 1
                    kristik "Sure why not, I might as well work with someone as cute as you."
                    hide sho21a_504
                    show sho21a_101:
                        xpos 250
                        ypos 30
                    beatrice "Hehehe.... those fluffy comments won't work on me... heh..."
                    hide sho21a_101
                    show sho21a_102:
                        xpos 250
                        ypos 30
                    kristik "You're smiling. Alot."
                    hide sho21a_102
                    show sho21a_101:
                        xpos 250
                        ypos 30
                    beatrice "What? No I'm not... hehe...."
                    kristik "You are..."
                    hide sho21a_101
                    show sho21a_001:
                        xpos 250
                        ypos 30
                    beatrice "Well, if you're that eager to work with me, then let's get going right now!"
                    hide sho21a_001
                    show sho21a_002:
                        xpos 250
                        ypos 30
                    kristik "What??? NOW?!!!"
                    hide sho21a_002
                    show sho21a_101:
                        xpos 250
                        ypos 30
                    beatrice "Yeah, there shouldn't be any problems. Let's go! (dababy)"
                    stop music fadeout 2.0
                    hide sho21a_101
                    hide BG025
                    with dissolve
                    window hide
                    $ show_quick_menu = False
                    with dissolve
                    $ renpy.pause(1,hard=True)    
                    with dissolve
                    jump beatricepart
                "''No, I'm sorry. I have too much responsibility to leave at the moment.''":
                    $ show_quick_menu = True
                    window show
                    kristik "No, I'm sorry. I have too much responsibility to leave at the moment."
                    hide sho21a_504
                    show sho21a_201a:
                        xpos 250
                        ypos 30    
                    beatrice "What??!"
                    hide sho21a_201a
                    show sho21a_202:
                        xpos 250
                        ypos 30                                         
                    kristik "What....??"
                    hide sho21a_202
                    show sho21a_201a:
                        xpos 250
                        ypos 30                     
                    beatrice "You don't have a choice! You're going anyways!"
                    hide sho21a_201a
                    show sho21a_202:
                        xpos 250
                        ypos 30                                         
                    kristik "WHAT??!! NO!!!! YOU SAID I CAN CHOOSE!!!"
                    hide sho21a_202
                    show sho21a_201a:
                        xpos 250
                        ypos 30                     
                    beatrice "Be quiet! You're coming with me!"
                    stop music fadeout 2.0
                    hide sho21a_201a
                    hide BG025
                    with dissolve
                    window hide
                    $ show_quick_menu = False
                    with dissolve
                    $ renpy.pause(1,hard=True)    
                    with dissolve
                    jump beatricepart   
    else:                                     
        jump noHoesEnding
    return

label finalPart:
    $ renpy.pause(2,hard=True)
    $ show_quick_menu = True
    window show
    with dissolve 
    show BG011
    play music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps) intro.ogg"
    queue music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps).ogg"
    with dissolve  
    $ renpy.pause(0.5,hard=True)
    kristik "Who knew I would be here again..."  
    kristik "I just told the rest of the girls that I would probably be hanging out here... since Aaron told me to meet him here today."
    hide BG011
    show BG021
    with dissolve   
    $ renpy.pause(0.5,hard=True) 
    show girl4 (8):
        xpos 500
        zoom 0.6 
    with dissolve 
    hide girl4 (8)
    show girl4 (10):
        xpos 500
        zoom 0.6 
    c45 "Hey!"
    hide girl4 (10)
    show girl4 (9):
        xpos 500
        zoom 0.6    
    kristik "Huh...?"
    kristik "Watchu want shawty?"
    show girl4 (17):
        xpos 500
        ypos 100
        zoom 0.6 
    c45 "You killed our boss!"
    hide girl4 (17)
    show girl4 (18):
        xpos 500
        ypos 100
        zoom 0.6 
    $ show_quick_menu = False
    window hide
    menu:
        "''Look HOE, I ain't kill your boss, my friend did!''":
            $ show_quick_menu = True
            window show
            kristik "Look HOE, I ain't kill your boss, my friend did!"
            hide girl4 (18)
            show girl4 (21):
                xpos 500
                ypos 100
                zoom 0.6
            c45 "What did you just call me?!!"
            hide girl4 (21)
            show girl4 (20):
                xpos 500
                ypos 100
                zoom 0.6
            c45 "I AM NOT THAT!!!"
            kristik "Cap."
            jump partTwoTwoTwoTwo
        "''I didn't kill your boss bro.''":
            $ show_quick_menu = True
            window show
            $ EXPc45 += 1
            kristik "I didn't kill your boss bro."
            kristik "It was my friend."
            hide girl4 (18)
            show girl4 (17):
                xpos 500
                ypos 100
                zoom 0.6 
            c45 "Then I'll 1v1 your friend!!"
            kristik "It's Aaron though, didn't he steal your oil barrels or something?"
            hide girl4 (17)
            show girl4 (18):
                xpos 500
                ypos 100
                zoom 0.6   
            hide girl4 (18)
            show girl4 (21):
                xpos 500
                ypos 100
                zoom 0.6
            c45 "HIM?!!!!"
            c45 "HELL NO I'M OUTTA HERE!"
            hide girl4 (21)
            with dissolve
            kristik "Weirdo..."

    label partTwoTwoTwoTwo:
        if EXPc45 >= 1:
            aaron "The hell is up with her?"
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.4
            with dissolve
            kristik "Oh... hey."
            aaron "My daughter bugged me again today...."
        else:
            aaron "No need to be so mean."
            hide girl4 (20)
            with dissolve
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.4
            kristik "Oh... hey."
            aaron "..."
        hide aaron_11
        show aaron_11_1:
            xpos 450
            ypos 30
            zoom 0.4
        aaron "We need to talk about yesterday."
        aaron "I'll make it quick."
        aaron "Before I was so rudely interrupted..."
        aaron "We heard from an unknown source that you had the uncanny ability to get bitches..."
        kristikmind "{i}Wtf??? Who said that???"
        hide aaron_11_1
        show aaron_11:
            xpos 450
            ypos 30
            zoom 0.4        
        aaron "Of course, knowing you for a very long time, I would never have guessed that you had that ability."
        aaron "We performed an experiment where if you really had girls with emotional attachment, more would start to flock to you after we said that we would ''kill'' you."
        aaron "From what we've observed, it seems to be the case."
        hide aaron_11
        show aaron_11_1:
            xpos 450
            ypos 30
            zoom 0.4       
        aaron "However, we need to do more experiments."
        aaron "I need you to make your own harem with those guard girls."
        kristik "What?!!!! Why would I do that?!!"
        aaron "To fulfill my experiment of course."
        kristik "Why the hell would I care about your experiment?!!! What are you trying to fulfill?!!"
        aaron "We need to get some bitches on your dick."
        aaron "You've had a terrible track record in the past, so we need to fix this problem."
        kristik "What???? But...{p=0.05}{nw}"
        aaron "It doesn't matter. I will get going."
        kristik "WAIT! BUT YOU DIDNT EVEN TELL ME{p=0.05}{nw}"
        hide aaron_11_1
        with dissolve
        kristik "aaanndd.... he's gone."
        kristik "He's telling me to get some bitches...?"
        kristik "This is some uber mega hard shit...."
        kristik "But I suppose I shall try to get all 4 of them!"
        kristik "NTR STYLE!!!"
        stop music fadeout 2.0
        hide BG021
        with dissolve
        window hide
        $ show_quick_menu = False
        with dissolve
        $ renpy.pause(1,hard=True)                           
        jump chiesterEnding       
    return

label beatricepart:
    $ renpy.pause(2,hard=True)
    $ show_quick_menu = True
    window show
    with dissolve 
    show kor1
    with dissolve  
    play music "audio/Riddle Joker Original Soundtrack OST Perfect Girl Instrumental-(128kbps) intro.ogg"
    queue music "audio/Riddle Joker Original Soundtrack OST Perfect Girl Instrumental-(128kbps).ogg"
    $ renpy.pause(0.5,hard=True)
    kristik "Where the fuck are we...?"
    show sho21a_004:
        xpos 250
        ypos 30
    with dissolve
    beatrice "We're in 1940 Korea obviously."
    hide sho21a_004
    show sho21a_005:
        xpos 250
        ypos 30
    kristik "WHAT?!? HOW THE FUCK DID WE...?"
    hide sho21a_005
    show sho21a_101:
        xpos 250
        ypos 30
    beatrice "C'mon, you've never heard of breaking the space time continuum to go back to the past?"
    hide sho21a_101
    show sho21a_102:
        xpos 250
        ypos 30
    kristik "Ummm.. no."
    hide sho21a_102
    show sho21a_503:
        xpos 250
        ypos 30
    beatrice "Well someone is clearly a party pooper..."
    hide sho21a_503
    show sho21a_504:
        xpos 250
        ypos 30
    kristik "What the hell are we doing here?"
    hide sho21a_504
    show sho21a_501:
        xpos 250
        ypos 30
    beatrice "We've come here to destroy the communist party and the Soviet Red Army in the north obviously."
    hide sho21a_501
    show sho21a_502:
        xpos 250
        ypos 30
    kristik "WHAT??? WHY ARE WE DOING THAT??? ISN'T JUST THEIR PROBLEM?!!"
    hide sho21a_502
    show sho21a_201:
        xpos 250
        ypos 30
    beatrice "Are you saying that this communist party and the liberation of the north is useless and doesn't matter for the fate of Korea in the future?!"
    beatrice "It's the whole reason why North Korea is even a thing!"
    hide sho21a_201
    show sho21a_202:
        xpos 250
        ypos 30
    kristik "Well, no. It's just that how the hell are we going to FIGHT A WHOLE ASS ARMY OFF AND CRUSH AN ENTIRE POLITICAL PARTY?!!!"
    hide sho21a_202
    show sho21a_801:
        xpos 250
        ypos 30
    beatrice "Heh... I've got quite a lot of connections here. It's fine, we can do this."
    hide sho21a_801
    show sho21a_004:
        xpos 250
        ypos 30
    beatrice "But first, I need to meet somebody."
    beatrice "Follow me."
    hide sho21a_004
    with dissolve
    kristik "What the fuck am I getting myself into..."
    stop music fadeout 2.0
    hide kor1
    with dissolve
    $ show_quick_menu = False
    window hide 
    with dissolve 
    $ renpy.pause(2,hard=True)
    $ show_quick_menu = True
    window show
    with dissolve 
    show kor9
    with dissolve  
    $ renpy.pause(0.5,hard=True)
    play music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps) intro.ogg"
    queue music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps).ogg"
    show sho21a_004:
        xpos 250
        ypos 30
    with dissolve
    beatrice "They should be in here."    
    transform moverightslight:
        xpos 250
        ypos 30
        ease 0.5 xpos 500
    hide sho21a_004
    show sho21a_005 at moverightslight
    $ renpy.pause(0.05,hard=True)     
    hide sho21a_005
    with dissolve
    kristik "Aight... let's see these ''''connections''''"
    hide kor9
    show suburb_shanghaiint
    with dissolve
    show jasonc (1):
        xpos 700
        ypos 20
        zoom 0.6
    show sho21a_001:
        xpos 0
        ypos 30
    with dissolve  
    beatrice "Hello!"
    hide jasonc (1)
    show jasonc (9):
        xpos 700
        ypos 20
        zoom 0.6
    hide sho21a_001
    show sho21a_202:
        xpos 0
        ypos 30        
    kristik "PFFFFFFFFF"  
    kristik "WHAT THE HELL... JASON WHAT ARE YOU DOING HERE?!!!"
    hide sho21a_002
    show sho21a_201:
        xpos 0
        ypos 30  
    beatrice "Who the hell is Jason?"
    hide sho21a_201
    show sho21a_202:
        xpos 0
        ypos 30 
    hide jasonc (9)
    show jasonc (3):
        xpos 700
        ypos 20
        zoom 0.6
    jason "{font=malgunbd.ttf} 그.... 무슨 소리야??"
    hide jasonc (3)
    show jasonc (1):
        xpos 700
        ypos 20
        zoom 0.6       
    kristik "WHA....."
    kristik "Uhh.... jamganmanyo (hold up)!"
    hide jasonc (1)
    hide sho21a_202
    with dissolve
    show sho21a_202:
        xpos 250
        ypos 30 
    with dissolve
    kristik "Why is my friend here?!!"
    hide sho21a_202
    show sho21a_201:
        xpos 250
        ypos 30  
    beatrice "You guys were friends? Since when?"
    hide sho21a_201
    show sho21a_202:
        xpos 250
        ypos 30            
    kristik "Did everyone I know also get transported back to the past?"
    hide sho21a_202
    show sho21a_004:
        xpos 250
        ypos 30
    beatrice "Well it's not unheard of I guess..."
    beatrice "I didn't know you were friends with him in the previous world though..."
    hide sho21a_004
    show sho21a_005:
        xpos 250
        ypos 30
    kristik "Well yeah, now you know."
    hide sho21a_005
    show jasonc (9):
        xpos 700
        ypos 20
        zoom 0.6
    show sho21a_005:
        xpos 0
        ypos 30
    with dissolve
    kristik "Umm... mi-an haeyo.... (sorry)"
    kristik "Naneun... cheowahaeyo. (i'm good)"
    kristik "Uhh.... wakairimashita? (do you understand? (this is japanese though))"
    hide jasonc (9)
    show jasonc (3):
        xpos 700
        ypos 20
        zoom 0.6
    jason "{font=malgunbd.ttf}친구 진짜 이상해..."
    hide jasonc (3)
    show jasonc (9):
        xpos 700
        ypos 20
        zoom 0.6 
    kristik "Help me!!! I don't understand Korean!!"
    hide sho21a_005
    show sho21a_504:
        xpos 0
        ypos 30
    beatrice "Hahh...."
    hide sho21a_504
    show sho21a_503:
        xpos 0
        ypos 30
    beatrice "Just take this perc99 and you'll be 100%% fluent in the language instantly..."
    hide sho21a_503
    show sho21a_504:
        xpos 0
        ypos 30    
    kristik "HELL YEA LEMME POP THAT PILL RQ!!!"
    kristik "..."
    kristik "Witam, mogę teraz mówić w Twoim języku! CZEKAJ, TO NIE JEST WŁAŚCIWY JĘZYK, POMÓŻ MI AHHHHH!!!"
    hide sho21a_504
    show sho21a_401:
        xpos 0
        ypos 30
    beatrice "Woops, I gave you the wrong language pill!"
    hide sho21a_401
    show sho21a_202:
        xpos 0
        ypos 30
    beatrice "Take this one instead."
    kristik "TAK TAK TAK DAJ MI PRAWIDŁOWĄ PIGUŁKĘ!"
    kristik "..."
    kristik "{font=malgunbd.ttf}좋아... 지금 내가 올바른 언어로 말하고 있어!"
    hide jasonc (9)
    show jasonc (3):
        xpos 700
        ypos 20
        zoom 0.6
    jason "{font=malgunbd.ttf}뭐야..."    
    hide sho21a_202
    show sho21a_003:
        xpos 0
        ypos 30
    beatrice "I'll also enable the write everything in English plugin!"
    kristik "Woah... that totally works.."
    hide jasonc (3)
    show jasonc (81):
        xpos 700
        ypos 20
        zoom 0.6
    jason "So, what is this about Beatrice?"
    jason "You said you had a new plan?"
    hide sho21a_003
    show sho21a_504:
        xpos 0
        ypos 30
    beatrice "Yeah... to get to the point...."
    hide sho21a_504
    show sho21a_503:
        xpos 0
        ypos 30
    beatrice "That actor... he's been caught being a member in the communist party."
    hide sho21a_503
    show sho21a_004:
        xpos 0
        ypos 30
    beatrice "I thought of getting ourself a mob or gang first before we actually try to kill him."
    hide sho21a_004
    show sho21a_503:
        xpos 0
        ypos 30  
    beatrice "After all, he is a high profile target. We can destroy the entire party if we eliminate him first."
    hide sho21a_503
    show sho21a_005:
        xpos 0
        ypos 30
    kristik "Wait... a GANG???"
    kristik "WE GANG BANGING LIKE THIS SHIT IS 1980s COMPTON CRIPS vs BLOODS????"
    hide sho21a_005
    show sho21a_503:
        xpos 0
        ypos 30     
    beatrice "Well, I suppose you can compare it to that I guess."
    hide sho21a_503
    show sho21a_005:
        xpos 0
        ypos 30
    hide jasonc (81)
    show jasonc (10):
        xpos 700
        ypos 20
        zoom 0.6
    jason "I can round up a few people, but you guys need to find some more people as well."
    hide jasonc (10)
    show jasonc (9):
        xpos 700
        ypos 20
        zoom 0.6
    hide sho21a_005
    show sho21a_001:
        xpos 0
        ypos 30
    beatrice "That's fine. Me and Kristik here will search for new recruits for the gang as well."
    hide sho21a_001
    show sho21a_005:
        xpos 0
        ypos 30
    kristik "Woah woah woah woah woah.... hold up... we're actually gonna make a mob?"
    hide sho21a_005
    show sho21a_101:
        xpos 0
        ypos 30    
    beatrice "Why not? It'll be fun!"
    hide sho21a_101
    show sho21a_102:
        xpos 0
        ypos 30
    kristik "Damn.... my indian heart can't take this anymore...."
    stop music fadeout 2.0
    hide sho21a_102
    hide jasonc (9)
    with dissolve
    hide suburb_shanghaiint
    with dissolve
    $ show_quick_menu = False
    window hide 
    with dissolve 
    $ renpy.pause(2,hard=True)
    $ show_quick_menu = True
    window show
    with dissolve     
    show kor3
    with dissolve
    play music "audio/Sanoba Witch OST - Midday Star(InstVer.)-(128kbps).ogg"
    show sho21a_005:
        xpos 250
        ypos 30
    with dissolve
    $ renpy.pause(0.5,hard=True)
    kristik "So uh... how the hell are we going to round up some people for this ''mob''?"
    hide sho21a_005
    show sho21a_503:
        xpos 250
        ypos 30
    beatrice "The first step in finding a worthy person, is to fight!"
    hide sho21a_503
    show sho21a_504:
        xpos 250
        ypos 30
    kristik "WHAT???? WHY WOULD WE FIGHT THEM???"
    hide sho21a_504
    show sho21a_201:
        xpos 250
        ypos 30
    beatrice "There's no reason to fight THEM! We just need to walk around the city, waiting for a fight to occur."
    hide sho12a_201
    show sho21a_503:
        xpos 250
        ypos 30
    beatrice "It's the 1940s, so fights are super common!"
    hide sho21a_503
    show sho21a_005:
        xpos 250
        ypos 30
    stop music fadeout 2.0
    citizen "Hey! Look! A fight is going to break out!"
    hide sho21a_005
    show sho21a_101:
        xpos 250
        ypos 30
    beatrice "What a funny coincidence!"
    hide sho21a_101
    show sho21a_003:
        xpos 250
        ypos 30
    beatrice "Let's go check it out!"
    hide sho21a_003
    hide sho21a_201
    hide kor3
    with dissolve
    show kor2
    with dissolve
    play music "audio/Riddle Joker OST _ Invisibly Faster-(128kbps) intro.ogg"
    queue music "audio/Riddle Joker OST _ Invisibly Faster-(128kbps).ogg"

    show kevin (2):
        xpos 400
        zoom 0.6
    with dissolve
    kevin "Heh...."
    hide kevin (2)
    show kevin (3):
        xpos 400
        zoom 0.6
    kevin "You think it's so funny to step into other people's territory without showing respect?"
    kristikmind "{i}KEVIN?!!!!"
    hide kevin (3)
    show billc (33):
        xpos 400
        zoom 0.6
    with dissolve
    bill "With all due respect, which right now is about none, why would I need to conform to such social norms?"
    kristikmind "{i}BILL!?!?@?!@?!>@?>!?@>!?@>!?@>!@"
    hide billc (33)
    show billc (37):
        xpos 400
        zoom 0.6
    bill "You're just a subordinate for your ''armchair'' gang."
    hide billc (37)
    show kevin (2):
        xpos 400
        zoom 0.6
    kevin "Really? That's all you got?"
    hide kevin (2)
    show kevin (3):
        xpos 400
        zoom 0.6
    kevin "I'll make you regret ever stepping in our territory."
    show sho21a_101 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7
    beatrice "They're going to fight!!"
    hide sho21a_101 onlayer mcsprite
    hide kevin (3)
    show kevin (4):
        xpos 400
        zoom 0.6
    kristik "WAIT!!!!1"
    kristik "Don't fight! It's uhhh... it's GAY!!!"
    show sho21a_201 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7  
    beatrice "What the hell are you doing right now?"
    beatrice "They were just going to fight!"
    hide sho21a_201 onlayer mcsprite
    kristik "I can't let them fight! They were my friends!"
    hide kevin (4)
    show kevin (7):
        xpos 400
        zoom 0.6
    kevin "Friends...? But, i've never seen you before..."
    hide kevin (7)
    show billc (45):
        xpos 400
        zoom 0.6
    bill "I've never seen you before either. You're too weak to be my friend."
    hide billc (45)
    show billc (44):
        xpos 400
        zoom 0.6
    bill "Something about this kid just pisses me off..."
    hide billc (44)
    show kevin (10):
        xpos 400
        zoom 0.6
    kevin "Same here... he just looks so fat."
    hide kevin (10)
    show kevin (8):
        xpos 400
        zoom 0.6
    kevin "Hey, what district are you from?"
    kristik "District....?"
    kristik "Uhhh... San Jose?"
    hide kevin (8)
    show kevin (7):
        xpos 400
        zoom 0.6
    kevin "What? There's no such district name."
    show sho21a_201 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7  
    beatrice "Remember! We're in Korea right now!"  
    hide sho21a_201 onlayer mcsprite
    kristik "Oh shit! I forgot about that!"
    hide kevin (7)
    show billc (4):
        xpos 400
        zoom 0.6
    bill "Hey bitch. You think it's funny to say shit like that?"
    bill "Something makes me want to punch your face in."
    bill "Are you some foreigner brought in by Hayashi?"
    hide billc (4)
    show billc (2):
        xpos 400
        zoom 0.6
    kristik "Hayashi...?"
    show sho21a_503 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7  
    beatrice "Hayashi is the name of the Korean defector who joined the Yakuza."      
    hide sho21a_503 onlayer mcsprite
    kristik "Oh... No I don't know Hayashi..."
    hide billc (2)
    show billc (6):
        xpos 400
        zoom 0.6
    bill "Then why are you stepping in territory you don't know? You're certainly a Japanese or communist waiting to just kill us all!"
    hide billc (6)
    show billc (2):
        xpos 400
        zoom 0.6    
    kristik "WHAT??? NO!!"
    hide billc (2)
    show billc (6):
        xpos 400
        zoom 0.6
    bill "Get ready to get your jaw spun!"
    show sho21a_504 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7  
    beatrice "Geez, I didn't expect him to be the one getting the beating..."  
    hide sho21a_504 onlayer mcsprite     
    kristik "YOU'RE NOT HELPING!!!"   
    stop music fadeout 2.0
    jason "Bill, stand down."
    hide billc (6)
    show jasonc (146):
        xpos 400
        ypos 30
        zoom 0.6
    with dissolve
    jason "This is one of Beatrice's subordinates."
    show billc (7) onlayer mcsprite:
        xpos -70
        ypos 500
        zoom 0.5  
    bill "What?? But...!"    
    hide billc (7) onlayer mcsprite 
    show jasonc (141):
        xpos 400
        ypos 30
        zoom 0.6  
    #play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
    play music "audio/Sanoba Witch OST - What-(128kbps).ogg"
    jason "Are you trying to make a fool of me? I said back off or you'll be the one lying dead on the street."
    show billc (2) onlayer mcsprite:
        xpos -70
        ypos 500
        zoom 0.5  
    bill "Yes sir...."
    hide billc (2) onlayer mcsprite  
    hide jasonc (141)
    show jasonc (153):
        xpos 400
        ypos 30
        zoom 0.6
    jason "And if it concerns you so much, what seems the issue here, Kim Kae Bin?"
    hide jasonc (153)
    show kevin (9):
        xpos 400
        zoom 0.6
    kevin "Tch...."
    transform moverightslight2:
        xpos 400
        zoom 0.6
        ease 0.5 xpos 900    
    hide kevin (9) 
    play sound "audio/fast run sound effect-(128kbps).ogg"
    #================================================================================================================================================
    #               PLAY RUNNING SOUNDS
    #================================================================================================================================================
    
    show kevin (9) at moverightslight2
    $ renpy.pause(0.005,hard=True)  
    hide kevin (9)
    with dissolve      
    show jasonc (141):
        xpos 400
        ypos 30
        zoom 0.6
    with dissolve
    jason "Huh... the bastard ran off."
    show sho21a_503 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7
    beatrice "Awwww... I wanted to see a fight!"
    hide sho21a_503 onlayer mcsprite 
    jason "Bill!"
    hide jasonc (141)
    show jasonc (55):
        xpos 100
        ypos 30
        zoom 0.6
    show billc (2):
        xpos 700
        zoom 0.6
    with dissolve
    bill "Yes!"
    jason "Apologize to your new subordinate, Kristik Lal."
    hide billc (2)
    show billc (13):
        xpos 700
        zoom 0.6
    bill "I'm sorry. Tch..."
    hide jasonc (55)
    show jasonc (6):
        xpos 100
        ypos 30
        zoom 0.6   
    jason "Do it correctly! And get rid of your hand from your face!"
    hide jasonc (6)
    show jasonc (11):
        xpos 100
        ypos 30
        zoom 0.6
    hide billc (13)
    show billc (42):
        xpos 700
        zoom 0.6
    bill "I'm...."
    hide billc
    show billc (41):
        xpos 700
        zoom 0.6
    bill "I'M SORRY!!!! WAHAHAHAH!!!!"
    stop music fadeout 2.0
    hide billc (41)
    hide jasonc (11)
    with dissolve
    hide kor2 
    with dissolve
    $ show_quick_menu = False
    window hide 
    with dissolve 
    $ renpy.pause(1,hard=True)
    $ show_quick_menu = True
    window show
    with dissolve 
    show kor11
    with dissolve
    play music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k intro.ogg"
    queue music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k.ogg"
    hide jasonc (6)
    show jasonc (10) onlayer master1:
        xpos 0
        ypos 30
        zoom 0.6
    hide billc (9)
    show billc (2) onlayer master2:
        xpos 400
        zoom 0.6    
    show sho21a_005 onlayer master3:
        xpos 700
        ypos 30 
    with dissolve
    jason "Beatrice, did you find anybody yet?"
    hide jasonc (10) onlayer master1
    show jasonc (9) onlayer master1:
        xpos 0
        ypos 30
        zoom 0.6
    hide sho21a_005 onlayer master3
    show sho21a_503 onlayer master3:
        xpos 700
        ypos 30
    beatrice "No, unfortunately. We were actually looking for fights but it seemed like it was just you guys."
    hide sho21a_503 onlayer master3
    show sho21a_501 onlayer master3:
        xpos 700
        ypos 30
    beatrice "You seemed to have found a new person though."
    hide sho21a_501 onlayer master3
    show sho21a_402 onlayer master3:
        xpos 700
        ypos 30
    hide billc (2) onlayer master2
    show billc (3) onlayer master2:
        xpos 400
        zoom 0.6
    bill "Yes, my name is Kang Bi-il."
    hide billc (3) onlayer master2
    show billc (2) onlayer master2:
        xpos 400
        zoom 0.6    
    kristikmind "{i}Sounds hella simillar to Bill...."
    hide billc (2) onlayer master2
    show billc (4) onlayer master2:
        xpos 400
        zoom 0.6
    bill "The bastard we encountered was Kim Kae Bin."
    hide billc (4) onlayer master2
    show billc (2) onlayer master2:
        xpos 400
        zoom 0.6  
    kristikmind "{i}Sounds hella simillar to Kevin AGAIN...."
    hide billc (2) onlayer master2
    show billc (4) onlayer master2:
        xpos 400
        zoom 0.6    
    bill "I heard you guys are after the actor, Shim Young was it?"
    hide billc (4) onlayer master2
    show billc (2) onlayer master2:
        xpos 400
        zoom 0.6
    hide sho21a_402 onlayer master3
    show sho21a_503 onlayer master3:
        xpos 700
        ypos 30    
    beatrice "Yes, we heard one of his special concerts will be held in 3 days."
    hide sho21a_403 onlayer master3
    show sho21a_004 onlayer master3:
        xpos 700
        ypos 30        
    beatrice "We need to get some more people, at least one more person at least...."
    hide sho21a_004 onlayer master3
    show sho21a_005 onlayer master3:
        xpos 700
        ypos 30      
    kristik "What about that Kevin guy?" 
    hide billc (2) onlayer master2
    show billc (38) onlayer master2:
        xpos 400
        zoom 0.6  
    bill "Hell no!"
    hide billc (38) onlayer master2
    show billc (45) onlayer master2:
        xpos 400
        zoom 0.6     
    bill "I'd rather die before ever letting him join us!"
    hide billc (45) onlayer master2
    show billc (44) onlayer master2:
        xpos 400
        zoom 0.6 
    hide sho21a_005 onlayer master3
    show sho21a_201 onlayer master3:
        xpos 700
        ypos 30   
    beatrice "What did he even do to you??"
    hide sho21a_201 onlayer master3
    show sho21a_005 onlayer master3:
        xpos 700
        ypos 30       
    hide billc (44) onlayer master2
    show billc (38) onlayer master2:
        xpos 400
        zoom 0.6 
    bill "The bastard stole my fucking limited ROBLOX ITEM!!!!"
    hide billc (38) onlayer master2
    show billc (42) onlayer master2:
        xpos 400
        zoom 0.6 
    kristik "..."   
    hide sho21a_005 onlayer master3
    show sho21a_503 onlayer master3:
        xpos 700
        ypos 30       
    beatrice "I knew it was something stupid..."
    hide sho21a_503 onlayer master3
    show sho21a_402 onlayer master3:
        xpos 700
        ypos 30  
    hide billc (38) onlayer master2
    show billc (6) onlayer master2:
        xpos 400
        zoom 0.6   
    bill "WHAT ARE YOU CALLING STUPID?!!!"
    hide billc (6) onlayer master2
    show billc (1) onlayer master2:
        xpos 400
        zoom 0.6  
    bill "It was worth at least 5,000 ETH on the ROBLOX black market...."      
    hide jasonc (9) onlayer master1
    show jasonc (140) onlayer master1:
        xpos 0
        ypos 30
        zoom 0.6    
    jason "That is the saddest ROBLOX story I have heard bro..."
    hide sho21a_402 onlayer master3
    show sho21a_503 onlayer master3:
        xpos 700
        ypos 30  
    beatrice "So dumb..."
    stop music fadeout 2.0
    hide sho21a_503 onlayer master3
    hide jasonc (140) onlayer master1
    hide billc (1) onlayer master2 
    with dissolve
    hide kor11
    with dissolve
    $ show_quick_menu = False
    window hide 
    with dissolve 
    $ renpy.pause(1,hard=True)
    $ show_quick_menu = True
    window show
    with dissolve 
    show kor6
    with dissolve
    show sho21a_501:
        xpos 300
        ypos 30
    with dissolve
    play music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k intro.ogg"
    queue music "audio/Sanoba Witch OST - Hare-Hare Kibun-320k.ogg"
    beatrice "Any ideas?"
    hide sho21a_501
    show sho21a_502:
        xpos 300
        ypos 30
    kristik "For what...?"
    hide sho21a_502
    show sho21a_503:
        xpos 300
        ypos 30    
    beatrice "To get Kae Bin in our gang obviously!"
    beatrice "Jae Sun and Bi-Il won't do it, so we need to do it ourselves."
    hide sho21a_503
    show sho21a_504:
        xpos 300
        ypos 30  
    kristik "Hmmm..."
    hide sho21a_504
    show sho21a_005:
        xpos 300
        ypos 30               
    kristik "How about we lure Kae Bin out with a ROBLOX limited item????"
    hide sho21a_005
    show sho21a_503:
        xpos 300
        ypos 30   
    beatrice "I doubt that would work... that sounds really stupid."  
    hide sho21a_503
    show sho21a_504:
        xpos 300
        ypos 30    
    kristik "Yeah...." 
    kristik "...."
    hide sho21a_504
    show sho21a_005:
        xpos 300
        ypos 30         
    kristik "How about you lure him out with your womanly charms?" 
    hide sho21a_005
    show sho21a_401:
        xpos 300
        ypos 30     
    beatrice "Wha-...?"
    hide sho21a_401
    show sho21a_201a:
        xpos 300
        ypos 30         
    beatrice "What are you trying to say???!!"
    hide sho21a_201a
    show sho21a_503a:
        xpos 300
        ypos 30  
    beatrice "I wouldn't just do that to any person!!"
    hide sho21a_503a
    show sho21a_504:
        xpos 300
        ypos 30     
    $ show_quick_menu = False
    window hide
    menu:
        "Who would you do that to then?":
            $ show_quick_menu = True
            window show
            kristik "Who would you do that to then?"
            hide sho21a_504
            show sho21a_201a:
                xpos 300
                ypos 30  
            beatrice "I don't know!!! Stop asking me these pointless questions!"      
            hide sho21a_201a
            show sho21a_402:
                xpos 300
                ypos 30               
            kevin "Hey!"     
        "You would do it to me, huh babe?":
            $ show_quick_menu = True
            window show
            $ EXPbeatrice += 1 
            kristik "You would do it to me, huh babe?"
            hide sho21a_504
            show sho21a_401:
                xpos 300
                ypos 30 
            beatrice "...."
            hide sho21a_401
            show sho21a_503a:
                xpos 300
                ypos 30  
            beatrice "...who are you calling that?"
            hide sho21a_503a
            show sho21a_402:
                xpos 300
                ypos 30   
            kevin "Hey!"                             
    hide sho21a_402
    with dissolve
    show kevin (6):
        xpos 400
        zoom 0.6
    with dissolve
    kevin "You're the fat guy and with the hot chick!"
    show sho21a_401 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7
    beatrice "Hot??!!"
    hide sho21a_401 onlayer mcsprite 
    hide kevin (6)
    show kevin (3):
        xpos 400
        zoom 0.6
    kevin "I'll destroy you then fuck her right in front of you NTR style!!! MUAHAHAHA!!"
    show sho21a_503 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7
    beatrice "Ok... now that's pretty weird..."
    hide sho21a_503 onlayer mcsprite     
    hide kevin (3)
    show kevin (4):
        xpos 400
        zoom 0.6 
    kristik "Not on my watch! I, Kristik Lal, have the ANTI-NTR INATOR!!!!"
    hide kevin (4)
    show kevin (9):
        xpos 400
        zoom 0.6       
    kevin "Tch... my only weakness..."
    show sho21a_201 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7
    beatrice "What is going on ???!!!"
    hide sho21a_201 onlayer mcsprite     
    hide kevin (9)
    show kevin (3):
        xpos 400
        zoom 0.6       
    kevin "You also seem to forget, that I brought your only weakness."
    kristikmind "{i} OH NO.... IS IT....!!!"
    hide kevin (3)
    show kevin (3):
        xpos 100
        zoom 0.6  
    show beef:
        xpos 700
        zoom 1.2
    kevin "BEHOLD!! FRESH BEEF FROM THE GROCERY STORE!!!"
    kristik "N-NANI?!!!!"
    kristikmind "{i} IM HINDI!!! I CANT GO ANYWHERE NEAR BEEF MEAT!!"
    kristik "SHIT... IM STARTING TO FEEL DIZZY..."
    show sho21a_401 onlayer mcsprite:
        xpos -150
        ypos 500
        zoom 0.7
    beatrice "Are you okay??!!"
    hide sho21a_401 onlayer mcsprite      
    hide kevin (3)
    show kevin (2):
        xpos 100
        zoom 0.6 
    kevin "As expected of any hindu...."
    kristik "FUCK.... IM.... STARTING TO...."   
    kristik "SAVE ME BEATRICE!!!"
    if EXPbeatrice >= 2:
        show sho21a_504 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "Hmmm...."
        stop music
        hide sho21a_504 onlayer mcsprite        
        play sound "audio/awp.mp3" 
        hide beef
        hide kevin (2)
        show kevin (7):
            xpos 100
            zoom 0.6
        show white
        $ renpy.pause(0.1,hard=True)
        hide white 
        with Dissolve(2)   
        kristik "WTF???"
        show sho21a_503 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "I shot the beef out of existence using the OC3 optical line tactical nuke ICBM wormhole gun."
        hide sho21a_503 onlayer mcsprite 
        hide kevin (7)
        show kevin (8):
            xpos 400
            zoom 0.6
        kevin "Uh....." 
        kristik "Kae Bin."
        hide kevin (8)
        show kevin (11):
            xpos 400
            zoom 0.6  
        play music "audio/Sanoba Witch OST - Setsunakute-(128kbps).ogg" 
        kevin "WAHHHH!!!!"
        kristik "TF??? WHY YOU CRYIN???"
        hide kevin (11)
        show kevin (12):
            xpos 400
            zoom 0.6  
        kevin "I SWEAR ALL I WANTED WAS ROBUX!!!"
        kevin "I DON'T MEAN ANY HARM!!! PLEASE DON'T KILL ME!!!! PWEASE!!!!"     
        hide kevin (12)
        show kevin (11):
            xpos 400
            zoom 0.6  
        kristik "Hmm... tell you what."
        kristik "I won't use the cock and ball torture-inator on you IF you join our gang to defeat the communist actor Shim Young."
        show sho21a_401 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "The what???!"
        hide sho21a_401 onlayer mcsprite 
        hide kevin (11)
        show kevin (3):
            xpos 400
            zoom 0.6 
        stop music
        play music "audio/Sanoba Witch OST - Midday Star(InstVer.)-(128kbps).ogg"
        kevin "DEAL!!!!"
        kristikmind "{i}WTF HE ACCEPTED THAT FAST???!"
        show sho21a_503 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "I won't even question it anymore..."
        hide sho21a_503 onlayer mcsprite         
        $ renpy.pause(0.0001)
        hide kevin (3)
        hide kor6
        with dissolve
        jump beatriceparttwo
    else:
        show sho21a_201 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "What??!!!"
        hide sho21a_201 onlayer mcsprite  
        kevin "Goodbye Kribshit Lol."
        kristik "UGHGH....."
        stop music fadeout 2.0
        hide kevin (2)
        hide beef
        hide kor6
        with Dissolve(2)
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(1,hard=True)
        narrator "Kristik suffered a violent allergic reaction due to being in a 5 foot radius of cow produce."
        narrator "The resulting beef fumes entered his lungs and inflamed his inner trachea, causing him to suffocate."
        narrator "He slowly ran out of oxygen."
        narrator "{b}Bad ending 6/21{/b}"
        if (persistent.endingFinished6 < 1):
            $ persistent.endingFinished6 += 1
        elif (persistent.endingFinished6 >= 1):
            pass
        else:
            narrator "PERSISTENT DATA FAILURE FOR SECTION 14628. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
            $ renpy.quit()
        window hide
        with dissolve                
        $ renpy.pause(3,hard=True)
        $ MainMenu(confirm=False)()
    label beatriceparttwo:
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(1,hard=True)
        $ show_quick_menu = True
        window show
        with dissolve 
        show kor7
        with dissolve    
        show jasonc (10):
            xpos 100
            ypos 30
            zoom 0.6
        show billc (33):
            xpos 700
            zoom 0.6    
        with dissolve
        jason "Is that... Kae Bin?"        
        hide billc (33)
        show billc (6):
            xpos 700
            zoom 0.6
        kevin "WHAT IS MY ARCH NEMESIS DOING HERE?!!!"
        hide billc (6)
        hide jasonc (10)
        with dissolve
        show billc (2):
            xpos 100
            zoom 0.6 
        show kevin (6):
            xpos 700
            zoom 0.6  
        with dissolve
        kevin "I'm on your side now."
        hide kevin (6)
        hide billc (2)
        show billc (4):
            xpos 100
            zoom 0.6 
        show kevin (7):
            xpos 700
            zoom 0.6    
        bill "What??!! For all we know you could just be a commie spy!" 
        hide kevin (7)
        hide billc (4)
        show billc (2):
            xpos 100
            zoom 0.6 
        show kevin (10):
            xpos 700
            zoom 0.6    
        kevin "Look Bi-Il... I know it's hard to trust someone... who stole a limited Dominus from you."     
        kevin "But..."
        hide kevin (10)
        show kevin (12):
            xpos 700
            zoom 0.6
        stop music 
        play music "audio/Sanoba Witch OST - Sweet Treasure(QuietVer.)-(128kbps).ogg"
        kevin "I love you!"
        hide billc (2)
        show billc (7):
            xpos 100
            zoom 0.6
        kristikmind "WHAT?!?!!!"
        show sho21a_401 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "Huhh?!!!!"
        beatrice "Is this... BL?!?!!!"
        hide sho21a_401 onlayer mcsprite
        show sho21a_802 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "Hehehehe....."
        hide sho21a_802 onlayer mcsprite        
        kristikmind "{i} ew..."
        hide billc (7)
        show billc (19):
            xpos 100
            zoom 0.6
        bill "Ugh....!"
        hide billc (19)
        show billc (25):
            xpos 100
            zoom 0.6
        bill "...."
        kristikmind "{i} WHY TF IS HE CRYING??!?!?!"
        hide billc (25)
        show billc (39):
            xpos 100
            zoom 0.6
        bill "I too..."
        hide billc (39)
        show billc (41):
            xpos 100
            zoom 0.6
        bill "I LOVE YOU TOO!!!!!"
        kristikmind "{i} wtf is this gay shit.... "
        hide billc (41)
        show billc (1):
            xpos 100
            zoom 0.6   
        bill "I just... was so heartbroken after you stole my Dominus!!!"
        hide kevin (12)
        show kevin (11):
            xpos 700
            zoom 0.6  
        kevin "Yes... I'm so sorry!!!"
        hide kevin (11)
        show kevin (12):
            xpos 700
            zoom 0.6   
        kevin "I'm sure it won't happen again... babe!!!"
        kristikmind "{i} Yuck... I think I'm abouta throw up or some shit..." 
        hide kevin (12)
        hide billc (1)
        with dissolve
        show sho21a_802:
            xpos 600
            ypos 30  
            zoom 0.9       
        show jasonc (147):  
            xpos 150
            ypos 30
            zoom 0.6
        with dissolve
        jason "Those two never change..."
        beatrice "Mhmm~!"
        hide jasonc (147)
        hide sho21a_802
        show sho21a_202:
            xpos 600
            ypos 30      
            zoom 0.9   
        show jasonc (149):  
            xpos 150
            ypos 30
            zoom 0.6   
        kristik "WHY ARE YALL SMILING??!!!! THIS SHIT IS SUPER GAY!!!"    
        hide sho21a_202
        show sho21a_201:
            xpos 600
            ypos 30
            zoom 0.9
        beatrice "So???!! Who cares! Just let them be!"
        hide sho21a_201
        show sho21a_202:
            xpos 600
            ypos 30
            zoom 0.9    
        hide jasonc (149)
        show jasonc (83):
            xpos 150
            ypos 30
            zoom 0.6
        jason "Kristik, let's be mature here and accept the gay. You don't need to act like a child."
        kristik "WE STILL NEED TO KILL THAT ACTOR THO!!! THIS GAY SHIT GOT NOTHING WITH TO DO WITH IT!!!"
        hide jasonc (83)
        hide sho21a_202
        with dissolve
        show billd (5):
            xpos 100
            zoom 0.6      
        show kevin (3):
            xpos 700
            zoom 0.6 
        with dissolve
        kevin "Let's be happy together, forever!!!"  
        hide billd (5)
        show billd (4):
            xpos 100
            zoom 0.6
        bill "Yeah!!!"
        kristikmind "{i}God... this shit is so gay...."
        stop music fadeout 2.0
        hide billd (4)
        hide kevin (3)
        hide kor7
        with dissolve
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(1,hard=True)
        $ show_quick_menu = True
        window show
        with dissolve 
        show kor10
        with dissolve          
        show jasonc (10) onlayer master1:
            xpos 0
            ypos 30
            zoom 0.6
        show billc (2) onlayer master2:
            xpos 400
            zoom 0.6    
        show sho21a_005 onlayer master3:
            xpos 700
            ypos 30 
        with dissolve
        jason "Remember the plan guys! We're going to snipe him on stage!"
        hide jasonc (10) onlayer master1
        hide billc (2) onlayer master2
        hide sho21a_005 onlayer master3
        with dissolve
        hide kor10
        show simyoung2
        with dissolve
        simyo "To all my fellow and dear students, comrades and citizens."
        hide simyoung2
        show simyoung1
        simyo "We will deliver news of our patriotic citizens eagerly praising of our communist state!!"
        hide simyoung1
        show simyoung2
        simyo "Everyone, what does 'Sir' mean to you?"
        simyo "It's a title I always missed."
        simyo "It's our hearts. In our minds."
        hide simyoung2
        show simyoung3
        simyo "It's a name that we adore and weep for many years."
        simyo "This name, is to our social paradise everyone!!!!{p=3.7}{nw}"
        play sound "audio/awp.mp3" 
        hide simyoung3
        show white
        $ renpy.pause(0.1,hard=True)
        hide white 
        with Dissolve(2)       
        show sho21a_201 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        beatrice "You got him! Get outta there!"
        hide sho21a_201 onlayer mcsprite       
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(1,hard=True)
        $ show_quick_menu = True
        window show
        with dissolve 
        show simyoung5
        with dissolve 
        simyo "Ugh....."
        hide simyoung5
        show simyoung6
        with dissolve
        doctor "...."
        hide simyoung6
        show simyoung7
        with dissolve
        simyo "Where.... where am I?"
        hide simyoung7
        show simyoung8
        doctor "You're in a hospital, please calm down and rest."
        doctor "I applied hemostatic drugs and had you go through emergency surgery."
        doctor "You lost a lot of blood, it was quite a disaster."
        hide simyoung8
        show simyoung9
        simyo "How come I don't feel anything... down here?"
        hide simyoung9
        show simyoung10
        doctor "Uhh... so... the bullet hit a... very bad spot."
        hide simyoung10
        show simyoung9point1
        simyo "What does that mean...?"
        hide simyoung9point1
        show simyoung11
        doctor "I wasn't going to tell you this until you fully recovered but... please keep this in mind...."
        doctor "Uhhh... you won't be able to have children in the future."
        doctor "So basically, you can't have sex."
        doctor "The bullet passed right through your balls..."
        hide simyoung11
        show simyoung12
        simyo "What??!! Look, look! DOCTOR!!!"
        hide simyoung12
        show simyoung10
        doctor "Sir, please calm down. If you get excited again you will start to loose more blood, then you won't be able to walk."
        hide simyoung10
        show simyoung13
        simyo "Look, I can't stay like this for long."
        simyo "A phone! Please get me a phone to call on!"
        hide simyoung13
        show simyoung11
        doctor "Sir, this is the intensive care unit." 
        doctor "There is no phone."
        doctor "You came here because you weren't able to go to any other hospital."
        doctor "It would have been very dangerous if you were just a little bit late."
        doctor "Phones aren't good for you, so please just rest instead."
        hide simyoung11
        show simyoung14
        simyo "What...? What the hell did he say? There's no phone??!!"
        hide simyoung14
        show simyoung15
        simyo "No wait... what did he say before? I'm now sexually disabled??!"
        simyo "I've got no balls???!!!"
        hide simyoung15
        show simyoung16
        simyo "No balls... No... No balls???!!! WHAT THE FUCK IS THIS?!!!! I HAVE NO BALLS!!!! I... I HAVE NO BALLS!!!!!!!! AHHHHHHHHHH!!!!!!!"
        hide simyoung16
        with dissolve
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(1,hard=True)
        narrator "Shim Young later died that day after the thought of loosing his precious balls."
        $ renpy.pause(1,hard=True)
        $ show_quick_menu = True
        window show
        with dissolve 
        show kor7
        with dissolve    
        play music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k intro.ogg"
        queue music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k.ogg"     
        show sho21a_952:
            xpos 300
            ypos 30
            zoom 0.9
        with dissolve
        beatrice "We're going to have to wait..."
        beatrice "We won't know the true status of Shim Young until the media reports this..."   
        beatrice "But for the moment... let's lay low."
        kristik "Alright."
        hide sho21a_952
        show sho21a_911:
            xpos 300
            ypos 30
            zoom 0.9   
        beatrice "Now, we need to fight off the Soviet Red Army in the North!"
        kristik "WHAT??!?!! I NEED TO REST BRO!"
        hide sho21a_911
        show sho21a_921:
            xpos 300
            ypos 30
            zoom 0.9   
        beatrice "For what?! You take more care of your own shoes than your body!"
        beatrice "Stop your bitching and let's just go."
        kristik "AUghhghhhghg"
        hide kor7
        hide sho21a_921
        with dissolve
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(1,hard=True)
        $ show_quick_menu = True
        window show
        with dissolve 
        show hideout
        with dissolve     
        play sound "audio/Escape From Tarkov - Hideout Ambient Sound.rat-HQ.ogg" loop
        show sho21a_911 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7
        with dissolve
        beatrice "Welcome to my hideout!"
        hide sho21a_911 onlayer mcsprite        
        kristik "Damn bitch, you live like this?"
        kristik "Place looks like a shithole..."
        show sho21a_921 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7               
        beatrice "Hey! I'm only level 5 on my PMC so I can't really upgrade anything!"
        beatrice "Finding car batteries aren't easy for Vents Level 2 you know?!"
        hide sho21a_921 onlayer mcsprite        
        kristik "I feel like a very few amount of people would get that reference unless they played that game..."
        show sho21a_952 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7      
        beatrice "Whatever..."  
        hide sho21a_952 onlayer mcsprite 
        show sho21a_921 onlayer mcsprite:
            xpos -150
            ypos 500
            zoom 0.7     
        beatrice "Hurry up and pick your weapons."        
        hide sho21a_921 onlayer mcsprite
        kristik "Weapons????!! We stayin strapped?!!!"
        label weaponselect:
            $ show_quick_menu = False
            window hide
            menu:
                "Pick-up 5.56x45mm NATO HK 416A5":
                    $ show_quick_menu = True
                    window show
                    narrator "You picked the HK 416A5."
                    narrator "Please select your ammunition type."
                    $ show_quick_menu = False
                    window hide
                    menu:
                        "5.56x45mm Warmageddon":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 5.56x45mm Warmageddon."
                            narrator "Stats of this ammunition is: {b}85 Damage, 3 Penetration Power, 10%% More Accuracy, 10%% More Recoil, 5%% Ricochet Chance, 90%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    $ warDeathEnding == 1                                
                                    jump afterweapon                            
                        "5.56x45mm MK 318 Mod 0 (SOST)":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 5.56x45mm MK 318 Mod 0 (SOST)."
                            narrator "Stats of this ammunition is: {b}67 Damage, 20 Penetration Power, 10%% More Accuracy, 10%% Ricochet Chance, 15%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    $ warDeathEnding == 2
                                    jump afterweapon
                        "5.56x45mm M856A1":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 5.56x45mm M856A1."
                            narrator "Stats of this ammunition is: {b}51 Damage, 37 Penetration Power, 1%% Less Accuracy, 4%% More Recoil, 38%% Ricochet Chance, 32.8%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "5.56x45mm M995":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 5.56x45mm M995."
                            narrator "Stats of this ammunition is: {b}40 Damage, 53 Penetration Power, 8%% More Recoil, 36%% Ricochet Chance, 32%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon                            
                        "5.56x45mm SSA AP":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 5.56x45mm SSA AP."
                            narrator "Stats of this ammunition is: {b}36 Damage, 56 Penetration Power, 6%% Less Accuracy, 6%% More Recoil, 48%% Ricochet Chance, 20%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                "Pick-up 7.62x54mmR Dragunov SVDS":
                    $ show_quick_menu = True
                    window show
                    narrator "You picked the Dragunov SVDS."
                    narrator "Please select your ammunition type."
                    $ show_quick_menu = False
                    window hide
                    menu:
                        "7.62x54mm R PS gzh":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 7.62x54mm R PS gzh."
                            narrator "Stats of this ammunition is: {b}86 Damage, 45 Penetration Power, 10%% More Accuracy, 8%% More Recoil, 28.5%% Ricochet Chance, 8.3%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x54mm R T-46M gzh":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 7.62x54mm R T-46M gzh."
                            narrator "Stats of this ammunition is: {b}82 Damage, 41 Penetration Power, 1%% Less Accuracy, 5%% Less Recoil, 30%% Ricochet Chance, 18%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x54mm R BT gzh":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 7.62x54mm R BT gzh."
                            narrator "Stats of this ammunition is: {b}78 Damage, 59 Penetration Power, 2%% Less Accuracy, 4%% Less Recoil, 26.5%% Ricochet Chance, 8.1%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x54mm R SNB gzh":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 7.62x54mm R SNB gzh."
                            narrator "Stats of this ammunition is: {b}75 Damage, 62 Penetration Power, 10%% More Recoil, 28.5%% Ricochet Chance, 8%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x54mm R BS gs":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 7.62x54mm R BS gs."
                            narrator "Stats of this ammunition is: {b}72 Damage, 70 Penetration Power, 34%% Ricochet Chance, 8.3%% Fragmentation Chance."  
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon                                          
                "Pick-up 9x39mm TsNIITochMash AS VAL":
                    $ show_quick_menu = True
                    window show
                    narrator "You picked the TsNIITochMash AS VAL."
                    narrator "Please select your ammunition type."
                    $ show_quick_menu = False
                    window hide
                    menu:
                        "9x39mm SP-5 gs":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 9x39mm SP-5 gs."
                            narrator "Stats of this ammunition is: {b}68 Damage, 38 Penetration Power, 40%% Ricochet Chance, 20%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    $ warDeathEnding == 3                                
                                    jump afterweapon
                        "9x39mm SPP gs":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 9x39mm SPP gs."
                            narrator "Stats of this ammunition is: {b}64 Damage, 50 Penetration Power, 10%% More Accuracy, 20%% More Recoil, 40%% Ricochet Chance, 20%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "9x39mm PAB-9 gs":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 9x39mm PAB-9 gs."
                            narrator "Stats of this ammunition is: {b}62 Damage, 48 Penetration Power, 15%% Less Accuracy, 10%% More Recoil, 48%% Ricochet Chance, 10%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "9x39mm BP gs":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 9x39mm BP gs."
                            narrator "Stats of this ammunition is: {b}60 Damage, 55 Penetration Power, 10%% More Accuracy, 22%% More Recoil, 50%% Ricochet Chance, 10%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "9x39mm SP-6 gs":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 9x39mm SP-6 gs."
                            narrator "Stats of this ammunition is: {b}58 Damage, 46 Penetration Power, 10%% More Recoil, 50%% Ricochet Chance, 10%% Fragmentation Chance."  
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                "Pick-up 7.62x51mm NATO Lobaev Arms DVL-10":
                    $ show_quick_menu = True
                    window show
                    narrator "You picked the Lobaev Arms DVL-10."
                    narrator "Please select your ammunition type."
                    $ show_quick_menu = False
                    window hide
                    menu:
                        "7.62x51mm Ultra Nosler":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 7.62x51mm Ultra Nosler."
                            narrator "Stats of this ammunition is: {b}107 Damage, 15 Penetration Power, 10%% More Accuracy, 5%% Less Recoil, 20%% Ricochet Chance, 70%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    $ warDeathEnding == 4   
                                    jump afterweapon
                        "7.62x51mm BCP FMJ":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 7.62x51mm BCP FMJ."
                            narrator "Stats of this ammunition is: {b}88 Damage, 31 Penetration Power, 3%% More Recoil, 20%% Ricochet Chance, 25%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x51mm M80":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked 7.62x51mm M80."
                            narrator "Stats of this ammunition is: {b}80 Damage, 41 Penetration Power, 38%% Ricochet Chance, 17%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x51mm M61":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 7.62x51mm M61."
                            narrator "Stats of this ammunition is: {b}70 Damage, 64 Penetration Power, 3%% More Accuracy, 10%% More Recoil, 30%% Ricochet Chance, 13%% Fragmentation Chance."
                            narrator "Would you like to change your choice?"
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show
                                    jump afterweapon
                        "7.62x51mm M993":
                            $ show_quick_menu = True
                            window show
                            narrator "You picked the 7.62x51mm M993."
                            narrator "Stats of this ammunition is: {b}67 Damage, 70 Penetration Power, 5%% More Accuracy, 8%% More Recoil, 28%% Ricochet Chance, 13%% Fragmentation Chance."  
                            narrator "Would you like to change your choice?"       
                            $ show_quick_menu = False
                            window hide
                            menu:
                                "Yes":
                                    $ show_quick_menu = True
                                    window show
                                    narrator "Returning to weapon select."
                                    jump weaponselect
                                "No":
                                    $ show_quick_menu = True
                                    window show                                
                                    jump afterweapon                                               
        label afterweapon:
            show sho21a_902 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7  
            beatrice "Did'ya pick your stuff yet?"
            hide sho21a_902 onlayer mcsprite
            kristik "Yeah... "
            show sho21a_911 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7  
            beatrice "Cool! Now let's go to the border."
            hide sho21a_911 onlayer mcsprite
            kristik "Wait... what about... food? Meds? A backpack?"
            show sho21a_921 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7               
            beatrice "Stop crying and get going!"
            stop music fadeout 2.0
            stop sound fadeout 2.0
            hide sho21a_921 onlayer mcsprite
            hide hideout
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(1,hard=True)
            show customs1          
            with dissolve    
            play sound "audio/Rain with Thunder Sounds _ Escape from Tarkov - One Hours _ Game Ambience ASMR-(128kbps).ogg" fadein 2.0 loop
            show tarkovlbel
            with dissolve     
            $ renpy.pause(3,hard=True)
            hide tarkovlbel
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve 
            kristik "Ughh..... I'm so bored... and cold... and hungry..."   
            kristik "Where the hell is the enemy???"
            show sho21a_921 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7               
            beatrice "Why is it that the only thing that comes out of your mouth is complaints?"
            beatrice "Do something more productive!"
            hide sho21a_921 onlayer mcsprite
            kristik "sheesh... no need to be such a BITCH about it..."
            $ show_quick_menu = False
            window hide
            menu:          
                "Travel West":
                    $ EXPbeatrice += 1
                    $ show_quick_menu = True
                    window show                    
                    kristik "I'll go westward towards the storage area."
                    show sho21a_902 onlayer mcsprite:
                        xpos -150
                        ypos 500
                        zoom 0.7  
                    beatrice "Sure, but watch out. There tends to be a lot of scavs in the area."
                    beatrice "Oh, and take this M4. The guns you chose are pretty ass."
                    hide sho21a_902 onlayer mcsprite
                    kristik "What??!! But this is the meta setup!"
                    show sho21a_921 onlayer mcsprite:
                        xpos -150
                        ypos 500
                        zoom 0.7               
                    beatrice "Yeah and that meta sucks ass! Now hurry up and take this M4!"   
                    hide sho21a_921 onlayer mcsprite
                    kristik "AUuUHUGhghgh.gh.g.hf.gh.fgh.gh,g.h,tgfhmdorhuyduiorhtydryzdy"        
                    hide customs1
                    with dissolve
                    $ show_quick_menu = False
                    window hide 
                    with dissolve 
                    $ renpy.pause(1,hard=True)
                    show customs3          
                    with dissolve
                    $ show_quick_menu = True
                    window show
                    with dissolve   
                    kristik "Still quite cloudy...."
                    kristik "I didn't expect this place to be across a whole ass river!"
                    kristik "I'm so tired..."
                    "...."
                    kristik "Huh...?"
                    $ show_quick_menu = False
                    window hide        
                    hide customs3            
                    show twest1:
                        zoom 0.67
                    with dissolve
                    $ renpy.pause(2.5, hard=True)
                    show tarkovstill2
                    hide twest1                    
                    call screen text_timer2
                    label success_label2:
                        show twest2:
                            zoom 0.67
                        hide tarkovstill2   
                        with Dissolve(0.2)                      
                        $ renpy.pause(6.8, hard=True)    
                        hide twest2
                        show customs3
                        $ show_quick_menu = True
                        window show                           
                        kristik "Psh... just a dumb scav."
                        kristik "Yikes what the fuck is that?!"
                        kristik "Is that shit a landmine?!!"
                        kristik "I nearly stepped on that shit..."
                        show sho21a_501:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        with dissolve
                        beatrice "Is everything fine?"
                        hide sho21a_501
                        show sho21a_502:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        kristik "Yeah... uh.. but what are you doing here?"
                        kristik "Why'd you follow me?"
                        hide sho21a_502
                        show sho21a_402a:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        beatrice "..."
                        hide sho21a_402a
                        show sho21a_503a:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        beatrice "It doesn't concern you!"
                        hide sho21a_503a
                        show sho21a_504:
                            xpos 350
                            ypos 30
                            zoom 0.8  
                        kristik "Um.. it kinda does... cause you're following ME... which does concern ME.... Noob..."
                        hide sho21a_504
                        show sho21a_201a:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        beatrice "Fine! If you're going to be like that, then I'll just leave!"
                        hide sho21a_201a
                        with dissolve
                        kristik "WAIT! DON'T GO OVER THERE!"
                        show sho21a_201a onlayer mcsprite:
                            xpos -150
                            ypos 500
                            zoom 0.7               
                        beatrice "Shut up! I don't care what you say!"       
                        hide sho21a_201a onlayer mcsprite
                        kristik "THERE'S AN EXPLOSIVE OVER THERE-{p=0.4}{nw}"   
                        #======================================================================================================================================
                        ##########play explosion sound            
                        #======================================================================================================================================
                        $ renpy.pause(2,hard=True)
                        kristik "BEATRICE!!!"
                        hide customs3
                        stop sound fadeout 2.0
                        with dissolve
                        $ show_quick_menu = False
                        window hide 
                        with dissolve 
                        $ renpy.pause(1,hard=True)                        
                        jump wesleypart
                    label fail_label2:
                        show tarkovdeath:
                            zoom 0.67
                        hide tarkovstill2 
                        with Dissolve(0.2)                          
                        $ renpy.pause(6.9, hard=True)   
                        hide tarkovdeath
                        $ renpy.pause(1, hard=True) 
                        stop sound fadeout 2.0
                        "Kristik was unable to shoot the target fast enough and died due to a sudden explosion of a concealed landmine."
                        "His body and limbs were blown into pieces."
                        "{b} Bad ending 8/21"  
                        if (persistent.endingFinished8 < 1):
                            $ persistent.endingFinished8 += 1
                        elif (persistent.endingFinished8 >= 1):
                            pass
                        else:
                            narrator "PERSISTENT DATA FAILURE FOR SECTION 15596. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                            $ renpy.quit()
                        $ MainMenu(confirm=False)()                                               
                "Travel East":
                    $ show_quick_menu = True
                    window show                
                    kristik "I'll go east, towards the old factory and the military checkpoint."
                    show sho21a_902 onlayer mcsprite:
                        xpos -150
                        ypos 500
                        zoom 0.7  
                    beatrice "Sure, but watch out. There tends to be a lot of scavs in the area."
                    beatrice "Oh, and take this M4. The guns you chose are pretty ass."
                    hide sho21a_902 onlayer mcsprite
                    kristik "What??!! But this is the meta setup!"
                    show sho21a_921 onlayer mcsprite:
                        xpos -150
                        ypos 500
                        zoom 0.7               
                    beatrice "Yeah and that meta sucks ass! Now hurry up and take this M4!"                    
                    hide sho21a_921 onlayer mcsprite
                    kristik "AUuUHUGhghgh.gh.g.hf.gh.fgh.gh,g.h,tgfhmdorhuyduiorhtydryzdy"        
                    stop sound fadeout 2.0
                    hide customs1
                    with dissolve
                    $ show_quick_menu = False
                    window hide 
                    with dissolve 
                    $ renpy.pause(1,hard=True)
                    show customs2          
                    play sound "audio/The Ambient Sounds of Tarkov-(128kbps).ogg" fadein 2.0 loop
                    with dissolve
                    $ show_quick_menu = True
                    window show
                    with dissolve   
                    kristik "Looks like the weather is clearing up..."
                    kristik "But jeez.... I've been walking for so long...."
                    kristik "I'm so tired..."
                    "...."
                    kristik "Huh...?"
                    $ show_quick_menu = False
                    window hide        
                    hide customs2            
                    show teast1:
                        zoom 0.67
                    with dissolve
                    $ renpy.pause(1.825, hard=True)
                    show tarkovstill1
                    hide teast1                    
                    call screen text_timer
                    label success_label:
                        show teast2:
                            zoom 0.67
                        hide tarkovstill1   
                        with Dissolve(0.2)                      
                        $ renpy.pause(6.8, hard=True)    
                        hide teast2
                        show customs2
                        $ show_quick_menu = True
                        window show                           
                        kristik "Psh... just a dumb scav."
                        kristik "Yikes what the fuck is that?!"
                        kristik "Is that shit a landmine?!!"
                        kristik "I nearly stepped on that shit..."
                        show sho21a_501:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        with dissolve
                        beatrice "Is everything fine?"
                        hide sho21a_501
                        show sho21a_502:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        kristik "Yeah... uh.. but what are you doing here?"
                        kristik "Why'd you follow me?"
                        hide sho21a_502
                        show sho21a_402a:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        beatrice "..."
                        hide sho21a_402a
                        show sho21a_503a:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        beatrice "It doesn't concern you!"
                        hide sho21a_503a
                        show sho21a_504:
                            xpos 350
                            ypos 30
                            zoom 0.8  
                        kristik "Um.. it kinda does... cause you're following ME... which does concern ME.... Noob..."
                        hide sho21a_504
                        show sho21a_201a:
                            xpos 350
                            ypos 30
                            zoom 0.8
                        beatrice "Fine! If you're going to be like that, then I'll just leave!"
                        hide sho21a_201a
                        with dissolve
                        kristik "WAIT! DON'T GO OVER THERE!"
                        show sho21a_201a onlayer mcsprite:
                            xpos -150
                            ypos 500
                            zoom 0.7               
                        beatrice "Shut up! I don't care what you say!"       
                        hide sho21a_201a onlayer mcsprite
                        kristik "THERE'S AN EXPLOSIVE OVER THERE-{p=0.4}{nw}"   
                        #======================================================================================================================================
                        ##########play explosion sound            
                        #======================================================================================================================================
                        $ renpy.pause(2,hard=True)
                        kristik "BEATRICE!!!"
                        hide customs2
                        stop sound fadeout 2.0
                        with dissolve
                        $ show_quick_menu = False
                        window hide 
                        with dissolve 
                        $ renpy.pause(1,hard=True)                        
                        jump wesleypart

                    label fail_label:
                        show tarkovdeath:
                            zoom 0.67
                        hide tarkovstill1 
                        with Dissolve(0.2)                          
                        $ renpy.pause(6.9, hard=True)   
                        hide tarkovdeath
                        $ renpy.pause(1, hard=True) 
                        stop sound fadeout 2.0
                        "Kristik was unable to shoot the target fast enough and died due to a sudden explosion of a concealed landmine."
                        "His body and limbs were blown into pieces."
                        "{b} Bad ending 76"
                        if (persistent.endingFinishe7 < 1):
                            $ persistent.endingFinished7 += 1
                        elif (persistent.endingFinished7 >= 1):
                            pass
                        else:
                            narrator "PERSISTENT DATA FAILURE FOR SECTION 15734. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                            $ renpy.quit()
                        $ MainMenu(confirm=False)()
        label wesleypart:
            show customs1
            with dissolve
            play sound "audio/Rain with Thunder Sounds _ Escape from Tarkov - One Hours _ Game Ambience ASMR-(128kbps).ogg" fadein 2.0 loop
            $ show_quick_menu = True
            window show
            with dissolve     
            kristik "Hey! Wake up!"
            show sho21a_504 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7 
            beatrice "..." 
            hide sho21a_504 onlayer mcsprite  
            kristik "Fuck! This is why I told you to bring meds!"
            show wesley_3:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            unknown "Is she breathing?"
            kristik "Who are you?!!"
            unknown "My name is Ястржембский Уэслианский Христорождественский (Yastrzhembsky Ueslianskiy Khristorozhdestvensky)."
            unknown "You can call me Wesley."
            kristikmind "{i}Wesley???!!"
            wesley "I'm a Trauma Doctor and Certified Nurse Practitioner with an MD in General Internal Medicine as well as a PhD in both Biochemistry and Pharmacology."
            wesley "I've also worked in the fields of being an Otolaryngologist surgeon, Thoracic surgeon and Critical Care surgeon for 17 years."
            kristik "Ok, well now's not the time to flex! You need to save my girlfriend!"
            wesley "This is your spouse?"
            kristik "Um.. no not really."
            kristik "Well... uh... I guess?"
            wesley "Please stand clear. I'll bring her into this tent."
            kristik "Um ok... do you have a first aid kit?"
            wesley "A first aid kit isn't going to work on such severe trauma like this one."
            wesley "I'll have to give my initial treatment and analysis, so please bear with me."
            kristik "Ok..."
            hide wesley_3
            with dissolve
            hide customs1
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(1,hard=True)
            show customs1          
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve    
            show wesley_3:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            kristik "Is she okay?!!"
            wesley "Her brain is alive, however she has many fractured bones and it appears that some fragments have pierced through her body."   
            wesley "I used splints to support the bones for re-growth, but of course it will take much longer for those bones to heal properly." 
            wesley "No limbs have been lost however, but she was heavily bleeding. I used hemostatic agents to stop the bleeding."
            wesley "There's no telling if she had any internal bleeding, as I do not have my equipment out here in the field."   
            kristik "Fuck..."
            kristik "Will she be okay out here?!"
            wesley "Her neck is badly damaged, and will require tracheostomy in order for her lungs to breathe properly."
            wesley "This wouldn't be a problem if I had the proper equipment, however I do not have the anesthetics, suction equipment, or humidification system to allow for a proper tracheostomy procedure to occur."
            kristik "So... she can't breathe?!!"
            wesley "She is breathing though it may not be enough air to sustain her body fully for a period of time, at this rate."
            wesley "We need her to get to a hospital right away."
            wesley "Preferrably, the hospital I work at."
            kristik "Where is it? How far is it??"
            wesley "It's east of us. Quite far, I'd say a 2 hour walk if you're up with carrying her for that far without fracturing her bones even worse."
            wesley "Do you have a helicopter?"
            kristik "What the... why the fuck would I have an airlift helicopter?!! No I don't!"
            wesley "Well, do you know anybody who does?"
            kristik "No of course not! Wait... I may know ONE person..."
            kristik "Where is the nearest telephone box?"
            wesley "It's just down the road. Here's 50 cents. Make sure you call via the trunk line otherwise we won't be able to pay for the long distance."
            hide wesley_3
            with dissolve
            hide customs1
            with dissolve
            stop sound fadeout 2.0
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(1,hard=True)
            show office3         
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve  
            play sound "audio/lightingciggie.ogg"   
            show aaron_3:
                xpos -90
                ypos 175
                zoom 0.65   
            with dissolve
            hide aaron_3
            show aaron_8:
                ypos 175
                zoom 0.6          
            with dissolve  
            aaron "Another boring ass day...."
            aaron "With that northern war going on, life is still as boring as if nothing was happening..."
            play sound "audio/Old Ringing Phone Sound - Old Telephone Ring Effect-HQ.ogg"
            #============================================================================================================================================
            # play vintage phone ringing sounds
            #============================================================================================================================================
            $ renpy.pause(5,hard=True)
            stop sound
            hide aaron_8
            show aaron_2:
                ypos 175
                zoom 0.57            
            aaron "Who the hell is calling me?"
            aaron "Well I'm bored as shit so I might as well answer it."
            hide aaron_2
            show aaron_8:
                ypos 175
                zoom 0.6   
            aaron "Hello? Who are you?"
            kristik "Hey! Aaron! Yeah, you won't know me, but I need your help!"
            aaron "Who the hell are you and how do you know my name?"
            kristik "Look, that isn't important right now, my girlfriend is in serious trouble and we need your help!"
            aaron "Now how about YOU look here, I don't know what the hell kind of marital drama you're going through but whatever you do with YOUR girlfriend is none of my business."   
            kristik "She's hurt really bad! She stood on a landmine!"
            aaron "Then bring her to a hospital."
            kristik "The nearest one is 2 hours away!"
            aaron "Well what the hell do you want me to do? I don't run an ambulance service, the roads over there are probably really shitty."
            kristik "But you probably got a helicopter, a Bell 222 was it?"
            aaron "..."
            aaron "How the hell do you know that?"
            kristik "Look, just BRING YOUR HELICOPTER HERE! MY GIRLFRIEND IS PROLLY DYIN RN!!!!"
            aaron "Alright stop your bitchin and I'll be there. You didn't even tell me where the hell ya'll were."
            kristik "Between the rail tracks and the old dormitories. A set of tents."
            aaron "Ok. But you owe me big time mister mystery man."
            play sound "audio/Telephone, Antique - 1907 Wall Phone_ Hang up Receiver Vintage Entertainment-HQ.ogg"
            #============================================================================================================================================
            # play vintage phone hanging up sounds
            #============================================================================================================================================
            $ renpy.pause(2,hard=True)     
            aaron "Well shits gone interesting today at least."     
            hide aaron_8
            with dissolve
            hide office3
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)
            show customs1     
            with dissolve
            play sound "audio/Rain with Thunder Sounds _ Escape from Tarkov - One Hours _ Game Ambience ASMR-(128kbps).ogg" fadein 2.0 loop
            $ show_quick_menu = True
            window show
            with dissolve     
            kristik "He should be here any moment..."
            show wesley_3:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve            
            wesley "Her heartrate is slowing down."
            wesley "We need to hurry."
            play music "audio/Helicopter Flying Over Head Sound Effects-(128kbps).ogg" fadein 2.0
            #====================================================================================================================
            #play helicopter ambience
            #====================================================================================================================

            $ renpy.pause(2,hard=True)

            kristik "I hear it!"
            $ renpy.pause(2,hard=True)
            stop music fadeout 2.0
            play music "audio/helicopter.ogg" fadein 2.0
            hide customs1
            show helicopter
            with dissolve
            kristik "Wesley, bring her on! I'll talk to the pilot."
            stop music fadeout 2.0
            stop sound fadeout 2.0
            play music "audio/helicoptercockpit.ogg"
            hide helicopter
            show cockpit
            with dissolve
            show aaron_11 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4  
            aaron "So that's your girlfriend?"
            hide aaron_11 onlayer mcsprite
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "I've seen you two from somewhere... like the city..."
            aaron "Well, give me the directions. I have no idea where this hospital is."
            hide aaron_11_1 onlayer mcsprite
            kristik "Uhh...."
            kristik "Hold on, Wesley gave me a map..."
            show math
            with dissolve
            $ renpy.pause(2,hard=True)
            kristik "Fuck...."
            kristik "I have to use... math?!!!!"
            hide math
            with dissolve
            show wesley_3 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.5       
            wesley "Guys, she is in a critical state. Let's get going."
            hide wesley_3 onlayer mcsprite        
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "Well this guy here isn't giving me the directions to the hospital!"   
            hide aaron_11_1 onlayer mcsprite         
            show wesley_3 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.5       
            wesley "I gave you a map. Use it."
            hide wesley_3 onlayer mcsprite   
            kristik "Yeah, but this shit isn't a real map! I have to find the bearings myself!"
            show wesley_3 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.5       
            wesley "Just do it, I'd say we got a full 2 minutes until we cross the point of no return."
            hide wesley_3 onlayer mcsprite                        
            kristik "What?!!!"
            show math
            with dissolve
            "Find the bearing between your current location (marked on the bottom left) and to WP2 (waypoint 2)."
            "Your answer will be a whole number."
            "You will have 2 minutes to solve and answer this problem."
            show screen text_timermath   
            label question:
                style input:   
                    outlines [(2, "#000", 0, 0)] 
                "Please type your answer on the next page."  
                python:
                    answer = renpy.input("", length=32, exclude=u'{.}abcdefghijklmnopqrstuvwxyz~ABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()_+-=[]\|}{"'':;/,.<>?')
                if answer == "73":
                    hide screen text_timermath
                    "Your answer is correct. (Bearing: {b}N [answer]° E{/b})."
                    jump success_math
                else:
                    "Your answer is not correct. (Bearing: {b}N [answer]° E{/b}). You will be prompted to answer the question correctly."
                    jump question
                label fail_math:
                    "You were unable to answer the question in a timely manner."
                    "You will now die."
                    stop music fadeout 2.0
                    play sound "audio/awp.mp3"
                    show white
                    hide cockpit
                    hide math
                    $ renpy.pause(0.001,hard=True)           
                    "Kristik died due to a voice inside his head telling him he was not worth living after failing to solve such a simple math problem."
                    "{b}Bad ending 9/21"  
                    if (persistent.endingFinished9 < 1):
                        $ persistent.endingFinished9 += 1
                    elif (persistent.endingFinished9 >= 1):
                        pass
                    else:
                        narrator "PERSISTENT DATA FAILURE FOR SECTION 15991. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                        $ renpy.quit()
                    $ MainMenu(confirm=False)()    
                label success_math:
                    hide math
                    with dissolve
                    kristik "Bearnig is N 73° E, 368 meters away."
                    show aaron_11_1 onlayer mcsprite:
                        xpos -80
                        ypos 490
                        zoom 0.4
                    aaron "Alright."          
                    aaron "Everyone sit your asses down, we're getting to the hospital."
                    hide aaron_11_1 onlayer mcsprite
                    stop music fadeout 2.0
                    hide cockpit
                    hide wesley_3
                    with dissolve
                    $ show_quick_menu = False
                    window hide 
                    with dissolve 
                    $ renpy.pause(2,hard=True)    
                    jump lastpart       
        label lastpart:
            $ renpy.pause(2,hard=True)
            show BG049     
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve
            play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
            show wesley_3:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            wesley "I'll start on the operation right now."
            wesley "Expect this to be done in about 12 hours."
            kristik "Ok."
            hide BG049
            show BG003c
            with dissolve
            kristik "Ugh..."
            kristik "I haven't eaten anything in so long..."
            show aaron_11_1:
                xpos 450
                ypos 30
                zoom 0.4               
            with dissolve
            aaron "Hey."
            kristik "Sup...?"
            aaron "How exactly do you know me?"
            kristik "Umm.."
            kristikmind "{i} I can't tell him i'm a time traveller or he'd think I'm nuts!!"
            hide aaron_11_1
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.4                
            aaron "Time traveller huh?"
            kristik "uhh.. wuT?!?"
            aaron "Whatever. I'd imagine we met somewhere else in a separate plane of existance."
            hide aaron_11
            show aaron_11_1:
                xpos 450
                ypos 30
                zoom 0.4   
            aaron "I won't bother you and your girlfriend, plus I'm getting bored of this already. So seeya."
            kristik "Um... see you too i guess?{p=0.5}{nw}"
            hide aaron_11_1
            with dissolve
            kristik "And he's gone..."   
            stop music fadeout 2.0
            hide wesley_3    
            hide wesley_3   
            hide wesley_3       
            hide wesley_3   
            hide wesley_3   
            hide BG003c
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)

            show white_base
            with dissolve
            show next_base
            show transition2
            with blinds
            $ renpy.pause(5, hard=True)  
            hide white_base
            hide next_base
            hide transition2
            with blinds
            $ renpy.pause(1, hard=True) 


            "{i} 2 months later..."
            $ renpy.pause(2,hard=True)
            kristik "I haven't seen her in so long..."
            kristik "I hope she's a lot better."
            show BG017n1 
            with dissolve
            play music "audio/Sanoba Witch OST - Real Friend (Quiet Ver.)-(128kbps).ogg"
            $ show_quick_menu = True
            window show
            with dissolve 
            show wesley_3:
                xpos 500
                ypos 60
                zoom 0.4
            with dissolve
            wesley "She's in stable condition."
            wesley "Most of her bones had regrown, though she will have to go through some extra physical therapy in order to walk properly."          
            kristik "Can I speak to her right now?"
            wesley "Yes."
            hide wesley_3
            hide BG017n1
            show girl
            with dissolve
            beatrice "Hey."
            kristik "Sup."
            kristik "You doin okay?"
            beatrice "Yeah."
            beatrice "My legs still feel a little weird, but I'm doing fine."
            beatrice "Thanks for helping me."
            kristik "I didn't do anything, Wesley and Aaron both did a lot more than me."
            beatrice "Don't be like that! If it weren't for you they both would not even have helped me in the first place!"
            kristik "I guess..."
            beatrice "Sorry for being so mean to you back then..."
            beatrice "It probably annoyed you..."
            kristik "It's fine... if anything... it just made you cuter."
            beatrice "Hehe. I know that you had a crush on me by the way."
            kristik "U-uh... me? No.."
            beatrice "Don't lie to me right now. It doesn't matter anyways, because I return those feelings for you."
            kristik "Really...?"
            beatrice "Yeah."
            kristik "I love you."
            beatrice "Haha! No need to say it. I already know you do."
            kristik "Thanks a lot."
            beatrice "You're welcome."
            stop music fadeout 2.0
            hide girl
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve             
            $ renpy.pause(2,hard=True)
            show wesley_3 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.5       
            wesley "By the way, here's your bill for the surgery and the helicopter ride."
            wesley "Comes to about... $400,000."
            hide wesley_3 onlayer mcsprite      
            kristik "Hey... Beatrice?"
            show sho21b_004 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7               
            beatrice "Yeah?"       
            hide sho21b_004 onlayer mcsprite
            kristik "I think uh... we're going to have to discharge you a little early."
            kristik "I can't imagine the cost after physical therapy..."
            show sho22b_702 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7               
            beatrice "Jeez.... You really are hopeless.."       
            hide sho22b_702 onlayer mcsprite
            show sho22b_301 onlayer mcsprite:
                xpos -150
                ypos 500
                zoom 0.7               
            beatrice "Though that's what I like about you..."       
            hide sho22b_301 onlayer mcsprite            
            $ renpy.pause (2,hard=True)
            "{b}Good ending 14/21"  
            if (persistent.endingFinished14 < 1):
                $ persistent.endingFinished14 += 1
            elif (persistent.endingFinished14 >= 1):
                pass
            else:
                narrator "PERSISTENT DATA FAILURE FOR SECTION 16156. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                $ renpy.quit()
            $ renpy.pause(2,hard=True)
            $ MainMenu(confirm=False)()        



    return

label chiesterEnding:
    show BG005
    play music "audio/Riddle Joker Original Soundtrack (OST) _Common Scenery-(128kbps).ogg"
    with dissolve
    $ show_quick_menu = True
    window show
    with dissolve 
    show aaron_11_1 onlayer mcsprite:
        xpos -80
        ypos 490
        zoom 0.4
    aaron "Alright, so listen to me."
    aaron "I've got you and those girls to meet here today."
    aaron "I told them a big scary monster is trying to hunt you down and assassinate you."
    aaron "Assuming that they actually love you, they would all be here."
    hide aaron_11_1 onlayer mcsprite       
    kristik "Umm.. what the hell is that stupid ass plan?"
    show aaron_11_1 onlayer mcsprite:
        xpos -80
        ypos 490
        zoom 0.4
    aaron "Just shut up and act natural; I told them you'd be here at 12:00PM on the dot. You only got 5 minutes."
    hide aaron_11_1 onlayer mcsprite       
    show girl7 (5) onlayer master1:
        xpos -50
        zoom 0.6
    show girl5 (9) onlayer master2:
        xpos 300
        zoom 0.6
    show girl6 (2) onlayer master3:
        xpos 600
        zoom 0.6
    show girl4 (3) onlayer master4:
        xpos 900
        zoom 0.6
    with dissolve
    everyone "We're here!"
    hide girl4 (3) onlayer master4
    hide girl6 (2) onlayer master3
    hide girl5 (9) onlayer master2
    hide girl7 (5) onlayer master1                
    show girl7 (1) onlayer master1:
        xpos -50
        zoom 0.6
    show girl5 (7) onlayer master2:
        xpos 300
        zoom 0.6
    show girl6 (3) onlayer master3:
        xpos 600
        zoom 0.6
    show girl4 (1) onlayer master4:
        xpos 900
        zoom 0.6        
    kristik "Shit!! They're actually here!!"
    show aaron_11_1 onlayer mcsprite:
        xpos -80
        ypos 490
        zoom 0.4
    aaron "What really???! Ok uh..."
    aaron "Just use your natural coochie grabbing skillz. I gotta go now so bye~!!!"
    hide aaron_11_1 onlayer mcsprite
    kristik "WAIT HOLD UP-"
    "..."
    kristik "Fuckin bitch..."
    hide girl4 (1) onlayer master4
    show girl4 (18) onlayer master4:
        ypos 50
        xpos 900
        zoom 0.6       
    c45 "Ummm... where is the big scary monster?!" 
    kristik "Umm... let's not worry about that for now."
    kristik "I actually want to know more about you guys."
    hide girl4 (18) onlayer master4
    hide girl6 (2) onlayer master3
    hide girl5 (9) onlayer master2
    hide girl7 (5) onlayer master1                
    show girl7 (2) onlayer master1:
        xpos -50
        zoom 0.6
    show girl5 (18) onlayer master2:
        ypos 30
        xpos 357
        zoom 0.6
    show girl6 (5) onlayer master3:
        xpos 600
        zoom 0.6
    show girl4 (11) onlayer master4:
        ypos -50
        xpos 900
        zoom 0.6    
    everyone "...?"
    hide girl7 (2) onlayer master1  
    show girl7 (13) onlayer master1:
        xpos -5
        zoom 0.6  
    c00 "Why are we here?"  
    c00 "Just for you to talk to us?"
    hide girl7 (13) onlayer master1  
    show girl7 (10) onlayer master1:
        xpos -5
        zoom 0.6      
    kristik "Yeah...?"
    hide girl7 (10) onlayer master1  
    show girl7 (13) onlayer master1:
        xpos -5
        zoom 0.6  
    c00 "We're outta here."
    hide girl7 (13) onlayer master1  
    show girl7 (10) onlayer master1:
        xpos -5
        zoom 0.6         
    kristik "Wait!" 
    menu:
        "''Ya'll are busty asf!!!''":    
            kristik "Ya'll are busty asf!!!"
            hide girl7 (10) onlayer master1  
            hide girl4 (11) onlayer master4
            hide girl6 (5) onlayer master3
            hide girl5 (18) onlayer master2   
            show girl7 (11) onlayer master1:
                xpos -5
                zoom 0.6       
            show girl5 (18) onlayer master2:
                ypos 30
                xpos 357
                zoom 0.6
            show girl6 (3) onlayer master3:
                xpos 600
                zoom 0.6
            show girl4 (14) onlayer master4:
                ypos -50
                xpos 900
                zoom 0.6    
            everyone "What?!"
            hide girl7 (11) onlayer master1  
            hide girl4 (14) onlayer master4
            hide girl6 (3) onlayer master3
            hide girl5 (18) onlayer master2       
            show girl7 (1) onlayer master1:
                xpos -50
                zoom 0.6
            show girl5 (7) onlayer master2:
                xpos 300
                zoom 0.6
            show girl6 (3) onlayer master3:
                xpos 600
                zoom 0.6
            show girl4 (1) onlayer master4:
                xpos 900
                zoom 0.6        
            stop music  
            play sound "audio/gunload_Master.wav"
            show gun onlayer misc:
                xpos 750
                ypos 400 
                zoom 0.5   
            show gun onlayer misc2:
                xpos 1100
                ypos 400 
                zoom 0.5          
            show gun onlayer misc3:
                xpos 400
                ypos 400 
                zoom 0.5    
            show gun onlayer misc4:
                xpos 100
                ypos 400 
                zoom 0.5  
            $ renpy.pause(0.8,hard=True)                                                                        
            kristik "WAIT HOLDUPUPUP I WAS JOKIN!!!!"        
            #===========================================================================================================================================================================
            # INSERT GUN SHOOTING SOUNDS
            #===========================================================================================================================================================================
            play sound "audio/awp.mp3"
            show white

            hide girl7 (17) onlayer master1
            hide girl5 (1) onlayer master2
            hide girl4 (1) onlayer master4            
            hide girl6 (3) onlayer master3              
            hide gun onlayer misc
            hide gun onlayer misc2
            hide gun onlayer misc3
            hide gun onlayer misc4
            $ renpy.pause(1,hard=True)     
            $ show_quick_menu = False
            window hide
            with dissolve
            $ renpy.pause(2,hard=True)  
            narrator "Due to Kristik's perverted nature, he was instantly killed by 4 women."
            narrator "{b}Bad ending 15/21{/b}"
            if (persistent.endingFinished15 < 1):
                $ persistent.endingFinished15 += 1
            elif (persistent.endingFinished15 >= 1):
                pass
            else:
                narrator "PERSISTENT DATA FAILURE FOR SECTION 16359. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                $ renpy.quit()
            window hide
            with dissolve
            $ renpy.pause(2,hard=True) 
            $ MainMenu(confirm=False)()                    
        "''I have a ROBUX giftcard with OBC!!!''": 
            kristik "I have a ROBUX giftcard with OBC!!!"
            hide girl7 (10) onlayer master1  
            show girl7 (14) onlayer master1:
                xpos -5
                zoom 0.6  
            c00 "You're not fooling us with that."
            c00 "There's no way you even have something like that."
            hide girl7 (14) onlayer master1  
            show girl7 (9) onlayer master1:
                xpos -5
                zoom 0.6    
            kristikmind "{i}Shit... she's right."    
            kristikmind "{i}ROBUX giftcards are a relic these days..."
            kristikmind "{i}I'll have to lie my way through this..."
            kristik "No, I actually have THOUSANDS of dollars worth of ROBUX in my house."
            kristik "You guys can come over to see it for yourself."
            hide girl5 (18) onlayer master2
            show girl5 (12) onlayer master2:
                ypos 30
                xpos 357
                zoom 0.6
            c556 "Why are you lyin so much huh?"
            hide girl5 (12) onlayer master2
            show girl5 (10) onlayer master2:
                ypos 30
                xpos 357
                zoom 0.6     
            kristik "I ain't lyin bro... I dunno what you want from me but I ain't lying."
            hide girl5 (10) onlayer master2
            show girl5 (12) onlayer master2:
                ypos 30
                xpos 357
                zoom 0.6
            c556 "Oh really? Why don't you let us into your house then? So we can see the ROBUX for ourselves?"
            hide girl5 (12) onlayer master2
            show girl5 (10) onlayer master2:
                ypos 30
                xpos 357
                zoom 0.6     
            kristikmind "{i} shit.... what should I say??"
            kristik "Psh. Sure. Why not. Like I said, I have THOUSANDS of dollars worth of ROBUX."
            hide girl5 (10) onlayer master2
            show girl5 (12) onlayer master2:
                ypos 30
                xpos 357
                zoom 0.6
            c556 "Ha! We'll see about that dweeb!"
            hide girl7 (9) onlayer master1
            hide girl5 (12) onlayer master2
            hide girl4 (11) onlayer master4            
            hide girl6 (5) onlayer master3        
            with dissolve
            kristik "Fuck! I need to call Aaron!"
            kristik "I don't even LIVE here nor do I have thousands of dollars worth of ROBUX..."

            #===========================================================================
            # play phone dialing
            #===========================================================================   

            $ renpy.pause(2,hard=True)
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "Hello? How did it go? Did you fail?"
            hide aaron_11_1 onlayer mcsprite
            kristik "No, I technically didn't but... I need a mansion and $100,000 worth of ROBUX..."
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "Say no more. I know a couple of people."
            hide aaron_11_1 onlayer mcsprite
            kristik "Wait what?? I thought you were going to step back and call me crazy..."
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "Well in a experiment like this, you get a lot of perks."
            hide aaron_11_1 onlayer mcsprite                              
            kristik "Tf kind of perks..?"   
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "Meet me later today at your new mansion."
            aaron "I'll send you the address once I'm able to get it picked up."
            hide aaron_11_1 onlayer mcsprite                              
            kristik "Uh... sure I guess..."
            stop music fadeout 2.0
            hide BG005
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)
            show nicehouse 
            play music "audio/Sanoba Witch OST - Asa no Youki-320k.ogg"
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve     
            kristik "Ummm... wtf???"
            kristik "This is overkill... just for some bitches..."
            aaron "Nonsense."
            kristik "???!"
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.4   
            with dissolve
            aaron "There ain't no such thing as overkill."
            aaron "This is the bare minimum if you ask me."
            aaron "We didn't even get you any Apple products, or some luxury cars, or a private jet."
            kristik "Why the fuck would I need all that shit... just for... some bitches??!!"    
            hide aaron_11
            show aaron_11_1:
                xpos 450
                ypos 30
                zoom 0.4   
            aaron "Shut yer goddamn mouth and listen to me ya hear?"
            aaron "I went through a lot of fuckin hoops tryna get this all setup for you."
            aaron "Remember how I spent over $200 to develop a visual novel game back in high school?"
            aaron "Just think of this as part 2 of that."
            kristikmind "{i}Bruh... he's bringing up shit... from that long ago???"
            hide aaron_11_1
            show aaron_11:
                xpos 450
                ypos 30
                zoom 0.4               
            aaron "Not to mention I spent nearly 3 months on that project..."
            hide aaron_11
            show aaron_11_1:
                xpos 450
                ypos 30
                zoom 0.4   
            aaron "Anywho you got a severe case of ''not-accepting-shit-that-you-should-be-totally-taking-advantage-of-itis.''"
            aaron "I told em bitches that you'd be here for this meeting."
            aaron "There's also $10 million worth of ROBUX giftcards in there."
            kristik "WHAT??!!!!"
            kristik "$10 MILLION?!!!"
            aaron "Yeah. I took out a loan for that one."
            kristik "LOAN?!?!?!??!?!?!"
            aaron "Just remember to pay me back after all this."
            kristik "PAY BACK?!@?!?@!?!??!?!?!?!?!?!?"
            kristik "FUCK NO!!!!"
            aaron "Alright sounds good to me."
            hide aaron_11_1
            with dissolve
            kristik "WHAT THE FUCK..."    
            kristik "How the fuck... am I supposed to get in here with this big ass gate in the way?"  
            #===========================================================================
            # play phone ringing
            #===========================================================================   

            $ renpy.pause(2,hard=True)

            kristik "Uh... hello?"
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "By the way Krabby, I forgot to mention one thing."
            aaron "Those girls are your maids in that house."
            hide aaron_11_1 onlayer mcsprite
            kristik "WHAT??!?!?!?" 
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "It was hard to convince them to be your maids, but I convinced em nonetheless."          
            hide aaron_11_1 onlayer mcsprite
            kristik "Bruh..."
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4
            aaron "That's it. See ya."     
            hide aaron_11_1 onlayer mcsprite
            #===========================================================================
            # play phone hangup sound
            #===========================================================================   

            $ renpy.pause(2,hard=True)          
            kristik "BRUH.."
            hide nicehouse 
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)
            show niceroom 
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve  
            kristik "Holy shit..."
            kristik "This place be BALLIN!!!"
            show girl4 (18):
                ypos 100
                xpos 400
                zoom 0.6  
            with dissolve  
            c45 "U-um.... Lord Kristik?"
            kristikmind "{i}''LORD''?!??!?!?"
            hide girl4 (18)
            show girl4 (17):
                ypos 100
                xpos 400
                zoom 0.6  
            c45 "What would you like me to do??!!!!"
            kristikmind "{i} Yikes.. she is nervous asf..."
            hide girl4 (17)
            show girl4 (18):
                ypos 100
                xpos 400
                zoom 0.6 
            kristik "Um... well first I would like to change your name."
            c45 "My name?"
            kristik "Yeah uh.. your regular name kinda a ''lame'' LOOLOOLO!!!"
            hide girl4 (18)
            show girl4 (20):
                ypos 100
                xpos 400
                zoom 0.6    
            c45 "That's not funny."
            hide girl4 (20)
            show girl4 (18):
                ypos 100
                xpos 400
                zoom 0.6   
            kristik "Sorry." 
            kristik "So uh..."
            menu:
                "''I'll call you Big Booty Judy.''":
                    kristik "I'll call you Big Booty Judy!!!!"
                    hide girl4 (18)
                    show girl4 (16):
                        ypos 100
                        xpos 400
                        zoom 0.6      
                    c45 "...."
                    hide girl4 (16)
                    show girl4 (20):
                        ypos 100
                        xpos 400
                        zoom 0.6  
                    c45 "No."
                    hide girl4 (20)
                    stop music 
                    play sound "audio/gunload_Master.wav"
                    show girl4 (9):
                        xpos 400
                        zoom 0.6         
                    show gun:
                        xpos 600
                        ypos 400 
                        zoom 0.5    
                    $ renpy.pause(0.8,hard=True)                                                                        
                    kristik "NOONONOONOO NAH I WAS JUST JOKIN!!!!"        
                    #===========================================================================================================================================================================
                    # INSERT GUN SHOOTING SOUNDS
                    #===========================================================================================================================================================================
                    play sound "audio/awp.mp3"
                    show white     
                    hide girl4 (9)                    
                    hide gun
                    hide niceroom
                    $ renpy.pause(1,hard=True)     
                    $ show_quick_menu = False
                    window hide
                    with dissolve
                    $ renpy.pause(2,hard=True)  
                    narrator "Kristik died due to fatal bullet penetration through his frontal lobe."
                    narrator "He was instantly killed."
                    narrator "{b}Bad ending 16/21{/b}"
                    if (persistent.endingFinished16 < 1):
                        $ persistent.endingFinished16 += 1
                    elif (persistent.endingFinished16 >= 1):
                        pass
                    else:
                        narrator "PERSISTENT DATA FAILURE FOR SECTION 16643. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                        $ renpy.quit()
                    window hide
                    with dissolve
                    $ renpy.pause(2,hard=True) 
                    $ MainMenu(confirm=False)()                                                                                     
                "''How about... Kirsten?''":
                    $ EXPc45 += 1
                    kristik "How about Kirsten?"
                    c45 "Um...."
                    hide girl4 (18)
                    show girl4 (17):
                        ypos 100
                        xpos 400
                        zoom 0.6   
                    c45 "Okay!!!!???!"
                    hide girl4 (17)
                    with dissolve
                    kristik "She gon be a challenge to grab..."
                    jump chiesterPartTwo
    label chiesterPartTwo:                  
        c556 "Hey."
        show girl5 (12):
            xpos 400
            zoom 0.6
        with dissolve
        c556 "Why are you suddenly so flirty around us?"
        hide girl5 (12)
        show girl5 (10):
            xpos 400
            zoom 0.6
        kristik "You call that being flirty? I barely even said anything."
        kristikmind "{i}This one kinda worries me tbh... she looks SUPER crazy..."
        hide girl5 (10)
        show girl5 (13):
            xpos 400
            zoom 0.6    
        c556 "Y'know... it doesn't hurt if you would ONLY do that to me."
        hide girl5 (13)
        show girl5 (10):
            xpos 400
            zoom 0.6        
        kristikmind "{i}Only to her?? I would fail my experiment with Aaron! I NEED TO MAKE SURE I CAN GET ALL OF THE BITCHES!!!!"
        kristik "Um. Yeah, but it would hurt EVEN LESS if I got ALL OF YA'LL!!!"
        hide girl5 (10)
        show girl5 (16):
            xpos 400
            zoom 0.6   
        c556 "..."
        stop music fadeout 2.0

        #============================================================================================================
        # slowly fade bg music
        #============================================================================================================
        kristikmind "{i}tf is she doin starin at me like that...?"
        kristikmind "{i} WHY DID THE MUSIC CUT OFF?!!!!"     
        hide girl5 (16)
        show girl5 (20):
            xpos 250
            ypos -30
            zoom 0.6   
        play music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps) intro.ogg"
        queue music "audio/Riddle Joker Original Soundtrack OST _Precious Memories-(128kbps).ogg"
        c556 "Guess I can't help it then!"
        hide girl5 (20)
        show girl5 (26):
            xpos 250
            ypos -30
            zoom 0.6    
        c556 "It hurt... a lot..."    
        kristikmind "{i}Ummmm... wtf???"
        hide girl5 (26)
        with dissolve
        kristikmind "{i}yikes... that one is real scary."
        kristikmind "{i}better make sure I don't tick that one off...."


        # idea for story: make girl6 and girl5 want a monogamy (single marriage) and girl7 and girl4 want a polygamy (harem). make branching parts.
        show girl7 (14):
            xpos 400
            zoom 0.6   
        with dissolve
        c00 "So you really did have thousands of ROBUX..."
        c00 "Actually, you had millions..."
        hide girl7 (14)
        show girl7 (10):
            xpos 400
            zoom 0.6
        c00 "I guess..."
        hide girl7 (10)
        show girl7 (12):
            xpos 400
            zoom 0.6
        c00 "I'M SORRY MASTER!!!!!"
        kristikmind "{i} WTF?????"
        c00 "I WON'T EVER DOUBT YOU AGAIN!!!!!!"
        kristik "Umm..."
        kristik "You don't really need to cry..."
        kristik "Like I didn't really care all that much about it..."
        hide girl7 (12)
        show girl7 (10):
            xpos 400
            zoom 0.6
        c00 "Really?"
        kristik "Yeah."
        c00 "...."
        c00 "ok...."
        hide girl7 (10)
        with dissolve
        kristik "Psh. EZ shit. Imma get that one like it's a STEAM giftcard. (99%% of you won't get that reference)"      
        show girl6 (3):
            xpos 400
            zoom 0.6
        with dissolve
        c410 "..."
        kristik "Uh...?"
        hide girl6 (3)
        with dissolve
        kristik "Ok... then..."
        kristikmind "{i}That one is a bit weird..."
        kristikmind "{i}Not gon mess with that one either..."
        #===========================================================================
        # play phone ringing
        #===========================================================================   
        play sound "audio/notification.mp3"
        $ renpy.pause(2,hard=True)

        kristik "Hello?" 
        show aaron_11_1 onlayer mcsprite:
            xpos -80
            ypos 490
            zoom 0.4
        aaron "Good start."          
        hide aaron_11_1 onlayer mcsprite       
        kristik "Good start for ... what?"
        show aaron_11_1 onlayer mcsprite:
            xpos -80
            ypos 490
            zoom 0.4
        aaron "We've got several cameras within the house so we can monitor the experiment."          
        hide aaron_11_1 onlayer mcsprite            
        kristik "WHAT?!?!?!? YOU'RE WATCHING ME?!??!"
        show aaron_11_1 onlayer mcsprite:
            xpos -80
            ypos 490
            zoom 0.4
        aaron "Yeah. Duh."          
        hide aaron_11_1 onlayer mcsprite            
        kristik "WDYM DUH?!?!?!?!?"
        show aaron_11_1 onlayer mcsprite:
            xpos -80
            ypos 490
            zoom 0.4
        aaron "Shut yo bitch ass up." 
        aaron "This is PIVOTAL in this experiment; monitoring."
        hide aaron_11_1 onlayer mcsprite  
        kristik "But... what if... I fuck???!"
        show aaron_11_1 onlayer mcsprite:
            xpos -80
            ypos 490
            zoom 0.4
        aaron "Well we'll have to monitor your fucking skills as well."
        hide aaron_11_1 onlayer mcsprite  
        kristik "YOU'RE GONNA WATCH ME FUCK BITCHES??!!!"
        show aaron_11_1 onlayer mcsprite:
            xpos -80
            ypos 490
            zoom 0.4        
        aaron "That isn't until later so do not worry about that for now."
        aaron "Anyways, have fun and enjoy your new life."
        hide aaron_11_1 onlayer mcsprite  
        #===========================================================================
        # play phone hangup sound
        #===========================================================================   
        play sound "audio/iphonehangup.ogg"
        $ renpy.pause(2,hard=True)         
        kristik "Bruh...."   
        kristik "They're gonna watch me...."
        kristik "I'm just... I'm just gonna go to bed."
        kristik "I'm too tired to deal with this shit."
        stop music fadeout 2.0
        hide niceroom
        with dissolve
        $ show_quick_menu = False
        window hide 
        with dissolve 
        $ renpy.pause(2,hard=True)
        play sound "audio/dawnofthefirstday.ogg"
        show day1
        $ renpy.pause(5,hard=True)
        hide day1
        with dissolve
        $ renpy.pause(2,hard=True)
        show niceroom2
        with dissolve
        $ show_quick_menu = True
        window show
        with dissolve   
        play music "audio/Riddle Joker Original Soundtrack OST Perfect Girl Instrumental-(128kbps) intro.ogg"
        queue music "audio/Riddle Joker Original Soundtrack OST Perfect Girl Instrumental-(128kbps).ogg"
        kristik "Day 1 to get some bitches..."
        kristik "Wonder what I should do...?" 
        kristik "Maybe... I should cook them something!"
        kristik "But what to make?"
        $ show_quick_menu = False
        window hide          
        menu:
            "Fat smelly Indian curry":
                $ show_quick_menu = True
                window show
                kristik "MAAAannn let's make a FATASS INDIAN CURRY FIRST THING IN THE MORNING!!!"
                #===========================================================================
                # play fridge opening sound
                #===========================================================================
                $ renpy.pause(2,hard=True)         
                show girl7 (9):
                    xpos 400
                    zoom 0.6
                with dissolve
                hide girl7 (9)
                show girl7 (13):
                    xpos 400
                    zoom 0.6
                c00 "What are you doing?"     
                hide girl7 (13)
                show girl7 (9):
                    xpos 400
                    zoom 0.6
                kristik "I'm making a FATASS CURRY BROOOO!!!"  
                stop music
                play sound "audio/gunload_Master.wav"
                show gun onlayer misc:
                    xpos 600
                    ypos 400 
                    zoom 0.5    
                $ renpy.pause(0.8,hard=True)                                                                        
                kristik "YO WHAT THE FUCK IS THE GUN FOR??!?!!"
                hide girl7 (9)
                show girl7 (13):
                    xpos 400
                    zoom 0.6
                c00 "I hate curry."        
                #===========================================================================================================================================================================
                # INSERT GUN SHOOTING SOUNDS
                #===========================================================================================================================================================================
                play sound "audio/awp.mp3"
                show white     
                hide girl7 (13)                    
                hide gun onlayer misc
                hide niceroom2
                $ renpy.pause(1,hard=True)     
                $ show_quick_menu = False
                window hide
                with dissolve
                $ renpy.pause(2,hard=True)  
                narrator "Kristik's skull was fractured in 17 places due to bullet ricochet."
                narrator "He slowly bled out from the back of his head."
                narrator "{b}Bad ending 7/21{/b}"
                if (persistent.endingFinished7 < 1):
                    $ persistent.endingFinished7 += 1
                elif (persistent.endingFinished7 >= 1):
                    pass
                else:
                    narrator "PERSISTENT DATA FAILURE FOR SECTION 16898. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                    $ renpy.quit()
                window hide
                with dissolve
                $ renpy.pause(2,hard=True) 
                $ MainMenu(confirm=False)()                    
            "Light Breakfast":
                $ EXPc00 += 1
                $ EXPc410 += 1
                $ EXPc45 += 1
                $ EXPc556 += 1
                $ show_quick_menu = True
                window show
                kristik "Maybe just some eggs and bacon will do."
                #===========================================================================
                # play fridge opening sound
                #===========================================================================
                $ renpy.pause(2,hard=True)         
                show girl7 (9):
                    xpos 400
                    zoom 0.6
                with dissolve
                hide girl7 (9)
                show girl7 (13):
                    xpos 400
                    zoom 0.6
                c00 "What are you doing?"     
                hide girl7 (13)
                show girl7 (9):
                    xpos 400
                    zoom 0.6
                kristik "I'm making breakfast."  
                hide girl7 (9)
                show girl7 (13):
                    xpos 400
                    zoom 0.6
                c00 "We're maids for a reason! You don't need to cook yourself."     
                c00 "That's literally our job!"
                hide girl7 (13)
                show girl7 (9):
                    xpos 400
                    zoom 0.6
                kristik "Well I mean I consider you guys more like friends than maids to be honest..."
                hide girl7 (9)
                show girl7 (14):
                    xpos 400
                    zoom 0.6
                c00 "You only consider us as... friends?"
                hide girl7 (14)
                show girl7 (9):
                    xpos 400
                    zoom 0.6    
                kristik "ummm.. I guess?"                
                hide girl7 (9)
                show girl7 (13):
                    xpos 400
                    zoom 0.6
                c00 "Whatever! Just sit down and I'll do something instead."
                hide girl7 (13)
                show girl7 (9):
                    xpos 400
                    zoom 0.6
                kristik "Sure why not.." 
                hide girl7 (9)
                with dissolve
                kristik "I forgot they were considered my ''maids''"
                kristik "Maybe that means I can do some NTR ON EM!!! YEAH!!!!!!!!!!!!!!!!!!"    
                show girl4 (11):
                    xpos 400
                    zoom 0.6 
                with dissolve
                c45 "Ummm... what is an ''NTR''???"
                kristikmind "{i}Oh shit... I said that out loud..."    
                show girl5 (13):
                    xpos 800
                    zoom 0.6
                with dissolve
                c556 "NTR huh??"
                hide girl5 (13)
                show girl5 (11):
                    xpos 800
                    zoom 0.6
                kristikmind "{i}Fuck it's that weird ass one!!"   
                c45 "What the heck is that?"
                hide girl5 (11)
                show girl5 (12):
                    xpos 800
                    zoom 0.6                
                c556 "Well... it's-"
                kristik "I'm gonna have to interrupt you there."
                hide girl5 (12)
                with dissolve
                hide girl4 (11)
                show girl4 (13):
                    xpos 400
                    zoom 0.6
                c45 "I don't really understand. What is it??? Just tell me!!"
                hide girl4 (13)
                show girl4 (8):
                    xpos 400
                    zoom 0.6    
                kristik "It's..... it's uhh.h....."
                $ show_quick_menu = False
                window hide  
                menu:
                    "''It stands for Nuclear Thermal Rocket. I just wanted to make a nuclear ICBM.''":
                        $ EXPc00 += 1 
                        $ EXPc45 += 1
                        $ show_quick_menu = True
                        window show
                        kristik "It stands for Nuclear Thermal Rocket. I just wanted to make a nuclear ICBM."
                        hide girl4 (8)
                        show girl4 (13):
                            xpos 400
                            zoom 0.6  
                        c45 "That's it??!! Oh come on that's so lame!"
                        kristikmind "{i}how tf is that even lame??!"
                        show girl7 (13) onlayer mcsprite:
                            ypos 450
                            xpos -15
                            zoom 0.5
                        c00 "It's ready!"
                        hide girl7 (13) onlayer mcsprite
                        hide girl4 (13)
                        show girl4 (8):
                            xpos 400
                            zoom 0.6    
                        kristik "Looks like my food is ready so cya!!!!!!"
                        hide girl4 (8)
                        with dissolve
                        jump chiesterPartThree                        
                    "''It's uhh... short for Netorare which means to cheat on someone and fuck em brainless!!!''":      
                        $ EXPc410 += 1  
                        $ EXPc556 += 1
                        $ show_quick_menu = True
                        window show
                        kristik "It's uhh... short for Netorare which means to cheat on someone and fuck em brainless!!!"
                        hide girl4 (8)
                        show girl4 (14):
                            xpos 400
                            zoom 0.6   
                        c45 "W-WHAT??!!! YOU WERE GONNA DO THAT TO US!??!?!?!"       
                        show girl5 (13):
                            xpos 800
                            zoom 0.6
                        with dissolve  
                        c556 "I personally don't mind all that much... hehe..."      
                        kristikmind "{i} Ok... kinda weird that the GIRL likes NTR..." 
                        show girl7 (13) onlayer mcsprite:
                            ypos 450
                            xpos -15
                            zoom 0.5
                        c00 "It's ready!"
                        hide girl7 (13) onlayer mcsprite
                        kristik "Yeah... so uh.... I'mma go now..."
                        hide girl4 (14)
                        hide girl5 (13)
                        with dissolve
                        jump chiesterPartThree                        
        label chiesterPartThree:
            show girl7 (13):
                xpos 400
                zoom 0.6
            with dissolve
            c00 "Please sit."
            kristik "Ok."
            hide girl7 (13)
            hide niceroom2
            show food1
            with dissolve
            show girl7 (13) onlayer mcsprite:
                ypos 450
                xpos -15
                zoom 0.5
            with dissolve
            c00 "What do you think?"  
            hide girl7 (13) onlayer mcsprite   
            $ show_quick_menu = False
            window hide
            menu:
                "''It looks like absolute shit. Where's the indian??!''":
                    $ show_quick_menu = True
                    window show               
                    kristik "It looks like absolute shit. Where's the indian??!"
                    stop music
                    play sound "audio/gunload_Master.wav"
                    $ renpy.pause(0.8,hard=True)                                                                        
                    kristik "WHY DO I FEEL A GUN TO MY HEAD???!"
                    show girl7 (13) onlayer mcsprite:
                        ypos 450
                        xpos -15
                        zoom 0.5
                    c00 "Nobody shittalks my cooking."   
                    play sound "audio/awp.mp3"
                    hide girl7 (13) onlayer mcsprite
                    show white                       
                    hide gun onlayer misc
                    hide food1
                    $ renpy.pause(1,hard=True)     
                    $ show_quick_menu = False
                    window hide
                    with dissolve
                    $ renpy.pause(2,hard=True)  
                    narrator "Kristik was instantly killed due to a fatal gunshot wound from the back of the head, penetrating through his brain and exiting through his left eye."
                    narrator "{b}Bad ending 18/21{/b}"
                    if (persistent.endingFinished18 < 1):
                        $ persistent.endingFinished18 += 1
                    elif (persistent.endingFinished18 >= 1):
                        pass
                    else:
                        narrator "PERSISTENT DATA FAILURE FOR SECTION 17107. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                        $ renpy.quit()
                    window hide
                    with dissolve
                    $ renpy.pause(2,hard=True) 
                    $ MainMenu(confirm=False)()                                          
                "''YOoooo shit lookin epic!!!''":   
                    $ show_quick_menu = True
                    window show     
                    kristik "YOoooo shit lookin epic!!!"
                    show girl7 (14) onlayer mcsprite:
                        ypos 450
                        xpos -15
                        zoom 0.5
                    c00 "Glad to hear that somebody appreciates the work I put into this house."
                    hide girl7 (14) onlayer mcsprite
                    hide food1
                    with dissolve
                    $ show_quick_menu = False
                    window hide 
                    with dissolve 
                    $ renpy.pause(2,hard=True)
                    show niceroom2
                    with dissolve
                    $ show_quick_menu = True
                    window show
                    with dissolve 
                    kristik "ShhEsh.... I'm pooped."
                    kristik "I'm hella full."
                    show girl7 (9):
                        xpos 400
                        zoom 0.6      
                    with dissolve
                    hide girl7 (9)
                    show girl7 (13):
                        xpos 400
                        zoom 0.6
                    c00 "Next up is gym."           
                    hide girl7 (13)
                    show girl7 (9):
                        xpos 400
                        zoom 0.6
                    kristik "WHAT?!??!?! GYM!??!??!?!"
                    kristik "Sorry... uh.. my MOM SAYS I CANNOT GO TO GYM SO I CANT BYE!!!!"
                    hide girl7 (9)
                    show girl7 (10):
                        xpos 400
                        zoom 0.6
                    c00 "Are you 12 years old? Your mom does not dictate your every decision."
                    c00 "Besides, it's a home gym."
                    hide girl7 (10)
                    show girl7 (16):
                        xpos 400
                        zoom 0.6      
                    c00 "So you're not going anywhere until you turn that ''b'' shaped body into an ''l''!"
                    kristikmind "{i} Interesting set of vocabulary I guess...."
                    hide girl7 (16)
                    show girl7 (17):
                        xpos 400
                        zoom 0.6     
                    kristik "Fine... I'll hit the gym."
                    hide girl7 (17)
                    show girl7 (21):
                        xpos 400
                        zoom 0.6  
                    c00 "I'll go as well then."
                    hide girl7 (21)
                    show girl7 (17):
                        xpos 400
                        zoom 0.6  
                    kristik "WHAT?!?!?!"
                    kristikmind "{i}She's totally gonna make me do like 100 push ups in 2 minutes or some shit!!!"
                    hide girl7 (17)
                    show girl7 (21):
                        xpos 400
                        zoom 0.6  
                    c00 "Is there an issue?"                                                                                 
                    hide girl7 (21)
                    show girl7 (17):
                        xpos 400
                        zoom 0.6  
                    kristik "Nononooonooo... it's just that I'm fully capable of going by myself. As you said, I'm not 12 years old."
                    hide girl7 (17)
                    show girl7 (21):
                        xpos 400
                        zoom 0.6  
                    c00 "Well I would like to see how well you are at doing physical exercise."
                    hide girl7 (21)
                    show girl7 (17):
                        xpos 400
                        zoom 0.6  
                    kristik "Look, there's no point in doing that really. I'm like 800 pounds so I can theoretically deadlift like 1200 pounds."
                    hide girl7 (17)
                    show girl7 (24):
                        xpos 400
                        zoom 0.6  
                    c00 "Do you really take it as an issue that I come with you?"
                    hide girl7 (21)
                    show girl7 (17):
                        xpos 400
                        zoom 0.6  
                    $ show_quick_menu = False
                    window hide
                    menu:        
                        "''Yes.''":
                            $ show_quick_menu = True
                            window show                        
                            kristik "Yes."
                            stop music
                            play sound "audio/gunload_Master.wav"                             
                            show gun onlayer misc:
                                xpos 600
                                ypos 400 
                                zoom 0.5    
                            $ renpy.pause(0.8,hard=True)                                                                        
                            kristik "BRO HOW MANY TIMES ARE YOU GONNA PULL A GUN ON ME??!?!?!"    
                            hide girl(17)
                            show girl7 (22):
                                xpos 400
                                zoom 0.6  
                            c00 "There's many more possibilities..."                            
                            #===========================================================================================================================================================================
                            # INSERT GUN SHOOTING SOUNDS
                            #===========================================================================================================================================================================
                            play sound "audio/awp.mp3"
                            show white     
                            hide girl7 (22)                    
                            hide gun onlayer misc
                            hide niceroom2
                            $ renpy.pause(1,hard=True)     
                            $ show_quick_menu = False
                            window hide
                            with dissolve
                            $ renpy.pause(2,hard=True)  
                            narrator "Kristik was fatally wounded due to a 9x19mm Pst GZH bullet achieving the 1%% Head-eyes damage spot."
                            narrator "He was instantly killed."
                            narrator "{b}Bad ending 17/21{/b}"
                            if (persistent.endingFinished17 < 1):
                                $ persistent.endingFinished17 += 1
                            elif (persistent.endingFinished17 >= 1):
                                pass
                            else:
                                narrator "PERSISTENT DATA FAILURE FOR SECTION 17248. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                                $ renpy.quit()
                            window hide
                            with dissolve
                            $ renpy.pause(2,hard=True) 
                            $ MainMenu(confirm=False)()                              
                        "''No... it's just that...''":
                            $ show_quick_menu = True
                            window show                          
                            kristik "No... it's just that..."      
                            kristik "I.. uh..."
                            kristik "It's kinda embarrassing."    
                            hide girl7 (17)
                            show girl7 (21):
                                xpos 400
                                zoom 0.6        
                            c00 "How so?"
                            hide girl7 (21)
                            show girl7 (17):
                                xpos 400
                                zoom 0.6  
                            kristik "It's kinda hard to explain the psychology behind it... but it's just kinda weird to do things when other people are around you, y'know?" 
                            hide girl(17)
                            show girl7 (22):
                                xpos 400
                                zoom 0.6  
                            c00 "I have no idea what you're talking about."
                            hide girl7 (22)
                            show girl7 (17):
                                xpos 400
                                zoom 0.6   
                            show girl5 (13) onlayer mcsprite:
                                ypos 450
                                xpos -15
                                zoom 0.5    
                            c556 "Heyyyyy!!!"
                            hide girl5 (13) onlayer mcsprite
                            kristik "???"
                            hide girl7 (17)
                            with dissolve
                            show girl5 (13):
                                xpos 700
                                zoom 0.6    
                            show girl6 (3):
                                xpos 200
                                zoom 0.6  
                            with dissolve
                            c556 "Wanna go out with uuuuuuuuuus???"
                            kristik "Umm... I gotta-"
                            kristikmind "{i} Wait, I don't HAVE to hit the gym!"    
                            hide girl5 (13)
                            show girl5 (16):
                                xpos 700
                                zoom 0.6
                            show girl7 (16) onlayer mcsprite:
                                ypos 450
                                xpos -15
                                zoom 0.5
                            c00 "No he cannot!"
                            hide girl7 (16) onlayer mcsprite
                            kristik "Fuck..."      
                            hide girl5 (16)
                            hide girl6 (3)
                            with dissolve
                            show girl7 (16):
                                xpos 200
                                zoom 0.6 
                            show girl4 (8):
                                xpos 700
                                zoom 0.6                                              
                            with dissolve
                            c00 "You need to get some gains first!"
                            hide girl4 (8)
                            show girl4 (13):
                                xpos 700
                                zoom 0.6
                            c45 "Yeah! Definitely!"
                            hide girl4 (13)
                            hide girl7 (16)
                            with dissolve
                            show girl5 (13):
                                xpos 700
                                zoom 0.6    
                            show girl6 (3):
                                xpos 200
                                zoom 0.6  
                            with dissolve
                            c556 "Don't listen to them. They're weird."
                            hide girl5 (13)
                            show girl5 (16):
                                xpos 700
                                zoom 0.6
                            show girl7 (16) onlayer mcsprite:
                                ypos 450
                                xpos -15
                                zoom 0.5
                            c00 "Who are you calling weird?"   
                            hide girl7 (16) onlayer mcsprite
                            kristikmind "{i}Shits is getting out of hand really quickly..."
                            hide girl5 (16)
                            show girl5 (12):
                                xpos 700
                                zoom 0.6
                            c556 "Well there's your problem. If you weren't so weird you would know exactly who I'm calling weird LOLLOLOLOLO!!!!"
                            hide girl6 (3)
                            show girl6 (7):
                                xpos 200
                                zoom 0.6
                            c410 "Let's just ask the man himself and we'll see who he chooses."
                            kristik "Shit..."
                            c556 "Good idea! Though, I already know the answer, it's totally us."
                            hide girl6 (7)
                            hide girl5 (12)
                            with dissolve
                            $ show_quick_menu = False
                            window hide      
                            menu:
                                "Get some gains at the gym": 
                                    $ show_quick_menu = True
                                    window show                               
                                    kristik "You know what, I'll get some gains."     
                                    show girl7 (16):
                                        xpos 200
                                        zoom 0.6 
                                    show girl4 (8):
                                        xpos 700
                                        zoom 0.6                                              
                                    with dissolve
                                    c00 "See? I knew it!"
                                    c00 "Let's just go and leave these guys!"
                                    hide girl4 (8)
                                    hide girl7 (16)
                                    with dissolve
                                    show girl5 (18):
                                        xpos 700
                                        zoom 0.6    
                                    show girl6 (3):
                                        xpos 200
                                        zoom 0.6  
                                    with dissolve
                                    c556 "What??? That traitor!"
                                    hide girl6 (3)
                                    show girl6 (2):
                                        xpos 200
                                        zoom 0.6
                                    c410 "It's okay. We'll find the next victim later."
                                    hide girl6 (2)
                                    show girl6 (3):
                                        xpos 200
                                        zoom 0.6  
                                    hide girl5 (18)
                                    show girl5 (16):
                                        xpos 700
                                        zoom 0.6                  
                                    c556 "It'll be a while before we find a new person..."
                                    hide girl6 (3)
                                    show girl6 (2):
                                        xpos 200
                                        zoom 0.6
                                    c410 "It's fine. We can wait as long as we want anyways."
                                    stop music fadeout 2.0
                                    hide girl6 (2)
                                    hide girl5 (16)
                                    with dissolve
                                    hide niceroom2
                                    with dissolve
                                    $ show_quick_menu = False
                                    window hide 
                                    with dissolve 
                                    $ renpy.pause(2,hard=True)
                                    jump gym
                                "Hang out":
                                    $ show_quick_menu = True
                                    window show                               
                                    kristik "I'd rather hang out."      
                                    show girl5 (13):
                                        xpos 700
                                        zoom 0.6    
                                    show girl6 (3):
                                        xpos 200
                                        zoom 0.6  
                                    with dissolve
                                    c556 "See? I told you! Now let's go!"
                                    hide girl6 (3)
                                    hide girl5 (13)
                                    with dissolve
                                    show girl7 (16):
                                        xpos 200
                                        zoom 0.6 
                                    show girl4 (8):
                                        xpos 700
                                        zoom 0.6                                              
                                    with dissolve
                                    c00 "Tch. He's just going to get fatter by the day."
                                    stop music fadeout 2.0
                                    hide girl4 (8)
                                    hide girl7 (16)
                                    with dissolve
                                    hide niceroom2
                                    with dissolve
                                    $ show_quick_menu = False
                                    window hide 
                                    with dissolve 
                                    $ renpy.pause(2,hard=True)
                                    jump dungeon                                                                                                          

        label gym:
            show BG048
            with dissolve
            play music "audio/Sanoba Witch OST - Sweet Sweet Alice(InstVer.)-128k intro.ogg"
            queue music "audio/Sanoba Witch OST - Sweet Sweet Alice(InstVer.)-128k.ogg"
            $ show_quick_menu = True
            window show
            with dissolve 
            show girl7 (13):
                xpos 200
                zoom 0.6 
            show girl4 (8):
                xpos 700
                zoom 0.6                                              
            with dissolve
            c00 "Now, let's do one pushup."
            hide girl7 (13)
            show girl7 (9):
                xpos 200
                zoom 0.6
            kristik "Wow... starting off challenging ay?"
            hide girl4 (8)
            show girl4 (11):
                xpos 700
                zoom 0.6
            hide girl7 (9)
            show girl7 (10):
                xpos 200
                zoom 0.6 
            c00 ".... Is that seriously a challenge to you?"          
            kristik "Hahaha.... No... I'm totally joking...?"
            c00 "Look, it's fine if you can't do a single pushup... well actually for your age and gender it really ISN'T okay to be healthy..."
            kristik "This is exactly what I was talking about!"
            c00 "Alright... we got tons of work to do..."
            hide girl7 (10)
            hide girl4 (11)
            with dissolve
            hide BG048
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)            
            "{i}18 hours later..."
            $ renpy.pause(2,hard=True)
            show BG048
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve 
            show girl7 (13):
                xpos 200
                zoom 0.6 
            show girl4 (11):
                xpos 700
                zoom 0.6                                              
            with dissolve
            c00 "Well... you can do 2 at least. It is an improvement."
            hide girl7 (13)
            show girl7 (9):
                xpos 200
                zoom 0.6
            kristik "Yeah.... but... holy... shit.... im so.... trishjidfujhbnsdjkgbnfg....."
            hide girl7 (9)
            show girl7 (10):
                xpos 200
                zoom 0.6
            c00 "Jeez. Fell asleep..."
            c45 "He's gonna need some rest otherwise he'll probably die..."
            c00 "Yeah..."
            stop music fadeout 2.0
            hide girl7 (10)
            hide girl4 (11)
            with dissolve
            hide BG048
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)
            play sound "audio/dawnofthefirstday.ogg"
            show day2
            $ renpy.pause(5,hard=True)
            hide day2
            with dissolve
            $ renpy.pause(2,hard=True)
            show niceroom3
            play music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k intro.ogg"
            queue music "audio/Sanoba Witch OST  - Juu-Jitsu Seikatsu-320k.ogg"
            with dissolve
            $ show_quick_menu = True
            window show
            with dissolve  
            kristik "Holy shit..."
            kristik "My entire body still feels numb...."
            kristik "I feel like I won't be able to even stand up..."
            #========================================================================================================================================================================
            #PLAY PHONE RINGING SOUND
            #========================================================================================================================================================================
            play sound "audio/notification.mp3"
            $ renpy.pause(2,hard=True)
            kristik "heellOO???"
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            aaron "Jesus you sound terrible."
            aaron "That exercise was a bit too much wasn't it?"
            hide aaron_11_1 onlayer mcsprite              
            kristik "Yeah.... holy shit my body feels like it doesn't even exist... my muscles are just so numb."
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            aaron "Well anyways, I'd like to tell you that the experiment has failed."
            hide aaron_11_1 onlayer mcsprite              
            kristik "What?!?!! How??!"                        
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            aaron "Your goal was to get ALL the bitches and not just 2 of em!"
            hide aaron_11_1 onlayer mcsprite   
            kristik "What happened to... the other 2...?"
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            aaron "They probably didn't like the fact that you wanted to get some gains instead of hanging out with them. So they straight up left."
            aaron "I couldn't convince them to go back. Which means..."
            aaron "This experiment failed and is now terminated."
            hide aaron_11_1 onlayer mcsprite  
            kristik "WHAT>???! WHAT THE HELL???"
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            aaron "Seeing as how you also can't afford to pay back the loans I took out for this whole ordeal... we're going to have to talk about another form of payment."      
            hide aaron_11_1 onlayer mcsprite  
            kristik "Wait what..??? '''other form''' of payment???"
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            stop music fadeout 2.0
            aaron "That's right. You'll pay with your own life."
            hide aaron_11_1 onlayer mcsprite  
            play music "audio/Sanoba Witch OST - Fushigi-na Chikara-(128kbps).ogg"
            kristik "HUH?!??!?!?!"
            show aaron_11_1 onlayer mcsprite:
                xpos -80
                ypos 490
                zoom 0.4        
            aaron "Remember, I still have a bounty over your head this whole time. I was still going to kill you."
            aaron "It was nice knowing ya."
            aaron "We got our prviate military company USEC storming your location in a short while."
            aaron "So I'll see you at your grave I guess."   
            hide aaron_11_1 onlayer mcsprite    
            #========================================================================================================================================================================
            #PLAY PHONE HANGING UP SOUND
            #========================================================================================================================================================================
            play sound "audio/iphonehangup.ogg"
            $ renpy.pause(2,hard=True)   
            kristik "ARE YOU... SERIOUS RIGHT NOW???!?!?!?"
            show girl7 (13):
                xpos 200
                zoom 0.6 
            show girl4 (11):
                xpos 700
                zoom 0.6                                              
            with dissolve
            c00 "Is everything alright?"
            hide girl7 (13)
            show girl7 (9):
                xpos 200
                zoom 0.6
            kristik "NO!!! WE GOTTA LEAVE RIGHT NOW!!!"    
            hide girl7 (9)
            show girl7 (10):
                xpos 200
                zoom 0.6 
            c00 "The hell is going on?"  
            kristik "WE GOTTA MOVE OUTTA THE COUNTRY... START A NEW LIFE IN INDIA... CHANGE OUR IDENTITIES..."
            c00 "Do you care to explain what is going on?"
            kristik "There's not much time, a bunch of PMCs are gonna storm this house and kill us all!!!"
            hide girl4 (11)
            show girl4 (14):
                xpos 700
                zoom 0.6
            c45 "WHAT?!?!??!"
            kristik "We just gotta get outta here!!!"
            hide girl4 (14)
            hide girl7 (10)
            with dissolve
            hide niceroom3
            with dissolve
            $ renpy.pause(1,hard=True)
            show nicehouse
            with dissolve
            kristik "Ok... it looks like the PMCs aren't here."
            kristik "Now... let's just get the fuck outta here!!"
            stop music fadeout 2.0
            hide nicehouse
            with dissolve
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)
            "Kristik and his two friends would exfiltrate to India and reside their till their deaths."
            "The PMCs sent by Aaron to kill the 3 were not able to locate them."
            "They all shared 82 children by the time of their deaths."
            "{b}Neutral ending 20/21" 
            if (persistent.endingFinished20 < 1):
                $ persistent.endingFinished20 += 1
            elif (persistent.endingFinished20 >= 1):
                pass
            else:
                narrator "PERSISTENT DATA FAILURE FOR SECTION 17660. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                $ renpy.quit()
            $ show_quick_menu = False
            window hide              
            $ renpy.pause(2,hard=True)
            $ MainMenu(confirm=False)()                          

        label dungeon:
            show BG080B
            with dissolve
            play music "audio/Riddle Joker Original Soundtrack OST Secret Lab Instrumental-(128kbps).ogg"
            $ show_quick_menu = True
            window show
            with dissolve 
            kristik "Where are we going?"
            show girl5 (13) onlayer mcsprite:
                ypos 450
                xpos -15
                zoom 0.5  
            c556 "You'll see. But first, drink this."
            hide girl5 (13) onlayer mcsprite
            kristik "The hell is that???"
            show girl5 (13) onlayer mcsprite:
                ypos 450
                xpos -15
                zoom 0.5  
            c556 "It's Sprite!"
            hide girl5 (13) onlayer mcsprite
            kristik "Ummm... okay..."
            #===========================================================================================================================================================================
            # INSERT ROBLOX SLURPING SOUNDS
            #===========================================================================================================================================================================
            $ renpy.pause (2,hard=True)
            kristikmind "{i}Yuck! This shit tasted nasty!"
            kristikmind "{i} I think i'm getting lightheaded...."
            stop music fadeout 4.0
            hide BG080B
            with Pixellate(2,5)
            $ show_quick_menu = False
            window hide 
            with dissolve 
            $ renpy.pause(2,hard=True)
            show dungeon
            with dissolve
            play sound "audio/darkambience.ogg" loop
            $ show_quick_menu = True
            window show
            with dissolve
            kristik "Awhh god..."
            kristik "WAHT THE FUCK!?!?!? WHERE AM I !?!?@?!?@>!?@>?!@>"
            show girl5 (13):
                xpos 700
                zoom 0.6    
            show girl6 (3):
                xpos 200
                zoom 0.6  
            with dissolve
            c556 "Welcome to our little dungeon!!!"
            kristik "DUNGEON!>?!>?!?!??!@?!>@?>!?@>!"
            hide girl5 (13)
            show girl5 (10):
                xpos 700
                zoom 0.6
            kristik "THE FUCK IS GOIN ON?!!! WHY AM I CHAINED TO THE WALL!??!?!"
            hide girl5 (10)
            show girl5 (12):
                xpos 700
                zoom 0.6
            c556 "Oh stop it... no need to get so fight-or-flighty. We'll take good care of you, we promise."
            kristik "THIS ISN'T PART OF THE PLAN!!! WHERE IS AARON???!! IS HE INVOLVED IN THIS?!?"
            c556 "Oh... that guy... yeah we KILLED him."
            kristik "WAHTHJATAT!?@?!>@?!>@?>"
            hide girl5 (12)
            show girl5 (19):
                xpos 550
                ypos -30
                zoom 0.6     
            c556 "Yup! Teehee~"
            kristik "DONT FUCKIN TEEHEE ME BITCH!!"
            kristik "GET ME OUTTA HERE!!!"
            hide girl5 (19)
            show girl5 (21):
                xpos 550
                ypos -30
                zoom 0.6              
            c556 "Nope~!"
            c556 "We hope you enjoy your permanent stay!"
            c556 "You're going to love it... ~~~"
            stop sound fadeout 2.0
            hide girl5 (21)
            hide girl6 (3)
            with dissolve
            hide dungeon
            with dissolve
            $ renpy.pause (2,hard=True)
            "Kristik would spend the rest of his life in the love dungeon."
            "His record currently is 88 nuts /per day."
            "{b}Neutral ending 19/21" 
            if (persistent.endingFinished19 < 1):
                $ persistent.endingFinished19 += 1
            elif (persistent.endingFinished19 >= 1):
                pass
            else:
                narrator "PERSISTENT DATA FAILURE FOR SECTION 17759. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
                $ renpy.quit()
            $ show_quick_menu = False
            window hide              
            $ renpy.pause(2,hard=True)
            $ MainMenu(confirm=False)()              
    return

label noHoesEnding:
    $ show_quick_menu = False
    window hide 
    with dissolve 
    $ renpy.pause(2,hard=True)
    show BG080N
    with dissolve
    $ show_quick_menu = True
    window show
    with dissolve
    kristik "Ughhh..."
    jason "What's wrong Kristik?"
    hide BG080N
    show BG039n
    with dissolve
    show kyle (5):
        xpos 700
        ypos 20
        zoom 0.6
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    show kevin (14):
        xpos 0
        zoom 0.6     
    with dissolve
    play music "audio/Sabona Witch OST - Chotto Ennui-128k.ogg"
    kristik "Nothing..."
    kristik "It's just for some reason, the girls I talked to aren't responding to my texts anymore."
    kristik "They're not even being read!"
    hide jason (9)
    show jason (11):
        xpos 400
        ypos 20
        zoom 0.6   
    jason "Ugh... Bitches these days..."
    hide jason (11)
    show jason (4):
        xpos 400
        ypos 20
        zoom 0.6
    jason "It's why I hang out with the boys."
    kristik "You're right..."
    kristik "They didn't even know me!"
    kristik "Why would they even try to talk to me so much?!"
    hide jason (4)
    show jason (10):
        xpos 400
        ypos 20
        zoom 0.6
    jason "They were probably after that cock."
    hide jason (10)
    show jason (4):
        xpos 400
        ypos 20
        zoom 0.6
    jason "But they found out that you don't even have one"
    kristik "Ughhh....."
    hide jason (4)
    show jason (9):
        xpos 400
        ypos 20
        zoom 0.6
    jason "No need to sweat it, though."
    jason "We'll defeat Aaron and Wesley without those bitches!"
    kristik "Yeah. You're right!"
    kristik "I don't need pussy to be successful in life!"
    hide jason (9)
    show jason (8):
        xpos 400
        ypos 20
        zoom 0.6  
    jason "That's right. All you need is the boys."
    kristik "Yeah.... yeah!"
    kristik "Fuck them hoes!"
    kristik "Don't give a shit about em!!"
    hide jason (8)
    hide kevin (14)
    hide kyle (5)
    show kyle (7):
        xpos 700
        ypos 20
        zoom 0.6   
    show jason (4):
        xpos 400
        ypos 20
        zoom 0.6  
    show kevin (25):
        xpos 0
        zoom 0.6    
    everyone "(laughing)"   
    hide BG039n
    hide jason (4)
    hide kyle (7)
    hide kevin (25)
    show BG080N
    with dissolve
    "Kristik and his friends would prove to be the world's strongest force."
    "They would use their powerful friendship to defeat petty crime and level up their skillsets."
    "All working towards the goal of defeating Wesley Chang and Aaron Kim."
    "Kristik would never touch or interact with another woman."
    "However, none of that mattered to him, as he had: {b}The Boys."
    "{b}No bitches ending 21/21"
    $ show_quick_menu = False
    window hide 
    with dissolve 
    stop music fadeout 2.0
    hide BG080N
    with dissolve
    $ renpy.pause(3,hard=True)
    if (persistent.endingFinished21 < 1):
        $ persistent.endingFinished21 += 1
    elif (persistent.endingFinished21 >= 1):
        pass
    else:
        narrator "PERSISTENT DATA FAILURE FOR SECTION 16970. CHECK OFFSETS. PLEASE CONTACT DEVELOPER IF YOU ARE EXPERIENCING THIS ISSUE."
        $ renpy.quit()
    $ MainMenu(confirm=False)()  

label secretEnding:
    "Thank you for playing the entire game all the way through."
    "3 months of hard work for this game has (hopefully) paid off."
    "I don't get paid for this, and I really should have been, but whatever."
    "As a token of my appreciation, here's a steam gift card code: XXXXX-XXXXX-XXXXX-XXXX"
    "You'd better hope that nobody has already taken this code."
    "Each update to this game will generate a new steam gift code."
    "But anyways, thanks for playing!"
    $ MainMenu(confirm=False)()  