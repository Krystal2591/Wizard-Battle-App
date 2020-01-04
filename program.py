from actors import Wizard, Creature, Small_Animal, Predator, Dragon
import random
import time


def main():
    print_header()
    game_loop()



def print_header():
    print("---------------------------------")
    print("       WIZARD BATTLE APP")
    print("---------------------------------")
    print()

def game_loop():

    creatures=[Small_Animal('Toad', 1),
               Predator('Tiger', 12),
               Small_Animal('Bat', 3),
               Dragon('Dragon', 50, 35, True),
               Creature('Evil Wizard', 1000)]

    hero= Wizard('Gandolf', 75)


    while True:

        active_creature = random.choice(creatures)
        print ('A {} of level {} has appeared from a dark and foggy forest'.format(active_creature.name, active_creature.level))
        print ()

        user_command=input('Do you [a]ttack, [r]unaway or [l]ook around?')

        if user_command=='a':

            if hero.attack(active_creature)==True:
                creatures.remove(active_creature)
            else:
                print('The wizard Gandolf rests...')
                time.sleep(5)
                print("He's back!")

        elif user_command=='r':
            pass
        elif user_command=='l':
            print('Gandolf looks around and sees...')
            for i in creatures:
                print ('A {} of level {}'.format(i.name, i.level))
        else:
            print('Exiting game! Bye')
            break
        if not creatures:
            print("You've defeated all the creatures! Game over!")
            break



if __name__=='__main__':
    main()