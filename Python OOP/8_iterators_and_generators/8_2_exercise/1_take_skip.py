class take_skip:

    def __init__(self, step: int, count: int):

        self.step = step
        self.count = count
        self.current_num = 0
        self.current_count = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.current_count < self.count:

            self.current_count += 1
            self.current_num += self.step

            return self.current_num - self.step

        else:

            raise StopIteration



