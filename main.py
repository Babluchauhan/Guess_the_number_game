import random
import os.path

def game():
    while True:

        rand = random.randrange(1, 100)  # sets number range between 1 to 100
        print('###### Guess The Number ######\n~Guess the number between 1 to 100~')
        guess = 0
        num = None
        # print(rand)  # use only to test the game

        while num != rand:  # loop to keep guessing going
            guess += 1
            num = input('Enter the number or q to quit: ')
            if num == 'q':
                print('Thanks for playing this game!!')  # to exit the program
                exit()
            try:  # handling the exception
                num = int(num)
                if num == rand:
                    print(f'Correct!!! The number is {rand}.')
                    print(f'You guessed the number in {guess} guesses.\n\n')
                elif num < rand:
                    print("Wrong!!! It's a larger number.")
                elif num > rand:
                    print("Wrong!!! It's a smaller number.")
            except Exception as e:
                print('Enter a valid number!!')

        # checking if the file is present or not
        check_file = os.path.isfile('highscore.txt')
        if check_file == True:
            with open('highscore.txt') as f:
                highscore = f.read()
            if highscore == '':
                with open('highscore.txt', 'w')as f:
                    f.write(str(guess))
            elif int(highscore) == 0:
                with open('highscore.txt', 'w') as f:
                    f.write(str(guess))
            elif guess < int(highscore):
                with open('highscore.txt', 'w') as f:
                    f.write(str(guess))
        else:
            # if the file isn't present then it'll create one
            with open('highscore.txt', 'w') as f:
                f.write(str(guess))


game()  # run(calling) the geme
