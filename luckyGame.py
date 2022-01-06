from random import randint
from time import sleep

pc = randint(0, 5)
print('/=\=/'* 7)
user = int(input('Inform a number: '))
print('PROCESSING....')
if (pc == user):
    print('\nYou won!')
    print(f'The number chosen by the pc was {pc}')
    print('/=\=/' * 7)
else:
    print('\nTry again!')
    print(f'The number chosen by the pc was {pc}')
    print('/=\=/' * 7)