from random import randint

"""Welcome. This is my first project.
Here's a little game: the computer picks the number, then it tries to guess it.
"""

print("Welcome to Michael's first project. We're gonna guess the number our computer picks.")
print('Get ready!')
cycle_num = int(input('Please, input the number of cycles:'))

"""First you can set the number of game cycles. It's important. If we have only a few cycles we can't find out
the mean value correctly.
"""

total_num = 0
cycle = 0

""" total_num is a total number of attempts the computer makes to guess numbers
cycle is one cycle of game. Cycle ends when the computer finds out the correct number
"""

"""I decided to divide the range of possible options by four.
The system tries the number 50 first. Then depends on the result it tries 25 or 75.
Then it just goes up or down until it finds the correct one.
"""

while cycle < cycle_num:
    cycle += 1
    a = randint(1, 101)
    b = 50
    attempt = 0
    if b < a:
        attempt += 1
        b = 75
        while b != a:
            if b > a:
                attempt += 1
                b -= 1
            else:
                attempt += 1
                b += 1
    elif b > a:
        attempt += 1
        b = 25
        while b != a:
            if b > a:
                attempt += 1
                b -= 1
            else:
                attempt += 1
                b += 1
    else:
        attempt += 1

    total_num += attempt
mean_num = round(total_num/cycle_num)

""" To find out the mean value we need to divide the total number of attempts by the number of cycles.
And, of course, round it up
"""

print(f'We did it!! It took approximately {int(mean_num)} attempts per cycle')
print('Thanks for playing!')
