import random
from countries import country_list
from animals import animals_list
import os,time
names = country_list
names.extend(animals_list)
letters = "abcdefghiklmnopqrstuvwxyz"


def clear():
    os.system( 'cls' )


def string_manage(word, letter, guess_string):
    count = word.count(letter)
    index = word.index(letter)
    if index != 0:
        guess_string = guess_string[:index]+letter+guess_string[index+1:]
    else:
        guess_string = letter+guess_string[1:]
    if count > 1:
        for _ in range(count-1):
            index = word.index(letter, index+1, len(word))
            guess_string = guess_string[:index] + letter + guess_string[index + 1:]
    return guess_string


def guess_check(word, letter):
    return letter in word


def manage_score(s, word, letter):
    if int(guess_check(word, letter)):
        s += word.count(letter)
    return s


def game_loop(ask_word, score, guessed_string, chances,stmt):
    choice = ""
    first_out = "_ " * len(ask_word)
    entered_letters = []
    print(stmt)
    print(first_out)
    while True:
        print(stmt)
        guess = input("Enter your guess :").lower()
        if guess not in entered_letters:
            if guess_check(ask_word, guess):

                lst=["Wonderful Guess !! You are really good","Going on the right path Beautiful!!","You beauty wonderfully going"]
                choice="{}".format(random.choice(["You are on right track some more left to go","You are doing great keep it up!","Doing really well!!"]+lst))
                guessed_string = string_manage(ask_word, guess, guessed_string)
                score = manage_score(score, ask_word, guess)

            else:
                chances -= 1
                print("WRONG INPUT CHANCES LEFT:", chances)
                choice="{}".format(random.choice(["Keep going all the best","No problem keep on moving hard times come !!","You are going good don't let one wrong answer impact you"]))
            entered_letters.append(guess)
            clear()
            print(choice)
            print(" ".join(list(guessed_string)))
            print("\n           GUESSED={}%".format(round(float(score*100/len(ask_word))),3), "CHANCES LEFT:", chances)
        else:
            clear()
            print("GUESS LETTER HAS ALREADY BEEN ENTERED TRY SOME OTHER!!")
            print(" ".join(list(guessed_string)))
            print("\n           GUESSED={}%".format(round(float(score*100/len(ask_word))),3), "CHANCES LEFT:", chances)
        
        if score == len(ask_word):
            clear()
            print("YOU HAVE WON THE GAME 😍 ")
            break
        if chances == 0:
            clear()
            print("YOU ARE OUT OF CHANCES")
            print(" ---------------------- GAME ENDED 😕 ----------------------")
            break

    print(ask_word.upper(), "IS THE ANSWER")


def manage_random(lst):
    return lst[random.randrange(len(lst))]


def before_game(names_list):

    pass


def check():
    given=input("TYPE Y FOR YES OR N FOR QUIT ")
    if given not in ['Y','N','y','n']:
        return check()
    if given.isalpha() and given.upper() == 'N':
        return 0

    return 1


def start_game(names_list):
    value = 1
    while value:
        out_word = manage_random(names_list)
        if out_word in names_list and names_list.index(out_word) <= 171:
            statement = "HINT: COUNTRY WITH "+str(len(out_word))+" LETTERS."
        else:
            statement = "HINT: ANIMAL WITH "+str(len(out_word))+" LETTERS."
        scores = 0
        our_string = "_"*len(out_word)
        total_chances = 6
        game_loop(out_word.lower(), scores, our_string, total_chances,statement)
        print("GAME COMPLETED DO YOU WANT TO CONTINUE: ")
        value = check()


start_game(names)
print("GAME ENDED THANKS FOR PLAYING")




