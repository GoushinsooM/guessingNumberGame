import random

def verifyGuesses(guess_number, guess):
    if (guess > guess_number):
        print(f'Number {guess} is above. ')
    else:
        print(f'Number {guess} is below. ')

def results(guess_number, guesses):
    if (guesses == 1):
        return print('WOW first try, you\'re amazing !! ')

    else:
        return print(f'You won, the lucky number was: {guess_number} \nTries: {guesses}')

def playGame():
    guess_number = random.randint(1, 1000)
    guess = int(input("Try find the lucky number: "))
    guesses = 1

    while (guess_number != guess):
        verifyGuesses(guess_number, guess)
        guesses+=1
        guess = int(input("Try again: "))
            
    return results(guess_number, guesses)

if __name__ == '__main__':
    playGame()

