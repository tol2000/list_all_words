from functools import reduce


class ListAllWords:

    def __init__(self, alphabet, min_word_len, max_word_len, reduce_to_str=False, start_from=None):
        """

        :param alphabet:
        :param min_word_len:
        :param max_word_len:
        :param reduce_to_str: return word ['a','b','c'] as string 'abc'
        :param start_from: word to start from
            For example: if you have stopped or canceled previous iteration at some word (e.g. 'qwerty'),
            then simply set this parameter as ['q','w','e','r','t','y'] and ListAllWords
            will resumes iteration from this word to the end.
            Thus it applicable if you would like to do a long-time iteration in several stages
        """
        self.alphabet = alphabet
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len
        self.reduce_to_str = reduce_to_str
        self.start_from = start_from

        self.max_index = len(self.alphabet) - 1
        self.num_count = self.min_word_len
        self.num = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_count <= self.max_word_len:
            if self.num:
                self.inc_and_shift()
            else:
                # first initialization of self.num
                if not self.start_from:
                    self.num = [0] * self.num_count
                else:
                    # setting num according start_from and recalculating num_count
                    self.num_count = len(self.start_from)
                    self.num = [self.alphabet.index(x) for x in self.start_from]
            res = self.pos_to_symbols(self.num)
            return reduce(lambda x, y: x+y, res) if self.reduce_to_str else res
        else:
            raise StopIteration

    def pos_to_symbols(self, inp_list: list):
        return [self.alphabet[x] for x in inp_list]

    def inc_and_shift(self):
        last_index = self.num_count - 1
        if self.num[last_index] < self.max_index:
            self.num[last_index] += 1
        else:
            max_reached = True
            for i in range(last_index, -1, -1):
                if self.num[i] == self.max_index:
                    self.num[i] = 0
                else:
                    self.num[i] += 1
                    max_reached = False
                    break
            if max_reached:
                if self.num_count < self.max_word_len:
                    self.num.append(0)
                    self.num_count += 1
                else:
                    raise StopIteration
