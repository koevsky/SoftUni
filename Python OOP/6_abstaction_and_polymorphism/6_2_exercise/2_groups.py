class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):

        return f"{self.name} {self.surname}"

    def __add__(self, other):
        surname = other.surname
        name = self.name

        return Person(name, surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group = self.people + other.people
        new_name = f'{self.name} {other.name}'

        return Group(new_name, new_group)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"

    def __getitem__(self, item):
        return f'Person {item}: {self.people[item]}'