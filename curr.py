from list_all_words_generator import ListAllWords

for i, w in enumerate(ListAllWords(
    # alphabet="0123456789ABCDEF",
    # alphabet="0123456789",
    alphabet="жопа",
    min_word_len=4,
    max_word_len=4,
    reduce_to_str=True,
    start_from=None,
    only_unique=True
), start=1):
    # if (1 <= i <= 100) or (i >= (99999-10000 - 100)):
    print(f'{i}:  {w}')
