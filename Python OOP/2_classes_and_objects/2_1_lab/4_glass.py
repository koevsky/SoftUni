class Glass:

    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml) -> str:

        free_space = self.capacity - self.content

        if ml <= free_space:

            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self) -> str:

        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:

        space_left = self.capacity - self.content
        return f"{space_left} ml left"

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
