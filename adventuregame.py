import random

class Main:

    health = 100  # Variable to calculate health
    score = 0  # Variable to calculate score
    strength = 10

    def display():
        print('Health: ' + str(Main.health))
        print('Score: ' + str(Main.score))

    def confir():
        x = input("Do you wish to restart the game?(Y/N): ")
        if x.lower() == 'y':
            Main.health = 100
            Main.score = 0
            Main.start_game()
        else:
            print('weak')
    
    def death():
        Main.display()
        Main.confir()

    def deathTwo():
        print('Strength: ' + str(Main.strength))
        Main.strength =10
        Main.death()

    def exploreCave():
        print("You have entered a cave. There is a treasure chest. Do you wish to open the chest? ")
        openChest = input("Y/N: ")
        randomyay = random.randrange(0,2)
        if openChest.lower() == 'y':
            if randomyay == 0:
                print('The chest was a mimic. You have died, the game has ended')
                Main.death()
            else:
                yay =random.randint(0,101)
                print('You have found treasure, score increased by 20. However, you have cut your hands while opening the chest, your health has been lowered by ' + str(yay))
                Main.health -= yay
                Main.score += 20
                Main.display()
                if Main.health <= 0:
                    Main.confir()
                    return
                heavenHell = input("There are two paths, a red one and a white one, which one do you pick?(W/R): ")
                if heavenHell.lower() == 'w':
                    print('You have gone to heaven, congrats')
                    Main.score += 10000000
                    Main.health += 1000000
                    Main.death()
                elif heavenHell.lower() == 'r':
                    print('You have gone to hell')
                    Main.score -= 1000000
                    Main.health -= 10000000
                    Main.death()
                else:
                    print('I dont understand')
                    Main.death()
        elif openChest.lower() == 'n':
            print('You have chosen to leave the chest. The gods of adventure are disappointed at your lack of initiative. However they have given you a chance')
            choose = input('Accept their grace or not?(Y/N): ')
            if choose.lower() == 'y':
                print('You will now fight a dragon')
                runOrFight = input('Do you run away or do you fight?(F/R): ').lower()
                if runOrFight == 'f':
                    win = random.randrange(0,3)
                    if win == 0:
                        print("You have beat the dragon and won the game")
                        Main.score += 10000
                        Main.health += 10000
                        Main.death()
                    else:
                        print('Did you think you could win. Thank you for entertaining the gods. They have given you a meaningless +100 score')
                        Main.score = 100
                        Main.health = 0
                        Main.death()
                elif runOrFight == 'r':
                    print("Don't run")
                    Main.health = 0
                    Main.death()
                else:
                    print("I don't understand ")
                    Main.death()
            elif choose.lower() == 'n':
                print('Die')
                Main.health = 0
                Main.death()
            else:
                print("I don't understand")
                Main.death()
        else: 
            print('I dont understand')
            Main.death()

    def exploreForest():
        print('You have entered an enchanted forest')
        die =random.randrange(0,5)
        if die == 0:
            print('You have died. The forest is too much for you')
            Main.death()
            return
        leaveOrFight = input("In front of you there is a creature. Do you wish to fight or to leave?(F/L): ").lower()
        if leaveOrFight == 'f':
            print("Of course you can't beat it, how stupid can you be. The adventure gods laugh at you.")
            Main.death()
        elif leaveOrFight == 'l':
            print('The adventure gods realize that the creature is too strong and give you another stat: strength')
            print('Currently, your strength is: ' + str(Main.strength) + '. Your strength needs to be at least 500 to beat the monster.')
            train = input('Will you train your strength? You have one chance to train your strength until you fight the monster.(Y/N): ').lower()
            if train == 'y':
                print('The gods are training you')
                randomStrength = random.randint(0, 600)
                Main.strength += randomStrength
                print('Your strength is now ' + str(Main.strength))
                print('you will now fight the monster')
                if Main.strength < 500:
                    print('You have lost')
                    Main.health = 0
                    Main.deathTwo()
                else:
                    print('You won the game. You have become an adventure god')
                    print('Health: infinite')
                    print('Score: infinite')
                    print('Strength: infinite')
                    Main.confir()

            elif train == 'n':
                print('Idiot')
                Main.health = 0
                Main.deathTwo()
            else:
                print("I don't understand")
                Main.deathTwo()

    def start_game():
        Main.clear()
        x = int(input("Enter 1 to go into a cave. Enter 2 to go into the enchanted forest: "))
        y = random.randrange(0,5)
        if y == 0:
            print("You have chosen the sweet relief of death.")
            Main.death()
        elif x == 1:
            Main.exploreCave()
        elif x == 2:
            Main.exploreForest()
        else:
            print('You have inputted a wrong number')
            print('Your health is now 1 and your score is now 1000')
            print('You will now go into a cave')
            Main.health = 1
            Main.score = 1000
            Main.exploreCave()

    def main():

        print("Welcome To The Cool Adventure Game!")  # printing the heading

        print("\n\n")  # Adding space

        Main.start_game()  # Calling start_game()

    def explore_random():

        ran = random.randint(0, 1)  # Taking random number between 0 and 1

        return ran

    def pause():

        input("Press Enter to continue...")

    def clear():

        # This method is for clearing the screen, it's a bit complex in Python, using ANSI escape codes

        print("\033[H\033[2J")  # ANSI escape code for clearing the screen

        print("\n")  # Adding extra newline for clarity

if __name__ == "__main__":

    Main.main()