from random import randrange

from list_all_words_generator import ListAllWords

if __name__ == '__main__':
    print(f'----- Mat zagib :) -----')

    a = "твою за_ногу ебать через_плечо твой_хуй в_пизду в_жопу через_коромысло сука блядь пизда"
    alphabet = [f'{x} ' for x in a.split(' ')]
    alphabet = [item.replace("_", " ") for item in alphabet]

    words = ListAllWords(
        alphabet=alphabet, min_word_len=7, max_word_len=7, reduce_to_str=True
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
        ind = randrange(0, len(src)-1)
        print(src[ind])
        if input() in ('q', 'Q'):
            break
