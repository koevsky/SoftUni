class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int) -> str:

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        elif self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        try:
            employee = next(filter(lambda w: w.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(employee)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:

        total_expense = sum([w.salary for w in self.workers])

        if total_expense <= self.__budget:

            self.__budget -= total_expense
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        total_expense = sum([a.money_for_care for a in self.animals])

        if total_expense <= self.__budget:

            self.__budget -= total_expense
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):

        total_lions = list(filter(lambda l: l.__class__.__name__ == "Lion", self.animals))
        total_tigers = list(filter(lambda t: t.__class__.__name__ == "Tiger", self.animals))
        total_cheetahs = list(filter(lambda c: c.__class__.__name__ == "Cheetah", self.animals))

        result = [f"You have {len(self.animals)} animals"]

        result.append(f"----- {len(total_lions)} Lions:")
        [result.append(repr(lion)) for lion in total_lions]

        result.append(f"----- {len(total_tigers)} Tigers:")
        [result.append(repr(tiger)) for tiger in total_tigers]

        result.append(f"----- {len(total_tigers)} Cheetahs:")
        [result.append(repr(cheetah)) for cheetah in total_cheetahs]

        return "\n".join(result)

    def workers_status(self):

        total_keepers = list(filter(lambda k: k.__class__.__name__ == "Keeper", self.workers))
        total_caretakers = list(filter(lambda c: c.__class__.__name__ == "Caretaker", self.workers))
        total_vets = list(filter(lambda v: v.__class__.__name__ == "Vet", self.workers))

        result = [f"You have {len(self.workers)} workers"]

        result.append(f"----- {len(total_keepers)} Keepers:")
        [result.append(repr(keeper)) for keeper in total_keepers]

        result.append(f"----- {len(total_caretakers)} Caretakers:")
        [result.append(repr(caretaker)) for caretaker in total_caretakers]

        result.append(f"----- {len(total_vets)} Vets:")
        [result.append(repr(vet)) for vet in total_vets]

        return '\n'.join(result)
