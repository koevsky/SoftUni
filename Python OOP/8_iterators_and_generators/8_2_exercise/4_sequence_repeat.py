class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 < self.number:

            self.number -= 1

            if self.index < len(self.sequence):
                self.index += 1

            else:
                self.index = 1

            return self.sequence[self.index - 1]

        else:
            raise StopIteration
