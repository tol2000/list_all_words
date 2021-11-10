from functools import reduce


class ListAllWords:

    def __init__(self, alphabet, min_word_len, max_word_len, reduce_to_str=False, start_from=[]):
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
                    # setting num according start_from and recalculating num_counr
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
