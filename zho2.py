from random import randrange

if __name__ == '__main__':
    print(f'----- Kly4ko talker :) -----')

    a = "каждый охотник желает знать где сидит фазан сегодня не он лишь может смотреть завтрашний день карл клара украл кораллы кларнет нужно вернуть"
    alphabet = [f'{x}' for x in a.split(' ')]

    print('q - quit, otherwise - cont\n')
    loop = True
    while loop:
        src = alphabet.copy()
        dest = []
        cur = 1
        max_i = 4
        while src and cur <= max_i:
            ind = randrange(0, len(src))
            dest.append(src.pop(ind))
            cur += 1
        if input(' '.join(dest) + '\n') in ('q', 'Q'):
            loop = False
