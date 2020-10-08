init python:
    import random
    class Actr:
        name = "you forgot to add a name retard"
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
        extraATKdice = 0
        extraSTRdice = 0
        extraHEALdice = 0
        turnover = False
        isguarding = False
        wavetokens = 0
        tidetokens = 0
        nompflag = False
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
            if(magicstring.lower() == "One On One(1MP)".lower()): #Dice buff +1 dice on next attack roll for choice
                return "ATKDICEBUFF", 1
            if(magicstring.lower() == "Man Eater(1MP)".lower()):
                return "DMGDICEBUFF", 1
            if(magicstring.lower() == "Underswell(2MP)".lower()):
                return "HEAL", 2, 2
            if(magicstring.lower() == "Riptide(3MP)".lower()):
                return "HEAL", 3, 3

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

        def attackchoice(self, action,target):
            if (action == "Talk"):
                c = Character(target.name)
                x = renpy.display_menu([("Call him a faggot", "owned")])
                if (x == "owned"):
                    c("!!!!!!!")

            if (action == "Attack"):
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

                        if (self.tidetokens == 0):
                            narrator("Your dice rolls were [" + ''.join(str(x) + "," for x in dmg_roll) + "] Plus your DMG of [" + str(self.str) + "] for a total of [" + str((sum(dmg_roll) + self.str)) + "] against the enemy's [" + str(target.armor) + "] armor. Hitting for [" + str(final_dmg) + "]")  # Don't worry about it.
                        else:
                            narrator("Your dice rolls were [" + ''.join(str(x) + "," for x in dmg_roll) + "]" + "plus your POW of " + "[" + str(self.str) + "]" + " minus the enemy's armor of " + str(target.armor) + "for a total of " + str(displayable) + " multiplied by your tide token bonus of " + str(mult_val) + "for a total of " + str(final_dmg) + " damage")

                        target.hp -= final_dmg
                        if (target.hp <= 0):
                            return

                    else:
                        narrator("You miss!")
                    self.tidetokens = 0

                else:
                    narrator("CJs fists went right through them!")
                    narrator("0 Damage done")

        def magicchoice(self,action,enemy,pc,ally):
               def SUBFUNCTION_DICEBUFF(stat): #this feels so wrong but looks so good and python apparently specifically supports it. Essentially this is like eating junk food for programming. Or modern art. This is ethically wrong.
                   narrator("Choose who you want to give an extra "+stat+" dice to for 1mp")
                   actrtobuff = renpy.display_menu([  (ally.name, ally)])
                   narrator(actrtobuff.name + " will get an extra "+stat+" dice next turn!")
                   actrtobuff.extraATKdice += 1 if (stat=="ATK") else 0
                   actrtobuff.extraSTRdice += 1 if (stat=="STR") else 0
                   self.mp-=mpneeded

               buff_bool = self.ismagicbuff(action) #Check if magic name received is buff or not
               if(buff_bool == True): #Then the magic passed is a buff
                #Magic is a buff so we send action to self.magicbuff(action)
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


                    if("HEAL" in type):
                        narrator("Choose who you want to heal")
                        actrtobuff = renpy.display_menu([ (pc.name, pc),  (ally.name, ally)])
                        if(self.name == "Áine"):  #increment wave tokens if it is Aine that is healing
                            self.wavetokens+=mpneeded
                        self.mp -= mpneeded
                        heal_roll = actrtobuff.heal(diceamnt)
                        heal_roll_sum = sum(heal_roll)
                        actrtobuff.hp += heal_roll_sum
                        if(actrtobuff.hp > actrtobuff.mhp):
                            actrtobuff.hp = actrtobuff.mhp
                        narrator("Your dice rolls were ["+''.join(str(x)+"," for x in heal_roll)+ "]" + ", healing " +actrtobuff.name+" for "+str(heal_roll_sum) + " HP")


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
                        narrator("Your dice rolls were ["+''.join(str(x)+"," for x in attack_roll)+ "] Plus wave crash's ATK of ["+str(self.atk-2) + "] for a total of [" + str(attack_sum ) +"] against the enemy's ["+str(Enemycharacter.defense)+"] defense.")#Don't worry about it.
                        self.mp-=mpneeded
                        if(attack_sum == Enemycharacter.defense or attack_sum > Enemycharacter.defense): #You hit!
                            narrator("You hit!")
                            dmg_roll = self.magicdamage(action)
                            dmg_roll_sum =  (sum(dmg_roll)+self.str+3) - Enemycharacter.armor
                            displayable = dmg_roll_sum
                            mult_val = 0
                            if(self.name == "Áine" and self.tidetokens > 0 ):
                                mult_val = 1.25 if self.tidetokens is 1 else 1.5 if self.tidetokens is 2 else 2.0 if self.tidetokens is 3 else 0
                                dmg_roll_sum = int(math.ceil(dmg_roll_sum * mult_val))
                            final_dmg = dmg_roll_sum
                            if(final_dmg < 0):
                                 final_dmg = 0
                            if(self.tidetokens == 0):
                                narrator("Your dice rolls were ["+''.join(str(x)+"," for x in dmg_roll)+ "] Plus wave crash's POW of ["+str(self.str+3) + "] for a total of [" + str( (sum(dmg_roll)+self.str+3) ) +"] against the enemy's ["+str(Enemycharacter.armor)+"] armor. Hitting for [" +str(final_dmg)+"]")#Don't worry about it.
                            else:
                                narrator("Your dice rolls were ["+''.join(str(x)+"," for x in dmg_roll)+ "]" + "plus wave crash's POW of "+"["+str(self.str+3)+"]"+" minus the enemy's armor of "+str(Enemycharacter.armor) + "for a total of "+str(displayable)+" multiplied by your tide token bonus of "+ str(mult_val) + "for a total of " + str(final_dmg)+" damage")

                            #if(self.name == "Áine"):
                                #self.wavetokens +=mpneeded

                            Enemycharacter.hp -= final_dmg
                            if(Enemycharacter.hp <= 0):
                                return
                        else:
                          narrator("You miss!")
                          self.tidetokens = 0
                     self.tidetokens = 0
                 else: #Not enough mana
                     narrator("You don't have enough mana for that!")
                     self.nompflag   = True #Recursive loop to get player choice again, skipping selection.
