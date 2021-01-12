init python:
    import random
    class Actr:
        #Initial Implementation goals.
            #'''


            #2) Enemy NPC needs better behavior. She should do her normal attack 3-4 times before doing one of her special attacks (either a single target 2x hit attack or an AOE attack that hits both CJ and Aine).

            #2.1)The enemy NPC should not attack CJ if CJ has 0 MP at the end of his turn, that includes the AOE attack.

            #3) Wave/tide tokens need to be capped at 3 maximum.

            #4) Need to implement a Phase 1 and Phase 2 for the fight. Phase 1 is just CJ against the enemy (With 'Hostage' NPC present, see Task 5), CJ has no spells only Attack, talk and guard. Phase 1 lasts for 5 turns before transitioning to Phase 2.
            #Phase 2 is the current battle happening.

            #5) Friendly 'Hostage' NPC needs to be implemented for phase 1 and 2. NPC takes damage every turn, if HP reaches 0 its game over. Win condition for Phase 2 is to heal the NPC to full.

            #5.1) Enemy NPC will try to "block" healing to the 'Hostage'. All this means is that the first heal spell to the 'Hostage' will succeed, after that the Enemy needs to be damaged once or twice before heal spells will work again on the 'Hostage'.

            #6) Add little screen where abilities are shown that describes what each ability/spell does.
            #'''
        name = "you forgot to add a name retard"
        show_magic = False
        hostageHasBeenHealed = False
        atk = 0
        defense = 0
        hp = 0
        mhp = 0
        mp = 0
        str = 0
        mmp = 0
        agi = 0
        armor = 0
        attacks = []
        magic = {}
        abilities = {}
        items = []
        dice = 2
        heatToken = 0
        extraATKdice = 0
        extraSTRdice = 0
        extraHEALdice = 0
        turnover = False
        isguarding = False
        wavetokens = 0
        tidetokens = 0
        nompflag = False
        croHurtLastTurn = False
        azhp_flag = False
        def __init__(self, name, atk, defense, hp, mhp, mp, str, mmp, agi, armor, attacks=[], magic={}, abilities={}, items=[], dice=2):
            self.name = name
            self.atk = atk
            self.defense = defense
            self.hp = hp
            self.mhp = mhp
            self.mp = mp
            self.str = str
            self.mmp = mmp
            self.agi = agi
            self.armor = armor
            self.attacks = attacks
            self.magic = magic
            self.abilities = abilities
            self.items = items
            self.dice = dice

        def mpallocationincrement(self, pc):
            if (self.mp < 3 and pc.mp > 0):
                self.mp += 1
                pc.mp -= 1
            else:
                self.mp += 0

        def mpallocationdecrement(self, pc):
            if (self.mp > 0 and pc.mp < 5):
                self.mp -= 1
                pc.mp += 1
            else:
                self.mp -= 0

        def attack(self, attackstring):
            diceroll = []
            if (self.atk == 0):
                return 0
            print("minorhere")
            if (attackstring == "Attack" or attackstring == "Wave Crash(3MP)"):
                # roll dice many 6 sided die and add your attack stat
                print("HERE")
                for i in range(1, self.dice + 1 + self.extraATKdice):  # Roll "DICE" many times. e.g. if dice = 3, you roll 3 dice
                    diceroll.append(random.randrange(1, 6 + 1))  # roll a 6 sided dice
                self.extraATKdice = 0
                return diceroll  # Return the attack number result

        def damage(self, targetactr = None):
            diceroll = []
            if(targetactr!=None):
                if(targetactr.isguarding == True):
                    self.dice -=1
            for i in range(1, self.dice + 1 + self.extraSTRdice):  # Roll "DICE" many times. e.g. if dice = 3, you roll 3 dice
                diceroll.append(random.randrange(1, 6 + 1))  # roll a 6 sided dice
            self.extraSTRdice = 0
            if(targetactr!=None):
                if (targetactr.isguarding == True):
                    self.dice +=1
            return diceroll  # Return the damage number result

        def ismagicbuff(self, magicstring):
            if(self.magic[magicstring] == "BUFF"):
                return True
            else:
                return False

        def magicbuff(self,magicstring):
            #Return name,mp,dice
            #magicstring = "Gentle Current(1MP)"
            if(magicstring.lower() == "One On One(1MP)".lower()): #Dice buff +1 dice on next attack roll for choice
                return "ATKDICEBUFF", 1
            if(magicstring.lower() == "Man Eater(1MP)".lower()):
                return "DMGDICEBUFF", 1
            if(magicstring.lower() == "Underswell(2MP)".lower()):
                return "HEAL", 2, 2
            if(magicstring.lower() == "Riptide(3MP)".lower()):
                return "HEAL", 3, 3
            if(magicstring.lower() == "Gentle Current(1MP)".lower()):
                return "HEAL", 1, 1
            if(magicstring.lower() == "Out of Touch(3MP)".lower()):
                return "RES",3

        def magicattacktype(self, magicstring):

            if(magicstring.lower() == "Wave Crash(3MP)".lower()):
                return "DMG", 3

        def heal(self,dice):
            healroll = []
            for i in range(1,dice+1):
                healroll.append(random.randrange(1,6+1))
            return healroll

        def magicdamage(self,magicstring):
            if(magicstring.lower() == "Wave Crash(3MP)".lower()):
                diceroll = []
                for i in range(1,self.dice + 1 + self.extraSTRdice):  # Roll "DICE" many times. e.g. if dice = 3, you roll 3 dice
                    diceroll.append(random.randrange(1, 6 + 1))  # roll a 6 sided dice

                self.extraSTRdice = 0
                return diceroll  # Return the damage number result and the extra damage the spell does

        def attackchoice(self, action,target): #monolith
            if (action == "Talk"):
                c = Character(target.name)
                x = renpy.display_menu([("Call him a faggot", "owned")])
                if (x == "owned"):
                    c("!!!!!!!")

            if (action == "Attack"):
                renpy.show_screen("anim",random.randrange(0,5),"attack",self)
                renpy.pause(delay=5)
                renpy.show_screen("anim",random.randrange(0,5),"idle",self)
                if (self.name != "CJ"):

                    attack_roll = self.attack(action)  # Obtain the dice rolls
                    attack_sum = sum(attack_roll) + self.atk  # Obtain the sum of dice rolls and add the actor's ATK rating
                    narrator("Your dice rolls were [" + ''.join(str(x) + "," for x in attack_roll) + "] Plus your ATK of [" + str(self.atk) + "] for a total of [" + str(attack_sum) + "] against the enemy's [" + str(target.defense) + "] defense.")  # Don't worry about it.

                    if (attack_sum == target.defense or attack_sum > target.defense):  # You hit!
                        narrator("You hit!")
                        dmg_roll = self.damage()
                        dmg_roll_sum = (sum(dmg_roll) + self.str) - target.armor
                        displayable = dmg_roll_sum
                        mult_val = 0

                        if (self.name == "Áine" and self.tidetokens > 0):
                            mult_val = 1.25 if self.tidetokens is 1 else 1.5 if self.tidetokens is 2 else 2.0 if self.tidetokens is 3 else 0
                            dmg_roll_sum = int(math.ceil(dmg_roll_sum * mult_val))
                        final_dmg = dmg_roll_sum

                        if (final_dmg < 0):
                            final_dmg = 0

                        #renpy.movie_cutscene("dtyd.webm") #Plays a movie you can cancel and skip out of


                        if (self.tidetokens == 0):
                            narrator("Your dice rolls were [" + ''.join(str(x) + "," for x in dmg_roll) + "] Plus your DMG of [" + str(self.str) + "] for a total of [" + str((sum(dmg_roll) + self.str)) + "] against the enemy's [" + str(target.armor) + "] armor. Hitting for [" + str(final_dmg) + "]")  # Don't worry about it.
                        else:
                            narrator("Your dice rolls were [" + ''.join(str(x) + "," for x in dmg_roll) + "]" + "plus your POW of " + "[" + str(self.str) + "]" + " minus the enemy's armor of " + str(target.armor) + "for a total of " + str(displayable) + " multiplied by your tide token bonus of " + str(mult_val) + "for a total of " + str(final_dmg) + " damage")
                        target.hp -= final_dmg

                        target.croHurtLastTurn = True
                        if (target.hp <= 0):
                            return

                    else:
                        narrator("You miss!")
                    self.tidetokens = 0

                else:
                    narrator("CJs fists went right through them!")
                    narrator("0 Damage done")

        def magicchoice(self,action,enemy,pc,ally, hostage): #monolith, utter monolith, please fix.
               def SUBFUNCTION_DICEBUFF(stat): #update: found out why subfunctions exist: functional programming is a thing in python apparently. Might be good for this project? 
                   narrator("Choose who you want to give an extra "+stat+" dice to for 1mp")
                   actrtobuff = renpy.display_menu([  (ally.name, ally)])
                   renpy.show_screen("anim",random.randrange(0,5),"cast",self)
                   renpy.pause(delay=5)
                   renpy.show_screen("anim",random.randrange(0,5),"idle",self)
                   narrator(actrtobuff.name + " will get an extra "+stat+" dice next turn!")
                   actrtobuff.extraATKdice += 1 if (stat=="ATK") else 0
                   actrtobuff.extraSTRdice += 1 if (stat=="STR") else 0
                   self.mp-=mpneeded

               buff_bool = self.ismagicbuff(action) #Check if magic name received is buff or not
               if(buff_bool == True): #Then the magic passed is a buff
                #Magic is a buff so we send action to self.magicbuff(action)
                #action = "Gentle Current(1MP)"
                type = self.magicbuff(action)

                #type[0] is name, type[1] is mp, type[2] is dice
                #Because type[0] is name, we can simply access it by the 'in' operator
                mpneeded = type[1]
                diceamnt = type[2] if len(type) == 3 else 0
                
                
                if(self.mp - mpneeded >= 0):
                    if("ATKDICEBUFF" in type):
                        SUBFUNCTION_DICEBUFF("ATK")


                    if("DMGDICEBUFF" in type):
                        SUBFUNCTION_DICEBUFF("STR")

                    if("RES" in type):
                        ally.hp = ally.mhp
                        narrator("Aine was resurrected at full HP!")
                        Alliedcharacter1.azhp_flag =  (ally.hp <= 0)
                        self.mp -= mpneeded
                        
                    if("HEAL" in type):
                        
                        narrator("Choose who you want to heal")
                        items = []
                        if(pc!=None):
                            batteryItem = (pc.name, pc)
                            items.append(batteryItem)
                        if(ally!=None):
                            allyItem =  (ally.name, ally)
                            items.append(allyItem)
                        if(hostage!=None):
                            hostageItem =  (hostage.name, hostage)
                            items.append(hostageItem)
                        actrtobuff = renpy.display_menu(items)
                        
                        if(enemy.croHurtLastTurn == True or (actrtobuff.hostageHasBeenHealed == False and actrtobuff.name == "Hostage")):
                            if(self.name == "Áine"):  #increment wave tokens if it is Aine that is healing
                                self.wavetokens+=mpneeded
                            self.mp -= mpneeded
                            heal_roll = actrtobuff.heal(diceamnt)
                            heal_roll_sum = sum(heal_roll)
                            if(action == "Riptide(3MP)"):
                                heal_roll_sum += 4
                            actrtobuff.hp += heal_roll_sum
                            if(actrtobuff.hp > actrtobuff.mhp):
                                actrtobuff.hp = actrtobuff.mhp

                            renpy.show_screen("anim",random.randrange(0,5),"heal",self)
                            renpy.pause(delay=5)
                            renpy.show_screen("anim",random.randrange(0,5),"idle",self)
                            narrator("Your dice rolls were ["+''.join(str(x)+"," for x in heal_roll)+ "]+4" + ", healing " +actrtobuff.name+" for "+str(heal_roll_sum) + " HP")
                        else:
                            self.mp -= mpneeded
                            narrator("Undamaged Cro blocks the healing spell!")
                        if(actrtobuff.name == "Hostage" and actrtobuff.hostageHasBeenHealed == False):
                            actrtobuff.hostageHasBeenHealed = True


                else: #Not enough mana
                    narrator("You don't have enough MP for that!")
                    self.nompflag = True

               if(buff_bool == False): #Then the magic passed is not a buff and is an attack

                 type = self.magicattacktype(action)
                 #type[0] is name, type[1] is mp, type[2] is dice
                 mpneeded = type[1]
                 diceamnt = type[2] if len(type) ==3 else 0
                 if(self.mp - mpneeded >= 0):
                     if("DMG" in type):
                        attack_roll = self.attack(action)
                        attack_sum = sum(attack_roll) + self.atk-2 #Obtain the sum of dice rolls and add the actor's ATK rating
                        narrator("Your dice rolls were ["+''.join(str(x)+"," for x in attack_roll)+ "] Plus wave crash's ATK of ["+str(self.atk-2) + "] for a total of [" + str(attack_sum ) +"] against the enemy's ["+str(enemy.defense)+"] defense.")#Don't worry about it.
                        self.mp-=mpneeded
                        if(attack_sum == enemy.defense or attack_sum > enemy.defense): #You hit!
                            narrator("You hit!")
                            dmg_roll = self.magicdamage(action)
                            dmg_roll_sum =  (sum(dmg_roll)+self.str+3) - enemy.armor
                            displayable = dmg_roll_sum
                            mult_val = 0
                            if(self.name == "Áine" and self.tidetokens > 0 ):
                                mult_val = 1.25 if self.tidetokens is 1 else 1.5 if self.tidetokens is 2 else 2.0 if self.tidetokens is 3 else 0
                                dmg_roll_sum = int(math.ceil(dmg_roll_sum * mult_val))
                            final_dmg = dmg_roll_sum
                            if(final_dmg < 0):
                                 final_dmg = 0
                            if(self.tidetokens == 0):
                                narrator("Your dice rolls were ["+''.join(str(x)+"," for x in dmg_roll)+ "] Plus wave crash's POW of ["+str(self.str+3) + "] for a total of [" + str( (sum(dmg_roll)+self.str+3) ) +"] against the enemy's ["+str(enemy.armor)+"] armor. Hitting for [" +str(final_dmg)+"]")#Don't worry about it.
                            else:
                                narrator("Your dice rolls were ["+''.join(str(x)+"," for x in dmg_roll)+ "]" + "plus wave crash's POW of "+"["+str(self.str+3)+"]"+" minus the enemy's armor of "+str(enemy.armor) + "for a total of "+str(displayable)+" multiplied by your tide token bonus of "+ str(mult_val) + "for a total of " + str(final_dmg)+" damage")

                            #if(self.name == "Áine"):
                                #self.wavetokens +=mpneeded

                            enemy.hp -= final_dmg
                            enemy.croHurtLastTurn = True
                            if(enemy.hp <= 0):
                                return
                        else:
                          narrator("You miss!")
                          self.tidetokens = 0
                     self.tidetokens = 0
                 else: #Not enough mana
                     narrator("You don't have enough mana for that!")
                     self.nompflag   = True #Recursive loop to get player choice again, skipping selection.
