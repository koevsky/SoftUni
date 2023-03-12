from project.animal import Animal


class Cat(Animal):

    GENDER = ""

    def make_sound(self):
        return f'Meow meow!'
