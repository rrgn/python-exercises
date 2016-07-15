"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object): # make a class named character that inherits object
    def __init__(self): # class character has a dunder-init that takes self as a parameter
        self.name = '<undefined>' #from self get attribute name and set it to undefined
        self.health = 10 #from self get attribute healtt and set it to 10
        self.power = 5 #from self get attribute power and set it to 5
        self.coins = 20 #from self get attribute name and set it to 20

    def alive(self): # class character has a method named alive that takes self as a parameter
        return self.health > 0

    def attack(self, enemy): # class character has a method named attack that takes self and enemy parameters
        if not self.alive(): # #from self get alive method with parameter self
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power) # from enemy get the receive_damage method and call it with parameters self and self.power
        time.sleep(1.5) # from time get the sleep method and call it with parameters self and 1.5

    def receive_damage(self, points): #class character has a method named receive_damage that take parameters self and points
        self.health -= points # from self get attribute health and decrement it with points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self): # class character has a method print_status that takes in self as a parameter
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character): # make a class named hero that inherits character
    def __init__(self): # class hero has a dunder-init that takes self as a parameter
        self.name = 'hero' #from self get attribute name and set it to 'hero'
        self.health = 10 #from self get attribute health and set it to 10
        self.power = 5 #from self get attribute power and set it to 5
        self.coins = 20 #from self get attribute coins and set it to 20

    def restore(self): # class hero has a method named restore that takes self as a parameter
        self.health = 10 #from self get attribute health and set it to 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1) # from time get the sleep method and call it with parameters self, 1

    def buy(self, item): # class character has a method of buy that takes parameters self and item
        self.coins -= item.cost # from self get attribute coins and decrement it with items.cost
        item.apply(hero) #from item get the apply method and call it with parameters self and hero

class Goblin(Character): # make a class named goblin that inherits character
    def __init__(self): # class goblin has a dunder-init that takes self as a parameter
        self.name = 'goblin' #from self get attribute name and set it to 'goblin'
        self.health = 6 #from self get attribute health and set it to 6
        self.power = 2 #from self get attribute power and set it to 2

class Wizard(Character): # make a class named wizard that inherits character
    def __init__(self): # class wizard has a dunder-init that takes self as a parameter
        self.name = 'wizard' #from self get attribute name and set it to 'wizard'
        self.health = 8 #from self get attribute health and set it to 8
        self.power = 1 #from self get attribute power and set it to 1

    def attack(self, enemy): #class wizard has a method attack that takes parameters self and enemy
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object): # make a class named Battle that inherits object
    def do_battle(self, hero, enemy): # has a method do_battle takes self hero enemy as parameters
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive(): # from hero / enemy get alive method and call it with parameter self
            hero.print_status() # from hero get print_status method and call it with parameter self
            enemy.print_status() # from enemy get print_status method and call it with parameter self
            time.sleep(1.5) # from time get the sleep method and call it with parameters self, 1.5
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy) # from hero get attack method and call it with parameter self, enemy
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero) # from enemy get attack method and call it with parameter hero
        if hero.alive(): # from hero get alive method and call it with no parameters
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object): # make a class named Tonic that inherits object
    cost = 5
    name = 'tonic'
    def apply(self, character): # has method apply takes parameters self and character
        character.health += 2 # from character get health method and increment itself by 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object): # make a class named Sword that inherits object
    cost = 10
    name = 'sword'
    def apply(self, character): # has method apply takes parameters self and character
        character.power += 2 # from character get power method and increment itself by 2
        print "%s's power increased to %d." % (character.name, character.power)

class Shopping(object): # make a class named Shopping that inherits object
    items = [Tonic, Sword]
    def do_shopping(self, hero): #has method do_shopping that takes in parameters self and hero
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item) #from heron get buy method and call it with parameters self and item

hero = Hero() #set hero to instance of class Hero
enemies = [Goblin(), Wizard()]
battle_engine = Battle() #set battle_engine to instance of class Battle
shopping_engine = Shopping() #set shopping_engine to instance of class Shopping

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy) # from battle_engine get do_battle method and call it with parameters self, hero, enemy
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero) # from shopping_engine get method do shopping and call it with parameters self and hero

print "YOU WIN!"
