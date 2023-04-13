class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.tuple = tuple(self.dictionary.items())
        self.current = 0
        self.end = len(self.dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.tuple[self.current - 1]

        else:
            raise StopIteration



