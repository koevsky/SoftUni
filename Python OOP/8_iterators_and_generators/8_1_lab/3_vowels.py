class vowels:
    def __init__(self, text: str):
        self.text = text
        self.current = 0
        self.end = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:

            self.current += 1

            if self.text[self.current-1].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                return self.text[self.current-1]
            else:
                return self.__next__()

        else:
            raise StopIteration



