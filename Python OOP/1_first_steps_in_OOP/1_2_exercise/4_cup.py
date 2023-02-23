class Cup:

    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        free_space = self.size - self.quantity
        if free_space >= quantity:
            self.quantity += quantity

    def status(self):
        free_space = self.size - self.quantity
        return free_space
