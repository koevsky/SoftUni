class Player:

    NAMES_TAKEN = []
    DEFAULT_STAMINA = 100

    def __init__(self, name: str, age: int, stamina=DEFAULT_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")

        if value in Player.NAMES_TAKEN:
            raise Exception(f"Name {value} is already used!")

        self.__name = value
        Player.NAMES_TAKEN.append(self.__name)

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


