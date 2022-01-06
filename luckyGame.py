import random

pc = random.randint(0, 5)
user = int(input('Inform a number: '))
if (pc == user):
    print('\nYou won!')
    print(f'The number chosen by the pc was {pc}')
else:
    print('\nTry again!')
    print(f'The number chosen by the pc was {pc}')