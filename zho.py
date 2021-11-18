from list_all_words_generator import ListAllWords
from random import randrange

if __name__ == '__main__':

    print(f'----- ListAllBinaries -----')

    # alphabet = ['глав', 'внеш', 'прод', 'сов', 'мор', 'транс', 'авто']
    # min_word_len = 3
    # max_word_len = 3

    alphabet = [
        'бу', 'бе', 'ба', 'бо', 'би',
        'гу', 'ге', 'га', 'го', 'ги',
        'пу', 'пе', 'па', 'по', 'пи',
        'ду', 'де', 'да', 'до', 'ди',
        'жу', 'же', 'жа', 'жо', 'жи',
        'лу', 'ле', 'ла', 'ло', 'ли'
    ]
    min_word_len = 3
    max_word_len = 3

    words = ListAllWords(
        alphabet, min_word_len, max_word_len, reduce_to_str=True
        , start_from=None
        , only_unique=True
    )
    
    src = []

    for word_a in words:
        print('Getting', word_a, end=chr(13))
        src.append(word_a)

    # with open('out.txt', 'w') as f:
    #     while src:
    #         i = randrange(0, len(src))
    #         word = src[i]
    #         f.write(word + '\n')
    #         print(word)
    #         src.__delitem__(i)
    #     print('')

    print('q - quit, otherwise - cont\n')
    loop = True
    while loop:
        num_words = randrange(2, 4)
        for i in range(num_words):
            ind = randrange(0, len(src))
            print(src[ind], end=' ')
        if input() in ('q', 'Q'):
            break
