
#image idledance = Movie(play="images/dtyd.webm",size=(1280,720),xalign=0.5,yalign=0.5)


image aine_attack1= Movie(play="images/p1_an/AINE_ATTACK1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_attack2= Movie(play="images/p1_an/AINE_ATTACK2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_attack3= Movie(play="images/p1_an/aine_attack3.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_attack4= Movie(play="images/p1_an/AINE_ATTACK4.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_heal1= Movie(play="images/p1_an/AINE_HEAL1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_heal2= Movie(play="images/p1_an/AINE_HEAL2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_heal3= Movie(play="images/p1_an/AINE_HEAL3.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_idle1= Movie(play="images/p1_an/AINE_IDLE1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_wc= Movie(play="images/p1_an/AINE_WC.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle1= Movie(play="images/p1_an/AINE0HP_IDLE1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle2= Movie(play="images/p1_an/AINE0HP_IDLE2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle3= Movie(play="images/p1_an/AINE0HP_IDLE3.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle4= Movie(play="images/p1_an/AINE0HP_IDLE4.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle5= Movie(play="images/p1_an/AINE0HP_IDLE5.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_attack1= Movie(play="images/p1_an/CJ_ATTACK1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_attack2= Movie(play="images/p1_an/CJ_ATTACK2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_attacked1= Movie(play="images/p1_an/CJ_ATTACKED1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_cast1= Movie(play="images/p1_an/CJ_CAST1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_cast2= Movie(play="images/p1_an/CJ_CAST.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_idle1= Movie(play="images/p1_an/CJ_IDLE1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_idle2= Movie(play="images/p1_an/CJ_IDLE2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cro_attack1= Movie(play="images/p1_an/CRO_ATTACK1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image hostage_attacked1= Movie(play="images/p1_an/HOSTAGE_ATTACKED1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image hostage_attacked2= Movie(play="images/p1_an/HOSTAGE_ATTACKED2.webm", size=(1280,720),xalign=0.5,yalign=0.5)

#label rubyintro:
#    scene black
#    show movie
#
#    play movie "images/dtyd.webm" #If yer shit aint workin it's because of this
#    $ renpy.transition(fade)#optional
#    $ renpy.pause(126, hard=True)# substitute "1" with video length in seconds. Stop players from skipping the video. If you want to allow skipping, remove ", hard=True"
#    return
#lines 1-13, and line 37 are how to do movies
init python:
    import random
    import math


    #Actr Declaration
    #                           Actr(name, atk, defense, hp, mhp, mp, str, mmp, agi, armor, attacks=[], magic={"SPELLNAME":"BUFF OR DMG"}, abilities={"SPELLNAME":"BUFF OR DMG"}, items=[], dice=2) ###dice = 2 means default is 2, that's why enemy has a 3 there.
    Playercharacter = Actr("CJ",0,14,20,20,5,0,5,5,15,["Attack", "Talk"],{"One On One(1MP)":"BUFF","Man Eater(1MP)":"BUFF"})
    Alliedcharacter1 = Actr("Áine",8,16,40,40,0,11,5,4,18,["Attack"],{"Gentle Current(1MP)":"BUFF","Underswell(2MP)":"BUFF","Riptide(3MP)":"BUFF","Wave Crash(3MP)":"DMG"})
    Enemycharacter = Actr("Cro'Dhearg",9,15,60,60,0,14,5,5,18,["Attack"],3)

    def setend(end): #Likely unnecessary, can be trimmed out
        return "END"

    def roundstart():
        end =None
        Playercharacter.mp = Playercharacter.mmp #
        Alliedcharacter1.mp = 0 #
        Playercharacter.isguarding =False
        Alliedcharacter1.isguarding = False



        narrator("Select the amount of MP to allocate.", interact=True)
        #SCALABILITY PROBLEM: Will have to detect what allies one has in the future; 1, 2, 3, whether you have ally X or Y, etcetc.
        while(end != "END"):
             end = renpy.call_screen("mpallocation",Playercharacter ,Alliedcharacter1,end)

        narrator(Playercharacter.name+" now has "+ str(Playercharacter.mp) + " MP" )
        narrator(Alliedcharacter1.name+" now has "+ str(Alliedcharacter1.mp) + " MP" )

    def get_characters_turn():
                narrator("Which character will move?", interact=False) #Get which char will move
                Actr = renpy.display_menu([ (Playercharacter.name, Playercharacter), (Alliedcharacter1.name, Alliedcharacter1)]) #Get which char will move
                while(Actr.turnover == True): #While selected char's turn is over, get which char will move
                    narrator(Actr.name + "Has already gone this turn!")
                    narrator("Which character will move?", interact=False)
                    Actr = renpy.display_menu([ (Playercharacter.name, Playercharacter), (Alliedcharacter1.name, Alliedcharacter1)])
                narrator(Actr.name + "'s turn!'")
                return Actr

    def get_characters_action(Actr, choice):
            action = " "
            if(choice=="Guard"):
                Actr.isguarding = True
                Actr.turnover = True
                narrator("You ready yourself for the enemy's next attack.")
            if(choice!="Guard"):
                action = renpy.call_screen("battlechoice",Actr,choice,random.randrange(0,2),"idle")


            return action

    def playerturn(Actr = None, skipSelect = False):


        if(Actr != None):
            Actr.nompflag = False
        while(Playercharacter.turnover == False or Alliedcharacter1.turnover == False ): #while neither the player nor ally's turns are over
            #renpy.call("rubyintro")
            action = " " #action is declared
            if(skipSelect == False): #If we are not recursed due to using a spell, a talk action, or low mana
                Actr = get_characters_turn() #then get which character's turn it is
            renpy.show_screen("anim",random.randrange(0,2),"idle",Actr)
            choice = renpy.call_screen("battle",Playercharacter,Alliedcharacter1,Enemycharacter,random.randrange(0,2),"idle",Actr) #we get the choice from the battle screen

            action = get_characters_action(Actr,choice) #we get the action from the action screen
            while(action=="b"): #if the player chose "BACK" , do the above again

                choice = renpy.call_screen("battle",Playercharacter,Alliedcharacter1,Enemycharacter,random.randrange(0,2),"idle",Actr)

                action = get_characters_action(Actr,choice)
            if(choice =="Attack"): #if choice was attack
                Actr.attackchoice(action,Enemycharacter) #parse which attack was chosen
            if(choice =="Magic"): #if choice was magic
                Actr.magicchoice(action,Enemycharacter,Playercharacter,Alliedcharacter1) #parse which magic was chosen
            if((choice == "Magic" or action =="Talk" or Actr.nompflag == True)):#if we used a spell, a talk action, or didn't have enough mana for a spell
                playerturn(Actr,True) #then we restart all our previous actions, running playerturn() again, but with the param True as to NOT select whose turn it is
            if(skipSelect == True): #if skipselect is true, then we are recursed; main() - > playerturn() - > playerturn() -> playerturn(), 'return' will return us to the first playerturn()  in all cases.
               return #We are recursed, exit to main function
            Actr.turnover = True #turn is over for this Actor
        Playercharacter.turnover = False #now that both actor's turns are over, we reset their turn flags.
        Alliedcharacter1.turnover = False

    def enemyturn():

        Actr = Enemycharacter
        wavebonus = 0
        target = None
        rand_target = random.randrange(0,2)
        if((rand_target == 0) and (Playercharacter.mp == 0 )):
            target = Alliedcharacter1
        elif(rand_target == 0):
            target = Playercharacter
        if(rand_target ==1):
            target = Alliedcharacter1
        narrator("Enemy is attacking "+target.name+"!")
        choice = "Attack"
        if(choice =="Attack"):
              action = "Attack"
              attack_roll = Actr.attack(action)
              attack_sum = sum(attack_roll) + Actr.atk
              if(target.name == "Áine"):
                wavebonus = target.wavetokens * 2
                target.tidetokens = target.wavetokens
                target.wavetokens = 0
              narrator("Enemy's dice rolls were ["+''.join(str(x)+"," for x in attack_roll)+ "] Plus their ATK of ["+str(Actr.atk) + "] for a total of [" + str(attack_sum ) +"] against "+target.name+"'s '["+str(target.defense+wavebonus)+"] defense.")#Don't worry about it.

              if(attack_sum == Enemycharacter.defense+wavebonus or attack_sum > Enemycharacter.defense+wavebonus): #You hit!
                  narrator("Enemy hits!")
                  dmg_roll = Actr.damage(target)
                  dmg_roll_sum =  (sum(dmg_roll)+Actr.str)
                  final_dmg = dmg_roll_sum - target.armor
                  if(final_dmg < 0):
                       final_dmg = 0
                  narrator("Enemy's dice rolls were ["+''.join(str(x)+"," for x in dmg_roll)+ "] Plus their DMG of ["+str(Actr.str) + "] for a total of [" + str(dmg_roll_sum ) +"] against "+target.name+"'s '["+str(target.armor)+"] armor. Hitting for [" +str(final_dmg)+"]")#Don't worry about it.
                  target.hp -= final_dmg
                  if(Playercharacter.hp <=0):
                    return
                  if(target.isguarding==True):
                    target.isguarding =False
              else: #You miss!
                    narrator("Enemy misses!")

label start: #game starts here

    python:

    #Bando thinks after load, splashscreen, main menu, finaly main menu, lets some option in main menu start a battle
        while(Enemycharacter.hp > 0 and Playercharacter.hp > 0):


            roundstart()
            if(Playercharacter.hp> 0):

                playerturn()
            if(Enemycharacter.hp > 0):
                enemyturn()
    return
