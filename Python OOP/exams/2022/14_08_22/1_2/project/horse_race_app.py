from typing import List

from project.jockey import Jockey
from project.horse_race import HorseRace

from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_type in ["Appaloosa", "Thoroughbred"]:

            is_same_horse = list(filter(lambda h: h.name == horse_name, self.horses))
            if is_same_horse:
                raise Exception(f"Horse {horse_name} has been already added!")

            horses_dict = {"Appaloosa": Appaloosa(horse_name, horse_speed),
                           "Thoroughbred": Thoroughbred(horse_name, horse_speed)}

            horse = horses_dict[horse_type]
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        is_same_jockey = list(filter(lambda j: j.name == jockey_name, self.jockeys))
        if is_same_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        is_same_race = list(filter(lambda r: r.race_type == race_type, self.horse_races))
        if is_same_race:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            reversed_horses = list(reversed(self.horses))
            horse = next(filter(lambda h: not h.is_taken and h.__class__.__name__ == horse_type, reversed_horses))

        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        try:
            horse_race = next(filter(lambda race: race.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        try:
            horse_race = next(filter(lambda race: race.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = max(horse_race.jockeys, key=lambda jokey: jokey.horse.speed)
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."



