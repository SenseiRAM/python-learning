def main():
    print_header()
    game_loop()

def print_header():
    print('-------------------------------')
    print('         WIZARD GAME           ')
    print('-------------------------------')

def game_loop():
    creatures = [
        # TODO create creatures
    ]

    hero = None # TODO: Create hero
     while True:

        #Randomly choose a creature
        active_creature = None

        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(...))
        print()

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            pass
            # TODO Attack
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            # TODO Show creatures in the room
        else:
            print('OK, exiting game... so long!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()
        #if win or exit:
        #    break

    print('Goodbye!')

