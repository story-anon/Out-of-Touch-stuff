#Is this battle system a jojos reference?

image aine_attack1= Movie(play="images/p1_an/AINE_ATTACK1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_attack2= Movie(play="images/p1_an/AINE_ATTACK2.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_attack3= Movie(play="images/p1_an/aine_attack3.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_attack4= Movie(play="images/p1_an/AINE_ATTACK4.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_heal1= Movie(play="images/p1_an/AINE_HEAL1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_heal2= Movie(play="images/p1_an/AINE_HEAL2.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_heal3= Movie(play="images/p1_an/AINE_HEAL3.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image aine_idle1= Movie(play="images/p1_an/AINE_IDLE1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image aine_wc= Movie(play="images/p1_an/AINE_WC.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle1= Movie(play="images/p1_an/AINE0HP_IDLE1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle2= Movie(play="images/p1_an/AINE0HP_IDLE2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle3= Movie(play="images/p1_an/AINE0HP_IDLE3.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle4= Movie(play="images/p1_an/AINE0HP_IDLE4.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image ainezhp_idle5= Movie(play="images/p1_an/AINE0HP_IDLE5.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_attack1= Movie(play="images/p1_an/CJ_ATTACK1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image cj_attack2= Movie(play="images/p1_an/CJ_ATTACK2.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image cj_attacked1= Movie(play="images/p1_an/CJ_ATTACKED1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image cj_cast1= Movie(play="images/p1_an/CJ_CAST1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image cj_cast2= Movie(play="images/p1_an/CJ_CAST.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image cj_idle1= Movie(play="images/p1_an/CJ_IDLE1.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cj_idle2= Movie(play="images/p1_an/CJ_IDLE2.webm", size=(1280,720),xalign=0.5,yalign=0.5)
image cro_attack1= Movie(play="images/p1_an/CRO_ATTACK1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image hostage_attacked1= Movie(play="images/p1_an/HOSTAGE_ATTACKED1.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)
image hostage_attacked2= Movie(plaxy="images/p1_an/HOSTAGE_ATTACKED2.webm",loop=False, size=(1280,720),xalign=0.5,yalign=0.5)

#label rubyintro:
#    scene black
#    show movie
#
#    play movie "images/dtyd.webm" #If yer shit aint workin it's because of this
#    $ renpy.transition(fade)#optional
#    $ renpy.pause(126, hard=True)# substitute "1" with video length in seconds. Stop players from skipping the video. If you want to allow skipping, remove ", hard=True", but then suffer in the knowledge you are now the developer that creates unskippable cutscenes (during a BATTLE no-less).
#    return
#lines 1-13, and line 37 are how to do movies
init python:
    import random
    import math

    def setend(end): #Necessary, gets used in Screens.rpy. I put it in the weirdest place possible.
        return "END"

    def roundstart(battery,ally):

        battery.mp = battery.mmp #set battery's current mana to max mana for battery
        ally.mp = 0 #set mana for mp
        battery.isguarding =False #battery is no longer guarding
        ally.isguarding = False #ally is no longer guarding

        narrator("Select the amount of MP to allocate.", interact=True)
        #SCALABILITY PROBLEM: Will have to detect what allies one has in the future; 1, 2, 3, whether you have ally X or Y, etcetc.

        end =None
        while(end != "END"):
             end = renpy.call_screen("mpallocation",battery ,ally,end) #Player sets numbers for mana until they press the big enter button, which returns "END" via setend()

        narrator(battery.name+" now has "+ str(battery.mp) + " MP" )
        narrator(ally.name+" now has "+ str(ally.mp) + " MP" )

    def get_characters_turn(battery,ally):
                Actr = None
                if(ally.name!=""):
                    narrator("Which character will move?", interact=False) #Get which char will move
                    
                    #This code is for me, much later when I want to make menus a bit dynamic.
                    #The display_menu function takes sets of 2-item tuples. 
                    #essentially this sets display menu items to be tuples of characters if that character's name is not ""
                    #quick hack, I know, but this is a setup for better code much later.
                    items = []
                    if(battery!=None):
                        batteryItem = (battery.name, battery)
                        items.append(batteryItem)
                    if(ally!=None):
                        allyItem =  (ally.name, ally)
                        items.append(allyItem)
                    Actr = renpy.display_menu(items) #Get which char will move
                    while(Actr.turnover == True): #While selected char's turn is over, get which char will move
                        narrator(Actr.name + "Has already gone this turn!")
                        narrator("Which character will move?", interact=False)
                        Actr = renpy.display_menu(items)
                    while(Actr.hp <= 0): #While selected char's turn is fucking DEAD, get which char will move
                        narrator(Actr.name + "is dead!")
                        narrator("Which character will move?", interact=False)
                        Actr = renpy.display_menu(items)
                    
                else:
                    Actr = battery
                    
                return Actr

    def get_characters_action(Actr, choice):
            action = " "
            if(choice=="Guard"):
                Actr.isguarding = True
                Actr.turnover = True
                narrator("You ready yourself for the enemy's next attack.")
            if(choice!="Guard"):
                action = renpy.call_screen("battlechoice",Actr,choice,random.randrange(0,5),"idle")


            return action

    def playerturn(battery,ally,enemy,Actr = None, skipSelect = False,hostage=None):
        if(Actr != None): #If Actr exists recursively
            Actr.nompflag = False #Actr's nompflag is False, meaning they can cast another spell or do another action.

        if( ally.hp <=0 ):  #check ally to see if they're FUCKING DEAD
                ally.turnover = True #obviously corpses don't move

        while(battery.turnover == False or ally.turnover == False ): #while neither the player nor ally's turns are over
            action = " " #action is delcare & made blank
            if(skipSelect == False): #If we are not recursed due to using a spell, a talk action, or low mana
                Actr = get_characters_turn(battery,ally) #then get which character's turn it is
                narrator(Actr.name + "'s turn!'")
            
            
            
            renpy.show_screen("anim",random.randrange(0,5),"idle",Actr,ally)

            choice = renpy.call_screen("battle",battery,ally,enemy,hostage) #we get the choice from the battle screen
            action = get_characters_action(Actr,choice) #we get the action from the action screen
            while(action=="b"): #if the player chose "BACK" , do the above again
                choice = renpy.call_screen("battle",battery,ally,enemy,hostage)
                action = get_characters_action(Actr,choice)
            if(choice =="Attack"): #if choice was attack
                Actr.attackchoice(action,enemy) #parse which attack was chosen
            if(choice =="Magic"): #if choice was magic
                Actr.magicchoice(action,enemy,battery,ally) #parse which magic was chosen
            if((choice == "Magic" or action =="Talk" or Actr.nompflag == True)):#if we used a spell, a talk action, or didn't have enough mana for a spell
                playerturn(battery,ally,enemy,Actr,True) #then we restart all our previous actions, running playerturn() again, but with the param True as to NOT select whose turn it is
            if(skipSelect == True): #if skipselect is true, then we are recursed; main() - > playerturn() - > playerturn() -> playerturn(), 'return' will return us to the first playerturn()  in all cases.
               return #We are recursed, exit to main function
            Actr.turnover = True #turn is over for this Actor
        battery.turnover = False #now that both actor's turns are over, we reset their turn flags.
        ally.turnover = False

    def enemyturn(enemy,battery,ally):

        Actr = enemy
        wavebonus = 0
        target = None
        rand_target = random.randrange(0,2)
        if((rand_target == 0) and (battery.mp == 0 )):
            target = ally
        elif(rand_target == 0):
            target = battery
        if(rand_target ==1):
            target = ally

        narrator("Enemy is attacking "+target.name+"!")
        renpy.show_screen("anim",random.randrange(0,5),"attack",Actr)
        renpy.pause(delay=5)
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

              if(attack_sum == enemy.defense+wavebonus or attack_sum > enemy.defense+wavebonus): #You hit!
                  narrator("Enemy hits!")

                  dmg_roll = Actr.damage(target)
                  dmg_roll_sum =  (sum(dmg_roll)+Actr.str)
                  final_dmg = dmg_roll_sum - target.armor
                  if(final_dmg < 0):
                       final_dmg = 0

                  renpy.show_screen("anim",random.randrange(0,5),"attacked",target)
                  renpy.pause(delay=5)
                  if(target.name == "CJ" and target.mp >0):
                      target.mp-=1
                      narrator("CJ lost 1 mp!")
                  else:
                      narrator("Enemy's dice rolls were ["+''.join(str(x)+"," for x in dmg_roll)+ "] Plus their DMG of ["+str(Actr.str) + "] for a total of [" + str(dmg_roll_sum ) +"] against "+target.name+"'s '["+str(target.armor)+"] armor. Hitting for [" +str(final_dmg)+"]")#Don't worry about it.
                      target.hp -= final_dmg

                  if(battery.hp <=0):
                    return
                  if(target.isguarding==True):
                    target.isguarding =False
              else: #You miss!
                    narrator("Enemy misses!")



label start: #game starts here

    python:
        
        #Actr Declaration
        #Actr(name, atk, defense, hp, mhp, mp, str, mmp, agi, armor, attacks=[], magic={"SPELLNAME":"BUFF OR DMG"}, abilities={"SPELLNAME":"BUFF OR DMG"}, items=[], dice=2) ###dice = 2 means default is 2, that's why enemy has a 3 there.
        Playercharacter = Actr("CJ",0,14,20,20,5,0,5,5,15,["Attack", "Talk"],{"One On One(1MP)":"BUFF","Man Eater(1MP)":"BUFF"})
        Enemycharacter =Actr("Cro'Dhearg",9,15,60,60,0,14,5,5,18,["Attack"],3)
        #Alliedcharacter1 =Actr("Áine",8,16,40,40,0,11,5,4,18,["Attack"],{"Gentle Current(1MP)":"BUFF","Underswell(2MP)":"BUFF","Riptide(3MP)":"BUFF","Wave Crash(3MP)":"DMG"})
        Alliedcharacter1 =  Actr("",0,0,0,0,0,0,0,0,0,["Attack"],{"Gentle Current(1MP)":"BUFF","Underswell(2MP)":"BUFF","Riptide(3MP)":"BUFF","Wave Crash(3MP)":"DMG"})
        Hostage = Actr("Hostage",0,0,20,0,0,0,0,0,0,["Whine"])
    jump phase1


label phase1:
    python:
        while(Hostage.hp>5):
            
            renpy.show_screen("anim",random.randrange(0,5),"idle",Playercharacter,Alliedcharacter1)
            renpy.pause(delay=0.01)
            playerturn(Playercharacter,Alliedcharacter1,Enemycharacter,None,False,Hostage)
            Hostage.hp-=5
    jump phase2

label phase2:
    python:
        Alliedcharacter1 =Actr("Áine",8,16,40,40,0,11,5,4,18,["Attack"],{"Gentle Current(1MP)":"BUFF","Underswell(2MP)":"BUFF","Riptide(3MP)":"BUFF","Wave Crash(3MP)":"DMG"})
        while(Enemycharacter.hp > 0 and Playercharacter.hp > 0):
            roundstart(Playercharacter,Alliedcharacter1)
            if(Playercharacter.hp> 0):
                playerturn(Playercharacter,Alliedcharacter1,Enemycharacter,None,False)
            if(Enemycharacter.hp > 0):
                enemyturn(Enemycharacter,Playercharacter,Alliedcharacter1)

