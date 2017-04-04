
def guess_num():
    import random                                   #random practice
    number = int(random.randrange(1, 100))

    still_playng = True
    guess = int(input('what is your guess?: '))
    while still_playng == True:
        if guess > number:
            print("Too high. Go lower.")
            guess = int(input('what is your guess?: '))
        elif guess < number:
            print("Too low. Go higher.")
            guess = int(input('what is your guess?: '))
        else:
            still_playng = False
            print('Spot on!')
            again = input('Want to play again? Y/N: ').lower
            if again == y :
                guess_num()                         #not workign yet
            elif again == n :
                print('Bye')


guess_num()

# name  = input('What is you name?: ')          #while loop practice
#
# valid_int = False
#
# while not valid_int:
#     try:
#         age = int(input('hello {}, how old are you?: '.format(name)))
#         valid_int = True
#     except ValueError:
#         print('That is not a number you twit!')



# if age > 100:                                 #elif practice
#         print('You should be dead by now {}' .format(name))
# elif age > 20:
#     print('Old aready.')
# elif age == 20:
#     print("smug little shit aren\'t you?")
# else:
#     print('Get your ass off my lawn you whippersnapper!!')
