import string
import random

words = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes',
         'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar',
         'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb',
         'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex',
         'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord',
         'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby',
         'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip',
         'rogginess']


def hangman():
    word = random.choice(words).upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters guessed

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        # letters guessed
        print("You have",lives, "lives. You gueesed these letters : ", " ".join(used_letters))

        # the current word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("The word : ", " ".join(word_list))

        player_guessing = input(" \nGuess a letter : ").upper()
        if player_guessing in alphabet - used_letters:
            used_letters.add(player_guessing)
            if player_guessing in word_letters:
                word_letters.remove(player_guessing)

            else:
                lives = lives - 1
                print("Letter not in the word. ")

        elif player_guessing in used_letters:
            print("You already guessed this character. Choose another one. ")

        else:
            print("Invalid character. Try again. ")

    if lives == 0:
        print("You died. The word was ",word, ". Try again! ")
    else:
        print("Congrats, you gueesed the word", word, "correcty! ")

hangman()
