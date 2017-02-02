import random

def main():

    guessNum = 0

    number = RamdomGuess()

    while guessNum < 6:
        print('take a guess')

        userGuess=UserGuess()
        guessNum = guessNum + 1

        if userGuess < number:
            print('Your guess is too low')

        if userGuess > number:
            print ('your guess is too high')

        if userGuess == number:
            break
    won = win()
    if won:
        print('correct')
    else :
        print ('wrong')

def UserGuess():
    userGuess = input('')
    userGuess = int(userGuess)
    return userGuess

def RamdomGuess():
    number = random.randint(1,6)
    return number

def win():
    number = RamdomGuess()
    userGuess=UserGuess()

    if number == userGuess:
        print ('you have guessed' , number )
        return userGuess == number
if __name__== '__main__':

    main()
